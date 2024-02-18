

import os
import glob
import importlib
import inspect
from protocol.base import *



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
        self.m_S2C_Class_Dict = {}
        self.m_C2S_Class_Dict = {}
        self.m_Other_Class_Dict = {}

        self.m_S2C_Json = {}
        self.m_C2S_Json = {}

    def print_class_names(self, module_name):
        module = importlib.import_module(module_name)
        classes = inspect.getmembers(module, inspect.isclass)
        # class_names = [cls[0] for cls in classes]
        # print(f"Classes in module {module_name}: {class_names}")


        module_name = module_name.replace("protocol.", "")

        
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




    def import_and_print_classes_in_files(self, folder_path):
        py_files = glob.glob(os.path.join(folder_path, "*.py"))


        for py_file in py_files:
            module_name = os.path.basename(py_file)[:-3]  # Remove .py extension
            print(f"Importing module {module_name} from {py_file}")
            module_name = f"{os.path.basename(folder_path)}.{module_name}"
            self.print_class_names(module_name)


    def get_cls_json(self, cls_type):
        ans_list = []
        tid = None
        subtid = None
        str_code = get_source_code(cls_type)
        short_code = "".join(str_code.split())
        print("111111111111", cls_type, short_code)
        attrList = []
        for attr_name, attr_value in cls_type.__dict__.items():
            if isinstance(attr_value, Data):
                if short_code.find(attr_name+"=") < 0:
                    raise Exception("attr error "+attr_name)
                
                attrList.append(attr_name)

        def sortFunc(attr_name):
            return short_code.find(attr_name)

        attrList.sort(key=sortFunc)

        if "tid" in attrList:  #如果 有 tid  那必须放在第一位置
            if attrList[0] != "tid" or attrList[1] != "subtid":
                raise Exception("tid error in " +  str_code) 

            tid = cls_type.__dict__["tid"].getvalue()
            subtid = cls_type.__dict__["subtid"].getvalue()

        for attr_name in attrList:
            if attr_name in ("tid", "subtid"):
                continue

            attr_value = cls_type.__dict__[attr_name]
            itype = attr_value.get_itype()
            
            print(f"jjjjjjjjjjjj   {attr_name}: {attr_value}")
            if itype == LIST:
                list_data_cls = self.get_list_data_cls()
                _, _, ans_list2 = self.get_cls_json(list_data_cls)
                ans_list.append((attr_name, LIST, ans_list2))
            else:
                ans_list.append((attr_name, itype))

        return tid, subtid, ans_list
        
    def make_server_json(self):
        for name, cls_type in self.m_S2C_Class_Dict.items():
            tid, subtid, json_list = self.get_cls_json(cls_type)
            if tid not in self.m_S2C_Json:
                self.m_S2C_Json[tid] = {}

            dict1 = self.m_S2C_Json[tid]
            dict1[subtid] = json_list


        for name, cls_type in self.m_C2S_Class_Dict.items():
            tid, subtid, json_list = self.get_cls_json(cls_type)
            if tid not in self.m_C2S_Json:
                self.m_C2S_Json[tid] = {}

            dict1 = self.m_C2S_Json[tid]
            dict1[subtid] = json_list

def main():
    folder_path = "protocol"
    obj = MakeJson()
    obj.import_and_print_classes_in_files(folder_path)
    obj.make_server_json()
    

main()
