import discord
from discord.ext import commands

class userctrl(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('UserCtrl is loaded.')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server!')

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member} for reason: {reason}')

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member} for reason: {reason}')

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

def setup(client):
    client.add_cog(userctrl(client))
