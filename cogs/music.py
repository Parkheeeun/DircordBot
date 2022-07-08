import discord
from discord.ext import commands
# from discord.opus import load_opus
# from discord.opus import _load_default
# from discord.opus import is_loaded
from youtube_dl import YoutubeDL
from .module.youtube import getUrl
# #from ctypes import *
# import ctypes
# from ctypes.util import find_library
#import opuslib

class Music(commands.Cog):
    
    # opuslib._load_default()
    # opuslib.load_opus()
    # if not opuslib.is_loaded():
    #     raise commands.CommandError('Opus failed to load')
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
    

    @commands.command(name ="음악재생",description="노래제목을 입력해주시면 노래가 재생됩니다. 금지된사랑듣는걸추천")
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
        embed = discord.Embed(title = '음악 재생', description = '음악재생을 준비중. 잠시만 기다려주세요~!' , color = discord.Color.green())
        await ctx.send(embed=embed)

        data = self.DL.extract_info(url, download = False)
        link = data['url']
        title = data['title']

        ffmpeg_options = {
            'options': '-vn',
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        }
        player = discord.FFmpegPCMAudio(link, **ffmpeg_options, executable = "/Users/parkheeeun/Downloads/ffmpeg")
        ctx.voice_client.play(player)
        
        embed = discord.Embed(title = '음악 재생', description = f'{title} 재생 시작!' , color = discord.Color.blue())
        await ctx.send(embed=embed)

        
    @commands.command(name ="음악종료",description="현재 재생중인 음악을 종료합니다.")
    async def quit_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_connected():
            await voice.disconnect()
            embed = discord.Embed(title = '', description = '음악 재생 종료.' , color = discord.Color.blue())
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Music(client))
