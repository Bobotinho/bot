# -*- coding: utf-8 -*-
from collections import namedtuple


def create_afks():
    __keys = ["emoji", "afk", "isafk", "returned", "rafk"]
    __values = [
        ["afk", "🏃⌨", "ficou AFK", "AFK", "voltou", "AFK"],
        ["art", "🎨", "foi desenhar", "desenhando", "desenhou", "desenhando"],
        ["brb", "🏃⌨", "volta já", "fora", "voltou", "fora"],
        ["code", "💻", "foi programar", "programando", "programou", "programando"],
        ["food", "🍽", "foi comer", "comendo", "comeu", "comendo"],
        ["game", "🎮", "foi jogar", "jogando", "jogou", "jogando"],
        ["gn", "💤", "foi dormir", "dormindo", "acordou", "dormindo"],
        ["work", "💼", "foi trabalhar", "trabalhando", "trabalhou", "trabalhando"],
        ["shower", "🚿", "foi pro banho", "no banho", "tomou banho", "o banho"],
        ["study", "📚", "foi estudar", "estudando", "estudou", "estudando"],
    ]
    return {value[0]: namedtuple(value[0], __keys)(*value[1:]) for value in __values}


afks = create_afks()
