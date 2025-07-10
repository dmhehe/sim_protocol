

import os
import glob
import importlib
import inspect
from _protocol.base import *
import json


def get_source_code(cls):
    # 获取类所在的模块
    module = inspect.getmodule(cls)
    # 获取类的源代码
    source_lines, _ = inspect.getsourcelines(cls)
    # 将源代码连接成字符串
    source_code = ''.join(source_lines)
    return source_code



class MakeJson:
    def __init__(self) -> None:
        #放S2C类的字典
        self.m_S2C_Class_Dict = {}
        #放C2S类的字典
        self.m_C2S_Class_Dict = {}
        #放其他类的字典
        self.m_Other_Class_Dict = {}

        self.m_S2C_Json = {}
        self.m_C2S_Json = {}

    def init_class_names(self, module_name):
        module = importlib.import_module(module_name)
        classes = inspect.getmembers(module, inspect.isclass)
        # class_names = [cls[0] for cls in classes]
        # print(f"Classes in module {module_name}: {class_names}")


        module_name = module_name.replace("_protocol.", "")

        #获取遍历里面的所有类
        for cls in classes:
            cls_name = cls[0]
            cls_type = cls[1]

            name = module_name + "." + cls_name
            if cls_name.startswith("S2C"):
                self.m_S2C_Class_Dict[name] = cls_type
            elif cls_name.startswith("C2S"):
                self.m_C2S_Class_Dict[name] = cls_type
            else:
                self.m_Other_Class_Dict[name] = cls_type



    #加载文件夹下的所有py文件
    def import_classes_in_files(self, folder_path):
        py_files = glob.glob(os.path.join(folder_path, "*.py"))


        for py_file in py_files:
            module_name = os.path.basename(py_file)[:-3]  # Remove .py extension
            print(f"Importing module {module_name} from {py_file}")
            module_name = f"{os.path.basename(folder_path)}.{module_name}"
            self.init_class_names(module_name)


    def get_cls_json(self, cls_type):
        ans_list = []
        
        mid1 = None
        mid2 = None
        try:
            mid1 = cls_type.__base__.mid1
            mid2 = cls_type.__base__.mid2
        except:
            pass
        
        # if not(type(mid1) is int and type(mid1) is int):
        #     raise Exception("mid1, mid2 must be int")

        str_code = get_source_code(cls_type)
        short_code = "".join(str_code.split())
        
        attrList = []
        for attr_name, attr_value in cls_type.__dict__.items():
            if short_code.find(attr_name) >= 0:#数据必须在代码上有定义
                attrList.append(attr_name)

        def sortFunc(attr_name):
            return short_code.find(attr_name)

        attrList.sort(key=sortFunc)

        #不能用变量命名为mid11 和 mid1
        if "mid1" in attrList or "mid2" in attrList:  
            raise Exception("mid1, mid2 must not in" +  str_code) 

        for attr_name in attrList:
            attr_value = cls_type.__dict__[attr_name]
            
            item_attr = attr_value
            
            isList = False
            if type(attr_value) is list:
                isList = True
                if len(attr_value) > 1:
                    raise Exception("attr error "+attr_name)

                item_attr = attr_value[0]
                
            # if isinstance(item_attr, int) or isinstance(item_attr, str) or isinstance(item_attr, float):
            #     raise Exception("attr error "+attr_name)
            
            #这个数据的类型
            itype = 1
            if isinstance(item_attr, D):
                itype = attr_value.get_itype()
            
            if isList:  #列表类型
                _, _, ans_list2 = self.get_cls_json(item_attr)
                #类型版本 和  对应的list类型就是相差100
                ans_list.append((itype+100, attr_name, ans_list2))
            elif not isinstance(item_attr, D):#自定义类型
                _, _, ans_list2 = self.get_cls_json(item_attr)
                ans_list.append((OBJ, attr_name, ans_list2))
            else:#基础类型
                ans_list.append((itype, attr_name))

        return mid1, mid2, ans_list
        
    def make_json(self):
        for name, cls_type in self.m_S2C_Class_Dict.items():
            mid1, mid2, json_list = self.get_cls_json(cls_type)
            if mid1 not in self.m_S2C_Json:
                self.m_S2C_Json[mid1] = {}

            dict1 = self.m_S2C_Json[mid1]
            dict1[mid2] = json_list


        for name, cls_type in self.m_C2S_Class_Dict.items():
            mid1, mid2, json_list = self.get_cls_json(cls_type)
            if mid1 not in self.m_C2S_Json:
                self.m_C2S_Json[mid1] = {}

            dict1 = self.m_C2S_Json[mid1]
            dict1[mid2] = json_list


        self._ensure_directory_exists("jsondata")
        self._ensure_directory_exists("pydata")

        self.output_json("jsondata/s2c.json", self.m_S2C_Json)
        self.output_json("jsondata/c2s.json", self.m_C2S_Json)
        self.output_py_data("pydata/s2c.py", self.m_S2C_Json, "g_S2C")
        self.output_py_data("pydata/c2s.py", self.m_C2S_Json, "g_C2S")


	
    def _ensure_directory_exists(self, directory):
        os.makedirs(directory, exist_ok=True)

    def output_py_data(self, file_path, new_data, name):
        dict_string = repr(new_data)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(name + ' = ' + dict_string)
            
    def output_json(self, file_path, new_data):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)
            
def main():
    folder_path = "_protocol"
    obj = MakeJson()
    obj.import_classes_in_files(folder_path)
    obj.make_json()
    

main()
