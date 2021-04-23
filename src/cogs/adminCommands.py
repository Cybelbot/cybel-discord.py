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


class AdminCommands(commands.Cog, name="Commands for Server Management: Admin Commands"):
	""" Admin Level Commands

	Some commands May Require administrator access.
	"""

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		""" command to kick user

		command: !kick <member_name> <reason_to_kick>
		output: function will remove user from server with embed message.
		"""
		await ctx.message.delete()
		try:
			await member.kick(reason=reason)
			kick = discord.Embed(title=f":boot: Kicked {member.name}!",
								 description=f"Reason: {reason}\nBy: {ctx.author.mention}")
			await ctx.send(embed=kick)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def mute(self, ctx, member: discord.Member):
		""" Mute the user for voice activity

		command: !mute <member_name>
		output: It will mute the voice channel connected memeber.
		user should be connected to the voice channel.

		Cybel Need administrator access for mute command.
		"""
		await ctx.message.delete()
		try:
			await member.edit(mute=True)
			mute = discord.Embed(description=f'🔇 {member.mention} is muted by {ctx.author.mention}')
			await ctx.send(embed=mute)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def unmute(self, ctx, member: discord.Member):
		""" Unmute the user for voice activity

		command: !unmute <member_name>
		output: It will unmute the voice channel connected memeber.

		Cybel Need administrator access for mute command.
		"""
		await ctx.message.delete()
		try:
			await member.edit(unmute=True)
			unmute = discord.Embed(description=f'🔊 {member.mention} is unmuted by {ctx.author.mention}')
			await ctx.send(embed=unmute)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		""" command to ban user

		command: !ban <member> <reason>
		Cybel Need ban_members access for ban command.
		"""
		await ctx.message.delete()
		try:
			await member.ban(reason=reason)
			ban = discord.Embed(
				title=f":boom: Banned {member.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
			await ctx.send(embed=ban)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def unban(self, ctx, *, member_id: int):
		""" command to unban user.

		command: !unban <member_id>
		Cybel Need administrator access for Unban command.
		"""
		await ctx.message.delete()
		try:
			await ctx.guild.unban(discord.Object(id=member_id))
			await ctx.send(f"Unban {member_id}")
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

	@commands.command()
	@commands.has_permissions(manage_nicknames=True)
	async def chnick(self, ctx, member: discord.Member, nick):
		""" Change nicknames of the servers'members

		command: !chnick <member> <new_nickname>
		Cybel Need administrator access for change Nicknames.
		"""
		await ctx.message.delete()
		try:
			await member.edit(nick=nick)
			nickname = discord.Embed(description=f'Nickname was changed for {member.mention} ')
			await ctx.send(embed=nickname)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_category(self, ctx, category: str):
		""" Command for create category in Guild/Channel

		it will not override the previous category.
		"""
		guild = ctx.guild
		await guild.create_category(category)
		category_embed = discord.Embed(description=f'{category} category got created by {ctx.author.mention}')
		await ctx.send(embed=category_embed)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def delete_category(self, ctx, category: discord.CategoryChannel):
		""" Command for delete category from server """
		await category.delete()
		category_embed = discord.Embed(description=f"{category} category got deleted from {ctx.guild} by {ctx.author.mention}.")
		await ctx.send(embed=category_embed)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_text_channel(self, ctx, channel: str, category: discord.CategoryChannel = None):
		""" command for create text channel in Guild/Channel

		input: channel, category name

		it will not override the previous channel
		if category is not provided so It will make a channel without category.

		create category to make channel under it using !create_category
		"""
		guild = ctx.guild

		if category is None:
			await guild.create_text_channel(channel)
		else:
			await guild.create_text_channel(channel, category=category)
		txt_channel = discord.Embed(description=f'{channel} got created by {ctx.author.mention}')
		await ctx.send(embed=txt_channel)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def delete_text_channel(self, ctx, channel: discord.TextChannel):
		""" Command for delete text channel """
		await channel.delete()
		dlt_text_channel = discord.Embed(description=f"{channel} got deleted from {ctx.guild} by {ctx.author.name}.")
		await ctx.send(embed=dlt_text_channel)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def create_voice_channel(self, ctx, channel: str, category: discord.CategoryChannel = None):
		""" command for create voice channel in Guild/Channel

		input: channel, category name

		it will not override the previous channel
		if category is not provided so It will make a channel without category.

		create category to make channel under it using !create_category
		"""
		guild = ctx.guild
		if category is None:
			await guild.create_text_channel(channel)
		else:
			await guild.create_voice_channel(channel, category=category)
		voice_channel = f'{channel} got created by {ctx.author.mention}' 
		await ctx.send(embed=voice_channel)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def delete_voice_channel(self, ctx, channel: discord.VoiceChannel):
		""" Command for delete voice channel """
		await channel.delete()
		voice_channel = discord.Embed(description=f"{channel} got deleted from {ctx.guild} by {ctx.author.mention}.")
		await ctx.send(embed=voice_channel)

	@commands.command(aliases=['make_role'])
	@commands.has_permissions(manage_roles=True)
	async def create_role(self, ctx, *, new_role_name):
		""" Create New Roles in the Server """
		guild = ctx.guild
		await guild.create_role(name=new_role_name)
		role = discord.Embed(description=f'Role `{new_role_name.mention}` has been created')
		await ctx.send(embed=role)

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def give_role(self, ctx, member: discord.Member, role: discord.Role):
		""" Give role to one member """
		await member.add_roles(role)
		role = discord.Embed(f"hey {ctx.author.name}, {member.name} has been giving a role called: {role.name}")
		await ctx.send(embed=role)

	@commands.command(hidden=True)
	@commands.has_permissions(manage_roles=True)
	async def give_roll_to_all(self, ctx, role: discord.Role):
		""" Give Roll to all members in once """
		pass


def setup(bot: commands.Cog):
	bot.add_cog(AdminCommands(bot))
