# -*- coding: utf-8 -*-
from bobotinho.cogs.commands import pets as P

description = "Veja os pets disponíveis para adquirir"


async def func(ctx):
    pet_list = list(P.random_pets().values())
    pets = P.join_pets(pet_list, formatter="{pet} ({price})", sep=", ")
    ctx.response = f"pets disponíveis hoje: {pets}"
