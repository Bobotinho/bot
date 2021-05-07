# -*- coding: utf-8 -*-
from bobotinho.apis import twitch
from bobotinho.utils import checks, convert, timetools

description = "Saiba há quanto tempo algum usuário criou sua conta"
aliases = ["age"]
usage = "digite o comando e o nome de alguém para saber a data de criação da conta"
extra_checks = [checks.is_banword]


async def func(ctx, arg: str = None):
    name = convert.str2username(arg) or ctx.author.name
    if not name:
        ctx.response = "nome de usuário inválido"
    elif name == ctx.bot.nick:
        ctx.response = "eu sempre existi..."
    else:
        accountage = await twitch.TwitchAPI.accountage(name)
        mention = "você" if name == ctx.author.name else f"@{name}"
        if not accountage:
            ctx.response = "não foi possível verificar isso"
        elif "não existe" in accountage:
            ctx.response = accountage
        elif age := timetools.birthday(accountage):
            ctx.response = f"hoje completa {age} que {mention} criou a conta 🎂"
        else:
            ctx.response = f"{mention} criou a conta há {accountage}"