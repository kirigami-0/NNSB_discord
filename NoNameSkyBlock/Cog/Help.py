#いろいろインポート
import discord
from discord import colour
from discord.ext import commands

#クラス宣言
class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    #このクラスが読み込まれたかを確認する。
    @commands.Cog.listener()
    async def on_ready(self):
        print('ヘルプ部分')
        print('┗━埋め込みメッセージで送りつける\n')
        
    #ヘルプコマンド
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
            value = '**NNSB**制作に参加したい人へ\n押すとロールが付与されます。/nロールの有効期限は1時間です。/n１時間以内に専用チャンネルでフォームに記入してください。',
            inline = False
            )
        await ctx.send(embed=embed)
        
#コグを有効化する
def setup(bot):
    return bot.add_cog(Help(bot))
