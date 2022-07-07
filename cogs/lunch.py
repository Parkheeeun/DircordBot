#cogs/Lunch.py

from discord.ext import commands
import json
import random


class Lunch(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("./data/lunch.json", 'r', encoding='utf-8') as f:
            self.lunchDict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lunch Cog is Ready")

    @commands.command(name ="점심추천")
    async def recommand_lunch(self, ctx, arg = None):
        if arg == None:
            categories = list(self.lunchDict.keys())
            category = random.choice(categories)
            lunch = random.choice(self.lunchDict[category])
            await ctx.send(f"오늘의 점심메뉴 추천: {category} 중에서 {lunch}을 추천합니다!!!")
        else:
            category = arg
            lunch = random.choice(self.lunchDict[category])
            await ctx.send(f"오늘 점심은 {lunch} 어떠세요?")

def setup(client):
    client.add_cog(Lunch(client))