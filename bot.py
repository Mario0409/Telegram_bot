import logging
from collections import defaultdict
from datetime import datetime
from datetime import time  # Import time from datetime
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Dictionary to hold poop emoji counts for each user per day
user_emoji_counts = defaultdict(lambda: defaultdict(int))
# Dictionary to hold the first user who sent a poop emoji for each day
first_sender_of_day = {}
# Dictionary to map user IDs to usernames
usernames = {}
# Store the chat ID to send daily summaries
chat_id = None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "Available commands:\n"
        "/start - Start the bot.\n"
        "/help - Show this help message.\n"
        "/trigger_summary - Manually trigger the daily summary.\n"  # Added command
    )
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle incoming messages and count poop emojis."""
    global chat_id  # Declare chat_id as global to set it in the start command
    user_id = update.effective_user.id
    message_text = update.message.text
    current_date = datetime.now().date()  # Get the current date
    poop_emoji = "💩"

    # Set the chat_id for sending the daily summary
    chat_id = update.effective_chat.id

    # Store the username associated with the user_id
    usernames[user_id] = update.effective_user.username or update.effective_user.first_name

    # Check if the message contains the poop emoji
    if poop_emoji in message_text:
        # Increment the count for this user on the current date
        user_emoji_counts[user_id][current_date] += 1
        logger.info(f"User {user_id} sent 💩. Current count: {user_emoji_counts[user_id][current_date]}")

        # Check if this is the first poop emoji of the day
        if current_date not in first_sender_of_day:
            first_sender_of_day[current_date] = user_id
            await update.message.reply_text(f"🚨 {update.effective_user.first_name} è il primo cacatore di oggi!")

        # If the user has sent the poop emoji 3 times today, send a special message
        if user_emoji_counts[user_id][current_date] == 3:
            await update.message.reply_text("Male al pancino? oggi è già la terza volta che cachi")

async def send_daily_summary(context: ContextTypes.DEFAULT_TYPE):
    """Send a summary of the poop emoji counts for each user."""
    current_date = datetime.now().date()
    summary_message = "Mini classifica giornaliera:\n"

    for user_id, counts in user_emoji_counts.items():
        count_today = counts[current_date]
        username = usernames.get(user_id, "Unknown User")  # Get username or default to "Unknown User"
        summary_message += f"{username}: {count_today} 💩\n"

    # Send the summary to the specified chat
    if chat_id:
        await context.bot.send_message(chat_id=chat_id, text=summary_message)

    # Reset counts for the next day
    user_emoji_counts.clear()
    first_sender_of_day.clear()
    usernames.clear()  # Clear usernames for the next day

async def trigger_summary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Trigger the daily summary manually."""
    await send_daily_summary(context)  # Call the send_daily_summary function

def main() -> None:
    """Start the bot."""
<<<<<<< HEAD
    application = Application.builder().token("TOKEN").build()  # Replace with your bot token
=======
    application = Application.builder().token("ADD TOKEN").build()  # Replace with your bot token
>>>>>>> origin/master

    # On different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("trigger_summary", trigger_summary))  # Added command handler

    # On non-command i.e. message - handle the message
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Schedule the daily summary at midnight
    job_queue = application.job_queue
    job_queue.run_daily(send_daily_summary, time=time(0, 0))  # Schedule the job to run at midnight every day

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()


