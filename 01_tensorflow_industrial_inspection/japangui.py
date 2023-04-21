import tkinter
import pyautogui  # 外部ライブラリ
from PIL import Image, ImageTk  # 外部ライブラリ

RESIZE_RETIO = 2 # 缩小倍率的规定

# 拖动开始时的事件- - - - - - - - - - - - - - - - - - - - - - - - -
def start_point_get(event):
    global start_x, start_y # 声明写入全局变量

    canvas1.delete("rect1")  # 如果已经有“rect1”标记的图形，则删除

    # 在canvas 1上绘制一个矩形(rectangle是矩形的意思)
    canvas1.create_rectangle(event.x,
                             event.y,
                             event.x + 1,
                             event.y + 1,
                             outline="green",
                             tag="rect1")
    # 在全局变量中存储坐标
    start_x, start_y = event.x, event.y

# 拖动中的事件- - - - - - - - - - - - - - - - - - - - - - - - - - -
def rect_drawing(event):

    # 拖动中的鼠标指针出现在区域外时的处理
    if event.x < 0:
        end_x = 0
    else:
        end_x = min(img_resized.width, event.x)
    if event.y < 0:
        end_y = 0
    else:
        end_y = min(img_resized.height, event.y)

    # 重新绘制“rect1”标签的图像
    canvas1.coords("rect1", start_x, start_y, end_x, end_y)

# 释放拖动时的事件- - - - - - - - - - - - - - - - - - - - - - - -
def release_action(event):

    # 将“rect1”标签的图像坐标恢复到原来的比例尺并获取
    start_x, start_y, end_x, end_y = [
        round(n * RESIZE_RETIO) for n in canvas1.coords("rect1")
    ]

    # 显示所获取的坐标
    pyautogui.alert("start_x : " + str(start_x) + "\n" + "start_y : " +
                    str(start_y) + "\n" + "end_x : " + str(end_x) + "\n" +
                    "end_y : " + str(end_y))

# 主处理 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__":

    # 获取要显示的图像(屏幕截图)
    img = pyautogui.screenshot()
    # 屏幕截图的图像不能完全显示，所以图像调整大小
    img_resized = img.resize(size=(int(img.width / RESIZE_RETIO),
                                   int(img.height / RESIZE_RETIO)),
                             resample=Image.BILINEAR)

    root = tkinter.Tk()
    root.attributes("-topmost", True) # 始终在最前面显示tkinter窗口

    # 图像转换，以便在tkinter上显示
    img_tk = ImageTk.PhotoImage(img_resized)

    # 绘制Canvas小部件
    canvas1 = tkinter.Canvas(root,
                             bg="black",
                             width=img_resized.width,
                             height=img_resized.height)
    # 在Canvas小部件上绘制获取的图像
    canvas1.create_image(0, 0, image=img_tk, anchor=tkinter.NW)

    # 配置Canvas小部件并设置各种事件
    canvas1.pack()
    canvas1.bind("<ButtonPress-1>", start_point_get)
    canvas1.bind("<Button1-Motion>", rect_drawing)
    canvas1.bind("<ButtonRelease-1>", release_action)

    root.mainloop()