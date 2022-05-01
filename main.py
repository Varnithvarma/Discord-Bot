import discord
from discord.ext import commands

Client = commands.Bot(command_prefix='.')


@Client.event
async def on_ready():
    print("Bot is ready")


@Client.event
async def on_memberjoin(member):
    print(f"{member} has joined the server!")


@Client.command()
async def Hello(ctx):
    await ctx.send(f"Hello Sir!")


@Client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked{member.mention}")


@Client.command()
async def Ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned{member.mention}")


Client.run('[Enter your token]')
