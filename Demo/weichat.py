# coding=utf8
'''
SPECIAL THANK
OPEN SOURCE FROM littlecodersh/ItChat
GITHUB https://github.com/littlecodersh/ItChat

WEICHAT CONTRIBUITER
LAOHAN
'''
import itchat, time
import io, os
import sys
import datetime
from itchat.content import *

# unicode/encoding emoji
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# store sucking data here
messageText = ['hello','hi','你好']


# auto reply private message 
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # msg.user.send('微信自动回复: '+ '在工作[奸笑] 会迟回复')

    # lowercase sender text
    reveicemsg = msg.Text.lower()

    # under debug use(print something lah)
    print(str(datetime.datetime.now()))
    print(str(msg.User.City + " " + msg.User.NickName + ": "+ msg.Text))

    # return message to the sender
    if reveicemsg in messageText:
        itchat.send('助理回复: ' + '你好很高兴认识你[偷笑]', msg.fromUserName)
    else:
        itchat.send('助理回复: ' + '他不在[奸笑]', msg.fromUserName)



# auto reply group message 
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text + "Hello"))



# auto accept new friend
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')



itchat.auto_login(True)
itchat.run()