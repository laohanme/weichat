# coding=utf8
'''
SPECIAL THANK
OPEN SOURCE FROM littlecodersh/ItChat
GITHUB https://github.com/littlecodersh/ItChat

WEIWEI CONTRIBUITER
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


# private message auto reply
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
        itchat.send('助理回复: ' + '你好很高兴认识你[偷笑]', msg['FromUserName'])
    else:
        itchat.send('助理回复: ' + '\n他在工作[皱眉]他会迟些回复你的 \n今天是中秋节 祝福你中秋节快乐[玫瑰]', msg['FromUserName'])

    
itchat.auto_login(True)
itchat.run()
