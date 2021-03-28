#!/usr/bin/env python3
import discord
import typing
from discord.ext import commands
import os
import random
import gifs
from dotenv import load_dotenv

load_dotenv()


bot = commands.Bot(command_prefix='!')

incorrectPingErrMsg = "ping a user ya donkass"


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def hug(ctx, arg1, gif: typing.Optional[str] = "mf"):
    if arg1.startswith("<@!") and arg1.endswith(">"):
        await ctx.send("<@!{0}> hugged {1}".format(ctx.author.id, arg1))

        if gif == "mm":
            await ctx.send(random.choice(gifs.hugmm))

        elif gif == "mf":
            await ctx.send(random.choice(gifs.hugmf))

        elif gif == "ff":
            await ctx.send(random.choice(gifs.hugff))

        else:
            await ctx.send(random.choice(gifs.hugmf))
    elif "<@!" in ctx.message.content and ">" in ctx.message.content:
        await ctx.send("the command format is \"{}hug [user] [mm/mf/ff]\"".format(bot.command_prefix))
    else:
        await ctx.send(incorrectPingErrMsg)


@ bot.command()
async def kiss(ctx, arg1, gif: typing.Optional[str] = "mf"):
    if arg1.startswith("<@!") and arg1.endswith(">"):
        await ctx.send("<@!{0}> kissed {1}".format(ctx.author.id, arg1))

        if gif == "mm":
            await ctx.send(random.choice(gifs.kissmm))

        elif gif == "mf":
            await ctx.send(random.choice(gifs.kissmf))

        elif gif == "ff":
            await ctx.send(random.choice(gifs.kissff))

        else:
            await ctx.send(random.choice(gifs.kissmf))

    elif "<@!" in ctx.message.content and ">" in ctx.message.content:
        await ctx.send("the command format is \"{}kiss [user] [mm/mf/ff]\"".format(bot.command_prefix))

    else:
        await ctx.send(incorrectPingErrMsg)


@ bot.command()
async def cuddle(ctx, arg1, gif: typing.Optional[str] = "mf"):
    if arg1.startswith("<@!") and arg1.endswith(">"):
        await ctx.send("<@!{0}> cuddled {1}".format(ctx.author.id, arg1))

        if gif == "mm":
            await ctx.send(random.choice(gifs.cuddlemm))

        elif gif == "mf":
            await ctx.send(random.choice(gifs.cuddlemf))

        elif gif == "ff":
            await ctx.send(random.choice(gifs.cuddleff))

        else:
            await ctx.send(random.choice(gifs.cuddlemf))

    elif "<@!" in ctx.message.content and ">" in ctx.message.content:
        await ctx.send("the command format is \"{}cuddle [user] [mm/mf/ff]\"".format(bot.command_prefix))
    else:
        await ctx.send(incorrectPingErrMsg)

bot.run(os.getenv("TOKEN"))
