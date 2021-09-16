# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="$")


class MyClient(discord.Client):
    async def on_ready(self):
        print("up and running {0} ".format(self.user))


client = MyClient()
client.run("ODg2NzI5NzE2MzMyMTM0NTIz.YT51Zw.ZPNnDqusRBAzqfAvY2H3fjSlSPM")
