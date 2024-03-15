import os
import discord
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Set up the Discord client with intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Prompt for multiline input
    print("Enter your message (press Ctrl+D or Ctrl+Z to finish):")
    message = []
    while True:
        try:
            line = input()
            message.append(line)
        except EOFError:
            break

    # Join the lines into a single string
    message_text = '\n'.join(message)

    # Get the list of channel IDs from the environment variable
    channel_ids = os.getenv('CHANNEL_IDS').split(',')

    # Send the message to each specified channel
    for channel_id in channel_ids:
        channel = client.get_channel(int(channel_id))
        if channel:
            await channel.send(message_text)
        else:
            print(f"Channel with ID {channel_id} not found.")

    await client.close()

# Run the client using the user token from the environment variable
client.run(os.getenv('DISCORD_USER_TOKEN'))