import json
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("up and running {0} ".format(bot.user))


class IDC(commands.Cog):
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
        print("running command")
        if not os.path.isfile("{0}.json".format(user)):
            # create json format
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
            # open file
            f = open("{0}.json".format(user), "r")
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
                    f = open("{0}.json".format(user), "w")
                    f.write(json.dumps(file))
                    f.close()
                    await ctx.reply("added id to profile")
            else:
                await ctx.reply("invalid id")


# add bot token
bot.add_cog(IDC(bot))
with open('token.txt') as t:
    token = t.readline()

bot.run(token)
