import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

class DevPSUBot(discord.Client):
    async def on_ready(self):
        print("logged on!")

    async def on_message(self, message):
        print(f"message found: {message.content} from {message.author} in {message.channel}")
        # print(f"mentions: {message.mentions}")
        if message.author == client.user:
            return
        if "hello" in message.content.lower():
            print(f"command recognized: hello")
            await message.channel.send("hello")
        if client.user in message.mentions:
            print("bot mentioned!!!!!")
            await message.channel.send("I WAS MENTIONED!!!!")
        if message.content == "react":
            print("react command recognized")
            await message.add_reaction("👍")
            await message.add_reaction("👽")

    
    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"i see you typing, {user}")
    
client = DevPSUBot(intents=intents)
client.run(token)