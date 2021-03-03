'''
I'm learning to use regular expresions, and after reading all the confusing symbols I decided I needed to play a little. This is what I came up with :)

Inspired by:
'The Mom song', by Anita Renfroe
https://youtu.be/YYukEAmoMCQ
'''

import re

the_mom_song = "Get up now\nGet up now\nGet up out of bed\nWash your face\nBrush your teeth\nComb your sleepy head\nHere's your clothes\nAnd your shoes\nHear the words I said\nGet up now\nGet up and make your bed\nAre you hot?\nAre you cold?\nAre you wearing that?\nWhere's your books and your lunch and your homework at?\nGrab your coat and your gloves and your scarf and hat\nDon't forget you gotta feed the cat\nEat your breakfast\nThe experts tell us it's the most important meal of all\nTake your vitamins so you will grow up one day to be big and tall\nPlease remember the orthodon'tist will be seeing you at three today?\nDon't forget your piano lesson is this afternoon\nSo you must play\nDon't shovel\nChew slowly\nBut hurry\nThe bus is here\nBe careful\nCome back here\nDid you wash behind your ears?\nPlay outside\nDon't play rough\nWould you just play fair?\nBe polite\nMake a friend\nDon't forget to share\nWork it out\nWait your turn\nNever take a dare\nGet along\nDon't make me come down there\nClean your room\nFold your clothes\nPut your stuff away\nMake your bed\nDo it now\nDo we have all day?\nWere you born in a barn?\nWould you like some hay\nCan you even hear a word I say?\nAnswer the phone\nGet Off the phone\nDon't sit so close\nTurn it down\nNo texting at the table\nNo more computer time tonight\nYour ipod's my ipod if you don't listen up\nWhere you going and with whom and what time do you think you're coming home?\nSaying thank you, please, excuse me\nMakes you welcome everywhere you roam\nYou'll appreciate my wisdom\nSomeday when you're older and you're grown\nCan't wait 'til you have a couple little children of your own\nYou'll thank me for the counsel I gave you so willingly\nBut right now\nI thank you not to roll your eyes at me\nClose your mouth when you chew\nWould appreciate\nTake a bite\nMaybe two\nOf the stuff you hate\nUse your fork\nDo not you burp\nOr I'll set you straight\nEat the food I put upon your plate\nGet an A, Get the door\nDon't get smart with me\nGet a Grip\nGet in here I'll count to 3\nGet a job\nGet a life\nGet a Phd\nGet a dose of...\nI don't care who started it\nYou're grounded until your 36\nGet your story straight\nAnd tell the truth for once for heaven's sake\nAnd if all your friends jumped off a cliff\nWould you jump too?\nIf I've said it once, I've said at least a thousand times before that\nYou're too old to act this way\nIt must be your father's DNA\nLook at me when I am talking\nStand up straight when you walk\nA place for everything\nAnd everything must be in place\nStop crying or I'll give you something real to cry about\nOh!\nBrush your teeth\nWash your face\nGet your pjs on\nGet in bed\nGet a hug\nSay a prayer with Mom\nDon't forget\nI love you\n\"Kiss\"\nAnd tomorrow we will do this all again\n because a mom's work never ends\nYou don't need the reason why\nBecause\nBecause\nBecause\nBecause\nI said so\nI said so\nI said so\nI said so\nI'm the Mom\nThe mom\nThe mom\nThe mom\nThe mom\nTa-da."

print(the_mom_song)

donot_regex = re.compile(r'do(n\'t| not)', re.I)
do_regex = re.compile(r'Do')
now_regex = re.compile(r'now', re.I)
you_regex = re.compile(r'you')
get_regex = re.compile(r'get', re.I)
i_regex = re.compile(r'I')

mo_donot = donot_regex.findall(the_mom_song)
mo_do = do_regex.findall(the_mom_song)
mo_now = now_regex.findall(the_mom_song)
mo_you = you_regex.findall(the_mom_song)
mo_get = get_regex.findall(the_mom_song)
mo_I = i_regex.findall(the_mom_song)

msg = "\n\n\nThe Mom says:\n\tdon't/do not {} times,\n\tdo {} times,\n\tyou/your/you're {} times,\n\tnow {} times,\n\tget {} times\n\tand I {} times.".format(len(mo_donot), len(mo_do), len(mo_you), len(mo_now), len(mo_get), len(mo_I))

print(msg)