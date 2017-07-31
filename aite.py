#!/usr/bin/env python
# coding=utf-8

import random

def onQQMessage(bot, contact, member, content):
    rand = random.randint(1,5)
    if '@ME' in content:
        if rand == 1:
            bot.SendTo(contact, member.name + ',艾特我干嘛！我在撩妹呢！')
        elif rand == 2:
            bot.SendTo(contact, member.name + ',我在撸码呢！别来打扰我！')
        elif rand == 3:
            bot.SendTo(contact, member.name + ',你好！找我有事么？')
        elif rand == 4:
            bot.SendTo(contact, member.name + ',Welcome! (:')
        elif rand == 5:
            bot.SendTo(contact, member.name + ',你又艾特我！有事快说!')

