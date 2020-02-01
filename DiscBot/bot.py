import discord
import random
from discord.ext import commands
import Objects
import config


bot = commands.Bot(command_prefix = config.prefix)
g = Objects.Game()

@bot.event
async def on_ready():
    print('bot is ready')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, ques):
    responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]

    await ctx.send(f'Question: {ques}\n Answer: {random.choice(responses)}')

@bot.command()
async def cls(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command() 
async def kick(ctx, member : discord.Member, * , reason=None): 
    await member.kick(reason=reason)

@bot.command() 
async def ban(ctx, member : discord.Member, * , reason=None): 
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    mem_name, mem_disc = member.split('#')

    for ban in banned_users:
        user = ban.user()

        if (user.name, user.discriminator) == (mem_name, mem_disc):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@bot.command()
async def create(ctx, args):
    player = Objects.Player(args)
    g.add(player)
    await ctx.send(str(player))

@bot.command()
async def murder(ctx, args):
    player_id = int(args) #TODO make sure args is actually an integer and not a string or something
    g.kill(player_id)

@bot.command()
async def GAME(ctx):
    await ctx.send(str(g))
    
bot.run(config.token)