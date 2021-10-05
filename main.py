import json
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("up and running {0} ".format(bot.user))


class IDC(commands.Cog):
    PATH = os.getcwd()+"/profile"
    FILENAME = "{0}.json"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def addid(self, ctx, game, ID):
        # what do i need, game, pokeid,
        # how to gather this data
        # scope, remember this is just for lotto odds
        # dictionary for user games, games keys game abbreviations, those key lists
        # write to file, do not append
        user = ctx.author.id
        path = os.path.join(self.PATH, self.FILENAME.format(user))

        if not os.path.isfile(path):
            # create json format

            if not os.path.isdir(self.PATH):
                os.mkdir(self.PATH)

            file = {
                "user": "{0}".format(ctx.author),
                "games": {
                    "sw": [],
                    "sh": [],
                    "us": [],
                    "um": [],
                    "lge": [],
                    "lgp": [],
                    "sun": [],
                    "moon": [],
                    "x": [],
                    "y": [],
                    "or": [],
                    "as": []
                }
            }
        else:

            f = open(path, "r")
            x = f.read()
            file = json.loads(x)
            f.close()

        edit = file["games"]
        if not (game in edit.keys()):
            await ctx.reply("invalid game, valid type: \n  ")
            await ctx.reply("```sw\nsh\nus\num\nlge\nlgp\nsun\nmoon\nx\ny\nor\nas```")

        else:
            found = False
            if ID.isdigit() and (len(ID) == 6 or len(ID) == 5):
                bank = edit[game]
                if len(ID) == 6:
                    if ID in bank:
                        await ctx.reply("already have this ID, your free to re-trade")
                        found = True
                else:
                    if ID in bank:
                        await ctx.reply("already have this ID, your free to re-trade")
                        found = True
                if not found:
                    bank.append(ID)
                    edit[game] = bank
                    file["games"] = edit
                    f = open(path, "w")
                    f.write(json.dumps(file))
                    f.close()
                    await ctx.reply("added id to profile")
            else:
                await ctx.reply("invalid id")

    @commands.group()
    async def delete(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.reply("please specify with adding the following")
            await ctx.send("```profile\nid\ngame ```")

    @delete.command()
    async def profile(self, ctx):
        await ctx.reply("This cannot be undone! are you sure? y/n")
             msg = await bot.wait_for('message', check=check)
            if msg.content.



# add bot token
bot.add_cog(IDC(bot))
with open('token.txt') as t:
    token = t.readline()

bot.run(token)
