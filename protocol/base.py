INT_16 = 1
INT_32 = 2
FLOAT = 3
STR = 4


LIST = 10
INT_16_LIST = 11
INT_32_LIST = 12
FLOAT_LIST = 13
STR_LIST = 14


TYPE_LIST = [
    INT_16,
    INT_32,
    FLOAT,
    STR,


    LIST,
    INT_16_LIST,
    INT_32_LIST,
    FLOAT_LIST,
    STR_LIST,
]

class Data:
    def __init__(self, itype, value=None, list_data_cls=None) -> None:
        self.itype = itype
        self.value = value
        self.list_data_cls = list_data_cls 

    def get_itype(self):
        return self.itype
    
    def get_value(self):
        return self.value
    

    def get_list_data_cls(self):
        return self.list_data_cls
    

