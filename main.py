import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "K?", description = "Bot en developpement")

@bot.event
async def on_ready():
    print("Le bot est lancé ✔")

@bot.command()
async def bonjour(ctx):
    await ctx.send("Bonjour !")

@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    TextChannel = len(server.text_channels)
    VoiceChannel = len(server.voice_channels)
    serverDescription = server.description
    TotalPeople = server.member_count
    serverName = server.name
    message = f"**Le serveur** **__{serverName}__** **contient** **{TotalPeople}** **personnes.** \nDescription du serveur : **{serverDescription}**. \nNombres de salon textuel : **{TextChannel}**. \nNombre de salons vocaux : **{VoiceChannel}**."
    await ctx.send(message)

@bot.command()
async def status(ctx):
    messagestatus = "**Le bot est en développement.**"
    await ctx.send(messagestatus)

bot.run("ODg2NjY0NDk2OTAxNDIzMTA0.YT44qQ.PXARLShI5Gm6lORDRkocG-4YrLk")