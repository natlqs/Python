#### 哪些系列PLC/HMI可以用博图进行编程

**硬件配置的目录可以看到**

**CPU**: S7-1500/1200/300/400, SIMATIC ET200;

**HMI**:SIMATIC-精简系列面板（档次最低）、精智面板、移动式面板、Key Panel、Push Button Panel、HMI SIPLUS

#### 晶体管和继电器输出的区别

**继电器**：可以驱动2A左右的负载，响应速度慢10ms左右。使用寿命一百万次。

**晶体管**：可以驱动200mA左右的负载，响应速度快大概毫秒级以下。可以指定脉冲100k~200kHz输出。不考虑使用寿命。

#### PLC可以和哪些设备连接

PLC可以连接以下模块：

**输入**：**DI** 传感器，按钮；**AI** 传感器（电流，电阻，电压）；**高速计数通道** 位置计数/流量计数

**输出**：**DO** 指示灯，电磁阀，继电器，接触器；**AO** 温控器/调压阀；**PTO** 伺服/步进定位；**PWM** 调压

**通讯**：**串口 、232、485、422**串口设备；**TCP/IP UDP** 工控机、服务器；**3G 4G通讯模块** 做分散管理；**总线** CAN/DEVICE NET/CCLINK/Profibus DP/Profinet；**触摸屏**

#### 硬件配置

#### 归档和恢复

#### 编程语言种类

**IEC61131-3**

-   [指令表](https://baike.baidu.com/item/指令表)（Instruction List Diagram，ILD）
-   阶梯图（Ladder Diagram，LD）
-   [功能区块图](https://baike.baidu.com/item/功能区块图)（Function Block Diagram，FBD）
-   结构化文字（Structured Text Language，STL）
-   [顺序功能流程图](https://baike.baidu.com/item/顺序功能流程图)（Sequential Function Chart，SFC）

#### OB - program cycle OB1

循环调用，程序运行过程中以一定周期不停的调用。

#### OB - Startup OB100

启动时调用一次此块，并执行内部程序。

#### OB Cyclic interrupt 循环中断 OB30

定期启动该循环块中的程序，无需执行循环程序。可以在对话框或该OB属性中定义时间间隔。

#### 函数 - FC

函数是没有专用存储区的代码块

#### 数据块 - DBs

#### 功能块 - FBs