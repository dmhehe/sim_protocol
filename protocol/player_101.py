
from protocol.base import *



#物品
class item:
    id = i
    name = s
    num = i


#  i是64位整形  s是字符串


S2C_PLAYER = 101

#S2C玩家信息             父协议， 子协议
class S2CPlayerInfo(S2C(S2C_PLAYER, 1)):
    name = s   #名字
    grade = i  #等级

#玩家的一个属性            父协议， 子协议
class S2COneInfo(S2C(S2C_PLAYER, 2)):
    attname = s #属性名字
    val = i   #属性值


class S2CAllItem(S2C(S2C_PLAYER, 3)):
    first_item = item
    item_list = [item]


#客户端发给服务端
C2S_PLYAER = 101

#S2C玩家信息            父协议， 子协议
class C2SGetOneInfo(C2S(C2S_PLYAER, 1)):
    attname = s  #属性名字

    
    
    


