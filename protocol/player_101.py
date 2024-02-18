
from protocol.base import *



S2C_PLAYER = 101

class S2CPlayerInfo:
    tid = Data(INT_16, S2C_PLAYER)
    subtid = Data(INT_16, 1)
    name = Data(STR)
    grade = Data(INT_32)

class S2COneInfo:
    tid = Data(INT_16, S2C_PLAYER)
    subtid = Data(INT_16, 2)
    attname = Data(STR)



C2S_PLYAER = 101

class C2SGetOneInfo:
    tid = Data(INT_16, C2S_PLYAER)
    subtid = Data(INT_16, 1)
    attname = Data(STR)