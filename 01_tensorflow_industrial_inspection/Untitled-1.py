# %%
import tkinter as tk
from tkinter import filedialog, scrolledtext
from PIL import ImageTk, Image

# %%


# %% [markdown]
# ### 创建主窗体

# %%
GUI = tk.Tk()
# GUI.withdraw()
# GUI = tk.Toplevel()       # 主窗口
GUI.title('AI图片分类')     # 窗口标题
GUI.geometry('900x700')     # 主窗口的大小
GUI.config(bg='orange')

# %% [markdown]
# ### 创建背景图片

# %%

# canvas = tk.Canvas(GUI, width=900, height=700, bd=0, highlightthickness=0)
# imgpath = "C:\\Users\\natlq\\Pictures\\sunflower.jpg"
# img = Image.open(imgpath)
# photo = ImageTk.PhotoImage(img)
# canvas.create_image(200, 700, image=photo)
# canvas.pack()

# %% [markdown]
# ## 函数

# %% [markdown]
# ### 文件选择及文件夹选择

# %%
def File_Choose():

    filename = filedialog.askopenfilename()
    filename = filename.replace('/', '\\')
    return filename


def Folder_Choose():
    folder_path = filedialog.askdirectory()
    folder_path = folder_path.replace('/', '\\')
    return(folder_path)

# %% [markdown]
# ### 读写文件

# %%
def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(str(content))


# %%
def read_file(file_name):
    with open(file_name, 'r') as f:
        Box_read = f.read()
    return Box_read

# %% [markdown]
# ### 获取选择区域坐标及画框

# %%
def start_point_get(event):
    global start_x, start_y # 声明写入全局变量
    # global Canvas_Image_Source, Select_Pic_Region_Win
    Canvas_Image_Source.delete("rect1")  # 如果已经有“rect1”标记的图形，则删除
    # 在canvas 1上绘制一个矩形(rectangle是矩形的意思)
    Canvas_Image_Source.create_rectangle(event.x,
                             event.y,
                             event.x + 1,
                             event.y + 1,
                             outline="green",
                             width=5,
                             tag="rect1")
    # 在全局变量中存储坐标
    start_x, start_y = event.x, event.y

# 拖动中的事件- - - - - - - - - - - - - - - - - - - - - - - - - - -
def rect_drawing(event):
    # 拖动中的鼠标指针出现在区域外时的处理
    if event.x < 0:
        end_x = 0
    else:
        end_x = min(img_open.width, event.x)
    if event.y < 0:
        end_y = 0
    else:
        end_y = min(img_open.height, event.y)
    # 重新绘制“rect1”标签的图像
    Canvas_Image_Source.coords("rect1", start_x, start_y, end_x, end_y)

# 释放拖动时的事件- - - - - - - - - - - - - - - - - - - - - - - -
def release_action(event):
    global  canvas2_size, Box
    canvas2_size = (400, 300)
    Img_Selected_Source =Image.open(Image_Source[0])


    # 将“rect1”标签的图像坐标恢复到原来的比例尺并获取
    start_x, start_y, end_x, end_y = [
        round(n) for n in Canvas_Image_Source.coords("rect1")
    ]
    ratio_canvas1 = img_ratio(Img_Selected_Source, canvas1_size)


    # 将所选区域恢复到实际图片尺寸
    Box = (start_x*ratio_canvas1, start_y*ratio_canvas1, end_x*ratio_canvas1, end_y*ratio_canvas1)
    Stringvar_Selected_Rectangle_Region.set(str(Box))


    # 将所选的区域显示出来
    Croped_Selected_Img = Img_Selected_Source.crop(Box)     # 截取Box为左上角和右下角点的方框
    ratio_canvas2 = img_ratio(Croped_Selected_Img, canvas2_size)    # 计算将图片缩放到canvas2的比率
    Croped_Selected_Img_size_width, Croped_Selected_Img_size_height = Croped_Selected_Img.size      # 获取截取到的图片的宽度和高度
    Canvas2_Croped_Selected_Img = Croped_Selected_Img.resize((int(Croped_Selected_Img_size_width/ratio_canvas2),    # resize 按照canvas2的尺寸
                                                              int(Croped_Selected_Img_size_height/ratio_canvas2)))   
    Opened_Canvas_Croped_Selected_Img = ImageTk.PhotoImage(Canvas2_Croped_Selected_Img)     # 打开图片
    Canvas_Image_Selected_Region= tk.Canvas(Select_Pic_Region_Win, bg = 'gray')
    Canvas_Image_Selected_Region.place(x=canvas1_size[0]+2, y=0,width = canvas2_size[0], height = canvas2_size[1])
    Canvas_Image_Selected_Region.create_image(0, 0, image=Opened_Canvas_Croped_Selected_Img, anchor=tk.NW)  # 显示到canvas2上
    Canvas_Image_Selected_Region.image = Opened_Canvas_Croped_Selected_Img


# 保存选择的区域到文件
def Save_Region_to_File(folderpath):
    global Box
    file_path_selected_folder = folderpath
    filesavename = file_path_selected_folder.split('\\')
    write_file(filesavename[-1]+'.txt', Box)

# %% [markdown]
# ### 训练模型

# %%
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow import keras as kr
from tensorflow.python.keras import layers
import keras.backend as KTF
from tensorflow.python.keras import Sequential
import pathlib

# %%
def Train_Model():
    data_dir= StringVar_Selected_Source_Folder.get()
    data_dir = pathlib.Path(data_dir)
    image_count = len(list(data_dir.glob('*/*.jpg')))
    print("图片总数：",image_count)
    Scrolltext_Start_Train_Result.insert('end', '图片总数'+str(image_count) + '\n') 
    batch_size = 32
    Train_Img_Selected_Source =Image.open(Image_Source[0])
    img_height ,img_width = Train_Img_Selected_Source.size

    # train_ds = tf.keras.utils.image_dataset_from_directory(
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)


    # val_ds = tf.keras.utils.image_dataset_from_directory(
    val_ds = tf.keras.utils.img_to_array(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    global class_names
    class_names = train_ds.class_names
    print("一共有以下几种分类：", class_names)
    Scrolltext_Start_Train_Result.insert('end', '一共有以下几种分类：'+str(class_names) + '\n') 


    # plt.figure(figsize=(10, 10))
    # for images, labels in train_ds.take(1):
    #     for i in range(9):
    #         ax = plt.subplot(3, 3, i + 1)
    #         plt.imshow(images[i].numpy().astype("uint8"))
    #         plt.title(class_names[labels[i]])
    #         plt.axis("off")


    for image_batch, labels_batch in train_ds:
        print(image_batch.shape)
        print(labels_batch.shape)
        break
    Scrolltext_Start_Train_Result.see('end')

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds  = train_ds.cache().shuffle(1000).prefetch(buffer_size = AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    normalization_layer = tf.keras.layers.Rescaling(1./255)

    normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    image_batch, labels_batch = next(iter(normalized_ds))
    first_image = image_batch[0]
    print(np.min(first_image), np.max(first_image))

    num_classes = len(class_names)

    # model = Sequential([
    #     tf.keras.layers.Rescaling(1./255, input_shape = (img_height, img_width, 3)),
    #     layers.Conv2D(16, 3, padding='same', activation = 'relu'),
    #     layers.MaxPooling2D(),
    #     layers.Conv2D(32, 3, padding='same', activation='relu'),
    #     layers.MaxPooling2D(),
    #     layers.Conv2D(64, 3, padding='same', activation='relu'),
    #     layers.MaxPooling2D(),
    #     layers.Flatten(),
    #     layers.Dense(128, activation='relu'),
    #     layers.Dense(num_classes)
    # ]) 

    data_augmentation = Sequential(
        [
        # tf.keras.layers.RandomFlip("horizontal",
                                #    input_shape=(img_height,
                                                # img_width,
                                                # 3)),
        # tf.keras.layers.RandomRotation(0.1),
        # tf.keras.layers.RandomZoom(height_factor=(-0.7, -0.7))
        # tf.keras.layers.Cropping2D(cropping=((138, (1600-418)),(127, (1200-383))))
        # tf.keras.layers.Cropping2D(cropping=((492, (1600-777)),(372, (1000-711))))
        tf.keras.layers.Cropping2D(cropping=((444, (1600-792)),(372, (1200-717))))
        # tf.keras.layers.Cropping2D(cropping=((int(492/1.6), (int((1600-777)/1.6))),(int(372*1.2), (int((1200-711)*1.2)))))
        ]
    )

    model = Sequential([
    data_augmentation,
    tf.keras.layers.Rescaling(1./255),
    layers.Conv2D(16, 3, padding='same', activation = 'relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, name="outputs")
    ])

    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
    
    epochs = 5
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    model.summary()


    # 保存训练好的模型到文件
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    Model_file_path_selected_folder = StringVar_Selected_Source_Folder.get()
    Model_Save_name= Model_file_path_selected_folder.split('\\')
    Model_Save_name = Model_Save_name[-1] + '.tflite'
    with open(Model_Save_name, 'wb') as f:
        f.write(tflite_model)
    
    Scrolltext_Start_Train_Result.insert('end', '模型已训练完成，模型保存在当前程序所在文件夹，文件名：'+ '\n' +Model_Save_name + '\n')  


# %%
def Start_Recognition():
    TF_Model_File_Path = StringVar_Selected_Model_Name.get()
    Target_Folder = StringVar_Selected_Target_Folder.get()
    Rectangle_file_name = TF_Model_File_Path.replace('.tflite', '.txt')
    Rectangle = eval(read_file(Rectangle_file_name))
    start_x, start_y, end_x, end_y= Rectangle
    start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
    interpreter = tf.lite.Interpreter(model_path=TF_Model_File_Path)
    interpreter.get_signature_list()
    classify_lite = interpreter.get_signature_runner('serving_default')
    classify_lite
    Target_DIR = pathlib.Path(Target_Folder)
    for i in range(len(list(Target_DIR.glob('*')))):
        image_name= list(Target_DIR.glob('*'))[i]
        Start_Recognition_Selected_Image =Image.open(image_name)
        print(Start_Recognition_Selected_Image)
        image_arr = np.array(Start_Recognition_Selected_Image)
        Cropped_Image_arr = image_arr[start_y:end_y, start_x:end_x]




        Cropped_Image= Image.fromarray(Cropped_Image_arr)
        img_height ,img_width = Cropped_Image.size
        # img = tf.keras.utils.load_img(Cropped_Image, target_size=(img_height,img_width))
        # img_array = tf.keras.utils.img_to_array(img)
        # image_array = np.expand_dims(img_array, axis=0)



        image_array = np.expand_dims(Cropped_Image_arr, axis=0)
        print(image_array)
        predictions_lite = classify_lite(sequential_1_input = image_array)['outputs']
        score_lite = tf.nn.softmax(predictions_lite)
        result_text =  "[{}]This image most likely belongs to {} with a {:.2f} percent confidence.".format(image_name, class_names[np.argmax(score_lite)], 100* np.max(score_lite))
        Scrolltext_Start_Train_Result.insert('end', result_text + '\n')  
        print(result_text)

# %% [markdown]
# ### 选择框范围，绑定鼠标事件

# %%
def Select_Pic_Region_Rectangle(canvas):
    canvas.bind("<ButtonPress-1>", start_point_get)
    canvas.bind("<Button1-Motion>", rect_drawing)
    canvas.bind("<ButtonRelease-1>", release_action)

# %% [markdown]
# ### 计算图片缩放比率

# %%
def img_ratio(img, canvas_size):
    w, h = img.size
    w_ratio = w/canvas_size[0]
    h_ratio = h/canvas_size[1]
    if w_ratio > h_ratio:
        ratio = w_ratio
    else:
        ratio = h_ratio
    return ratio

# %% [markdown]
# ### 选择图片

# %%
def choosepic(image_label):
    global img_open, canvas1_size, Image_Source
    Image_Source = ['']
    path_ = filedialog.askopenfilename()
    Image_Source[0] = path_
    img_open = Image.open(path_)
    w, h = img_open.size
    ratio_canvas1 = img_ratio(img_open, canvas1_size)
    img_open = img_open.resize((int(w/ratio_canvas1), int(h/ratio_canvas1)))
    img = ImageTk.PhotoImage(img_open)
    image_label.create_image(0, 0, image=img, anchor=tk.NW)
    image_label.image = img

# %% [markdown]
# ### 创建选择图片范围子窗体

# %%
def Select_Pic_Region():
      global canvas1_size , Select_Pic_Region_Win
      canvas1_size = (600, 400)
      Select_Pic_Region_Win = tk.Toplevel()
      Select_Pic_Region_Win.title('选择图片识别区域')
      Select_Pic_Region_Win.geometry('1000x600')
      Select_Pic_Region_Win.config(bg='orange')
      Select_Pic_Region_Win.focus_force()
      tk.Button(Select_Pic_Region_Win, text = '打开示例图片',bg='lightyellow', font='黑体 18 bold', command=lambda: choosepic(Canvas_Image_Source)).place(x = 100, y = 430,w = 250, h = 80)
      tk.Button(Select_Pic_Region_Win, text = '选择识别区域',bg='lightyellow', font='黑体 18 bold', command=lambda: Select_Pic_Region_Rectangle(Canvas_Image_Source)).place(x = 400, y = 430,w = 250, h = 80)
      tk.Button(Select_Pic_Region_Win, text = '保存识别区域',bg='lightyellow', font='黑体 18 bold', command=lambda: Save_Region_to_File(StringVar_Selected_Source_Folder.get())).place(x = 700, y = 430,w = 250, h = 80)
      global Canvas_Image_Source
      Canvas_Image_Source = tk.Canvas(Select_Pic_Region_Win, bg = 'gray')
      Canvas_Image_Source.place(x=0, y=0,width = canvas1_size[0], height = canvas1_size[1])


# %% [markdown]
# #### 创建训练子窗体

# %%
def Train_Win():
      global StringVar_Selected_Source_Folder, Stringvar_Selected_Rectangle_Region,Scrolltext_Start_Train_Result 
      Train_Win = tk.Toplevel()
      Train_Win.title('图片分类训练')
      Train_Win.geometry('1000x800')
      # Train_Win.attributes("-topmost", True) # 始终在最前面显示tkinter窗口
      Train_Win.config(bg='orange')
      Train_Win.focus_force()


      # 选择源文件夹
      StringVar_Selected_Source_Folder = tk.StringVar()
      Stringvar_Selected_Rectangle_Region = tk.StringVar()
      Frame_Source_Folder_Select = tk.LabelFrame(Train_Win, text='Step1', bg='darkseagreen', padx=10, pady=10)
      Frame_Source_Folder_Select.place(x=20, y=15)
      tk.Button(Frame_Source_Folder_Select, text="请选择源数据文件夹", font='宋体 18 bold',bg='lightyellow', 
            command=lambda: StringVar_Selected_Source_Folder.set(Folder_Choose())).pack(side="left", padx=6)
      tk.Entry(Frame_Source_Folder_Select, textvariable=StringVar_Selected_Source_Folder, font='宋体 10 bold', width=65
                  ).pack(side='left', padx=6)


      # 选择识别区域
      Frame_Select_Recognize_Region = tk.LabelFrame(Train_Win, text='Step2',bg='darkseagreen',  padx=10, pady=10)
      Frame_Select_Recognize_Region.place(x=20, y=100)
      tk.Button(Frame_Select_Recognize_Region, text="请选择识别区域", font='宋体 18 bold',bg='lightyellow', 
            command=Select_Pic_Region).pack(side="left", padx=6)
      tk.Entry(Frame_Select_Recognize_Region, textvariable=Stringvar_Selected_Rectangle_Region, font='宋体 10 bold', width=65
                        ).pack(side='left', padx=6)

      # 开始训练
      Frame_Start_Train = tk.LabelFrame(Train_Win, text='Step3',bg='darkseagreen',  padx=10, pady=10)
      Frame_Start_Train.place(x=20, y=185)
      tk.Button(Frame_Start_Train, text="开始训练", font='宋体 18 bold',bg='lightyellow', 
            command=Train_Model).pack(side="left", padx=6)
      Scrolltext_Start_Train_Result=scrolledtext.ScrolledText(Train_Win,bg='white', font='宋体 18 bold', width=64,height=20, padx=6, pady=6)
      Scrolltext_Start_Train_Result.place(x=20, y=285)
      Scrolltext_Start_Train_Result.insert('end', '\n'+ '欢迎使用程序' + '\n')
      Scrolltext_Start_Train_Result.see('end')

      # # 保存模型及识别区域
      # Frame_Save_Model = tk.LabelFrame(Train_Win, text='Step4',bg='darkseagreen', padx=10, pady=10)
      # Frame_Save_Model.place(x=20, y=670)
      # tk.Button(Frame_Save_Model, text="保存模型及识别区域", font='宋体 18 bold',bg='lightyellow', 
      #       ).pack(side="left", padx=6)

# %% [markdown]
# ## 主窗口

# %% [markdown]
# ### Step1：

# %%
Frame_Select_Or_Train_Model = tk.LabelFrame(GUI, text='Step1:', bg='darkseagreen', padx=10, pady=10)
Frame_Select_Or_Train_Model.place(x=10, y=15)

# %%
tk.Label(Frame_Select_Or_Train_Model, text="请训练新的模型或直接进入'Step2'选择现有模型:", font='宋体 18 bold', bg='darkseagreen' 
          ).pack(side="left", padx=6)
tk.Button(Frame_Select_Or_Train_Model, text='训练新的模型', font='宋体 18 bold', bg='lightyellow', 
          command=lambda: Train_Win()).pack(side='left', padx=6)

# %% [markdown]
# ### Step2:

# %%
Frame_Display_Selected_Model =tk.LabelFrame(GUI, text='Step2:', bg='darkseagreen', padx=10, pady=10)
Frame_Display_Selected_Model.place(x=10, y=100) 

# %%
global StringVar_Selected_Model_Name 
StringVar_Selected_Model_Name = tk.StringVar()
tk.Button(Frame_Display_Selected_Model, text="选择现有模型", font='宋体 18 bold', bg='lightyellow', 
          command=lambda: StringVar_Selected_Model_Name.set(File_Choose())).pack(side="left", padx=6)
tk.Label(Frame_Display_Selected_Model, text="选择的模型:", font='宋体 18 bold', bg='aliceblue', 
          ).pack(side="left", padx=6)
tk.Entry(Frame_Display_Selected_Model, textvariable=StringVar_Selected_Model_Name, font='宋体 10 bold', width=65,
         ).pack(side='left', padx=6)

# %% [markdown]
# ### Step3:

# %%
Frame_Select_Target_Pic_Folder = tk.LabelFrame(GUI, text='Step3:', bg='darkseagreen', padx=10, pady=10)
Frame_Select_Target_Pic_Folder.place(x=10, y=185)

# %%
global StringVar_Selected_Target_Folder
StringVar_Selected_Target_Folder = tk.StringVar()
tk.Button(Frame_Select_Target_Pic_Folder, text="选择待识别图片文件夹", font='宋体 18 bold', bg='lightyellow', 
          command=lambda: StringVar_Selected_Target_Folder.set(Folder_Choose())).pack(side="left", padx=6)
tk.Label(Frame_Select_Target_Pic_Folder, text="选择的文件夹:", font='宋体 18 bold', bg='aliceblue', 
          ).pack(side="left", padx=6)
tk.Entry(Frame_Select_Target_Pic_Folder, textvariable=StringVar_Selected_Target_Folder, font='宋体 10 bold', width=50
                ).pack(side='left', padx=6)

# %% [markdown]
# ### Step4:

# %%
Frame_Start_Recognize = tk.LabelFrame(GUI, text='Step4:', bg='darkseagreen', padx=10, pady=10)
Frame_Start_Recognize.place(x=10, y=270)

# %%
tk.Button(Frame_Start_Recognize, text="开始识别", font='宋体 18 bold', bg='lightyellow', 
          command=Start_Recognition).pack(side="left", padx=6)

# %% [markdown]
# ### 程序启动位置

# %%
GUI.update()
GUI.mainloop()



