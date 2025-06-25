<p align="center">
  <img src="Images/app.png" alt="Mega Search Logo" width="100" height="100" />
</p>

<h1 align="center">LaunchNow 
<br> Search Smarter. Search Everywhere.</h1>

<p align="center">
  <a href="https://github.com/JayeshVegda/Flow.Launcher.Plugin.LaunchNow/releases">
    <img src="https://img.shields.io/github/v/release/JayeshVegda/Flow.Launcher.Plugin.LaunchNow?style=for-the-badge&color=blue" alt="Latest Release">
  </a>
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.7%2B-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/github/license/JayeshVegda/Flow.Launcher.Plugin.LaunchNow?style=for-the-badge&color=lightgrey" alt="License">
  </a>
  <a href="https://github.com/JayeshVegda/Flow.Launcher.Plugin.LaunchNow/releases">
    <img src="https://img.shields.io/github/downloads/JayeshVegda/Flow.Launcher.Plugin.LaunchNow/total?style=for-the-badge&color=success" alt="Total Downloads">
  </a>
</p>

---

<p align="center">
  🚀 <strong>LaunchNow </strong> is a powerful Flow Launcher plugin that lets you open multiple websites at once using a single keyword.<br>
  Define search groups, customize your engines, and boost your productivity with one quick command.
</p>


---

## 🎯 Quick Start

**Basic Usage:**
- Type `ln` → See all available groups
- Type `ln ai hello world` → Search "hello world" on all AI platforms
- Type `ln yt lofi music` → Search YouTube for "lofi music"

What makes it special : <br>
✨ Open multiple websites at once  <br>
⚡ Custom shortcuts for every site   <br>
🎨 Visual icons for easy recognition   <br>
🔧 Simple JSON configuration  <br>

---

## 📋 Table of Contents

- [🚀 Installation](#-installation)
- [💡 How to Use](#-how-to-use)
- [⚙️ Configuration](#️-configuration)
- [📚 Examples](#-examples)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🚀 Installation

<details>
<summary><strong>📋 Prerequisites</strong></summary>

Before installing, make sure you have:
- [Flow Launcher](https://www.flowlauncher.com/) installed and running
- Python 3.7 or higher

</details>

<details>
<summary><strong>📥 Method 1: Download from Releases (Recommended)</strong></summary>

1. Go to [Releases](https://github.com/JayeshVegda/Flow.Launcher.Plugin.LaunchNow/releases)
2. Download the latest `.zip` file
3. Extract to: `C:\Users\<YourUsername>\AppData\Roaming\FlowLauncher\Plugins`
4. Restart Flow Launcher

</details>

<details>
<summary><strong>🔧 Method 2: Manual Installation</strong></summary>

1. **Open Plugin Directory:**
   ```
   C:\Users\<YourUsername>\AppData\Roaming\FlowLauncher\Plugins
   ```

2. **Clone Repository:**
   ```bash
   git clone https://github.com/JayeshVegda/Flow.Launcher.Plugin.LaunchNow
   ```

3. **Restart Flow Launcher**

</details>

---

## 💡 How to Use

### Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `ln` | Show all available groups | `ln` to display all search groups |
| `ln <group>` | Open all sites in group | `ln ai` to open all AI platforms |
| `ln <group> <query>` | Search query on all group sites | `ln shopping wireless headphones` to search all shopping sites |
| `ln <code> <query>` | Search specific site using short code | `ln yt lofi music` to search YouTube |
| `ln <site_name> <query>` | Search specific site using full name | `ln google flow launcher` to search Google |
| `ln config` | Open the configuration file (`engines.json`) | `ln config` |


---

## ⚙️ Configuration

<details>
<summary><strong>📝 Basic Configuration</strong></summary>

All settings are in `engines.json`. Here's the structure:

```json
{
  "groupName": {
    "name": "Display Name",
    "icon": "path/to/icon.png",
    "websites": [
      {
        "name": "Site Name",
        "code": "short-code",
        "url": "https://example.com/search?q={}",
        "icon": "path/to/site-icon.png"
      }
    ]
  }
}
```

**Key Points:**
- Use `{}` where the search query should go
- Keep codes short and memorable
- Icons should be in the `Images/` folder

</details>

---

## 📚 Examples

<details>
<summary><strong>🔍 Search Examples</strong></summary>

```
ln g python tutorial          → Google search
ln yt python course          → YouTube search  
ln ai explain recursion      → Search all AI platforms
ln shopping wireless mouse   → Search all shopping sites
```

</details>

<details>
<summary><strong>⚡ Quick Actions</strong></summary>

```
ln                    → See all available groups
ln ai                 → Open all AI platforms (no search)
ln video             → Open all video platforms  
ln shopping          → Open all shopping sites
```

</details>

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

<details>
<summary><strong>🐛 Reporting Issues</strong></summary>

Found a bug? Please include:
- Your Flow Launcher version
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots if helpful

</details>

<details>
<summary><strong>✨ Adding Features</strong></summary>

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

**Guidelines:**
- Keep code clean and documented
- Follow existing patterns in `engines.json`
- Include icons for new sites
- Update README if needed

</details>

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

GitHub: [@JayeshVegda](https://github.com/JayeshVegda/)

---

<p align="center">
  <strong>⭐ If you find this plugin helpful, please give it a star!</strong><br>
  <em>Made with ❤️ to make your web searching blazing fast.</em>
</p>
</p>
