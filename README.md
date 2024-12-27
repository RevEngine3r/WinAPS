# WinAPS

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-brightgreen)](https://github.com/yourusername/ac-power-monitor/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://github.com/yourusername/ac-power-monitor)

Windows Acts on Power State is a lightweight and efficient application that automatically executes custom commands when
AC power is
connected or disconnected. It's perfect for managing power-intensive tasks or optimizing your workflow based on power
state.

## 🚀 Features

- **Real-time monitoring** of AC power connection status.
- **Customizable commands** for both connected and disconnected states.
- **Cross-platform support** for Windows, ~~Linux~~, and ~~macOS~~.
- **Lightweight and easy to use** with minimal resource usage.

## 🖥️ How It Works

1. The application continuously monitors the AC power state of your system.
2. Based on the connection status (connected or lost), it triggers predefined commands or scripts.
3. Logs each state change and the corresponding actions for easy debugging.

## 📥 Installation

### Prerequisites

- Nothing!

### Steps

1. Download the latest setup,

2. Install the program using setup,

3. Specify the commands on the config file,

4. The program is installed as a service and started automatically and will run your commands.

## ⚙️ Configuration

Edit the `config.json` file to customize the commands:

```json
{
  "on_ac_connected": "echo 'AC power connected'",
  "on_ac_disconnected": "echo 'AC power lost'"
}
```

- **`on_ac_connected`**: Command to execute when AC power is connected.
- **`on_ac_disconnected`**: Command to execute when AC power is lost.

## 🛠️ Usage

1. Start the application:
   ```bash
   python monitor.py
   ```
2. The app will run in the background and execute commands based on the AC power state.
3. Check the logs in the `logs` directory for execution history.

## 📄 Example Use Cases

- **Data backup**: Trigger an automatic backup when AC power is connected.
- **Shutdown**: Gracefully shut down or hibernate the system when AC power is lost.
- **Notifications**: Send desktop or mobile alerts based on power status changes.

## 📚 Documentation

For more details, visit the [Wiki](https://github.com/yourusername/ac-power-monitor/wiki).

## 🖋️ Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ **Star this repository** if you find it helpful! 😊
