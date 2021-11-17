import discord
from discord import colour
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('ヘルプ部分')
        print('┗━埋め込みメッセージで送りつける\n')

    @commands.command()
    async def help(self,ctx):
        embed = discord.Embed(
            title = 'ヘルプ',
            description='いろんな機能を持っております。',
            color = 0xfaff1a
            )
        embed.add_field(
            name = 'n.omi',
            value = 'おみくじができます。',
            inline = False
            )
        embed.add_field(
            name = 'n.nnsb',
            value = '**No Name Sky Block**の公式サイトを表示します。',
            inline = False
            )
        embed.add_field(
            name = 'n.github',
            value = '**NNSB**のgithubリンクを表示します。',
            inline = False
            )
        embed.add_field(
            name = 'n.join',
            value = '**NNSB**制作に参加したい人へ\n押すとDMが届きます。了承すると。専用のロールが付与されます。',
            inline = False
            )
        await ctx.send(embed=embed)


def setup(bot):
    return bot.add_cog(Help(bot))