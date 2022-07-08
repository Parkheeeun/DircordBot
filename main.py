# main.py
import discord
from cogs.music import Music
from cogs.lunch import Lunch
from discord.ext import commands
import os

def main():
       
        prefix = '!'
        intents = discord.Intents.all()

        client = commands.Bot(command_prefix=prefix, intents = intents, help_command=None)

        @client.command(name = 'hello')
        async def _ping(ctx):
            await ctx.send("hello!")


        @client.event
        async def on_member_join(member):
            if member.dm_channel:
                channel = member.dm_channel
            else:
                channel = await member.create_dm()
            name = member.name
            await channel.send(f"{name}님, 안녕하세요! 제 서버에 오신걸 환영합니다. 명령어추천:!음악재생 금지된사랑")



        for filename in os.listdir('./cogs'):
            if '.py' in filename:
                filename = filename.replace('.py', '')
                client.load_extension(f"cogs.{filename}")
        with open('token.txt','r') as f:
            token=f.read()
            
        client.run(token)
if __name__ == '__main__':
    main()




