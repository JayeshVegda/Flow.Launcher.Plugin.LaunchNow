# Mega Search

[![GitHub release](https://img.shields.io/github/v/release/yourusername/mega-search?style=flat-square)](https://github.com/yourusername/mega-search/releases)
[![Issues](https://img.shields.io/github/issues/yourusername/mega-search?style=flat-square)](https://github.com/yourusername/mega-search/issues)
[![License](https://img.shields.io/github/license/yourusername/mega-search?style=flat-square)](LICENSE)

---

**Mega Search** is a Flow Launcher plugin that lets you search or open multiple websites and search engines at once. Configure your favorite engines and groups in a single JSON file, and use short codes or names for instant access.

## Features

- Open multiple tabs with one command
- Search across groups (e.g., all AI engines, all shopping sites)
- Direct search on a specific website (by name or code)
- Easy configuration via `engines.json`
- Custom icons for each engine/site
- Fast, lightweight, and extensible (Python)

## Installation

1. Download or clone this repository into your Flow Launcher plugins directory.
2. Ensure you have Python 3.7+ installed.
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. (Re)start Flow Launcher. Use the action keyword (default: `bu`).

## Usage

- Show all groups: `bu`
- Search a group: `bu <group> <query>` (e.g., `bu ai python tutorial`)
- Search a specific site: `bu <sitename|code> <query>` (e.g., `bu google cats` or `bu yt cats`)
- Open all sites in a group (no search): `bu <group>`

## Configuration

All engines and groups are defined in `engines.json` in the plugin directory. Example:

```json
{
  "search": {
    "name": "Search",
    "icon": "Images/search/search.png",
    "websites": [
      {"name": "Google", "code": "g", "url": "https://www.google.com/search?q={}", "icon": "Images/search/google.png"},
      {"name": "Bing", "code": "bing", "url": "https://www.bing.com/search?q={}", "icon": "Images/search/bing.png"}
    ]
  },
  ...
}
```

- Add a new group: Copy the structure above and add your own group key.
- Add a new website: Add a new object to the `websites` array in the relevant group.
- URL format: Use `{}` as the placeholder for the search term.
- Icons: Place your PNG icon in the appropriate `Images/` subfolder and reference its path.
- Code: Add a short, memorable code for each website for quick access.

## Contributing

Pull requests and suggestions are welcome! Please:
- Keep code clean and well-documented
- Update `engines.json` and icons as needed
- Test your changes before submitting

## License

MIT License. See [LICENSE](LICENSE) for details.

---

**Author:** Tarik Jaber  
**GitHub:** [Mega Search](https://github.com/yourusername/mega-search)
