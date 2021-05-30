# -*- coding: utf-8 -*-
from bobotinho.database import models
from bobotinho.utils import checks

description = "Pause o bot"
extra_checks = [checks.is_mod]


async def func(ctx):
    ctx.bot.channels[ctx.channel.name]["status"] = False
    await models.Channel.filter(user_id=ctx.bot.channels[ctx.channel.name]["id"]).update(status=False)
    ctx.response = "você me desligou 💤"
