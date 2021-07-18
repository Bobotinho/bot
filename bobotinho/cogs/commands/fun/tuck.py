# -*- coding: utf-8 -*-
from bobotinho.utils import checks, convert

description = "Coloque alguém do chat na cama para dormir"
usage = "digite o comando e o nome de alguém para colocá-lo na cama"
extra_checks = [checks.banword]


async def func(ctx, arg: str):
    name = convert.str2name(arg)
    if name == ctx.bot.nick:
        ctx.response = "eu não posso dormir agora..."
    elif name == ctx.author.name:
        ctx.response = "você foi para a cama"
    else:
        ctx.response = f"você colocou @{name} na cama 🙂👉🛏"
