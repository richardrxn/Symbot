import discord
import random
from discord.ext import commands

class funstuff(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Funstuff is loaded.')
        
    @commands.command(aliases = ['eightball', '8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['Of course.', 'Maybe.', 'Not at all.']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        
def setup(client):
    client.add_cog(funstuff(client))