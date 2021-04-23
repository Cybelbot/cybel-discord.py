from discord.ext import commands
import discord


class MusicCommands(commands.Cog, name="Commands for music activity."):
	def __init__(self, bot):
		self.bot = bot


def setup(bot: commands.Cog):
	bot.add_cog(MusicCommands)
