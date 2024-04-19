import os
from telethon import TelegramClient, events, Button

# Set your API ID, API hash, and bot token here
API_ID = "13279715"
API_HASH = '56e198053932ecf216af72a2ddffcd78'
BOT_TOKEN = '6753549807:AAEfAzx9dJslsByEp1WY6QzpFe_UGjjhIMY'

# Create a TelegramClient instance
client = TelegramClient('vote_bot_session', API_ID, API_HASH)


# Handler for processing votes
@client.on(events.CallbackQuery(pattern=r'^vote_'))
async def vote_handler(event):
    # Parse the user ID from the button data
    user_id = int(event.data.decode('utf-8').split('_')[1])

    # Increment the vote count for the user
    # Store this information in a database (not implemented in this example)

    # Answer the callback query to remove the "loading" status
    await event.answer('Vote counted!')


# Handler for update button
@client.on(events.NewMessage(pattern='/update'))
async def update_handler(event):
    await event.respond('Here are the latest updates:\n1. Update 1\n2. Update 2')


# Handler for support button
@client.on(events.NewMessage(pattern='/support'))
async def support_handler(event):
    await event.respond('For support, join our Telegram group: [Support Group](https://t.me/BWANDARLOK)')


# Start the client
client.start(bot_token=BOT_TOKEN)
client.run_until_disconnected()
