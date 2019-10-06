import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import ChannelType
import asyncio
import random
import datetime
from datetime import timedelta
import os

bot = commands.Bot(command_prefix="cs!")
bot.remove_command("help")
client = discord.Client()

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="cs!help for commands", type=0), status=discord.Status("online"))
	message = ("Bot started successfully!")
	user = await bot.get_user_info("284398011310800898")
	await bot.send_message(user, message)
	print(message)
	
@bot.event
async def on_member_join(member):
	message = (f"Welcome {member.mention} to the [OFFICIAL] Creator School! Remember to read the rules and have fun!")
	await bot.send_message(member, message)

#CHANGING TEACHER NEED STATUS

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def blockdeco(ctx):
	message = await bot.get_message(ctx.message.channel, "528221270157033482")
	if ctx.message.content == "cs!blockdeco yes":
		await bot.edit_message(message, "-Block Deco Teachers: *YES*")
	if ctx.message.content == "cs!blockdeco no":
		await bot.edit_message(message, "-Block Deco Teachers: *NO*")

	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def airdeco(ctx):
	message = await bot.get_message(ctx.message.channel, "528221291099062299")
	if ctx.message.content == "cs!airdeco yes":
		await bot.edit_message(message, "-Air Deco Teachers: *YES*")
	if ctx.message.content == "cs!airdeco no":
		await bot.edit_message(message, "-Air Deco Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def tech(ctx):
	message = await bot.get_message(ctx.message.channel, "528221313114963969")
	if ctx.message.content == "cs!tech yes":
		await bot.edit_message(message, "-Tech Teachers: *YES*")
	if ctx.message.content == "cs!tech no":
		await bot.edit_message(message, "-Tech Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def glow(ctx):
	message = await bot.get_message(ctx.message.channel, "528221331062390795")
	if ctx.message.content == "cs!glow yes":
		await bot.edit_message(message, "-Glow Teachers: *YES*")
	if ctx.message.content == "cs!glow no":
		await bot.edit_message(message, "-Glow Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def core(ctx):
	message = await bot.get_message(ctx.message.channel, "528221350515703818")
	if ctx.message.content == "cs!core yes":
		await bot.edit_message(message, "-Core Teachers: *YES*")
	if ctx.message.content == "cs!core no":
		await bot.edit_message(message, "-Core Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def modern(ctx):
	message = await bot.get_message(ctx.message.channel, "528221369599655946")
	if ctx.message.content == "cs!modern yes":
		await bot.edit_message(message, "-Modern Teachers: *YES*")
	if ctx.message.content == "cs!modern no":
		await bot.edit_message(message, "-Modern Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def design(ctx):
	message = await bot.get_message(ctx.message.channel, "528221387786289153")
	if ctx.message.content == "cs!design yes":
		await bot.edit_message(message, "-Design Teachers: *YES*")
	if ctx.message.content == "cs!design no":
		await bot.edit_message(message, "-Design Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def art(ctx):
	message = await bot.get_message(ctx.message.channel, "528221408447430676")
	if ctx.message.content == "cs!art yes":
		await bot.edit_message(message, "-Art Teachers: *YES*")
	if ctx.message.content == "cs!art no":
		await bot.edit_message(message, "-Art Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def effect(ctx):
	message = await bot.get_message(ctx.message.channel, "528221431671160860")
	if ctx.message.content == "cs!effect yes":
		await bot.edit_message(message, "-Effect Teachers: *YES*")
	if ctx.message.content == "cs!effect no":
		await bot.edit_message(message, "-Effect Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def gameplay(ctx):
	message = await bot.get_message(ctx.message.channel, "528221449614262301")
	if ctx.message.content == "cs!gameplay yes":
		await bot.edit_message(message, "-Gameplay Teachers: *YES*")
	if ctx.message.content == "cs!gameplay no":
		await bot.edit_message(message, "-Gameplay Teachers: *NO*")
		
	await bot.delete_message(ctx.message)
		
@bot.command(pass_context=True)
@commands.has_role("Staff")
async def trigger(ctx):
	message = await bot.get_message(ctx.message.channel, "528221468862185472")
	if ctx.message.content == "cs!trigger yes":
		await bot.edit_message(message, "-Trigger Teachers: *YES*")
	if ctx.message.content == "cs!trigger no":
		await bot.edit_message(message, "-Trigger Teachers: *NO*")
		
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def threedl(ctx):
	message = await bot.get_message(ctx.message.channel, "528221486679326720")
	if ctx.message.content == "cs!threedl yes":
		await bot.edit_message(message, "-3DL Teachers: *YES*")
	if ctx.message.content == "cs!threedl no":
		await bot.edit_message(message, "-3DL Teachers: *NO*")
		
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def colour(ctx):
	message = await bot.get_message(ctx.message.channel, "546690051656908800")
	if ctx.message.content == "cs!colour yes":
		await bot.edit_message(message, "-Colour Teachers: *YES*")
	if ctx.message.content == "cs!colour no":
		await bot.edit_message(message, "-Colour Teachers: *NO*")
		
	await bot.delete_message(ctx.message)

#ACCEPTING TEACHERS

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def accept(ctx, user: discord.Member):
	channel = bot.get_channel("435052485065965568")
	request_channel = ctx.message.channel.name
	teacher_type_lower = request_channel.replace("-", " ")
	teacher_type_lower = teacher_type_lower.replace(" application", "")
	teacher_type = teacher_type_lower.title()
	message = ctx.message.content
	accepted_user = message.replace("cs!accept ", "")
	acceptance = (f"User: {accepted_user}\nRequested: {teacher_type}\nAnswer: Yes\nAccepted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
	await bot.send_message(channel, acceptance)

	if teacher_type == "Block Deco":
		teacher_role = get(ctx.message.server.roles, id="414368972272697344")
		applicant_role = get(ctx.message.server.roles, id="528240842352099348")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)

	if teacher_type == "Air Deco":
		teacher_role = get(ctx.message.server.roles, id="414369150581080074")
		applicant_role = get(ctx.message.server.roles, id="528267301242404874")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Tech":
		teacher_role = get(ctx.message.server.roles, id="414367660449595394")
		applicant_role = get(ctx.message.server.roles, id="528267451327184906")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Glow":
		teacher_role = get(ctx.message.server.roles, id="414367702371532800")
		applicant_role = get(ctx.message.server.roles, id="528267538103271424")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Core":
		teacher_role = get(ctx.message.server.roles, id="414367616778502144")
		applicant_role = get(ctx.message.server.roles, id="528267575222861834")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Modern":
		teacher_role = get(ctx.message.server.roles, id="414369109745205248")
		applicant_role = get(ctx.message.server.roles, id="528267616620642321")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Design":
		teacher_role = get(ctx.message.server.roles, id="414307474066374656")
		applicant_role = get(ctx.message.server.roles, id="528267680680247303")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Art":
		teacher_role = get(ctx.message.server.roles, id="414367762819842053")
		applicant_role = get(ctx.message.server.roles, id="528267733910028321")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Effect":
		teacher_role = get(ctx.message.server.roles, id="414730929454710794")
		applicant_role = get(ctx.message.server.roles, id="528267780370464779")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Gameplay":
		teacher_role = get(ctx.message.server.roles, id="414894098273796096")
		applicant_role = get(ctx.message.server.roles, id="528267823441641492")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Trigger":
		teacher_role = get(ctx.message.server.roles, id="431896062144413696")
		applicant_role = get(ctx.message.server.roles, id="528267870577098756")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "3DL":
		teacher_role = get(ctx.message.server.roles, id="524184498188058628")
		applicant_role = get(ctx.message.server.roles, id="528267909181734928")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)
	
	if teacher_type == "Colour":
		teacher_role = get(ctx.message.server.roles, id="546683085823934504")
		applicant_role = get(ctx.message.server.roles, id="546683604735098880")
		await bot.add_roles(user, teacher_role)
		await bot.remove_roles(user, applicant_role)

	role = get(ctx.message.server.roles, id="414808431581462538")
	await bot.add_roles(user, role)
	reminder = (f"Please add ◇ to the front of {user}'s name. Also check that they have the correct Teacher roles as the bot may have had a mishap. Otherwise the bot has done everything else : )")
	await bot.send_message(ctx.message.author, reminder)
	message_to_new_teacher = (f"Congratulations on becoming a {teacher_type} Teacher! Please only post lessons in your class channel, no other messages. Also, once you have taught, please post in #teacher-log the date you have taught, and the class you taught in. Thank you, and well done once again!")
	await bot.send_message(user, message_to_new_teacher)
	
	applicant_stage2_role = get(ctx.message.server.roles, id="527966801158602793")
	await bot.remove_roles(user, applicant_stage2_role)
	
	await bot.say(f"{user.mention} was accepted. Please ignore their request.")
	
	await bot.delete_message(ctx.message)

#DECLINING TEACHERS

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def decline(ctx, user: discord.Member):
	channel = bot.get_channel("435052485065965568")
	request_channel = ctx.message.channel.name
	teacher_type_lower = request_channel.replace("-", " ")
	teacher_type_lower = teacher_type_lower.replace(" application", "")
	teacher_type = teacher_type_lower.title()
	message = ctx.message.content
	declined_user = message.replace("cs!decline ", "")
	decline = (f"User: {declined_user}\nRequested: {teacher_type}\nAnswer: No\nDeclined by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}. To reapply, please complete the form again. You may need to unreact and react again on the 1st and 2nd stages of the form.*")
	await bot.send_message(channel, decline)
	
	if teacher_type == "Block Deco":
		teacher_role = get(ctx.message.server.roles, id="414368972272697344")
		applicant_role = get(ctx.message.server.roles, id="528240842352099348")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Air Deco":
		teacher_role = get(ctx.message.server.roles, id="414369150581080074")
		applicant_role = get(ctx.message.server.roles, id="528267301242404874")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Tech":
		teacher_role = get(ctx.message.server.roles, id="414367660449595394")
		applicant_role = get(ctx.message.server.roles, id="528267451327184906")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Glow":
		teacher_role = get(ctx.message.server.roles, id="414367702371532800")
		applicant_role = get(ctx.message.server.roles, id="528267538103271424")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Core":
		teacher_role = get(ctx.message.server.roles, id="414367616778502144")
		applicant_role = get(ctx.message.server.roles, id="528267575222861834")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Modern":
		teacher_role = get(ctx.message.server.roles, id="414369109745205248")
		applicant_role = get(ctx.message.server.roles, id="528267616620642321")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Design":
		teacher_role = get(ctx.message.server.roles, id="414307474066374656")
		applicant_role = get(ctx.message.server.roles, id="528267680680247303")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Art":
		teacher_role = get(ctx.message.server.roles, id="414367762819842053")
		applicant_role = get(ctx.message.server.roles, id="528267733910028321")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Effect":
		teacher_role = get(ctx.message.server.roles, id="414730929454710794")
		applicant_role = get(ctx.message.server.roles, id="528267780370464779")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Gameplay":
		teacher_role = get(ctx.message.server.roles, id="414894098273796096")
		applicant_role = get(ctx.message.server.roles, id="528267823441641492")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "Trigger":
		teacher_role = get(ctx.message.server.roles, id="431896062144413696")
		applicant_role = get(ctx.message.server.roles, id="528267870577098756")
		await bot.remove_roles(user, applicant_role)
		
	if teacher_type == "3DL":
		teacher_role = get(ctx.message.server.roles, id="524184498188058628")
		applicant_role = get(ctx.message.server.roles, id="528267909181734928")
		await bot.remove_roles(user, applicant_role)
	
	if teacher_type == "Colour":
		teacher_role = get(ctx.message.server.roles, id="546683085823934504")
		applicant_role = get(ctx.message.server.roles, id="546683604735098880")
		await bot.remove_roles(user, applicant_role)

	applicant_stage2_role = get(ctx.message.server.roles, id="527966801158602793")
	await bot.remove_roles(user, applicant_stage2_role)
	
	await bot.say(f"{user.mention} was declined. Please ignore their request.")
	
	await bot.delete_message(ctx.message)

#ACCEPTING STAFF

@bot.command(pass_context=True)
@commands.has_role("Senior Staff")
async def staffaccept(ctx, user: discord.Member):
	channel = bot.get_channel("430287093525250058")
	message = ctx.message.content
	accepted_user = message.replace("cs!staffaccept ", "")
	acceptance = (f"**NEW STAFF MEMBER**\n\n{accepted_user} is now a Helper!\nAccepted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
	await bot.send_message(channel, acceptance)

	helper_role = get(ctx.message.server.roles, id="414299910666452997")
	await bot.add_roles(user, helper_role)
	staff_role = get(ctx.message.server.roles, id="443221684594671636")
	await bot.add_roles(user, staff_role)
	
	reminder = (f"Please add ❖ to the front of {user}'s name. Also check that they have the Staff and Helper role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
	await bot.send_message(ctx.message.author, reminder)
	message_to_new_helper = (f"Congratulations on becoming a Helper and a member of the Staff team! Please moderate the chat well, and set a good example for server members. **DO NOT** ask to be promoted or for extra permissions. Thank you, and well done once again!")
	await bot.send_message(user, message_to_new_helper)
	
	await bot.say(f"{user.mention} was accepted. Please ignore their request.")
	
	await bot.delete_message(ctx.message)

#DECLINING STAFF

@bot.command(pass_context=True)
@commands.has_role("Senior Staff")
async def staffdecline(ctx, user: discord.Member):
	channel = bot.get_channel("430287093525250058")
	message = ctx.message.content
	declined_user = message.replace("cs!staffdecline ", "")
	
	message_to_declined_helper = (f"Unfortunately you weren't accepted into the Staff team. Feel free to reapply again, and if you would like a reason, please DM {ctx.message.author.mention}.")
	await bot.send_message(user, message_to_declined_helper)
	
	await bot.say(f"{user.mention} was declined. Please ignore their request.")
	
	await bot.delete_message(ctx.message)

#PROMOTING STAFF

@bot.command(pass_context=True)
@commands.has_role("Senior Staff")
async def staffpromote(ctx, user: discord.Member):
	helper_role = get(ctx.message.server.roles, id="414299910666452997")
	mod_role = get(ctx.message.server.roles, id="414299731133595648")
	admin_role = get(ctx.message.server.roles, id="414299222318383121")
	headadmin_role = get(ctx.message.server.roles, id="430202269880025109")
	coowner_role = get(ctx.message.server.roles, id="414295722205380608")
	owner_role = get(ctx.message.server.roles, id="414295547764146186")
	staff_role = get(ctx.message.server.roles, id="443221684594671636")
	seniorstaff_role = get(ctx.message.server.roles, id="554363184962863105")
	
	channel = bot.get_channel("430287093525250058")

	message = ctx.message.content
	term = "helper"
	term1 = "moderator"
	term2 = "admin"
	term3 = "headadmin"
	term4 = "coowner"
	term5 = "owner"
	words = message.split()
	
	await bot.remove_roles(user, helper_role)
	await bot.remove_roles(user, mod_role)
	await bot.remove_roles(user, admin_role)
	await bot.remove_roles(user, headadmin_role)
	await bot.remove_roles(user, coowner_role)
	await bot.remove_roles(user, owner_role)
	await bot.remove_roles(user, staff_role)
	await bot.remove_roles(user, seniorstaff_role)
	
	if term in words:
		await bot.add_roles(user, helper_role)
		await bot.add_roles(user, staff_role)
		
		promotion = (f"**NEW STAFF MEMBER**\n\n{user.mention} is now a Helper!\nAccepted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ❖ to the front of {user}'s name. Also check that they have the Staff and Helper role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "Helper"
	
	elif term1 in words:
		await bot.add_roles(user, mod_role)
		await bot.add_roles(user, staff_role)
		
		promotion = (f"**PROMOTED STAFF MEMBER**\n\n{user.mention} is now a Moderator!\nPromoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ♤ to the front of {user}'s name. Also check that they have the Staff and Moderator role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "Moderator"
	
	elif term2 in words:
		await bot.add_roles(user, admin_role)
		await bot.add_roles(user, staff_role)
		
		promotion = (f"**PROMOTED STAFF MEMBER**\n\n{user.mention} is now an Admin!\nPromoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ♙ to the front of {user}'s name. Also check that they have the Staff and Admin role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "Admin"
	
	elif term3 in words:
		await bot.add_roles(user, headadmin_role)
		await bot.add_roles(user, staff_role)
		
		promotion = (f"**PROMOTED STAFF MEMBER**\n\n{user.mention} is now a Head Admin!\nPromoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ♗ to the front of {user}'s name. Also check that they have the Staff and Head Admin role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "Head Admin"
	
	elif term4 in words:
		await bot.add_roles(user, coowner_role)
		await bot.add_roles(user, staff_role)
		await bot.add_roles(user, seniorstaff_role)
		
		promotion = (f"**PROMOTED STAFF MEMBER**\n\n{user.mention} is now a Co Owner!\nPromoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ❖ to the front of {user}'s name. Also check that they have the Staff, Senior Staff and Co Owner role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "Co Owner"
	
	elif term5 in words:
		await bot.add_roles(user, owner_role)
		await bot.add_roles(user, staff_role)
		await bot.add_roles(user, seniorstaff_role)
		
		promotion = (f"**PROMOTED STAFF MEMBER**\n\n{user.mention} is now an Owner!\nPromoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ♕ to the front of {user}'s name. Also check that they have the Staff, Senior Staff and Owner role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "Owner"
	
	else:
		await bot.say(f"{ctx.message.author.mention}, please select a valid role, 'helper', 'moderator', 'admin', 'headadmin', 'coowner' or 'owner'.")
	
	try:
		message_to_user = (f"Congratulations on becoming a {role} and a member of the Staff team! Please moderate the chat well along with other duties, and set a good example for server members. **DO NOT** ask to be promoted or for extra permissions. Thank you, and well done once again!")
		await bot.send_message(user, message_to_user)
		await bot.say(f"{user.mention} has been promoted to {role} successfully!")
	except discord.Forbidden:
		await bot.say(f"**{user.mention}, I am unable to send you a DM so the DM has been sent here instead:**\nCongratulations on becoming a {role} and a member of the Staff team! Please moderate the chat well along with other duties, and set a good example for server members. **DO NOT** ask to be promoted or for extra permissions. Thank you, and well done once again!")
		await bot.say(f"{user.mention} has been promoted to {role} successfully!")
		
#DEMOTING STAFF

@bot.command(pass_context=True)
@commands.has_role("Senior Staff")
async def staffdemote(ctx, user: discord.Member):
	helper_role = get(ctx.message.server.roles, id="414299910666452997")
	mod_role = get(ctx.message.server.roles, id="414299731133595648")
	admin_role = get(ctx.message.server.roles, id="414299222318383121")
	headadmin_role = get(ctx.message.server.roles, id="430202269880025109")
	coowner_role = get(ctx.message.server.roles, id="414295722205380608")
	owner_role = get(ctx.message.server.roles, id="414295547764146186")
	staff_role = get(ctx.message.server.roles, id="443221684594671636")
	seniorstaff_role = get(ctx.message.server.roles, id="554363184962863105")
	
	channel = bot.get_channel("430287093525250058")

	message = ctx.message.content
	term = "helper"
	term1 = "moderator"
	term2 = "admin"
	term3 = "headadmin"
	term4 = "coowner"
	term5 = "none"
	words = message.split()
	
	await bot.remove_roles(user, helper_role)
	await bot.remove_roles(user, mod_role)
	await bot.remove_roles(user, admin_role)
	await bot.remove_roles(user, headadmin_role)
	await bot.remove_roles(user, coowner_role)
	await bot.remove_roles(user, owner_role)
	await bot.remove_roles(user, staff_role)
	await bot.remove_roles(user, seniorstaff_role)
	
	if term in words:
		await bot.add_roles(user, helper_role)
		await bot.add_roles(user, staff_role)
		
		promotion = (f"**DEMOTED STAFF MEMBER**\n\n{user.mention} is now a Helper!\nDemoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ❖ to the front of {user}'s name. Also check that they have the Staff and Helper role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "now a Helper"
		role1 = "Helper"
	
	elif term1 in words:
		await bot.add_roles(user, mod_role)
		await bot.add_roles(user, staff_role)
		
		promotion = (f"**DEMOTED STAFF MEMBER**\n\n{user.mention} is now a Moderator!\nDemoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ♤ to the front of {user}'s name. Also check that they have the Staff and Moderator role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "now a Moderator"
		role1 = "Moderator"
	
	elif term2 in words:
		await bot.add_roles(user, admin_role)
		await bot.add_roles(user, staff_role)
		
		promotion = (f"**DEMOTED STAFF MEMBER**\n\n{user.mention} is now an Admin!\nDemoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ♙ to the front of {user}'s name. Also check that they have the Staff and Admin role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "now a Admin"
		role1 = "Admin"
	
	elif term3 in words:
		await bot.add_roles(user, headadmin_role)
		await bot.add_roles(user, staff_role)
		
		promotion = (f"**DEMOTED STAFF MEMBER**\n\n{user.mention} is now a Head Admin!\nDemoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, promotion)
		
		reminder = (f"Please add ♗ to the front of {user}'s name. Also check that they have the Staff and Head Admin role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "now a Head Admin"
		role1 = "Head Admin"
	
	elif term4 in words:
		demotion = (f"**DEMOTED STAFF MEMBER**\n\n{user.mention} is now a Co Owner!\nDemoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, demotion)
		
		reminder = (f"Please add ❖ to the front of {user}'s name. Also check that they have the Staff, Senior Staff and Co Owner role as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "now a Co Owner"
		role1 = "Co Owner"
	
	elif term5 in words:
		demotion = (f"**DEMOTED STAFF MEMBER**\n\n{user.mention} is no longer a Staff Member!\nDemoted by: {ctx.message.author.mention}\n*If you would like a reason, please DM {ctx.message.author.mention}.*")
		await bot.send_message(channel, demotion)
		
		reminder = (f"Please remove the Staff symbol from the front of {user}'s name and change it to a Tutor (◆) or Teacher (◇) one if required. Also check that all the Staff related roles are gone as the bot may have had a mishap. Otherwise the bot has done everything else : )")
		await bot.send_message(ctx.message.author, reminder)
		
		role = "now no longer part of the Staff Team. Thank you for everything you've brought to the server during your time as a Staff Member and for all your help"
		role1 = "out of the Staff Team"
	
	else:
		await bot.say(f"{ctx.message.author.mention}, please select a valid role, 'helper', 'moderator', 'admin', 'headadmin', 'coowner' or 'none'.")
	
	try:
		message_to_user = (f"Unfortunately you have been demoted. You are {role}.")
		await bot.send_message(user, message_to_user)
		await bot.say(f"{user.mention} has been demoted to {role1} successfully!")
	except discord.Forbidden:
		await bot.say(f"**{user.mention}, I am unable to send you a DM so the DM has been sent here instead:**\nUnfortunately you have been demoted. You are {role}.")
		await bot.say(f"{user.mention} has been demoted to {role1} successfully!")


#TEAM EVENTS

@bot.command(pass_context=True)
async def teambattlejoin(ctx):
	if ctx.message.channel.id == "611134356714684456":
		author = ctx.message.author
		dawn_role = get(ctx.message.server.roles, id="611131841331724288")
		dusk_role = get(ctx.message.server.roles, id="611131938148712448")
		dawn_channel = bot.get_channel("611132331570364437")
		dusk_channel = bot.get_channel("611132404706574346")
		join_channel = bot.get_channel("611134356714684456")
		number = random.randint(0,1)
		if number == 0:
			await bot.remove_roles(author, dusk_role)
			await bot.add_roles(author, dawn_role)
			await bot.say(f"{author.mention}, thank you for joining the Team Battle event, you have been added to {dawn_channel.mention}!")
		if number == 1:
			await bot.remove_roles(author, dawn_role)
			await bot.add_roles(author, dusk_role)
			await bot.say(f"{author.mention}, thank you for joining the Team Battle event, you have been added to {dusk_channel.mention}!")
	else:
		await bot.say(f"You can only use this command in {join_channel.mention}. Your message and this message will be deleted in approx. 30 seconds.")
		reply = (f"{ctx.message.author.mention}, you can only use this command in {join_channel.mention}. Your message and this message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)
		

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def setteam(ctx, user: discord.Member):
	dawn_role = get(ctx.message.server.roles, id="611131841331724288")
	dusk_role = get(ctx.message.server.roles, id="611131938148712448")
	dawn_channel = bot.get_channel("611132331570364437")
	dusk_channel = bot.get_channel("611132404706574346")
		
	message = ctx.message.content
	term = "dawn"
	term1 = "dusk"
	term2 = "none"
	words = message.split()
	if term in words:
		await bot.remove_roles(user, dusk_role)
		await bot.add_roles(user, dawn_role)
		await bot.say(f"{user.mention} has been added to {dawn_channel.mention} successfully!")
	
	elif term1 in words:
		await bot.remove_roles(user, dawn_role)
		await bot.add_roles(user, dusk_role)
		await bot.say(f"{user.mention} has been added to {dusk_channel.mention} successfully!")
	
	elif term2 in words:
		await bot.remove_roles(user, dawn_role)
		await bot.remove_roles(user, dusk_role)
		await bot.say(f"{user.mention} has been removed from their team successfully!")
	
	else:
		await bot.say(f"{ctx.message.author.mention}, please select a valid team, 'dawn' or 'dusk'; or 'none' if you're removing them from a team.")


#SUGGEST COMMAND

@bot.command(pass_context=True)
async def suggest(ctx):
	if ctx.message.channel.id == "528572257774338079":
		message = ctx.message.content
		messagereplace = message.replace("cs!suggest ", "")
		author = ctx.message.author
		suggestion = (f"**NEW SUGGESTION!**\n**USER ID IS:** *{ctx.message.author.id}*\n**TAG IS: *{ctx.message.author.mention}***\n**SUGGESTION IS:** *{messagereplace}*\n---")
		suggestion_channel = bot.get_channel("528573991871447050")
		await bot.send_message(suggestion_channel, suggestion)
		reply = (f"Thanks for your suggestion, {author.mention}! We will look at adding this in the future, thanks for your continued support! This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)
	else:
		correct_channel = bot.get_channel("528572257774338079")
		reply = (f"{ctx.message.author.mention}, please go to {correct_channel.mention} to use this command. This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)

#SUPPORT COMMAND	

@bot.command(pass_context=True)
async def support(ctx):
	if ctx.message.channel.id == "528572257774338079":
		message = ctx.message.content
		messagereplace = message.replace("cs!support", "")
		author = ctx.message.author
		ID = random.randint(1,1000)
		support_req = (f"**NEW SUPPORT REQUEST!**\n**USER ID IS:** *{ctx.message.author.id}*\n**TAG IS: *{ctx.message.author.mention}***\n**SUPPORT ID IS:** *{ID}*\n**REQUEST IS:** {messagereplace}\n---")
		embed = discord.Embed(title="Your Support Request", description=f"Your support request from *{ctx.message.channel.name}*", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
		embed.add_field(name="Your Support Message:", value=f"{messagereplace}", inline=False)
		embed.add_field(name=f"Your Support ID is: *{ID}*", value=f"It will be used when someone responds to your request.", inline=False)
		embed.add_field(name="Great News!", value="Your query is being handled!", inline=False)
		embed.set_thumbnail(url=bot.user.avatar_url)
		support_channel = bot.get_channel("528574066710544404")
		await bot.send_message(support_channel, support_req)
		await bot.send_message(author, embed=embed)
		confirm = (f"Your support query has been sent {author.mention}, we'll try and look at it soon. Meanwhile check your DMs for more info! This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, confirm)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)
	else:
		correct_channel = bot.get_channel("528572257774338079")
		reply = (f"{ctx.message.author.mention}, please go to {correct_channel.mention} to use this command. This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def supportresponse(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!supportresponse", "")
	embed = discord.Embed(title="Your Support Request", description=f"Your support request is complete!", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
	embed.add_field(name="Great News!", value="**Your query has a response!**\n"
											 f"Response from *{ctx.message.author}*, who says:\n"
											 f"{messagereplace}", inline=False)
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.send_message(member, embed=embed)

#HELP COMMAND

@bot.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(title="**COMMANDS**", description="This bots commands are shown below (the prefix is cs!)"
															"\n---", color=0x00ff00)
	embed.add_field(name="**GENERAL COMMANDS**", value= "**cs!help** - Displays this message for the list of bot commands\n"
													 "**cs!support** - Have a question or query about the server or bot? Just ask after cs!support\n"
													 "**cs!suggest** - Have a suggestion for the server or bot? Just tell us after cs!suggest\n"
													 "**cs!ping** - Checks and returns the bots ping\n"
													 "**cs!report** - Report a user. Type cs!report <tag user> <reason/proof>. If you need to send image proof, please DM that straight to a Staff member, ideally the owner as unforunately the bot doesn't support the sending of images. EG. cs!report @ChiefJack_YT#4450 Being the Owner\n"
													 "---")

	embed.add_field(name="**SCHOOL-RELATED COMMANDS**", value= "**cs!format** - Displays the teacher application format\n"
													 "**cs!tutor** - Request a tutor for you desired class. Type cs!tutor <class name here>. See pinned message in #private-tutoring\n"
													 "**cs!teacherrate** - Rate a teacher out of 10 (it is anonymous). Type cs!teacherrate <tag teacher> <score out of 10>. EG. cs!teacherrate @ChiefJack_YT#4450 10\n"
													 "**cs!tutorrate** - Rate a tutor out of 10 (it is anonymous). Type cs!tutorrate <tag tutor> <score out of 10>. EG. cs!tutorrate @ChiefJack_YT#4450 10\n"
													 "---")
													 
	embed.add_field(name="**EVENT COMMANDS**", value= "**cs!teambattlejoin** - Use this command in #team-join to join a Team Battle Event team\n"
													"---")
													 
	embed.add_field(name="**STAFF COMMANDS**", value= "**cs!staffhelp** - Use this for the list of Staff commands and how to use them\n"
													"---")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def staffhelp(ctx):
	embed = discord.Embed(title="**COMMANDS**", description="This bots commands are shown below (the prefix is cs!)"
															"\n---", color=0x00ff00)
	embed.add_field(name="**STAFF COMMANDS**", value= "**cs!supportresponse** - Responds to support requests. See pinned message in #support-log\n"
													"**cs![class name] [yes/no]** - Toggles whether we are accepting certain teachers. See #bot-support for more details\n"
													"**cs!accept [tag user]** - Accepts the tagged user as a teacher for the teacher application channel this is used in\n"
													"**cs!decline [tag user]** - Declines the tagged user as a teacher for the teacher application channel this is used in\n"
													"**cs!tutorresponse** - Reply to a tutor request. See pinned message in #tutor-request-log\n"
													"**cs!reportresponse** - Reply to a user report. See pinned message in #user-reports\n"
													"**cs!warn** - Warns the tagged user. Usage: cs!warn1 @ChiefJack_YT#4450 Stop spamming. Change cs!warn1 to cs!warn2 or cs!warn3 depending on if they already have a previous warning.\n"
													"---")
	embed.add_field(name="**SENIOR STAFF COMMANDS**", value= "**cs!staffaccept** - Accepts the tagged user as a new Staff member (Helper)\n"
													"**cs!staffdecline** - Declines the tagged user as a new Staff member (Helper)\n"
													"**cs!staffpromote** - Promotes the tagged user. Usage: cs!staffpromote @ChiefJack_YT#4450 helper. Change helper to moderator, admin, headadmin, coowner or owner.\n"
													"**cs!staffdemote** - Demotes the tagged user. Usage: cs!staffdemote @ChiefJack_YT#4450 helper. Change helper to moderator, admin, headadmin, coowner or none.\n"
													"---")
	embed.add_field(name="**EVENT COMMANDS**", value= "**cs!setteam [tag user] [dawn / dusk / none]** - Set the team of the tagged user in the Team Battle Event. Type dawn or dusk after the tagged user to set them to that team. Or type none to remove them from a team.\n"
													"---")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.say(embed=embed)

#2019 HALLOWEEN EVENT

#RIDDLE 1

@bot.command(pass_context=True)
async def r1a(ctx):
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def r1b(ctx):
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def r1c(ctx):
	ht1c_role = get(ctx.message.server.roles, id="630338623476072449")
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	await bot.add_roles(ctx.message.author, ht1c_role)
	await bot.remove_roles(ctx.message.author, wrong_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-2 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def r1d(ctx):
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

#OTHER 1

@bot.command(pass_context=True)
async def o1a(ctx):
	ht1c_role = get(ctx.message.server.roles, id="630338623476072449")
	await bot.remove_roles(ctx.message.author, ht1c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def o1b(ctx):
	ht2c_role = get(ctx.message.server.roles, id="630342614201401344")
	await bot.add_roles(ctx.message.author, ht2c_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-3 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht1c_role = get(ctx.message.server.roles, id="630338623476072449")
	await bot.remove_roles(ctx.message.author, ht1c_role)
	
@bot.command(pass_context=True)
async def o1c(ctx):
	ht1c_role = get(ctx.message.server.roles, id="630338623476072449")
	await bot.remove_roles(ctx.message.author, ht1c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def o1d(ctx):
	ht1c_role = get(ctx.message.server.roles, id="630338623476072449")
	await bot.remove_roles(ctx.message.author, ht1c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

#QUESTION 1

@bot.command(pass_context=True)
async def q1a(ctx):
	ht2c_role = get(ctx.message.server.roles, id="630342614201401344")
	await bot.remove_roles(ctx.message.author, ht2c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q1b(ctx):
	ht2c_role = get(ctx.message.server.roles, id="630342614201401344")
	await bot.remove_roles(ctx.message.author, ht2c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q1c(ctx):
	ht2c_role = get(ctx.message.server.roles, id="630342614201401344")
	await bot.remove_roles(ctx.message.author, ht2c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q1d(ctx):
	ht3c_role = get(ctx.message.server.roles, id="630342640038314014")
	await bot.add_roles(ctx.message.author, ht3c_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-4 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht2c_role = get(ctx.message.server.roles, id="630342614201401344")
	await bot.remove_roles(ctx.message.author, ht2c_role)

#QUESTION 2

@bot.command(pass_context=True)
async def q2a(ctx):
	ht3c_role = get(ctx.message.server.roles, id="630342640038314014")
	await bot.remove_roles(ctx.message.author, ht3c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q2b(ctx):
	ht4c_role = get(ctx.message.server.roles, id="630342656475791361")
	await bot.add_roles(ctx.message.author, ht4c_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-5 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht3c_role = get(ctx.message.server.roles, id="630342640038314014")
	await bot.remove_roles(ctx.message.author, ht3c_role)
	
@bot.command(pass_context=True)
async def q2c(ctx):
	ht3c_role = get(ctx.message.server.roles, id="630342640038314014")
	await bot.remove_roles(ctx.message.author, ht3c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q2d(ctx):
	ht3c_role = get(ctx.message.server.roles, id="630342640038314014")
	await bot.remove_roles(ctx.message.author, ht3c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

#RIDDLE 2

@bot.command(pass_context=True)
async def r2a(ctx):
	ht4c_role = get(ctx.message.server.roles, id="630342656475791361")
	await bot.remove_roles(ctx.message.author, ht4c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def r2b(ctx):
	ht4c_role = get(ctx.message.server.roles, id="630342656475791361")
	await bot.remove_roles(ctx.message.author, ht4c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def r2c(ctx):
	ht4c_role = get(ctx.message.server.roles, id="630342656475791361")
	await bot.remove_roles(ctx.message.author, ht4c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def r2d(ctx):
	ht5c_role = get(ctx.message.server.roles, id="630342676062928912")
	await bot.add_roles(ctx.message.author, ht5c_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-6 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht4c_role = get(ctx.message.server.roles, id="630342656475791361")
	await bot.remove_roles(ctx.message.author, ht4c_role)

#QUESTION 3

@bot.command(pass_context=True)
async def q3a(ctx):
	ht6c_role = get(ctx.message.server.roles, id="630342692601200641")
	await bot.add_roles(ctx.message.author, ht6c_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-7 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht5c_role = get(ctx.message.server.roles, id="630342676062928912")
	await bot.remove_roles(ctx.message.author, ht5c_role)
	
@bot.command(pass_context=True)
async def q3b(ctx):
	ht5c_role = get(ctx.message.server.roles, id="630342676062928912")
	await bot.remove_roles(ctx.message.author, ht5c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q3c(ctx):
	ht5c_role = get(ctx.message.server.roles, id="630342676062928912")
	await bot.remove_roles(ctx.message.author, ht5c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q3d(ctx):
	ht5c_role = get(ctx.message.server.roles, id="630342676062928912")
	await bot.remove_roles(ctx.message.author, ht5c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

#OTHER 2

@bot.command(pass_context=True)
async def o2a(ctx):
	ht7c_role = get(ctx.message.server.roles, id="630342708795408394")
	await bot.add_roles(ctx.message.author, ht7c_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-8 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht6c_role = get(ctx.message.server.roles, id="630342692601200641")
	await bot.remove_roles(ctx.message.author, ht6c_role)
	
@bot.command(pass_context=True)
async def o2b(ctx):
	ht6c_role = get(ctx.message.server.roles, id="630342692601200641")
	await bot.remove_roles(ctx.message.author, ht6c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def o2c(ctx):
	ht6c_role = get(ctx.message.server.roles, id="630342692601200641")
	await bot.remove_roles(ctx.message.author, ht6c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def o2d(ctx):
	ht6c_role = get(ctx.message.server.roles, id="630342692601200641")
	await bot.remove_roles(ctx.message.author, ht6c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

#QUESTION 4

@bot.command(pass_context=True)
async def q4a(ctx):
	ht7c_role = get(ctx.message.server.roles, id="630342708795408394")
	await bot.remove_roles(ctx.message.author, ht7c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q4b(ctx):
	ht8c_role = get(ctx.message.server.roles, id="630342725409046538")
	await bot.add_roles(ctx.message.author, ht8c_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-9 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht7c_role = get(ctx.message.server.roles, id="630342708795408394")
	await bot.remove_roles(ctx.message.author, ht7c_role)
	
@bot.command(pass_context=True)
async def q4c(ctx):
	ht7c_role = get(ctx.message.server.roles, id="630342708795408394")
	await bot.remove_roles(ctx.message.author, ht7c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def q4d(ctx):
	ht7c_role = get(ctx.message.server.roles, id="630342708795408394")
	await bot.remove_roles(ctx.message.author, ht7c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

#RIDDLE 3

@bot.command(pass_context=True)
async def r3a(ctx):
	ht8c_role = get(ctx.message.server.roles, id="630342725409046538")
	await bot.remove_roles(ctx.message.author, ht8c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def r3b(ctx):
	ht9c_role = get(ctx.message.server.roles, id="630342741783740446")
	await bot.add_roles(ctx.message.author, ht9c_role)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-10 and see if you can advance onto the next question! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht8c_role = get(ctx.message.server.roles, id="630342725409046538")
	await bot.remove_roles(ctx.message.author, ht8c_role)
	
@bot.command(pass_context=True)
async def r3c(ctx):
	ht8c_role = get(ctx.message.server.roles, id="630342725409046538")
	await bot.remove_roles(ctx.message.author, ht8c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	
@bot.command(pass_context=True)
async def r3d(ctx):
	ht8c_role = get(ctx.message.server.roles, id="630342725409046538")
	await bot.remove_roles(ctx.message.author, ht8c_role)
	wrong_role = get(ctx.message.server.roles, id="630338717676077056")
	wrong_channel = bot.get_channel("630341732197859329")
	await bot.add_roles(ctx.message.author, wrong_role)
	message = (f"Uh oh, that's a wrong answer! Head to {wrong_channel.mention}. Better luck next time! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

#LAST QUESTION

@bot.command(pass_context=True)
async def fa(ctx):
	survivor_channel = bot.get_channel("630401651580338199")
	end_role = get(ctx.message.server.roles, id="630355475682164786")
	await bot.add_roles(ctx.message.author, end_role)
	survivor = (f"{ctx.message.author.mention} made it out of the trail alive...")
	await bot.send_message(survivor_channel, survivor)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-end and thanks for playing! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht9c_role = get(ctx.message.server.roles, id="630342741783740446")
	await bot.remove_roles(ctx.message.author, ht9c_role)
	
@bot.command(pass_context=True)
async def fb(ctx):
	survivor_channel = bot.get_channel("630401651580338199")
	end_role = get(ctx.message.server.roles, id="630355475682164786")
	await bot.add_roles(ctx.message.author, end_role)
	survivor = (f"{ctx.message.author.mention} made it out of the trail alive...")
	await bot.send_message(survivor_channel, survivor)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-end and thanks for playing! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht9c_role = get(ctx.message.server.roles, id="630342741783740446")
	await bot.remove_roles(ctx.message.author, ht9c_role)
	
@bot.command(pass_context=True)
async def fc(ctx):
	survivor_channel = bot.get_channel("630401651580338199")
	end_role = get(ctx.message.server.roles, id="630355475682164786")
	await bot.add_roles(ctx.message.author, end_role)
	survivor = (f"{ctx.message.author.mention} made it out of the trail alive...")
	await bot.send_message(survivor_channel, survivor)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-end and thanks for playing! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht9c_role = get(ctx.message.server.roles, id="630342741783740446")
	await bot.remove_roles(ctx.message.author, ht9c_role)
	
@bot.command(pass_context=True)
async def fd(ctx):
	survivor_channel = bot.get_channel("630401651580338199")
	end_role = get(ctx.message.server.roles, id="630355475682164786")
	await bot.add_roles(ctx.message.author, end_role)
	survivor = (f"{ctx.message.author.mention} made it out of the trail alive...")
	await bot.send_message(survivor_channel, survivor)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-end and thanks for playing! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht9c_role = get(ctx.message.server.roles, id="630342741783740446")
	await bot.remove_roles(ctx.message.author, ht9c_role)
	
@bot.command(pass_context=True)
async def fe(ctx):
	survivor_channel = bot.get_channel("630401651580338199")
	end_role = get(ctx.message.server.roles, id="630355475682164786")
	await bot.add_roles(ctx.message.author, end_role)
	survivor = (f"{ctx.message.author.mention} made it out of the trail alive...")
	await bot.send_message(survivor_channel, survivor)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-end and thanks for playing! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht9c_role = get(ctx.message.server.roles, id="630342741783740446")
	await bot.remove_roles(ctx.message.author, ht9c_role)
	
@bot.command(pass_context=True)
async def ff(ctx):
	survivor_channel = bot.get_channel("630401651580338199")
	end_role = get(ctx.message.server.roles, id="630355475682164786")
	await bot.add_roles(ctx.message.author, end_role)
	survivor = (f"{ctx.message.author.mention} made it out of the trail alive...")
	await bot.send_message(survivor_channel, survivor)
	message = (f"Well done, that's correct! Now have a look for halloween-trail-end and thanks for playing! (A witch will brew this message out of extinction in approx. 30 seconds)")
	send = await bot.send_message(ctx.message.channel, message)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	ht9c_role = get(ctx.message.server.roles, id="630342741783740446")
	await bot.remove_roles(ctx.message.author, ht9c_role)

#MISC

@bot.command(pass_context=True)
async def ping(ctx):
	message1 = await bot.say(":ping_pong: Pong! Loading...")
	difference = message1.timestamp - ctx.message.timestamp
	await bot.edit_message(message1, f":ping_pong: Pong! That took {1000*difference.total_seconds():.1f}ms.")

@bot.command(pass_context=True)
async def format(ctx):
	channel = False
	staff_channel = False
	
	if ctx.message.channel.id == "528215464136933387":
		channel = True
	elif ctx.message.channel.id == "528265872008019969":
		channel = True
	elif ctx.message.channel.id == "528266014358503466":
		channel = True
	elif ctx.message.channel.id == "528266063503294484":
		channel = True
	elif ctx.message.channel.id == "528266105702318101":
		channel = True
	elif ctx.message.channel.id == "528266173280681994":
		channel = True
	elif ctx.message.channel.id == "528266221729349642":
		channel = True
	elif ctx.message.channel.id == "528266267266646036":
		channel = True
	elif ctx.message.channel.id == "528266333654351882":
		channel = True
	elif ctx.message.channel.id == "528266397340663808":
		channel = True
	elif ctx.message.channel.id == "528266444182388765":
		channel = True
	elif ctx.message.channel.id == "528266496711852035":
		channel = True
	elif ctx.message.channel.id == "546684101420253184":
		channel = True
	elif ctx.message.channel.id == "554369895383564319":
		staff_channel = True
	else:
		await bot.say("You can only use this command in a Teacher or Staff application channel.")
	
	if channel == True:
		await bot.say("**This is the format for requesting a teacher role:**\n\n"
					  "Requesting Teacher: *[teacher type you're requesting]*\n"
					  "Tutor for this class? (helping students via DM): *[yes/no]*\n"
					  "Skills: *[skills in this subject]*\n"
					  "Weaknesses: *[weaknesses in this subject]*\n"
					  "Works: *[at least 2 photos or videos showcasing your work, if you are requesting gameplay you can leave a level ID if it is under 7 stars]*")
	
	if staff_channel == True:
		await bot.say("**This is the format for applying to the Staff Team:**\n\n"
					  "Why do you want to be Staff? *[answer]*\n"
					  "What do you expect out of a Staff Member? *[answer]*\n"
					  "Experience you have? (List servers and how long you have been Staff including the member count): *[answer]*\n"
					  "What would you do as a Staff Member in this server? *[answer]*\n"
					  "What is your current age? *[answer]*")

#REQUESTING TUTORING

@bot.command(pass_context=True)
async def tutor(ctx):
	if ctx.message.channel.id == "543775636959789056":
		message = ctx.message.content
		messagereplace = message.replace("cs!tutor", "")
		author = ctx.message.author
		ID = random.randint(1,1000)
		tutor_req = (f"**NEW TUTOR REQUEST!**\n**USER ID IS:** *{ctx.message.author.id}*\n**TAG IS: *{ctx.message.author.mention}***\n**TUTOR REQUEST ID IS:** *{ID}*\n**CLASS REQUESTED IS:** {messagereplace}\n---")
		embed = discord.Embed(title="Your Tutor Request", description=f"Your tutor request from *{ctx.message.channel.name}*", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
		embed.add_field(name="Your Class Requested For Tutoring:", value=f"{messagereplace}", inline=False)
		embed.add_field(name=f"Your Tutor Request ID is: *{ID}*", value=f"It will be used when someone responds to your request.", inline=False)
		embed.add_field(name="Great News!", value="Your request is being handled!", inline=False)
		embed.set_thumbnail(url=bot.user.avatar_url)
		request_channel = bot.get_channel("544141539597746186")
		await bot.send_message(request_channel, tutor_req)
		await bot.send_message(author, embed=embed)
		confirm = (f"Your tutor request has been sent {author.mention}, we'll try and look at it soon. Meanwhile check your DMs for more info! This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, confirm)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)
	else:
		correct_channel = bot.get_channel("543775636959789056")
		reply = (f"{ctx.message.author.mention}, please go to {correct_channel.mention} to use this command. This message and your message will be deleted in approx. 30 seconds.")
		send = await bot.send_message(ctx.message.channel, reply)
		await asyncio.sleep(30)
		await bot.delete_message(ctx.message)
		await bot.delete_message(send)

@bot.command(pass_context=True)
@commands.has_any_role("◆ - Tutors", "Staff")
async def tutorresponse(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!tutorresponse", "")
	embed = discord.Embed(title="Your Tutor Request", description=f"Your tutor request is complete!", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
	embed.add_field(name="Great News!", value="**Your tutor request has a response!**\n"
											 f"Response from *{ctx.message.author}*, who says:\n"
											 f"{messagereplace}", inline=False)
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.send_message(member, embed=embed)
	reminder = (f"You are now {member}'s tutor for the style they requested. Please DM them when tutoring, and DM them a welcome message!")
	await bot.send_message(ctx.message.author, reminder)

#TEACHER RATE

@bot.command(pass_context=True)
async def teacherrate(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!teacherrate", "")
	teacher_rate = (f"**NEW TEACHER RATING!**\n**TEACHER IS:** {member.mention}\n**RATING IS:** {messagereplace}/10\n---")
	teacher_rate_channel = bot.get_channel("544201403959214090")
	await bot.send_message(teacher_rate_channel, teacher_rate)
	await bot.say(f"Your Teacher rating has been submitted successfully, {ctx.message.author.mention}!")

#TUTOR RATE

@bot.command(pass_context=True)
async def tutorrate(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!tutorrate", "")
	tutor_rate = (f"**NEW TUTOR RATING!**\n**TUTOR IS:** {member.mention}\n**RATING IS:** {messagereplace}/10\n---")
	tutor_rate_channel = bot.get_channel("544201584658350091")
	await bot.send_message(tutor_rate_channel, tutor_rate)
	await bot.say(f"Your Tutor rating has been submitted successfully!, {ctx.message.author.mention}")

#USER REPORT

@bot.command(pass_context=True)
async def report(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!report", "")
	author = ctx.message.author
	ID = random.randint(1,1000)
	report = (f"**NEW USER REPORT!**\n**USER ID IS:** *{member.id}*\n**TAG IS: *{member.mention}***\n**REPORTER USER ID IS:** *{ctx.message.author.id}*\n**REPORTER IS: *{ctx.message.author.mention}***\n**REPORT ID IS:** *{ID}*\n**REPORT IS:** {messagereplace}\n---")
	embed = discord.Embed(title="Your User Report", description=f"Your user report from *{ctx.message.channel.name}*", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
	embed.add_field(name="Your User Report:", value=f"{messagereplace}", inline=False)
	embed.add_field(name=f"Your Report ID is: *{ID}*", value=f"It will be used when someone responds to your report.", inline=False)
	embed.add_field(name="Great News!", value="Your report is being handled!", inline=False)
	embed.set_thumbnail(url=bot.user.avatar_url)
	report_channel = bot.get_channel("544206000467738626")
	await bot.send_message(report_channel, report)
	await bot.send_message(author, embed=embed)
	confirm = (f"Your user report has been sent {author.mention}, we'll try and look at it soon. Meanwhile check your DMs for more info! This message and your message will be deleted in approx. 30 seconds.")
	send = await bot.send_message(ctx.message.channel, confirm)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)

@bot.command(pass_context=True)
async def reportresponse(ctx, member: discord.Member):
	message = ctx.message.content
	messagereplace = message.replace("cs!reportresponse", "")
	embed = discord.Embed(title="Your User Report", description=f"Your user report is complete!", timestamp=datetime.datetime.utcnow(), inline=False, color=0x00FF00)
	embed.add_field(name="Great News!", value="**Your user report has a response!**\n"
											 f"Response from *{ctx.message.author}*, who says:\n"
											 f"{messagereplace}", inline=False)
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.send_message(member, embed=embed)

#WARNINGS

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def warn1(ctx, user: discord.Member):
	warn1_role = get(ctx.message.server.roles, id="414297796280188928")
	await bot.add_roles(user, warn1_role)

	try:
		message = ctx.message.content
		messagereplace = message.replace("cs!warn1", "")
		await bot.send_message(user, messagereplace)
	except:
		exception = bot.send_message(f"{user.mention} is unable to be DMed the reason. Therefore please DM {ctx.message.author.mention} if you would like a reason. This message will be deleted in approx. 30 seconds.")
	
	rules = bot.get_channel("414296584172470302")
	warning_message = (f"{user.mention} has been given Warning 1. This is your 1st Warning so there is no punishment. Please see {rules.mention} to reread the rules and see how Warnings work. The reason has been DMed to you if you have DMs enabled, if not, ask the Staff member who warned you.\n**WARNED BY:** *{ctx.message.author}*")
	warning_channel = bot.get_channel("414302090412949505")
	await bot.send_message(warning_channel, warning_message)
	
	reply = (f"{user.mention} has been given Warning 1 successfully. This message and your message will be deleted in approx. 30 seconds.")
	send = await bot.send_message(ctx.message.channel, reply)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	await bot.delete_message(exception)
	
	await asyncio.sleep(604800)
	await bot.remove_roles(user, warn1_role)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def warn2(ctx, user: discord.Member):
	warn2_role = get(ctx.message.server.roles, id="414298160215883777")
	await bot.add_roles(user, warn2_role)
	muted_role = get(ctx.message.server.roles, id="414372473753305099")
	await bot.add_roles(user, muted_role)
	
	try:
		message = ctx.message.content
		messagereplace = message.replace("cs!warn2", "")
		await bot.send_message(user, messagereplace)
	except:
		exception = bot.send_message(f"{user.mention} is unable to be DMed the reason. Therefore please DM {ctx.message.author.mention} if you would like a reason. This message will be deleted in approx. 30 seconds.")
	
	rules = bot.get_channel("414296584172470302")
	giveaways = bot.get_channel("546352695506763806")
	polls = bot.get_channel("414903624020394014")
	s_and_s = bot.get_channel("528572257774338079")
	feedback = bot.get_channel("460101527915462656")
	warning_message = (f"{user.mention} has been given Warning 2. This is your 2nd Warning; you have been muted for 10 minutes AND you no longer have access to Teacher and Staff application channels, {giveaways.mention}, {polls.mention}, {s_and_s.mention} and {feedback.mention}. Please see {rules.mention} to reread the rules and see how Warnings work. The reason has been DMed to you if you have DMs enabled, if not, ask the Staff member who warned you.\n**WARNED BY:** *{ctx.message.author}*")
	warning_channel = bot.get_channel("414302090412949505")
	await bot.send_message(warning_channel, warning_message)
	
	reply = (f"{user.mention} has been given Warning 2 successfully. This message and your message will be deleted in approx. 30 seconds.")
	send = await bot.send_message(ctx.message.channel, reply)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	await bot.delete_message(exception)
	
	await asyncio.sleep(600)
	await bot.remove_roles(user, muted_role)
	
	await asyncio.sleep(604800)
	await bot.remove_roles(user, warn2_role)

@bot.command(pass_context=True)
@commands.has_role("Staff")
async def warn3(ctx, user: discord.Member):	
	try:
		message = ctx.message.content
		messagereplace = message.replace("cs!warn3", "")
		await bot.send_message(user, messagereplace)
	except:
		exception = bot.send_message(f"{user.mention} is unable to be DMed the reason. This message will be deleted in approx. 30 seconds.")
	
	warning_message = (f"{user.mention} has been given Warning 3 and is therefore kicked from the server.\n**WARNED BY:** *{ctx.message.author}*")
	warning_channel = bot.get_channel("414302090412949505")
	await bot.send_message(warning_channel, warning_message)
	
	reply = (f"{user.mention} has been given Warning 3, and therefore a kick successfully. This message and your message will be deleted in approx. 30 seconds.")
	send = await bot.send_message(ctx.message.channel, reply)
	await asyncio.sleep(30)
	await bot.delete_message(ctx.message)
	await bot.delete_message(send)
	await bot.delete_message(exception)
	
	await bot.kick(user)

bot.run(os.environ["TOKEN"])