import discord
from discord.ext import commands

import random

class Omikuji(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('おみくじ部分')
        print('┗[大吉,中吉,吉,末吉,凶,大凶,You Lose!!,You Winner]\n')
        
    @commands.command()
    async def omi(self,ctx):
        result = [
            '　 大吉　 ',
            '　 中吉　 ',
            '　　 吉 　　',
            '　 末吉　 ',
            '　　 凶　　 ',
            '　 大凶　 ',
            'You Lose!!',
            'You Winner'
            ]
        res = '||' + random.choice(result) + '||'

        await ctx.channel.send(f'{ctx.author.mention}\n今日の運勢は\n' + res + 'でした。')

def setup(bot):
    return bot.add_cog(Omikuji(bot))
