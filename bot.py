import os
import asyncio
import discord
from discord.ext.commands import bot
from discord import game
from discord.ext import commands
from itertools import cycle

client = commands.Bot(command_prefix = '/', case_insensitive=True)
client.remove_command('help')
Client = discord.client
Clientdiscord = discord.Client()
players ={}
servers = list(client.servers)
status = ['users', 'Arijit Singh Live', 'and playing /help', 'Trivia Champ', 'Languages'] 

async def change_status(): 
  await client.wait_until_ready() 
  msgs = cycle(status) 
    
  while not client.is_closed:
    sum=0
    bb=len(client.servers)
    for s in client.servers:
      sum+=len(s.members)
    sum=sum+10000
    current_status = next(msgs)
    await client.change_presence(game=discord.Game(name=current_status, type=3))
    await asyncio.sleep(10)
    await client.change_presence(game=discord.Game(name="%s users" % sum, type=3))
    await asyncio.sleep(10)
    await client.change_presence(game=discord.Game(name="%s servers" % bb, type=3))
    await asyncio.sleep(10)

        
@client.event
async def on_ready():
    print('Starting the bot...')


@client.command(pass_context=True)
@commands.bot_has_permissions(kick_members=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def kick(ctx, userName: discord.User, reason):
    try:
        if ctx.message.author.server_permissions.kick_members:
            await client.kick(userName)
            await client.send_message(ctx.message.channel, '**' + str(userName) + ' has been kicked from ' + str(ctx.message.server) + '**')
        else:
            await client.say("**Bad try, you do not have the permissions to use the command.**") 
    except Exception as trasherror:
        await client.say("Unable to kick this user, error: `" + str(trasherror) + '`, requested by: `' + str(ctx.message.author) + '`')

@client.command(pass_context=True)
@commands.bot_has_permissions(kick_members=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def ban(ctx, requestedperson: discord.Member, days: int = 7):
    try:
        if ctx.message.author.server_permissions.ban_members:
            await client.ban(requestedperson, days)
            await client.say("**" + str(requestedperson) + "** has been banned from **" + str(ctx.message.server) + "** and the previous `7` days of his messages have been deleted.")
        else:
            await client.say("**Bad try, you do not have the permissions to use the command.**")
    except Exception as trasherror:
        await client.say("Unable to ban " + str(requestedperson) + ", error: **" + str(trasherror) + '`, requested by: `' + str(ctx.message.author) + '`')

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User, *, message:str): 
    await client.send_message(userName, "You have been warned for: **{}**".format(message))
    await client.say("__**Done {0} Has Been Warned!**__ ** Reason:{1}** ".format(userName,message))
    pass
              
@client.command(pass_context=True)
async def ping(ctx):
    await client.say(":ping_pong: pong!! xSSS")

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context = True)

@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member, *, role: discord.Role = None):
        if role is None:
            return await client.say("You haven't specified a role! ")

        if role not in user.roles:
            await client.add_roles(user, role)
            return await client.say("{} role has been added to {}.".format(role, user))

        if role in user.roles:
            await client.remove_roles(user, role)
            return await client.say("{} role has been removed from {}.".format(role, user))

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command()
async def ans1():
    embed = discord.Embed(
        title = ' FetchingAnswer...',
        description = '••Playing Trivia Galaxy!,••',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='© made by ❤By Dr.$trange#0135.')
    embed.set_image(url='')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/486060277046181888/8803b2ee6a2ede52bda9c117179e119d.webp?size=1024')
    embed.add_field(name='Suggested Answer', value=':one: ', inline=True)
    embed.add_field(name=':one: ', value='Team Trivia Galaxy', inline=True)
    
    await client.say(embed=embed)
    
@client.command()
async def ans2():
    embed = discord.Embed(
        title = ' FetchingAnswer...',
        description = '••Playing Trivia Galaxy!,••',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='© made by ❤By Dr.$trange#0135.')
    embed.set_image(url='')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/486060277046181888/8803b2ee6a2ede52bda9c117179e119d.webp?size=1024')
    embed.add_field(name='Suggested Answer', value=':two:  ', inline=True)
    embed.add_field(name=':two:  ', value='Team Trivia Galaxy', inline=True)
    
    await client.say(embed=embed)
    
@client.command()
async def ans3():
    embed = discord.Embed(
        title = ' FetchingAnswer...',
        description = '••Playing Trivia Galaxy!,••',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='© made by ❤By Dr.$trange#0135.')
    embed.set_image(url='')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/486060277046181888/8803b2ee6a2ede52bda9c117179e119d.webp?size=1024')
    embed.add_field(name='Suggested Answer', value=':three:    ', inline=True)
    embed.add_field(name=':three:    ', value='Team Trivia Galaxy', inline=True)
    
    await client.say(embed=embed)
    
@client.command()
async def la1():
    embed = discord.Embed(
        title = ' FetchingAnswer...',
        description = '••Lifes Only!••',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='© made by ❤By Andy Murray#7400.')
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    embed.add_field(name='Suggested Answer', value=':one: ', inline=True)
    embed.add_field(name=':one: ', value='Lifes Only', inline=True)
    
    await client.say(embed=embed)
    
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.add_roles(member, role)
        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)
        
@client.command()
async def la2():
    embed = discord.Embed(
        title = ' FetchingAnswer...',
        description = '••Lifes Only!••',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='© made by ❤By Andy Murray#7400.')
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    embed.add_field(name='Suggested Answer', value=':two: ', inline=True)
    embed.add_field(name=':two: ', value='Lifes Only', inline=True)
    
    await client.say(embed=embed)
    
@client.command()
async def la3():
    embed = discord.Embed(
        title = ' FetchingAnswer...',
        description = '••Lifes Only!••',
        colour = discord.Colour.blue()
    )
    
    embed.set_footer(text='© made by ❤By Andy Murray#7400.')
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    embed.add_field(name='Suggested Answer', value=':three: ', inline=True)
    embed.add_field(name=':three: ', value='Lifes Only', inline=True)
    
    await client.say(embed=embed)
                       
@client.command(pass_context = True)
async def unmute(ctx, member: discord.User):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await client.remove_roles(member, role)
        embed=discord.Embed(title="User Unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await client.say(embed=embed)
     else:
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await client.say(embed=embed)

@client.command(pass_context = True, aliases=['Clear'])
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an 
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
     
@client.command(pass_context=True)
async def servers():
  servers = list(bot.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_footer(text='© Made by niloj#6798.')
    embed.set_author(name='Hey there you need help! my prefix is/ and here is my some commands:')
    embed.add_field(name='/ping', value='Return ping!', inline=False)
    embed.add_field(name='/kick', value='Return kick member', inline=False)
    embed.add_field(name='/play(song name)',  value='Return play music', inline=False)
    embed.add_field(name='/ban', value='Return ban member', inline=False)
    embed.add_field(name='/mute', value='Return mute member', inline=False)
    embed.add_field(name='/unmute', value='Return unmute member', inline=False)
    embed.add_field(name='/clear', value='Return clear no.of message in the chat', inline=False)
    embed.add_field(name='/Dance', value='Return show a dance gif', inline=False)
    embed.add_field(name='/cat', value='Return show random cats photo', inline=False)
    embed.add_field(name='/angryface', value='Return show an anry pic', inline=False)
    embed.add_field(name='/Roll', value='Return Rock', inline=False)
    embed.add_field(name='Hi Champ', value='Return Helo{user}', inline=False)
    embed.add_field(name='/How are you?', value='Return Fine message', inline=False)
    embed.add_field(name='Fine', value='Return Gud', inline=False)
    embed.add_field(name='/botinfo', value='Return shows the bot owner name build date.', inline=False)
    embed.add_field(name='/Hello', value='Return Hey there!.', inline=False)
    embed.add_field(name='/say ```(any message)```', value='Bot say that ```(message)```!.', inline=False)
    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def say(ctx, *, message):
    await client.send_message(ctx.message.channel, message)
        
client.loop.create_task(change_status())

client.run('NTI5MDEyNDY3OTc2NjM0Mzc5.D2J6Dw.qHX61NF-__wUyzrnCNb_lSt9ExA')
