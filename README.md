# �� Password Manager

A secure, Python-based password management application that allows you to safely store, encrypt, and manage your passwords with military-grade encryption. Built with security-first principles and user-friendly interface.

## 🚀 Quick Start
 
| Option | Description |
|--------|-------------|
| [📥 Download Release](#download-release) | Ready-to-use executable for Windows |
| [💻 Install from Source](#installation-with-source-code) | Full source code with customization options |

---

## ✨ Features

- **🔒 Military-Grade Encryption**: AES-256 encryption for maximum security
- **🔑 Key Management**: Secure key generation and storage
- **📱 User-Friendly Interface**: Simple command-line interface for easy navigation
- **💾 Password Storage**: Organized storage for multiple accounts and services
- **🔄 Backup & Restore**: Easy backup and restoration of your password database
- **⚡ Fast Performance**: Lightweight application with minimal resource usage
- **🛡️ Local Storage**: All data stored locally on your device

## 🎯 Use Cases

- **Personal Use**: Store passwords for social media, email, and online accounts
- **Business Use**: Manage credentials for work-related services and applications
- **Developer Use**: Store API keys, database credentials, and development passwords
- **Student Use**: Manage educational platform logins and academic accounts

---

## �� Download Release

### For Windows Users (Recommended)

1. **Download**: Visit [Releases Page](https://github.com/sametgurtuna/passwordmanager/releases)
2. **Extract**: Unzip the downloaded file to any folder
3. **Run**: Double-click `pm.exe` to launch the application
4. **Start Using**: Follow the on-screen instructions

### First-Time Setup
- **Create New Key**: Generate your first encryption key
- **Create Password File**: Initialize your password database
- **Add Passwords**: Start storing your credentials securely

---

## 💻 Installation with Source Code

### Prerequisites

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: See requirements below

### Required Libraries

```bash
pip install cryptography
pip install clipboard
```

### Step-by-Step Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/sametgurtuna/passwordmanager.git
   cd passwordmanager
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Application**
   ```bash
   python main.py
   ```

---

## 🎮 Usage Guide

### Main Menu Options

| Option | Description | When to Use |
|--------|-------------|-------------|
| **1** | Create New Key | First-time setup or key rotation |
| **2** | Load Existing Key | Access existing password database |
| **3** | Create Password File | Initialize new password storage |
| **4** | Load Password File | Access existing password storage |
| **5** | Add New Password | Store new account credentials |
| **6** | Get Password | Retrieve stored password |
| **7** | Remove Password | Delete unwanted credentials |

### Workflow Example

1. **First Time Setup**
   ```
   Create New Key → Create Password File → Add New Password
   ```

2. **Daily Usage**
   ```
   Load Existing Key → Load Password File → Get Password
   ```

---

## 🔒 Security Features

- **Encryption**: AES-256 bit encryption
- **Key Management**: Secure key generation and storage
- **Local Storage**: No cloud dependencies or data transmission
- **Access Control**: Key-based authentication required
- **Data Integrity**: Encrypted password database

## ⚠️ Important Security Notes

- **🔑 Key File**: Never lose your encryption key file
- **💾 Backup**: Regularly backup your password database
- **🔄 Updates**: Keep the application updated for security patches
- **🚫 Sharing**: Never share your key file or password database
- **�� Device Security**: Ensure your device is secure and malware-free

---

## ��️ Technical Details

- **Language**: Python 3.x
- **Encryption**: AES-256 via cryptography library
- **Storage**: Local file-based database
- **Interface**: Command-line interface (CLI)
- **Platform**: Cross-platform (Windows, macOS, Linux)


---

## 🚧 Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| **Key file not found** | Ensure key file is in the same directory as the application |
| **Import errors** | Install required dependencies: `pip install cryptography clipboard` |
| **Permission denied** | Run as administrator or check file permissions |
| **Python not found** | Install Python 3.7+ and add to PATH |

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/sametgurtuna/passwordmanager/issues)
- **Discussions**: [GitHub Discussions](https://github.com/sametgurtuna/passwordmanager/discussions)
- **Wiki**: Check the project wiki for detailed guides

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Test** thoroughly
5. **Submit** a pull request

### Development Setup

```bash
git clone https://github.com/sametgurtuna/passwordmanager.git
cd passwordmanager
pip install -r requirements.txt
python main.py
```

---

## �� Acknowledgments

- **Cryptography Library**: For robust encryption capabilities
- **Python Community**: For excellent documentation and tools
- **Open Source Contributors**: For inspiration and feedback


---

**🔐 Secure • Simple • Reliable**

*Built with security in mind for the modern digital world*
