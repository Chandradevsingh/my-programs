from instabot import Bot

bot = Bot()

bot.login(username = 'Jonathanjohn_77', password = 'Jonathan$70')

bot.follow('guillemlimia')

bot.upload_photo('C:/Users/welcome/Downloads/nature.jpg', caption='Green World')

bot.unfollow('guillemlimia')

bot.send_message('Hi...', ['', '', '', ''])

followers = bot.get_user_followers('Jonathanjohn_77')

for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following('Jonathanjohn_77')

for _ in following:
    print(bot.get_user_info(_))

