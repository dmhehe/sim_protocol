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



TYPE_LIST = [
    INT_16,
    INT_32,
    INT_64,
    FLOAT_32,
    FLOAT_64,
    STR,
]

class D:
    def __init__(self, itype, value=None, list_data_cls=None) -> None:
        self.itype = itype
        self.value = value
        self.list_data_cls = list_data_cls
        if self.itype not in TYPE_LIST:
            raise Exception("itype error")
        
    def get_itype(self):
        return self.itype
    
    def get_value(self):
        return self.value
    

    def get_list_data_cls(self):
        return self.list_data_cls


g_CheckS2CDict = {}

def S2C(param1, param2):
    #检查类型
    if not(type(param1) is int):
        raise Exception("param1 must be int")
    
    if not(type(param2) is int):
        raise Exception("param2 must be int")
    
    
    #检查是否重复
    global g_CheckS2CDict
    g_CheckS2CDict[param1] = g_CheckS2CDict.get(param1, {})
    
    if g_CheckS2CDict[param1].get(param2) is not None:
        raise Exception("S2C repeat")
    
    g_CheckS2CDict[param1][param2] = True
    
    
    class NewS2C:
        def __init__(self):
            pass

    NewS2C.mid1 = param1
    NewS2C.mid2 = param2
    NewS2C.type = "S2C"
    
    
    return NewS2C




g_CheckC2SDict = {}

def C2S(param1, param2):
    
    if not(type(param1) is int):
        raise Exception("param1 must be int")
    
    if not(type(param2) is int):
        raise Exception("param2 must be int")
    
    
    
    #检查是否重复
    global g_CheckC2SDict
    g_CheckC2SDict[param1] = g_CheckC2SDict.get(param1, {})
    
    if g_CheckC2SDict[param1].get(param2) is not None:
        raise Exception("S2C repeat")
    
    g_CheckC2SDict[param1][param2] = True
    
    class NewC2S:
        def __init__(self):
            pass

    NewC2S.mid1 = param1
    NewC2S.mid2 = param2
    NewC2S.type = "C2S"
    return NewC2S




i16 = D(INT_16)
i32 = D(INT_32)
i64 = D(INT_64)
i = i64


f32 = D(FLOAT_32)
f64 = D(FLOAT_64)

f = f64

s = D(STR)



