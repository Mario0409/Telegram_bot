# Telegram Emoji Counter Bot

A simple Telegram bot that counts the number of poop emojis (💩) sent by users in a group chat and provides daily summaries. Users can also request counts for specific months and view available commands.

## Features

- Count poop emojis sent by each user daily.
- Provide a daily summary of emoji counts at the end of the day.
- Count emojis for specific months upon request.
- Help command to show available functions.

## Requirements

- Python 3.7 or higher
- [python-telegram-bot](https://pypi.org/project/python-telegram-bot/)
- Basic understanding of Python and Telegram bot usage.

## Installation

1. **Clone the repository** (or download the files):
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install python-telegram-bot
    ```

4. **Get your Bot Token**:
   - Talk to [BotFather](https://t.me/botfather) on Telegram.
   - Use `/newbot` to create a new bot and get the token.

5. **Set the Bot Token**:
   - Update the token in your `bot.py` file:
     ```python
     application = Application.builder().token("YOUR_BOT_TOKEN").build()
     ```

## Usage

1. **Run the bot**:
    ```bash
    python bot.py
    ```

2. **Add the bot to your group**:
   - Make sure the bot has the necessary permissions to read and send messages.

3. **Interact with the bot**:
   - Type `/start` to initiate the bot.
   - Use `/help` to see available commands.

## Commands

- `/start`: Start the bot and receive a welcome message.
- `/help`: Show available commands.
- `/emoji_count`: Check how many poop emojis you have sent today.
- `/monthly_emoji_count <month> <year>`: Check how many poop emojis you have sent in a specific month.

## Notes

- The bot tracks poop emoji usage per user per day and will send a summary at the end of the day.
- Ensure the bot is not muted in the group and has permission to read messages.
- To disable privacy mode, contact [BotFather](https://t.me/botfather) and change the settings for your bot.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

