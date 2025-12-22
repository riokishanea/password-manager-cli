# 🔐 Password Manager CLI

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Basic-yellow?style=for-the-badge)

A lightweight, secure, and easy-to-use Command Line Interface (CLI) tool to manage your passwords locally. Built with Python and secured with **Symmetric Encryption**.

---

## 📑 Table of Contents
- [About](#-about)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](installation)
- [Usage](usage)
- [Security Disclaimer](#-security-disclaimer)

---

## 🧐 About
This project provides a simple vault for your credentials. Instead of storing passwords in plain text, it uses the `cryptocode` library to encrypt them using a **Master Password**. This ensures that even if someone accesses your storage file, they cannot read your passwords without the key.

## 🚀 Features
* **🔒 Secure Storage**: Encrypts sensitive data before writing to disk.
* **🔑 Master Password**: A single key to lock and unlock your entire vault.
* **📝 CRUD Operations**: Easily **Add** new credentials and **View** existing ones.
* **🛡️ Git Safe**: Automatically configured to keep your secrets local and out of version control.
* **🚫 Error Handling**: Gracefully handles incorrect keys and missing files.

---

## 📂 Project Structure
```bash
password-manager-cli/
├── 📄 pwd_manager.py      # Main application logic
├── 📄 .gitignore          # Ensures password.txt is ignored
└── 📄 password.txt        # Encrypted storage (Generated automatically)
```

---

## Prerequisites

-   Python 3.6 +
-   `cryptocode` library

## Installation

1.  Clone the repository.
       ```bash
    git clone https://github.com/riokishanea/password-manager-cli.git
    cd password-manager-cli
    ```
3.  Install the required dependency:
    ```bash
    pip install cryptocode
    ```
    or
    ```bash
    python3 -m pip install cryptocode
    ```

## Usage

1.  Run the script:
    ```bash
    python pwd_manager.py
    ```
2.  Enter your **Master Password** when prompted. This key is required to encrypt new passwords and decrypt existing ones.
3.  Choose an option from the menu:
    -   Type `add` to save a new password.
    -   Type `view` to see your saved passwords.
    -   Type `q` to quit the application.

## 🔐 Security Disclaimer

This is a basic CLI tool intended for educational purposes or simple personal use. Please note the following:
-   The master password is not stored; if you forget it, your data cannot be recovered.
-   While passwords are encrypted on disk, the master password and decrypted data exist in plain text in the system's memory while the program is running.
