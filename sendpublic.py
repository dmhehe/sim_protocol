# -*- coding: utf-8 -*-

import pydata.s2c






OBJ = 1  # 对象类型
INT_16 = 2
INT_32 = 3
INT_64 = 4
FLOAT_32 = 5
FLOAT_64 = 6
STR = 7


OBJ_LIST = 101
INT_16_LIST = 102
INT_32_LIST = 103
INT_64_LIST = 104
FLOAT_32_LIST = 105
FLOAT_64_LIST = 106
STR_LIST = 107



def PackFunc(json_list, data):
    for i in json_list:
        itype = i[0]
        name = i[1]
        if itype == OBJ:
            new_data = data[name]
            PackFunc(i[2], new_data)
            
        elif itype == OBJ_LIST:
            new_data = data[name]
            PackInt(len(new_data))
            for item in new_data:
                PackFunc(i[2], item)
        elif itype == INT_16:
            new_data = data[name]
            PackInt(new_data)
        elif itype == INT_16_LIST:
            new_data = data[name]
            PackInt(len(new_data))
            for item in new_data:
                PackInt(item)
        elif itype == INT_32:
            new_data = data[name]
            PackInt(new_data)
        elif itype == INT_32_LIST:
            new_data = data[name]
            PackInt(len(new_data))
            for item in new_data:
                PackInt(item)
        elif itype == INT_64:
            new_data = data[name]
            PackInt(new_data)
        elif itype == INT_64_LIST:
            new_data = data[name]
            PackInt(len(new_data))
            for item in new_data:
                PackInt(item)
        elif itype == STR:
            new_data = data[name]
            PackString(new_data)
        elif itype == STR_LIST:
            new_data = data[name]
            PackInt(len(new_data))
            for item in new_data:
                PackString(item)
                

def doSendData(pid: int, mid1: int, mid2: int, data):
    """
    发送数据的函数
    :param mid1: 消息ID1
    :param mid2: 消息ID2
    :param data: 数据内容，必须是符合Protocol的类型
    """
    # 这里可以添加实际的发送逻辑，比如通过网络发送数据
    # print(f"Sending data with mid1={mid1}, mid2={mid2}, data={data}")
    
    json_list = pydata.s2c.g_S2C.get(mid1, {}).get(mid2)
    
    Prepare()
    PackInt(mid1)
    PackInt(mid2)
    PackFunc(json_list, data)
    PacketSend(pid)







def UnPackFunc(json_list):
    data = {}
    for i in json_list:
        itype = i[0]
        name = i[1]
        if itype == OBJ:
            data[name] = UnPackFunc(i[2])
            
        elif itype == OBJ_LIST:
            ilen = UnPackInt()
            if (ilen > 1000):
                raise ValueError(f"List length {ilen} exceeds maximum limit of 1000")
            new_data = []
            data[name] = new_data
            for j in range(ilen):
                item = UnPackFunc(i[2])
                new_data.append(item)
                
        elif itype == INT_16:
            data[name] = UnPackInt()
        elif itype == INT_16_LIST:
            ilen = UnPackInt()
            if (ilen > 1000):
                raise ValueError(f"List length {ilen} exceeds maximum limit of 1000")
            new_data = []
            data[name] = new_data
            for j in range(ilen):
                item = UnPackInt()
                new_data.append(item)
        elif itype == INT_32:
            data[name] = UnPackInt()
        elif itype == INT_32_LIST:
            ilen = UnPackInt()
            if (ilen > 1000):
                raise ValueError(f"List length {ilen} exceeds maximum limit of 1000")
            new_data = []
            data[name] = new_data
            for j in range(ilen):
                item = UnPackInt()
                new_data.append(item)
        elif itype == INT_64:
            data[name] = UnPackInt()
        elif itype == INT_64_LIST:
            ilen = UnPackInt()
            if (ilen > 1000):
                raise ValueError(f"List length {ilen} exceeds maximum limit of 1000")
            new_data = []
            data[name] = new_data
            for j in range(ilen):
                item = UnPackInt()
                new_data.append(item)
        elif itype == STR:
            data[name] = UnPackString()
        elif itype == STR_LIST:
            ilen = UnPackInt()
            if (ilen > 1000):
                raise ValueError(f"List length {ilen} exceeds maximum limit of 1000")
            new_data = []
            data[name] = new_data
            for j in range(ilen):
                item = UnPackString()
                new_data.append(item)

    return data

def doUnpackData(pid:int, mid1: int, mid2: int):
    json_list = pydata.s2c.g_C2S.get(mid1, {}).get(mid2)
    
    data = UnPackFunc(json_list)
    return data