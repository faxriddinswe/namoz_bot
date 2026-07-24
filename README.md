# 🌙 Telegram Prayer Times & Auto-Forwarder Userbot

A high-performance, asynchronous **Telegram Userbot** built with Python and Telethon. This bot actively monitors target Telegram channels in real-time, filters messages for specific prayer time keywords, and automatically forwards matching posts to designated recipients instantly.

---

## 🎯 Project Overview & Purpose

In busy Telegram channels, time-sensitive posts—such as daily prayer schedules (`Namoz vaqtlari`), Ramadan calendars, or urgent notifications—can easily get lost or overlooked.

This project was engineered to solve that problem by providing an automated pipeline:

1. **Real-time Channel Monitoring** — Continuously listens for new posts published in specified Telegram channels without polling delays.
2. **Smart Keyword Filtering** — Inspects incoming text for predefined keywords (e.g., *bomdod, peshin, asr, shom, xufton, taqvim, namoz vaqtlari*), normalizes text case, and prevents false positives.
3. **Instant Auto-Forwarding** — Dispatches matching messages directly to targeted Telegram accounts or groups instantly.
4. **Cloud-Ready Architecture** — Configured with environment variables (`os.environ`) and session strings, making it fully compatible with headless servers and 24/7 cloud deployments.

---

## 🛠 Tech Stack & Dependencies

- **Language:** [Python 3.10+](https://www.python.org/)
- **Telegram Framework:** [Telethon](https://docs.telethon.dev/) (MTProto API Client library)
- **Asynchronous Engine:** `asyncio` (for non-blocking event handling and concurrent message processing)
- **Environment Management:** `python-dotenv` / environment variable parsing (`os`)
- **Version Control:** Git & GitHub

---

## 📂 Repository Structure

```text
namoz_bot/
├── main.py             # Core event-driven bot engine and handler logic
├── requirements.txt    # Project dependencies and library versions
├── Procfile             # Deployment configuration for worker process manager
├── .gitignore           # Strict protection rules for sensitive keys and sessions
└── README.md            # Comprehensive project documentation
```

---

## 🚀 Installation & Setup Guide

### 1. Prerequisites

- Python 3.10 or higher
- Telegram API Credentials (`API_ID` and `API_HASH`) from [my.telegram.org](https://my.telegram.org)

### 2. Clone the Repository

```bash
git clone https://github.com/USERNAME/namoz_bot.git
cd namoz_bot
```

### 3. Create & Activate Virtual Environment

```bash
# Linux / macOS (Fedora/Ubuntu)
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Install Requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Generate Telethon String Session

Since binary `.session` files should not be published to Git repositories, generate a string session using Python:

```python
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = 12345678  # Replace with your API_ID
API_HASH = "your_api_hash"

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print("YOUR_SESSION_STRING:", client.session.save())
```

### 6. Environment Variables Configuration

Set the following environment variables in your operating system or deployment platform:

| Variable          | Type    | Description                                   |
|--------------------|---------|------------------------------------------------|
| `API_ID`           | Integer | Your Telegram App API ID                       |
| `API_HASH`         | String  | Your Telegram App API Hash                      |
| `SESSION_STRING`   | String  | Generated Telethon String Session token         |
| `TARGET_CHANNEL`   | String  | Username of the source channel (without `@`)    |
| `RECEIVER_USERS`   | String  | Target recipient usernames (comma-separated)    |

### 7. Run the Userbot

```bash
python main.py
```

---

## 🔒 Security Best Practices

> ⚠️ **Security Warning:** Never hardcode personal credentials or publish `.session` / `.env` files to public or private Git repositories.

This repository enforces security using a `.gitignore` configuration blocking:

- Virtual environments (`venv/`)
- Local Telegram session binary files (`*.session`, `*.session-journal`)
- Python bytecode caches (`__pycache__/`)

---

## 📄 License

This project is open-source software licensed under the **MIT License**.

```text
MIT License

Copyright (c) 2026 Faxriddin Baxtiyorov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👤 Author

**Faxriddin Baxtiyorov**
