# Password Manager CLI

A basic Command Line Interface (CLI) tool written in Python to securely store and retrieve passwords using symmetric encryption.

## Description

This application allows users to store usernames and passwords in a local vault. All passwords are encrypted using a master password provided by the user at runtime. It utilizes the `cryptocode` library to ensure that stored data is not human-readable without the correct key.

## Features

-   **Master Password Protection**: Access to the vault requires a master password.
-   **Encryption**: Passwords are encrypted before being saved to `password.txt` using the `cryptocode` library.
-   **Secure Storage**: The storage file (`password.txt`) is automatically ignored by Git to prevent accidental uploads to version control.
-   **Modes**:
    -   **Add**: Encrypt and save a new username/password combination.
    -   **View**: Decrypt and display saved credentials. If the wrong master password is provided, passwords appear as `[LOCKED - Wrong key]`.

## Prerequisites

-   Python 3.x
-   `cryptocode` library

## Installation

1.  Clone the repository.
2.  Install the required dependency:
    ```bash
    pip install cryptocode
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

## Security Disclaimer

This is a basic CLI tool intended for educational purposes or simple personal use. Please note the following:
-   The master password is not stored; if you forget it, your data cannot be recovered.
-   While passwords are encrypted on disk, the master password and decrypted data exist in plain text in the system's memory while the program is running.