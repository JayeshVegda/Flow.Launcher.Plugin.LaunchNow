
<p align="center">
  <img src="Images/app.png" alt="Mega Search Logo" width="100" height="100" />
</p>

<h1 align="center">Mega Search</h1>
<h3 align="center">Search Smarter. Search Everywhere.</h3>

<p align="center">
  <!-- Core Badges -->
  <a href="https://github.com/JayeshVegda/Flow.Launcher.Plugin.MegaSearch/releases">
    <img src="https://img.shields.io/github/v/release/JayeshVegda/Flow.Launcher.Plugin.MegaSearch?style=for-the-badge&color=blue" alt="GitHub release">
  </a>
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/python-3.7+-blue?style=for-the-badge&logo=python" alt="Python Version">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/JayeshVegda/Flow.Launcher.Plugin.MegaSearch?style=for-the-badge" alt="License">
  </a>
  <a href="https://github.com/JayeshVegda/Flow.Launcher.Plugin.MegaSearch/releases">
    <img src="https://img.shields.io/github/downloads/JayeshVegda/Flow.Launcher.Plugin.MegaSearch/total?style=for-the-badge&color=success" alt="Downloads">
  </a>
  <!-- Optional/Extra Badges -->
  <a href="https://github.com/JayeshVegda/Flow.Launcher.Plugin.MegaSearch/stargazers">
    <img src="https://img.shields.io/github/stars/JayeshVegda/Flow.Launcher.Plugin.MegaSearch?style=for-the-badge&color=yellow" alt="Stars">
  </a>
  <a href="https://github.com/JayeshVegda/Flow.Launcher.Plugin.MegaSearch/issues">
    <img src="https://img.shields.io/github/issues/JayeshVegda/Flow.Launcher.Plugin.MegaSearch?style=for-the-badge&color=orange" alt="Issues">
  </a>
</p>

<p align="center">
  🚀 <em>A powerful Flow Launcher plugin that opens multiple search engines or websites with one command.</em><br>
  <em>Group your favorite platforms, customize your shortcuts, and supercharge your search experience.</em>
</p>

---


## 📆 Features

* 🔗 **Multi-tab search** — Open all sites in a group at once.
* 🎯 **Targeted engine search** — Search specific websites via short codes or names.
* 🧹 **Group-based control** — Organize engines by category like `AI`, `Shopping`, `Video`, etc.
* ✍️ **Simple JSON config** — Easily modify engines and groups.
* 🎨 **Custom icons** — Set personalized logos for visual recognition.
* ⚡ **Built with Python** — Lightweight, fast, and fully extensible.

---

## 🚀 Installation Guide

### ✅ Prerequisites

* [Flow Launcher](https://www.flowlauncher.com/) installed
* Python 3.7+

### 📁 Steps

1. **Clone or download** this repository into Flow Launcher's plugin directory:

   ```bash
   git clone https://github.com/yourusername/mega-search
   ```

2. **Navigate** to the plugin folder:

   ```bash
   cd mega-search
   ```

3. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Restart Flow Launcher**.

---

## ⚙️ Usage

### 🔑 Default Keyword: `bu`

| Command Format           | Example                           | Result                                   |
| ------------------------ | --------------------------------- | ---------------------------------------- |
| `bu`                     | `bu`                              | Lists all available groups               |
| `bu <group>`             | `bu ai`                           | Opens all AI-related websites            |
| `bu <group> <query>`     | `bu shopping wireless headphones` | Searches for query on all shopping sites |
| `bu <site/code> <query>` | `bu yt lofi music`                | Searches YouTube for "lofi music"        |

> 💡 Tip: Codes are short aliases like `yt` for YouTube, `g` for Google, etc.

---

## 🔄 Configuration

All configuration is stored in `engines.json`. Here’s an example:

```json
{
  "search": {
    "name": "Search",
    "icon": "Images/search/search.png",
    "websites": [
      {
        "name": "Google",
        "code": "g",
        "url": "https://www.google.com/search?q={}",
        "icon": "Images/search/google.png"
      },
      {
        "name": "YouTube",
        "code": "yt",
        "url": "https://www.youtube.com/results?search_query={}",
        "icon": "Images/video/youtube.png"
      }
    ]
  },
  "ai": {
    "name": "AI Engines",
    "icon": "Images/ai/ai.png",
    "websites": [
      {
        "name": "ChatGPT",
        "code": "chatgpt",
        "url": "https://chat.openai.com/?q={}",
        "icon": "Images/ai/chatgpt.png"
      }
    ]
  }
}
```

### ✅ Configuration Tips

* Use `{}` as the placeholder for the query string.
* Place icons in their respective folders (e.g. `Images/ai/`, `Images/search/`).
* Codes should be short and easy to remember.
* Group similar websites under categories like `search`, `shopping`, `video`, `ai`, etc.

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome!

Please:

* Keep the code clean and readable
* Follow the structure in `engines.json`
* Add icons for new sites
* Test before submitting your changes

---

## 📄 License

Released under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Tarik Jaber**
GitHub: [@yourusername](https://github.com/yourusername/mega-search)

---

> Made with ❤️ to make your web searching blazing fast.
