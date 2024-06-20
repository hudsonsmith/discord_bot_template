# Import threading to be able to run multiple class functions easier.
import os
import discord
from discord.ext import commands
import asyncio

with open("token.txt", "r") as f:
    TOKEN = f.read()

description = "Put the name here..."

intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", description=description, intents=intents)

async def load_discord_cogs():
    for file in os.listdir(f"{os.getcwd()}/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            print(f"{file} loaded!")
            await client.load_extension(f"cogs.{file[:-3]}")


async def main():
    await load_discord_cogs()


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

if __name__ == "__main__":
    asyncio.run(main())
    client.run(TOKEN)
