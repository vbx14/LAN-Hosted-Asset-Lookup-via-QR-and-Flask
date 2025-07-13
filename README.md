# QR Code–Based Hardware Tracking System

A LAN-hosted, Flask-powered web application for secure IT asset identification using QR codes. This project enables authenticated employees to retrieve real-time hardware specifications by scanning a QR code, logging in via a browser, and querying a MySQL database—all from within a local network.

## Overview

This system provides a lightweight, in-house solution for managing and identifying hardware devices in an organization. Each device is tagged with a unique QR code that links to a Flask web interface. Upon scanning, users are prompted to log in with their credentials. If authenticated, the app fetches and displays hardware details such as RAM, CPU, and storage from a MySQL database.

Ideal for use in office environments, server rooms, or educational labs, where quick, secure access to system specifications is needed without installing dedicated client software.

## Features

- QR code integration for quick hardware identification
- User authentication system for controlled access
- Hardware details served dynamically via MySQL queries
- Modular Flask backend with Jinja2 templating
- Hosted locally for security and speed
- Mobile-friendly, accessible via LAN from any device
- Clean separation of frontend, backend, and database config

## Tech Stack

| Layer       | Technology                     |
|-------------|--------------------------------|
| Frontend    | HTML, CSS (optional Bootstrap) |
| Backend     | Python, Flask, Jinja2          |
| Database    | MySQL                          |
| Deployment  | Localhost / LAN (port 5000)    |
| Utilities   | QR Code (PyQRCode, Pillow)     |

## How It Works

1. Each hardware device is assigned a unique QR code encoding a URL like:
   ```
   http://<LAN_IP>:5000/hardware?id=HW103
   ```

2. The QR code redirects users to a login page served by Flask.

3. User credentials are verified against the users table in MySQL.

4. Upon successful authentication, hardware details for the given ID are fetched from the database and displayed in the browser.

## Database Schema

Database: asset_db
Tables:

- users (id, username, password)
- hardware (id, type, ram, cpu, storage)

Refer to /sql/sample_data.sql for example data.

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/hardware-qr-app.git
   cd hardware-qr-app
   ```

2. (Optional) Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure MySQL credentials in db_config.py.

5. Start the Flask server:
   ```bash
   flask run --host=0.0.0.0
   ```

6. Open the URL from any device on the same LAN (e.g., http://192.168.1.100:5000/hardware?id=HW101)

## Security Notes

- This project uses plain-text passwords for demonstration — always hash credentials (e.g., bcrypt) in production.
- Only run this app on a secure, firewall-restricted local network.
- Do not expose port 5000 to the public internet.

## Folder Structure

```
hardware-qr-app/
├── app.py
├── db_config.py
├── templates/
│   ├── login.html
│   └── hardware.html
├── static/
│   └── style.css
├── sql/
│   └── sample_data.sql
└── requirements.txt
```

## Sample Users

| Username | Password     |
|----------|--------------|
| alice    | wonderland   |
| bob      | secure456    |
| admin    | adminpass    |
