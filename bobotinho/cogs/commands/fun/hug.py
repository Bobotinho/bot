# -*- coding: utf-8 -*-
from bobotinho.utils import checks, convert

description = "Dê um abraço em alguém do chat"
usage = "digite o comando e o nome de alguém para abracá-lo"
extra_checks = [checks.banword]


async def func(ctx, arg: str):
    name = convert.str2name(arg)
    if name == ctx.bot.nick:
        ctx.response = "🤗"
    elif name == ctx.author.name:
        ctx.response = "você tentou se abraçar... FeelsBadMan"
    else:
        ctx.response = f"você abraçou @{name} 🤗"
