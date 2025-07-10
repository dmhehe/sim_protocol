# -*- coding: utf-8 -*-

from sendpublic import *
from typing import Protocol


class P_S2CAllItem_item_list(Protocol):
    id: int
    name: str
    num: int



class P_S2CAllItem_first_item(Protocol):
    id: int
    name: str
    num: int



class P_S2CAllItem(Protocol):
    first_item: P_S2CAllItem_first_item
    item_list: list[P_S2CAllItem_item_list]



def S2CAllItem_2(pid:int, data:P_S2CAllItem):
    doSendData(pid, 101, 3, data)






def S2COneInfo_1(pid:int , attname: str, val: int):
    Prepare()
    PackString(attname)
    PackInt(val)
    PacketSend(pid)

class P_S2COneInfo(Protocol):
    attname: str
    val: int



def S2COneInfo_2(pid:int, data:P_S2COneInfo):
    doSendData(pid, 101, 2, data)






def S2CPlayerInfo_1(pid:int , name: str, grade: int):
    Prepare()
    PackString(name)
    PackInt(grade)
    PacketSend(pid)

class P_S2CPlayerInfo(Protocol):
    name: str
    grade: int



def S2CPlayerInfo_2(pid:int, data:P_S2CPlayerInfo):
    doSendData(pid, 101, 1, data)





