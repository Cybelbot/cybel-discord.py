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

from src.utils import askme


class ExperimentalCommands(commands.Cog, name="Experimetal Commands"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="cybel", aliases=["c"])
	async def cybel(self, ctx, *args):
		""" AI Enabled Chatbot

		commands: !cybel
		aliase command: !c

		Example:
		input: !cybel Hello
		cybel: Hi
		-------------------
		input: !cybel What is value of PI?
		cybel: Pi = 3.14
		"""
		async with ctx.typing():
			user_question = ' '.join(args)
			try:
				bot_response = askme.askMe(user_question)
				await ctx.send(bot_response)
			except Exception as e:
				await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')


def setup(bot: commands.Cog):
	bot.add_cog(ExperimentalCommands(bot))
