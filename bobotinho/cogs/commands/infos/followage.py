# -*- coding: utf-8 -*-
from bobotinho.apis import twitch
from bobotinho.utils import checks, convert, timetools

description = "Saiba há quanto tempo algum usuário segue algum canal"
aliases = ["fa"]
extra_checks = [checks.banword]


async def func(ctx, arg1: str = "", arg2: str = ""):
    name = convert.str2name(arg1, default=ctx.author.name)
    channel = convert.str2name(arg2, default=ctx.channel.name)
    if name and channel:
        followage = await twitch.TwitchAPI.followage(channel, name)
        name = "você" if name == ctx.author.name else f"@{name}"
        channel = "você" if channel == ctx.author.name else f"@{channel}"
    if name == f"@{ctx.bot.nick}":
        ctx.response = f"eu sempre estive em {channel}..."
    elif name == channel:
        ctx.response = f"{name} não pode se seguir"
    elif not followage:
        ctx.response = f"{name} não segue {channel}"
    elif "não existe" in followage:
        ctx.response = followage
    elif age := timetools.birthday(followage):
        ctx.response = f"hoje completa {age} que {name} segue {channel} 🎂"
    else:
        ctx.response = f"{name} segue {channel} há {followage}"
