import discord
import os
import json

from discord.ext import commands, tasks
from itertools import cycle

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

intents = discord.Intents.all()
client = commands.Bot(command_prefix = get_prefix, intents=intents)
status = cycle(['!help for help!', 'Stay tuned for more'])


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('ball'))
    change_status.start()
    print('Bot is ready.')

@client.event
async def on_guild_join(guild):

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

@client.command()
async def change_prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4)

    await ctx.send(f'Prefix changed to: {prefix}')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#def is_it_me(ctx):
#    return ctx.author.id == 992991780062646372

#@client.command()
#@commands.check(is_it_me)
#async def example(ctx):
#    await ctx.send(f'Hi, I\'m {ctx.author}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command does not exist, refer to !help for known commands.')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'clogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('OTk0OTUzMTE3NTI5NTU5MDQy.GTb6Nw.fnGHdVWO-tSwI25ZJsgy6Hyibqz3QbFnWKwcWk')
