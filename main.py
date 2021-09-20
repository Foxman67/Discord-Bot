
import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix="$")


class MyClient(discord.Client):
    async def on_ready(self):
        print("up and running {0} ".format(self.user))



class IDC(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_ID(self,ctx,game,ID):

        #what do i need, game, pokeid, pokemon(?) box-probably, boxpos(?)?
        #how to gather this data





with open('token.txt') as t:
    token = t.readline()


client = MyClient()
client.run(token)
