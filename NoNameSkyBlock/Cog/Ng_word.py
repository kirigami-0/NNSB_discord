import discord
from discord.ext import commands
#いろんなやつ格納
zyogai_ch = 000000000000000000000

class Ng_word(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('NGワード部分')
        print('┣━除外チャンネルIDを登録しました？')
        print('┗━多分そんなにいらない\n')
    
    @commands.Cog.listener()
    async def on_message(self,message):
        
        def NG():
            temp = f'{message.author.mention}様\n失礼ですが周りのご迷惑となる言葉は\nお控えください。'
            return temp
            
        if message.channel.id != zyogai_ch:
            if message.content.startswith('死ね'):
                msg = NG()
            elif  message.content.startswith('氏ね'):
                msg = NG()
            elif  message.content.startswith('お前邪魔'):
                msg = NG()
            elif  message.content.startswith('クソ'):
                msg = NG()
            elif  message.content.startswith('お前'):
                msg = NG()
            elif  message.content.startswith('てめぇ'):
                msg = NG()
            elif  message.content.startswith('キチガイ'):
                msg = NG()
            elif  message.content.startswith('ガキ'):
                msg = NG()
            elif  message.content.startswith('餓鬼'):
                msg = NG()
            elif  message.content.startswith('クズ'):
                msg = NG()
            elif  message.content.startswith('SEX'):
                msg = NG()
            elif  message.content.startswith('セックス'):
                msg = NG()
            elif  message.content.startswith('せっくす'):
                msg = NG()
            elif  message.content.startswith('オナニー'):
                msg = NG()
            elif  message.content.startswith('おなにー'):
                msg = NG()
            elif  message.content.startswith('フェラ'):
                msg = NG()
            elif  message.content.startswith('ふぇら'):
                msg = NG()
            elif  message.content.startswith('アクメ'):
                msg = NG()
            elif  message.content.startswith('乳首イキ'):
                msg = NG()
            elif  message.content.startswith('おっぱい'):
                msg = NG()
            elif  message.content.startswith('乳首'):
                msg = NG()
            elif  message.content.startswith('オマンコ'):
                msg = NG()
            elif  message.content.startswith('おまんこ'):
                msg = NG()
            elif  message.content.startswith('ちんこ'):
                msg = NG()
            elif  message.content.startswith('ちんちん'):
                msg = NG()
            elif  message.content.startswith('ちんぽ'):
                msg = NG()
            elif  message.content.startswith('ペニス'):
                msg = NG()
            elif  message.content.startswith('撞木ぞり'):
                msg = NG()
            elif  message.content.startswith('百閉'):
                msg = NG()
            elif  message.content.startswith('志がらみ'):
                msg = NG()
            elif  message.content.startswith('鵯越えの逆落とし'):
                msg = NG()
            elif  message.content.startswith('立ち花菱'):
                msg = NG()
            elif  message.content.startswith('雁が首'):
                msg = NG()
            elif  message.content.startswith('浮き橋'):
                msg = NG()
            elif  message.content.startswith('うしろやぐら'):
                msg = NG()
            elif  message.content.startswith('抱き地蔵'):
                msg = NG()
            elif  message.content.startswith('鶯の谷渡り'):
                msg = NG()
            elif  message.content.startswith('首引き恋慕'):
                msg = NG()
            elif  message.content.startswith('立ち鼎'):
                msg = NG()
            elif  message.content.startswith('茶臼のばし'):
                msg = NG()
            elif  message.content.startswith('締め小股'):
                msg = NG()
            elif  message.content.startswith('鵯越え'):
                msg = NG()
            elif  message.content.startswith('時雨茶臼'):
                msg = NG()
            elif  message.content.startswith('松葉崩し'):
                msg = NG()
            elif  message.content.startswith('仏壇返し'):
                msg = NG()
            elif  message.content.startswith('菊一文字'):
                msg = NG()
            elif  message.content.startswith('帆かけ茶臼'):
                msg = NG()
            elif  message.content.startswith('理非知らず'):
                msg = NG()
            elif  message.content.startswith('本駒駆け'):
                msg = NG()
            elif  message.content.startswith('絞り芙蓉'):
                msg = NG()
        ##送信
        await message.channel.send(msg)


    
    

def setup(bot):
    return bot.add_cog(Ng_word(bot))
