import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import os
bot = commands.Bot( command_prefix = '!')

bot.remove_command('mute')
@bot.event
async def ready():
	print('ready')
	
@bot.command()
@commands.has_permissions(administrator = True)

async def muting(ctx, member: discord.Member, time:int):
	await ctx.channel.purge(limit = 1)

	roles = discord.utils.get(ctx.message.guild.roles, name = 'muted' )
	await member.add_roles(roles)
	await ctx.send(f'Есс, +мут {member.mention}, юхууу!')
	await asyncio.sleep(time * 60)
	await member.remove_roles(roles)
@bot.command()
@commands.has_permissions(administrator = True)
async def unmuting(ctx, member: discord.Member):
	await ctx.channel.purge(limit = 1)
	roles = discord.utils.get(ctx.message.guild.roles, name = 'muted' )
	await member.remove_roles(roles)
	ctx.send(f'Эххх, +размученный {member.mention},:(.')

token = os.environ.get('BOT_TOKEN')
bot.run(token)
