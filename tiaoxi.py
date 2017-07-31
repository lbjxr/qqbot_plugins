# -*- coding:utf-8 -*-

import random

def onQQMessage(bot, contact, member, content):
	x = random.randint(1, 10)

	if content == '谁最帅':
		bot.SendTo(contact, '你最帅！')
	
	elif content == '谁最帅.':
		bot.SendTo(contact, '群主最帅！')
	elif content == '你叫什么':
		bot.SendTo(contact, '我叫计算机协会小C，我是计算机协会官方QQ号  (:')
	elif content == '笑话':
	    if x == 1:
	 	    bot.SendTo(contact, '''有天隔壁女孩说她家灯泡烧了让我给她换灯泡，我想机会来了，然后去到她家正在换时就随口问了句：你没有男朋友么？
									她说：有啊！
									我说：那怎么不让她换？
									她：我怕他被电死！
									我靠。。。''')
	    elif x == 2:
	 	    bot.SendTo(contact, '''我：你刚刚撤回什么了？
									女友：没什么。
									我：别以为我没看到，你发的是“你走吧”，肯定发完又后悔了是不是？
									女友：并不是。
									我：别不承认了，你舍不得我了。
									女友：你想多了，我只是觉得程度不够，你滚吧！！''')
	    elif x == 3:
	 	    bot.SendTo(contact, '''偶遇前女友，礼貌性地说了句你现在变化蛮大的。
									她笑着说：可不咋地，离开了人渣就是容光焕发。''')
	    elif x == 4:
	 	    bot.SendTo(contact, '''女A ：“真想体验一下有钱人的感觉，那种上Tao.bao不考虑预算的！”
									女B：“活该你吊丝，有钱人不上Tao.bao！”''')
	    elif x == 5:
	 	    bot.SendTo(contact, '''我爸跟我妈说：我们李家跟你们唐家还是很有渊源的，你看我们李家建个朝代都叫唐朝。
									我。。。''')
	    elif x == 6:
	 	    bot.SendTo(contact, '''每次方便面里有“秘制酱包”的时候，我都要四下看看确定没有人了才拆。''')
	    elif x == 7:
	 	    bot.SendTo(contact, '''上联：爱妻，爱子，爱家庭，不爱群主等于零。
									下联：有钱，有权，有成功，没有群主一场空。
									横批：群主无价''')
	    elif x == 8:
	 	    bot.SendTo(contact, '''教大家一个脸显白的方法：把脖子晒黑！''')
	    elif x == 9:
	 	    bot.SendTo(contact, '''心如死灰不代表绝望，因为还有个词儿叫死灰复燃。。。''')
	    elif x == 10:
	 	    bot.SendTo(contact, '''“穷”大概是一种什么样的感受呢？
									喜欢的东西没货了，竟然如释重负松了一口气。''')

