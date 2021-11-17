import discord
from discord.ext import commands

#リアクションロール用チャンネル。
reaction_id = ':sasasa:'
ch_id = 000000000000000
nnsb_role_id = 12345678

class Reaction_roll(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print('リアクションロール（未完成）')
        print('┣━ロールIDは登録しました？')
        print('┣━絵文字IDは登録しました？')
        print('┗━チャンネルIDは登録しました？\n')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        if payload.member.bot:
            return
        if payload.channel_id != ch_id:
            return
        
        if payload.emoji.name == 'reaction_id':
            await payload.member.add_roles(
                payload.member.guild.get_roles(nnsb_role_id))



def setup(bot):
    return bot.add_cog(Reaction_roll(bot))