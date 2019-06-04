from wxpy import *
import time

# crate the bot
bot =Bot()

# Use the bot to test a msg
bot.file_helper.send_msg("Hello my body!")
bot.file_helper.send_image("test.jpg")

# Join the group chat
my_group_chat = bot.groups().search('acm new ass')[0]

# Send a msg to group
my_group_chat.send_msg("大家好!我是Saeba的机器人")
time.sleep(3)
my_group_chat.send_image("group_test.png")
time.sleep(2)
my_group_chat.send_msg("要跟我聊天吗?不聊也要聊,除非那位正在打游戏的带哥把脚本关掉..")

# Create a tuling Bot
tuling = Tuling(api_key = 'be8f8245391e4ffbbbe535f43c131de4')

# watch
@bot.register(my_group_chat)
def reply_my_friend(msg):
    tuling.do_reply(msg, True)
    pass

bot.join()
