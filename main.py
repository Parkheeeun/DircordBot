# main.py
import discord
#from cogs.music import Music
#from cogs.lunch import Lunch
from youtube_dl import YoutubeDL
from discord.ext import commands
import os

def main():
        prefix = '!'
        intents = discord.Intents.all()

        client = commands.Bot(command_prefix=prefix, intents = intents)

        @client.command(name = 'hello')
        async def _ping(ctx):
            await ctx.send("hello!")
        
        for filename in os.listdir('./cogs'):
            if '.py' in filename:
                filename = filename.replace('.py', '')
                client.load_extension(f"cogs.{filename}")
        
        with open('token.txt','r') as f:
            token=f.read()
            
        client.run(token)
if __name__ == '__main__':
    main()


