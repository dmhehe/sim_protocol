# -*- coding: utf-8 -*-

from sendpublic import *
from typing import Protocol


class D_S2CAllItem_item_list(Protocol):
    id: int
    name: str
    num: int



class D_S2CAllItem_first_item(Protocol):
    id: int
    name: str
    num: int



class D_S2CAllItem(Protocol):
    first_item: D_S2CAllItem_first_item
    item_list: list[D_S2CAllItem_item_list]



def S2CAllItem_2(pid:int, data:D_S2CAllItem):
    doSendData(pip, 101, 3, data)


class D_S2COneInfo(Protocol):
    attname: str
    val: int



def S2COneInfo_2(pid:int, data:D_S2COneInfo):
    doSendData(pip, 101, 2, data)


class D_S2CPlayerInfo(Protocol):
    name: str
    grade: int



def S2CPlayerInfo_2(pid:int, data:D_S2CPlayerInfo):
    doSendData(pip, 101, 1, data)

