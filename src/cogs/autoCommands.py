"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot

"""
import discord
from discord.ext import commands
import aiohttp
from src.utils import utils
from src.utils import logging

class AutoCommands(commands.Cog):
	""" These commands will fire automatically."""

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		await self.bot.change_presence(activity=discord.Game(name="Fornite"))
		logging.info(f'{self.bot.user.name} is Online...')

	@commands.Cog.listener()
	async def on_member_join(self, member: discord.Member):
		picture_api = 'http://shibe.online/api/shibes?count=1&urls=true'
		result = await utils._fetch(picture_api)

		random_picture = result[0]

		channel = member.guild.system_channel
		if channel is not None:
			welcome_msg = discord.Embed(title="Welcome",
										description=f"welcome {member.mention}, Introduce yourself to community.")
			welcome_msg.set_thumbnail(
				url="https://cdn3.iconfinder.com/data/icons/chat-bot-emoji-filled-color/300/35618308Untitled-3-512.png")
			welcome_msg.set_image(url=random_picture)
			welcome_msg.set_footer(
				text="Image credit: https://shibe.online/")
			await channel.send(embed=welcome_msg)
			await member.send("welcome to the Server!\nPlease introduce yourself in server.\nOfficial Server for Cybel https://discord.gg/JfbK3bS")

	@commands.Cog.listener()
	async def on_member_remove(self, member: discord.Member):
		channel = member.guild.system_channel
		if channel is not None:
			bye_msg = discord.Embed(
				description=f"{member} has left the server.")
			bye_msg.set_image(url="https://cdn.pixabay.com/photo/2016/09/28/17/50/frogs-1701047_1280.jpg")
			await channel.send(embed=bye_msg)
			


def setup(bot: commands.Cog):
	bot.add_cog(AutoCommands(bot))
