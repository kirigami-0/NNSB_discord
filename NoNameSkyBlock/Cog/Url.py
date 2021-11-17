import discord
from discord.ext import commands

class Url(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print('URL飛ばし（未完成）')
        print('┣━リンクあってます？')
        print('┣━公式サイト')
        print('┗━Github\n')

    @commands.command()
    async def nnsb(self,ctx):
        embed = discord.Embed(
            title = '\n公式サイトについて',
            description='現在鋭意製作中です。\nしばらくお待ち下さい。',
            color = 0xa2d7dd
            )
        embed.set_author(
            name = 'NNSB公式サイト',
            url = 'https://seesaawiki.jp/no_name_sky_block/',
        )
        embed.set_thumbnail(
            url=''
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def github(self,ctx):
        embed = discord.Embed(
            title = '\nGitHubについて',
            description='現在、システム\n建築\nテクスチャ班が足りません。\n\n絶賛募集中です。',
            color = 0x66ff00
            )
        embed.set_author(
            name = 'NNSB公式GitHub',
        )
        embed.set_thumbnail(
            url=''
        )
        
        await ctx.send(embed=embed)


def setup(bot):
    return bot.add_cog(Url(bot))
