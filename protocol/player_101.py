
from protocol.base import *



S2C_PLAYER = 101

class S2CPlayerInfo:
    tid = D(INT_16, S2C_PLAYER)
    subtid = D(INT_16, 1)
    name = D(STR)
    grade = D(INT_32)

class S2COneInfo:
    tid = D(INT_16, S2C_PLAYER)
    subtid = D(INT_16, 2)
    attname = D(STR)



C2S_PLYAER = 101

class C2SGetOneInfo:
    tid = D(INT_16, C2S_PLYAER)
    subtid = D(INT_16, 1)
    attname = D(STR)
    
    
    


