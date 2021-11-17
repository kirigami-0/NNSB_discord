import discord
from discord import activity
from discord.colour import Color
from discord.ext import commands
from discord.flags import Intents
intents = discord.Intents.all()

key = "ODkwODkzNzczODAwODg2Mjky.YU2bew.KAVXW7BYmiuBR2_TuJjNoIy8Wy4"

bot = commands.Bot(
    command_prefix="n.",
    help_command=None,
    activity=discord.Game("NNSB"),
    intents=intents
    )

bot.load_extension('Cog.Omikuji')
bot.load_extension('Cog.Reaction_roll')
bot.load_extension('Cog.Ng_word')
bot.load_extension('Cog.Welcome')
bot.load_extension('Cog.Help')
bot.load_extension('Cog.Url')
bot.load_extension('Cog.Join')

bot.run(key)