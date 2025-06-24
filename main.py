# -*- coding: utf-8 -*-
import sys
import json
import re
import webbrowser
from pathlib import Path
from flowlauncher import FlowLauncher

plugindir = Path(__file__).parent.resolve()
config_file = plugindir / "engines.json"

class TabOpener(FlowLauncher):
    def __init__(self):
        self.config_file = config_file
        self.load_engine_config()
        super().__init__()

    def load_engine_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.engines = json.load(f)
            self.website_name_map = {}
            for code, group in self.engines.items():
                for w in group.get('websites', []):
                    name = w.get('name', '').lower() if w.get('name') else None
                    code_field = w.get('code', '').lower() if w.get('code') else None
                    if name:
                        self.website_name_map[name] = (code, w, group)
                    if code_field:
                        self.website_name_map[code_field] = (code, w, group)
        except Exception as e:
            print(f"Error loading engines.json: {e}")
            self.engines = {}
            self.website_name_map = {}

    def query(self, query):
        q = query.strip()
        results = []
        default_icon = 'Images/app.png'
        if not self.engines:
            results.append({
                "Title": "Configuration Error",
                "SubTitle": "Could not load engines.json. Please check the file for errors.",
                "IcoPath": default_icon
            })
            return results
        # If query is empty or only a partial code, show all matching codes
        if not q or len(q.split()) == 1:
            code_prefix = q.lower() if q else ''
            for code, group in self.engines.items():
                if code.startswith(code_prefix):
                    group_name = group.get('name', code.capitalize())
                    icon = group.get('icon', default_icon)
                    count = len(group.get('websites', []))
                    site_names = [w.get('name', '') for w in group.get('websites', [])]
                    site_preview = ', '.join(site_names[:3])
                    if len(site_names) > 3:
                        site_preview += f', +{len(site_names)-3} more'
                    title = f"{group_name} ({count} sites)"
                    subtitle = site_preview
                    urls = [w.get('url', '').format('') for w in group.get('websites', [])]
                    results.append({
                        "Title": title,
                        "SubTitle": subtitle,
                        "IcoPath": icon if icon else default_icon,
                        "JsonRPCAction": {
                            "method": "open_tabs",
                            "parameters": [urls]
                        }
                    })
            # Also show website name/code matches if any
            matched_sites = []
            for name_or_code, (group_code, w, group) in self.website_name_map.items():
                if name_or_code.startswith(code_prefix) and code_prefix:
                    name = w.get('name', name_or_code.capitalize())
                    codeword = w.get('code', '')
                    title = name
                    icon = w.get('icon', group.get('icon', default_icon))
                    url = w.get('url', '').format('')
                    subtitle = f"Direct search on {name} ({codeword})" if codeword else f"Direct search on {name}"
                    matched_sites.append({
                        "Title": title,
                        "SubTitle": subtitle,
                        "IcoPath": icon if icon else default_icon,
                        "JsonRPCAction": {
                            "method": "open_tab",
                            "parameters": [url]
                        }
                    })
            # Remove duplicates (by Title)
            seen_titles = set()
            unique_sites = []
            for site in matched_sites:
                if site["Title"].lower() not in seen_titles:
                    unique_sites.append(site)
                    seen_titles.add(site["Title"].lower())
            # Insert site matches at the top
            results = unique_sites + results
            if not results and code_prefix:
                results.append({
                    "Title": f"No match found for '{code_prefix}'",
                    "SubTitle": "No website or group matches your input.",
                    "IcoPath": default_icon
                })
            return results

        # If query is a code and a search term
        parts = q.split(None, 1)
        if len(parts) == 2:
            code = parts[0].lower()
            search_query = parts[1].strip()
            # Check if code matches a website name
            if code in self.website_name_map:
                code_, w, group = self.website_name_map[code]
                url = w.get('url', '').format(search_query)
                icon = w.get('icon', group.get('icon', default_icon))
                name = w.get('name', code)
                codeword = w.get('code', '')
                title = name
                subtitle = f"Search for '{search_query}' on {name} ({codeword})" if codeword else f"Search for '{search_query}' on {name}" if not w.get('description') else w['description']
                results.append({
                    "Title": title,
                    "SubTitle": subtitle,
                    "IcoPath": icon if icon else default_icon,
                    "JsonRPCAction": {
                        "method": "open_tab",
                        "parameters": [url]
                    }
                })
                return results
            # Otherwise, check if code matches a group
            group = self.engines.get(code)
            if group and 'websites' in group:
                urls = [w.get('url', '').format(search_query) for w in group['websites']]
                icon = group.get('icon', default_icon)
                results.append({
                    "Title": f"{group.get('name', code.capitalize())} - Search '{search_query}'",
                    "SubTitle": f"Open all {len(urls)} sites for this search",
                    "IcoPath": icon if icon else default_icon,
                    "JsonRPCAction": {
                        "method": "open_tabs",
                        "parameters": [urls]
                    }
                })
                for w in group['websites']:
                    url = w.get('url', '').format(search_query)
                    icon = w.get('icon', group.get('icon', default_icon))
                    name = w.get('name', code)
                    codeword = w.get('code', '')
                    title = name
                    subtitle = f"Search for '{search_query}' on {name} ({codeword})" if codeword else f"Search for '{search_query}' on {name}" if not w.get('description') else w['description']
                    results.append({
                        "Title": title,
                        "SubTitle": subtitle,
                        "IcoPath": icon if icon else default_icon,
                        "JsonRPCAction": {
                            "method": "open_tab",
                            "parameters": [url]
                        }
                    })
            else:
                results.append({
                    "Title": f"No match found for '{code}'",
                    "SubTitle": "No website or group matches your input.",
                    "IcoPath": default_icon
                })
        else:
            results.append({
                "Title": "Invalid format.",
                "SubTitle": "Use: <code> <query>",
                "IcoPath": default_icon
            })
        return results

    def open_tab(self, url):
        webbrowser.open(url)

    def open_tabs(self, urls):
        for url in urls:
            webbrowser.open(url)

if __name__ == "__main__":
    TabOpener()
