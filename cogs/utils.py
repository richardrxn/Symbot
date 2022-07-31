import discord
from discord.ext import commands

class utils(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utils is loaded.')
        
    @commands.command()
    async def ping(ctx):
        await ctx.send(f'Pong! ({round(client.latency * 1000)}ms)')
        
    @commands.command(aliases = ['clr', 'purge'])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, lines : int):
        if lines <= 0:
            await ctx.send('Cannot purge less than 1 lines')
        else:
            await ctx.channel.purge(limit=lines + 1)
            
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Specify an amount to clear.')
            
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have permission to use clear, contact a Mod if you believe this is an error.')
        
        
def setup(client):
    client.add_cog(utils(client))