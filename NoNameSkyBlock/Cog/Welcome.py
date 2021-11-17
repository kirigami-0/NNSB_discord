from typing import ChainMap
import discord
from discord import guild
from discord.ext import commands

guild_id = 878266583598895124
channel_id = 878266583598895127


class Welcome(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        print('ウェルカムメッセージ\n')

    @commands.Cog.listener()
    async def on_member_join(self, member):

        guild = self.bot.get_guild(878266583598895124)
        channel = guild.get_channel(878266583598895127)

        #鯖の名前と入居者の名前を取得
        g_mane = guild.name
        mem = member.name

        #ユーザー数を取得する。
        members = sum(1 for member in guild.members if not member.bot)

        await channel.send('ようこそ!!**' + mem + '**さん\n** ' + g_mane + '**へ!!\nあなたは__【 ' + str(members) + ' 人目】__の参加者です。')

def setup(bot):
    return bot.add_cog(Welcome(bot))