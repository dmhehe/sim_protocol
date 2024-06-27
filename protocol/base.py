INT_16 = 1
INT_32 = 2
FLOAT_32 = 3
STR = 4
INT_64 = 5
FLOAT_64 = 6



LIST = 10
INT_16_LIST = 11
INT_32_LIST = 12
FLOAT_32_LIST = 13
STR_LIST = 14
INT_64_LIST = 15
FLOAT_64_LIST = 16


TYPE_LIST = [
    INT_16,
    INT_32,
    FLOAT_32,
    STR,
    INT_64,
    FLOAT_64,
    

    LIST,
    INT_16_LIST,
    INT_32_LIST,
    FLOAT_32_LIST,
    STR_LIST,
    INT_64_LIST,
    FLOAT_64_LIST,
]

class D:
    def __init__(self, itype, value=None, list_data_cls=None) -> None:
        self.itype = itype
        self.value = value
        self.list_data_cls = list_data_cls
        if self.itype not in TYPE_LIST:
            raise Exception("itype error")
        
        if self.itype == LIST:
            if list_data_cls is None:
                raise Exception("list_data_cls is None")

    def get_itype(self):
        return self.itype
    
    def get_value(self):
        return self.value
    

    def get_list_data_cls(self):
        return self.list_data_cls



i16 = D(INT_16)
i32 = D(INT_32)
i64 = D(INT_64)
i = i64


f32 = D(FLOAT_32)
f64 = D(FLOAT_64)

f = f64

s = D(STR)



