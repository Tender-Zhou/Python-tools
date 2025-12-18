import os
import time
from pathlib import Path
def welcome():
    print(
         "=========================\n"
          "欢迎使用总结生成器系统\n"
          "请使用数字键选择需要的功能\n"
          "1.添加模板\n"
          "2.生成总结\n"
          "3.查看生成总结\n"
          "4.退出程序\n"
          "========================="
        )
    
def chose_function(chose):
    choose=int(chose)
    if choose==1:
        add_moudle()
    elif choose==2:
        make_moudle()
    elif choose==3:
        look_moudle()
    elif choose==4:
        exit()
    else:
        print("无效的输入！")

def add_moudle():
    file_name=input("请输入新增模板的名称:")
    file_name=file_name+".txt"
    if not file_name:
        print("文件名称不能为空")
    elif os.path.exists(file_name):
        print("该文件已存在,请重新定义文件名:")
    else:
        file_contect=input("请输入模板内容:")
        with open(file_name,"w",encoding="utf-8") as f:
            f.write(file_contect)
        print("添加模板成功")
        
def make_moudle():
    file_name=input("请输入需要生成的总结名称,输入0退出该项目:")
    if file_name=="0":
        return
    else:
        file_name=file_name+".txt"
        date=time.strftime("%Y-%M",time.localtime())
        file_name=date+"_"+file_name    
        if not file_name:
            print("文件名称不能为空")
        elif os.path.exists(file_name):
            print("文件名称已存在,是否重新创建文件名:")
            new_name=input("输入Y/N进行确认:")
            if new_name=="Y":
                Path(file_name).touch()
            else:
                print("已取消")
            
        while True:
            file_input=input("请插入需要总结的内容模板,返回上传请输入0:")
        #path=C:/Users/Desktop/yeartest/file_input #?? #change file path to use
            path="C:/Users/Desktop/test/"
            if not file_input:
                print("模板名称不能为空")
            elif file_input=="0":
                return make_moudle()
            elif not os.path.exists(path+file_input):
                print("模板不存在")
            else:
                try:
                #with open (file_input,"r",encoding="utf-8") as t:
                    with open (path+file_input,"r",encoding="utf-8") as t:
                        file_content=t.read()
                    with open(file_name,"a",encoding="utf-8") as f:
                        f.write(file_content+"\n")
                    print("模板已写入")
                except Exception as e:
                    print("文件读取失败或不存在，请检查文件名是否正确")
           
def look_moudle():
    path="C:/Users/27019/Desktop/test/"
    look=True
    while look:
        try:
            file_name=input("请输入需要查看的文件名称:")
            file_name=file_name+".txt"
            with open(file_name,"r",encoding="utf-8") as f:
                file_content=f.read()
                print(file_content)
        except Exception as e:
            print("文件无法正确查看，请确定打开的文件名是否正确！")
        num=input("文件输出完毕,按0返回上层菜单:")
        if num=="0":
            return
        else:
            print("无效的输入！")
        
        
    
if __name__=="__main__":
    while True:
        welcome()
        chose=input("请输入功能序号:")
        if chose.isdigit():
            chose_function(chose)
        else:
            print("无效的输入！")
        time.sleep(2)
        os.system("cls")

        continue
