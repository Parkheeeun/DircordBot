'''
# .cogs/Music.py
import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")

def setup(client):
    client.add_cog(Music(client))

def __init__(self, client):
    option = {
            'format': 'bestaudio/best',
            'noplaylist': True,
        }
    self.client = client
    self.DL = YoutubeDL(option)
@commands.command(name ="음악재생")
async def play_music(self, ctx, url):
		#봇의 음성 채널 연결이 없으면
    if ctx.voice_client is None: 
        # 명령어(ctx) 작성자(author)의 음성 채널에 연결 상태(voice)
        if ctx.author.voice:
            # 봇을 명령어 작성자가 연결되어 있는 음성 채널에 연결
            await ctx.author.voice.channel.connect()
        else:
            embed = discord.Embed(title = '오류 발생', description = "음성 채널에 들어간 후 명령어를 사용 해 주세요!", color = discord.Color.red())
            await ctx.send(embed=embed)
            raise commands.CommandError("Author not connected to a voice channel.")
    # 봇이 음성채널에 연결되어 있고, 재생중이라면
    elif ctx.voice_client.is_playing():
        # 현재 재생중인 음원을 종료
        ctx.voice_client.stop()
    await ctx.send(url)
    embed = discord.Embed(title = '음악 재생', description = '음악 재생을 준비하고있어요. 잠시만 기다려 주세요!' , color = discord.Color.red())
    await ctx.send(embed=embed)

    data = self.DL.extract_info(url, download = False)
    link = data['url']
    title = data['title']

    ffmpeg_options = {
        'options': '-vn',
        "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
    }
    player = discord.FFmpegPCMAudio(link, **ffmpeg_options, executable = "/Users/parkheeeun/Downloads/ffmpeg/bin/ffmpeg")
    ctx.voice_client.play(player)
    
    embed = discord.Embed(title = '음악 재생', description = f'{title} 재생을 시작힐게요!' , color = discord.Color.blue())
    await ctx.send(embed=embed)
'''



import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
from .module.youtube import getUrl

class Music(commands.Cog):
    def __init__(self, client):
        option = {
                'format': 'bestaudio/best',
                'noplaylist': True,
            }

        self.client = client
        self.DL = YoutubeDL(option)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")
    

    @commands.command(name ="음악재생")
    async def play_music(self, ctx, *keywords):
        if ctx.voice_client is None: 
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                embed = discord.Embed(title = '오류 발생', description = "음성채널에 들어간 후 명령어를 사용해주세요!", color = discord.Color.red())
                await ctx.send(embed=embed)
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        
        keyword = ' '.join(keywords)
        url = getUrl(keyword)
        
        await ctx.send(url)
        embed = discord.Embed(title = '음악 재생', description = '음악재생을 준비하고있어요. 잠시만 기다려주세요~!' , color = discord.Color.green())
        await ctx.send(embed=embed)

        data = self.DL.extract_info(url, download = False)
        link = data['url']
        title = data['title']

        ffmpeg_options = {
            'options': '-vn',
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        }
        player = discord.FFmpegPCMAudio(link, **ffmpeg_options, executable = "/Users/parkheeeun/ffmpeg/bin/ffmpeg")
        ctx.voice_client.play(player)
        
        embed = discord.Embed(title = '음악 재생', description = f'{title} 재생을 시작힐게요!' , color = discord.Color.blue())
        await ctx.send(embed=embed)

        
    @commands.command(name ="음악종료")
    async def quit_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_connected():
            await voice.disconnect()
            embed = discord.Embed(title = '', description = '음악 재생을 종료합니다.' , color = discord.Color.blue())
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Music(client))
