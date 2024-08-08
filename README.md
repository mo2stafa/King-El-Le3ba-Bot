<!-- python -m venv env

env\Scripts\activate

PIP install -r requirements.txt

PIP freeze > requirements.txt -->

# King-El-Le3ba Bot

King-El-Le3ba Bot is a Discord bot that allows users to manage and track scores in a server. It uses the Firebase Realtime Database for storing scores and includes commands for changing scores, viewing leaderboards, and more.

## Features

- **Score Management**: Users can increase or decrease their scores.
- **Leaderboard**: Displays the top 10 users in the server based on their scores.
- **Personal Score**: Users can view their own score.
- **Score Reset**: Admins can reset all users' scores to 0.

## Prerequisites

- Python 3.8+
- A Discord account and server
- Firebase project with a Realtime Database enabled
- Firebase Admin SDK service account key
- Discord bot token

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mo2stafa/King-El-Le3ba-Bot.git
cd king-el-le3ba-bot
```

### 2. Install Dependencies

Create a virtual environment (optional) and install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory of your project and add the following:

```env
TOKEN=your_discord_bot_token
DBLINK=https://your-firebase-database-url
```

### 4. Firebase Setup

- Download your Firebase Admin SDK service account key as a JSON file.
- Rename the downloaded JSON file to firebase_service_account.json.
- Place the firebase_service_account.json file in the root directory of your project.

### 5. Running the Bot

Run the bot using:

```bash
python bot.py
```

## Commands

### `m-cs <amount>`

Change your score by a specified amount. Use a positive number to increase or a negative number to decrease.

**Example:**

```bash
m-cs 5  # Increases your score by 5
m-cs -3  # Decreases your score by 3
```

### `m-leaderboard`

Displays the top 10 users in the server based on their scores.

### `m-me`

Displays your current score.

### `m-reset`

Resets all users' scores in the server to 0.

### `m-ping`

Responds with "pong" to check if the bot is online and responsive.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.
