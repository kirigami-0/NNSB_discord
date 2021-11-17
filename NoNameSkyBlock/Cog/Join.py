import discord
from discord import colour
from discord import channel
from discord.abc import User
from discord.ext import commands

n_role_system = 895688802100740186
n_role_art = 00000000000000000
n_role_texter = 00000000000000000
n_role_wiki = 00000000000000000
Adomin_role_name = str(00000000000000000)

class Join(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('参加届')
        print('┗━DM埋め込みメッセージで送りつける\n')
    
    @commands.command()
    @commands.has_role(Adomin_role_name)
    async def join(self, ctx):
        embed = discord.Embed(
            title = '参加届',
            description='内容をきちんと読んでくださいね',
            color = 0x6600ff
            )
        embed.add_field(
            name = '**参加に当たる注意**',
            value = '現在制作班には\n　・__システム班__\n　・__建築班__\n　・__テクスチャ班__\n　・__wiki編集班__\nに分かれております。',
            inline = False
            )
        embed.add_field(
            name = '__システム班__',
            value = 'NNSBのシステムを開発します。\nコマンドに自身がある人を募集しています。\n主にNNSBのシステム全般を担当することになります。\nすでに雛形は作ってあるので作業量はわずかに減少しています。\nこの班に入りたい際は\n\n```n.sys```\nと入力してください',
            inline  = False
            )
        embed.add_field(
            name = '__建築班__',
            value = '　NNSBを彩る建築を行います。\n　FAWEなどの建築用MODを使った人向けです。\n　基本は島を作りますが\n　街を作ることが確定しています\n　ファンタジー建築が得意な人は、ぜひお願いします\nこの班に入りたい際は\n\n```n.sys```\nと入力してください',
            inline  = False
            )
        embed.add_field(
            name = '__テクスチャ班__',
            value = '　NNSBのアイテムやMobのデザインを行います。\n　基本的に2Dのアイテムを作ってもらいます。\n　サイズは32pix*32pixで統一しています。\n\この班に入りたい際は\n\n```n.sys```\nと入力してください',
            inline  = False
            )
        embed.add_field(
            name = '__wiki編集班__',
            value = '　公式攻略サイトや制作陣用wikiの編集を行います。\n　常にオンラインの方が望ましいです。\n　追加したMobやアイテムなどを永遠にまとめてください。\nこの班に入りたい際は\n\n```n.sys_j```\nと入力してください',
            inline  = False
            )
        embed.set_author(
            name = 'NNSB公式サイト',
            url = 'https://seesaawiki.jp/no_name_sky_block/',
        )

        await ctx.send(embed = embed)

def setup(bot):
    return bot.add_cog(Join(bot))
