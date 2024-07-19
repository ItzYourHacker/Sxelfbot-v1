import os 
os.system("pip install -r requirements.txt")
import discord
from discord.ext import commands
from utils.config import *
import asyncio
from discord.ext import tasks

hacker = commands.Bot(command_prefix=prefix,self_bot=True) 

os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

@tasks.loop(minutes=15)
async def autosender():
    for h in channels:
        try:
            channel = hacker.get_channel(h)
            if channel:await channel.send(message)
            else:return
        except discord.errors.HTTPException as e:
            if e.status == 429:
                print(f'Rate limited while sending message. Retrying in {e.retry_after} seconds.')
                await asyncio.sleep(e.retry_after)
                await channel.send(message)
            else:
                print(f'Error while sending message: {e}')
    return 

@hacker.event
async def on_ready():
    print("Loaded & Online!")
    print(f"Logged in as: {hacker.user}")
    print(f"Connected to: {len(hacker.guilds)} guilds")
    print(f"Connected to: {len(hacker.users)} users")
    try:
        autosender.start()
        print("Started Autosender")
    except Exception as e:print(e)

async def main():
    async with hacker:
        initial_extensions = []
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                initial_extensions.append("cogs." + filename[:-3])
        for extension in initial_extensions:
            await hacker.load_extension(extension)
            print(f"Loaded :[{extension}]")
        try:await hacker.start(token)
        except Exception as e:print(e)

if __name__ == "__main__":
    asyncio.run(main())
