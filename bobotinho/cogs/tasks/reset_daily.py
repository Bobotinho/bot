# # -*- coding: utf-8 -*-
import asyncio
import os
from datetime import datetime, time, timedelta

from bobotinho.database import models
from bobotinho.logger import log


async def func(bot) -> None:
    while True:
        now = datetime.utcnow()
        target = datetime.combine(now.date(), time(9, 0, 0))
        if now.hour > 9:
            target += timedelta(days=1)
        delta = (target - now).total_seconds()
        await asyncio.sleep(delta, loop=bot.loop)
        log.info("Resetting daily cookies...")
        os.environ["RESETTING_DAILY"] = "1"
        sponsors = await models.User.filter(sponsor=True).all().values_list("id", flat=True)
        await models.Cookie.filter(id__in=sponsors).update(daily=2)
        await models.Cookie.filter(id__not_in=sponsors, daily=0).update(daily=1)
        log.info("Daily cookies reset")
        os.environ["RESETTING_DAILY"] = "0"
