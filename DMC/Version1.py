# Version1 ------FW   初始化窗口
from tkinter import *
from tkinter import ttk, filedialog, messagebox, scrolledtext
import tkinter
import openpyxl
import threading
import serial
import serial.tools.list_ports
import re
from tkinter import font


class Init_Window():
# Init window, lable, button, frame layout

    def __init__(self, name):
        self.init_window = name
    # widget config init
    def set_init_window(self):
        self.init_window.title('1# HSCB G Value Result Check')  #Title
        self.init_window.geometry("1024x768-10+10")     # window size and position
        #self.init_window.iconbitmap('C:\\Natlqs\Projects\\1# HSCB DMC Result Confirm\\icon.ico')
        self.init_window.configure(bg='white')      # Background color 
        self.init_window.attributes('-alpha', 1)


        # Buttons    按钮的command参数必须要指向一格函数进行调用
        self.file_choose_button=Button(self.init_window, text = '清空当前DMC', bg='red', font='helvetic 20 bold',width=10, command=self.clear_current_DMC)
        self.file_choose_button.place(x=410, y=240)      # place 布局， x, y指距离窗口左上端点的位置，像素位置
        self.file_choose_button=Button(self.init_window, text = '选择G值文件', bg='lightgray', font='helvetic 15 bold',width=10, command=self.thread_file)
        self.file_choose_button.place(x=415, y=197.5)      # place 布局， x, y指距离窗口左上端点的位置，像素位置
        self.file_choose_button=Button(self.init_window, text = '开始自动检查', bg='lightgreen', font='helvetic 20 bold',width=12, command=self.autoscan)
        self.file_choose_button.place(x=20, y=240)      # place 布局， x, y指距离窗口左上端点的位置，像素位置
        self.file_choose_button=Button(self.init_window, text = '重新扫描', bg='orange', font='helvetic 20 bold',width=10, command=self.rescan)
        self.file_choose_button.place(x=230, y=240)      # place 布局， x, y指距离窗口左上端点的位置，像素位置

        # Serial Frames
        self.com_choose_frame=Frame(self.init_window)
        self.com_choose_frame.place(x=20, y=10)


        # Serial 框架内容纳多个容器
        self.com_label=Label(self.com_choose_frame, text='COM:',font='helvetic 15 bold')
        self.com_label.grid(row=0, column=0, sticky=E)
        self.baudrate_label=Label(self.com_choose_frame, text='Baudrate:',font='helvetic 15 bold')
        self.baudrate_label.grid(row=1, column=0, sticky=E, pady=10)


        # Serial 框架内下拉选项
        self.com_choose=StringVar(value='请选择COM')
        self.com_choose_combobox=ttk.Combobox(self.com_choose_frame, width=20, textvariable=self.com_choose)
        self.com_choose_combobox['state']='readonly'
        self.com_choose_combobox.grid(row=0, column=1, padx=15)     # grid 是表格式结构，行列都是从0开始，padx表示x方向上两栏的间距
        self.com_choose_combobox['values']=self.com_name_get()      # 调用扫描com端口列表的函数，该函数返回值为一个数组


        # 波特率选项
        self.baudrate_value=StringVar(value='请选择波特率')
        self.baudrate_choose_combobox=ttk.Combobox(self.com_choose_frame, width=20, textvariable=self.baudrate_value)


        # 选项框中选中的值会赋值给字符串变量，并显示在combobox上
        self.baudrate_choose_combobox['values']=('9600', '115200')
        self.baudrate_choose_combobox['state']='readonly'
        self.baudrate_choose_combobox.grid(row=1, column=1, padx=15)


        # Serial 框架内按钮
        self.connect_button=Button(self.com_choose_frame, text='打开串口', bg='lightgray', width=15, command=self.com_connect)
        self.connect_button.grid(row=0, column=2, padx=20)
        self.close_button=Button(self.com_choose_frame, text='关闭串口', bg='lightgray', width=15, command=self.com_close)
        self.close_button.grid(row=1, column=2, padx=20)


        # 处理结果显示滚动文本框
        self.connect_status=scrolledtext.ScrolledText(self.init_window,width=58,height=40)
        self.connect_status.place(x=580, y=10)


        # 滚动文本框是tkinter库自带的一个小封装，将text构件scrollbar滚动条组合形成，可以直接调用
        self.com_log_text=Text(self.com_choose_frame, width=65, height=6)
        self.com_log_text.grid(row=2, column=0, columnspan=3, pady=5)
        self.com_log_text.insert(END, '此处显示串口工作信息' + '\n')
        
        
        self.file_path_text=Text(self.init_window, width=55, height=2)
        self.file_path_text.place(x=20,y=200)
        self.file_path_text.insert(tkinter.INSERT, self.thread_file())

        #
        self.current_DMC=Text(self.init_window, width=22, height=5, font='arial 30 bold')
        self.current_DMC.place(x=20, y=300)
        self.current_DMC.insert(tkinter.INSERT, 'aaa')
        


    def thread_file(file_path):
            file_path=filedialog.askopenfilename()
            print (file_path)
            file_path=file_path.replace('/', '\\')
            print(file_path)
            return file_path

    ''' 
        多线程无法取得返回值
        def thread_file(file_path1):
        def file_path(file_path3):
            #file_folder=filedialog.askdirectory()     # 获取选择好的文件夹路径
            file_path0= filedialog.askopenfilename()     # 获取选择好的文件路径
            #print(file_path0)
            return file_path0
        task1=threading.Thread(target=file_path, args=('G Value file Path',))
        task1.setDaemon(True)       # 把子进程设置为守护线程，当主进程结束后，子线程也会随之结束，必须在start（）前设置。
        task1.start()
        print(task1)
        print(file_path1)
        return file_path1'''


    def com_name_get(com_available):
        com_available= list(serial.tools.list_ports.comports())
        if len(com_available)==0:
            com_available='无可用串口，请插入串口'
        return com_available
        

    def com_connect():
        pass
    
    def com_close():
        pass


    def autoscan():
        pass


    def rescan():
        pass


    def clear_current_DMC(file_path):
        print(file_path)
        file_path=''
        print(file_path)


def start():
    root=Tk()                           # 因为写了一个类，所以要产生一个窗口对象，调用类的函数，进行窗口的构造和控件设置
    main_window = Init_Window(root)
    main_window.set_init_window()
    root.mainloop()


start()











