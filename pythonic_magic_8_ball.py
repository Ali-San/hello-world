'''This is Pythonic_Magic_8_Ball, a fortune-telling program.
Ask aloud (or in your mind) and you will receive the answer you need...
'''
import random
import time

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most Likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Don’t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful', 'Reply hazy', 'Try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again']

print("\tHello my friend.\n\n\tFocus on what is troubling you\n\tAsk a question in your mind\n\tand I'll give you the answer to your troubles...\n\t(press 'q' when you are ready)")

user_input = input('\n\t:')

if user_input != 'q':
    print("\n\tI do not enjoy the company of those\n\twho waste other people's time.\n\tI will be patient just this time\n\tand give you another chance.")
    user_input = input('\n\t:')
    if user_input != 'q':
        print("\n\tGood luck with that attitude. Good bye.")

if user_input.lower() == 'q':
    ball_shake = random.randint(0, len(answers) - 1)
    time.sleep(2)
    print("\n\t" + answers[ball_shake])
    print('\n\t🧙🏻')