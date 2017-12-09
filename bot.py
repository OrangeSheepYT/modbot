import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import time
import datetime
import threading

client = Bot(description="No Signal™'s Custom Moderation Bot! [BETA]", command_prefix="$", pm_help = True)


bot_version = "The bot is in BETA"


@client.event
async def on_ready():
	"""Shows bot's status"""
	print("Logged in as:")
	print("Name : No Signal Moderation")
	print("----------------")
	
@client.event
async def on_member_join(member):
	msg = "Hello and welcome {} to No Signal™! Heres a cookie for joining :cookie: uwu".format(member.mention)
	await client.send_message(member, msg)	
	await client.change_presence(game = discord.Game(type = 3, name = "Welcome {}!".format(member)))
	
tu = datetime.datetime.now()

@client.command()
async def uptime():
	"""Check bot uptime."""
	global tu
	await client.say(timedelta_str(datetime.datetime.now() - tu))
	
def timedelta_str(dt):
	days = dt.days
	hours, r = divmod(dt.seconds, 3600)
	minutes, sec = divmod(r, 60)

	if minutes == 1 and sec == 1:
		return '{0} days, {1} hours, {2} minute and {3} second.'.format(days,hours,minutes,sec)
	elif minutes > 1 and sec == 1:
		return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days,hours,minutes,sec)
	elif minutes == 1 and sec > 1:
		return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days,hours,minutes,sec)
	else:
		return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days,hours,minutes,sec)


@client.command(aliases=['p'])
async def ping():
    pingtime = time.time()
    pingms = await client.say("Please wait . . . ")
    ping = time.time() - pingtime
    await client.edit_message(pingms, "Pong!:ping_pong: The ping time is `%.01f seconds`" % ping)
	
	
client.run('Mzg5MTIyOTkxMDIxMDk2OTYx.DQ2_ZA.qtXYqtdvkMlJWVAgyIsQO5oW_uY')
