# Python读书笔记

--- 

>>>>>>>>>>

--- 
## 1 基本概念

#### 程序：

#### 注释

- 功能：可以帮主理解程序的意义
- 用法： ‘#’ 或 '''注释'''   """注释"""


---
>>>>>>>>>>
---

## 2 变量及基本数学运算

### 变量

- 定义：变量存在于我们电脑的内存里,变量是一个暂时存储数据的地方,通过给变量名赋值可以进行值的改变.
- 赋值语句  '='   例如： x = 120
- 组成：
  - 必须是数字，字母，下划线组成
  - 长度：任意长度，但不建议太长，20字符以内
  - 要求：开头必须是字母
  - 注意：区分大小写，有意义


#### 程序：

#### 注释

- 功能：可以帮主理解程序的意义
- 用法： ‘#’ 或 '''注释'''   """注释"""

---
>>>>>>>>>
---
## 2 变量及基本数学运算

### 变量

- 定义：变量存在于我们电脑的内存里,变量是一个暂时存储数据的地方,通过给变量名赋值可以进行值的改变.
- 赋值语句  '='   例如： x = 120
- 组成：
  - 必须是数字，字母，下划线组成
  - 长度：任意长度，但不建议太长，20字符以内
  - 要求：开头必须是字母
  - 注意：区分大小写，有意义

### 数学运算

- +、-、*、/
- %: 余数(mod),计算出除法运算中的余数
- //：整除，计算出除法运算中只保留整数部分
- **： 次方

### 运算的优先级

- 除了括号'(',')'最优先外，其余计算优先次序如下：
  - 次方
  - 乘法、除法、求余数、求整数
  - 加法、减法

### 赋值运算符

- +=： a += b  a = a + b
- -=:  a -= b  a = a - b
- *=:  a *= b   a = a * b
- /=:  a /= b   a = a / b
- %=:  a %= b   a = a % b
- //=:  a //= b  a = a // b
- **=:  a **= b  a = a ** b

------

>>>>>>>

-----

## 3 基本数据类型

### 基础

**由来**

为了可以适应更多的使用场景，将数据划分为多种类型，每种类型都有着各自的特点和使用场景，帮助计算机高效的处理与展示数据

#### **类型**

- 数字类型
- 字符串类型
- 布尔类型
- 空类型
- 列表类型
- 元组类型
- 字典类型

#### **数字类型**

- 整型int

  - 整型就是我们说的整数，0也是整数，但是是特殊的整数
  - int既是整型的代表，又是定义整型的内置函数
  - 定义一个整型，并不一定非要使用int
- 浮点型float

  - 浮点型 就是小数，凡是带小数点的类型，都可以认为是浮点类型
  - 在python中，float既是浮点型的代表，又是浮点类型定义的内置函数
  - 定义float类型的时候，并不一定使用float来声明
- 内置函数--type

  - 返回变量的类型
  - type（已经被赋值的变量名或变量）
- 字符串的累加

  - 字符串不是数字不能做加减法、乘除法
  - 字符串的拼接，用”+“这个符号
- python在定义变量时，可以不设定这个变量的数据类型。
- 基本数据类型：

  - 常见的数值数据 整数（int）和浮点数（float）
  - 布尔值（Boolean）数据类型
  - 字符串（String）数据类型
- type()函数:列出变量的数据类型

  - ```python
    x = 10
    y = x/3
    print(type(x))
    print(type(y))
    ```
- 整数与浮点数的运算：Python具有简单自动转换能力,在计算时会将整数转换为浮点数再执行运算。

#### 数值进制

- 二进制： '0b'开头，如：0b1101, bin()函数可将一般数字转换为二进制
- 八进制： '0o'开头，如：0o57, oct()可以将一般数字转换为八进制
- 十六进制： '0x'开头，如0x50， hex()可以将一般数字转换为十六进制

#### 数值运算常用函数

- abs():计算绝对值
- pow(x, y): 返回x的y次方
- round(): 返回**五舍六入**，不是~~四舍五入~~

#### 布尔类型和空类型

- bool代表布尔类型， 也可以对于结果进行真假的判断
  - int 0 -> False, 非0 ->True
  - float 0.0 -> False, 非0.0 -> True
  - str ' ' ->False(空字符串), 非空字符串 -> True
- 空类型（None）
  - 不属于任何数据类型，就是空类型
  - 固定值：None
  - 属于False的范畴

### 字符串数据类型

- 定义：两个单引号''或者两个双引号""之间任意个数元符号的数据
- 代号： str
- 字符串的连接：数学运算符'+'
- 多行字符使用三个单引号或三个双引号
- 逸出字符：如果字符串内有一些特殊字符，如单引号、双引号，必须在特殊字符前加上"\"（反斜杠），才可以正常使用
  - \\': 单引号
  - \\": 双引号
  - \\n: 换行
  - \\\\: 反斜杠
  - \o: 八进制显示
  - \x: 十六进制
  - \t: Tab键
- str()：将数值数据强制转换为字符串
- int(str): 将字符串转换为整数
- chr(x): 返回函数x值的字符，x是ASCII码值
- ord(x): 返回函数字符参数的Unicode码值
- 字符串与整数相乘，结果是字符串将重复该整数的次数
- 在字符串前加'r'，可以防止逸出字符被转译

#### **字符串的简单操作**

- string[i]:    # 字符串的索引，即第i个字符
- string[1:3]:	# 字符串的切片
- list(string):	#将参数内的对象转成列表
- 成员运算符in的使用
  - 成员运算符是用来判断你的数据中是否存在你想要的成员
- max函数返回数据中最大的成员
  - 中文符号>字母>数字>英文符号
  - 中文按照拼音的首字母计算
- min函数返回数据中最小的成员
- lower()： 将字符串转成小写
- upper()： 将字符串转成大写
- title():  将字符串转成第一个字母大写，其他小写
- rstrip():	删除字符串尾端多余的空白
- lstrip():	删除字符串开始端多余的空白
- strip():	删除字符串头尾两边多余的空白

#### 字符串的函数或方法

- split():	# 将字符串以空格为分隔符，将字符串拆开，变成一个列表
- in / not in: 	# 判断一个对象是否属于另一个对象，对象可以是字符串，列表，元组，字典
- is / is not:	 # 比较两个对象是否相同，不只是内容相同，对象变量指向相同的内存，对象可以是变量、字符串、列表、元组、字典



---
>>>>>>>>
---


## 4 基本输入与输出

### python的辅助说明help()

- help() 函数可以列出某一python的指令或函数的使用说明，如help(print)

### 格式化输出数据使用print()

#### print()函数的基本语法

- ```python
    print('aaa')
    num1=222
    print('aaa', num1)
    print('aaa', sep='$$$;)
  ```

#### 格式化print()输出

- 基本格式： print('输出格式区' % (变量系列去，...))，默认是sys.stdout，也就是屏幕
- 输出格式区：
  - %d / %nd: 格式化整数输出, n多少位
  - %f / %m.nf: 格式化浮点数输出, m多少位，n小数部分
  - %x / %nx: 格式化16进制整数输出
  - %o / %no：格式化8进制整数输出
  - %s / %ns: 格式化字符串输出
- format()函数
  - ```python
      score = 90
      str1 = 'aaa'
      count = 1
      print("{}你的第{}次物理考试成绩是{}".format(str1, count, score))
    ```

### 输出数据到文件

- open()函数可以打开一个文件供读取或写入，如果函数执行成功，会传回文件对象。
- open()函数的基本格式： file_obj = open(file, mode='r')
  - file:欲打开的文件
  - mode：打开文件的模式，默认为'r'
    - r: 读取
    - w: 写入，原先文件内容将被覆盖
    - a: 写入，新写入的数据将附加在后面
    - x: 写入，如果新打开的文件已经存在会产生错误
    - b: 打开二进制文件模式
    - t：打开文本（txt）文件模式，默认
    - +：打开文件供更新用
  - file_obj：文件对象，可以自行给名称，不使用时要关闭"file_obj.close()",才可以返回操作系统的文件管理器观察结果

### 数据输入input()

- input()函数从屏幕读取用户从键盘输入的数据。
- 格式：value = input('prompt:'), value是变量，输入数据存入这里，不论输入的是字符串还是数值，返回的一律是字符串数据

### 列出所有内置函数dir()

- dir(__builtins__)  # 列出python内置函数，可以列出对象有哪些内置的方法

---

>>>>>>>

---

## 5 流程控制使用 if 语句

### 关系运算符, 真 返回 True, 假 返回 False

- '>'   大于
- '>='  大于或等于
- '<'   小于
- '<='  小于或等于
- '=='  等于
- '!='  不等于

### 逻辑运算符

- and     AND
- or      OR
- not     NOT

### if 语句

#### if 语句

- ```
  if (条件判断):
    程序代码块
  ```

  - ```python
      if(age<20):
      print(age)
      print('age', age)
    ```

#### if else 语句

- ```
  if (条件判断): 
    程序代码块1
  else:
    程序代码块2
  ```

  - ```python
      age = 30
      if (age < 29):
        print(age)
      else:
        print('age', age)
    ```

#### if elif else 语句

- ```
  if (条件判断1):
    程序代码区块1
  elif(条件判断2):
    程序代码区块2
  ...
  else:
    程序代码区块n
  ```

#### 嵌套的 if 语句

```
  if (条件判断1）：
    if (条件判断a):
      程序代码区块a
    else:
      程序代码区块b
  else:
    程序代码区块2
```

---

---

>>>>>>>>
---
---

## 6 列表（list）

列表(list)是Python的一种可以更改内容的数据类型，它是由一系列元素所组成的序列。如果现在我们要设计班上同学的成绩表，班上有50位同学，可能需要设计50个变量，这是一件麻烦的事。如果学校单位要设计所有学生的数据库，学生人数有1000人，需要1000个变量，这似乎是不可能的事。Python的列表数据类型，可以只用一个变量，解决这方面的问题，要存取时用列表名称加上索引值即可，这也是本章的主题。

列表类似于其他编程语言的数组（array），不过，Python的列表功能除了可以存储相同数据类型，例如，整数、浮点数、字符串，也可以存储不同数据类型，例如，**列表内同时含有整数、浮点数和字符串**。甚至一个列表也可以内含其他列表或是字典(dict)

### 列表基础

#### 定义

- 定义： name_list = [元素1， 元素2， ...，元素n]
- 元素可以是整数、浮点数、字符串、列表、字典

#### 读取元素列表

用列表名称与索引读取列表元素的内容，在Python中元素是从索引值0开始配置。所以如果是列表的第一个元素，索引值是0，第二个元素索引值是1，其他依此类推。

- name_list[i] # 读取索引i的列表元素

#### 列表切片（list slices）

在设计程序时，常会需要取得列表前几个元素、后几个元素、某区间元素或是依照一定规则排序的元素，所取得的系列元素也可称子列表，这个观念称列表切片(list slices)

- name_list[start:end]    # 读取从索引start到(end-1)索引的列表元素
- name_list[:n]           # 取得列表前n名
- name_list[n:]           # 取得列表索引n到最后
- name_list[-n:]          # 取得列表后n名
- name[:]                 # 取得所有元素
- name_list[start🔚step]   # 每隔step，读取从索引start到(end-1）索引的列表元素
- name_list[-1]           # 取得最后一个元素

#### 列表统计资料、最大值max()、最小值min()、总和sum()

Python有内置一些执行统计运算的函数，如果列表内容全部是数值则可以使用

- max( )函数获得列表的最大值，
- min( )函数可以获得列表的最小值，
- sum( )函数可以获得列表的总和。
- 如果列表内容全部是字符或字符串则可以使用max( )函数获得列表的unicode码值的最大值，min( )函数可以获得列表的unicode码值最小值。sum( )则不可使用在列表元素为非数值情况。

#### 列表个数len()

#### 更改列表元素的内容

- 使用列表名称和索引值更改列表元素的内容
  - ```python
    james = [23, 19, 22, 31, 18]
    print(james)
    james[4] = 28
    print(james)
    ```

#### 列表的相加

- 列表的相加相当于列表的结合

#### 列表乘以一个数字

- 如果将列表乘以一个数字，相当于列表元素重复次数

#### 删除列表元素

- del name_list[i]		# 删除索引i的列表元素
- del name_list[start:end]		# 删除从索引start到end-1索引的列表元素
- del name_list[start🔚step] # 每隔step,删除从索引start到（end-1）索引的列表元素

#### 列表为空列表的判断

- name_list = [ ]		# 这是空列表

#### 删除列表

- del name_list 	# 删除列表 name_list

### 列表内置方法

#### 列表的元素更改方法

- append():		在列表末端增加元素, name_list.append('new item')
- insert():  	可以在任意位置插入元素， name_list.insert(i, 'new item')
- pop():		删除将弹出所删除的值，
  - value = name_list.pop()       # 默认删除最后一个
  - value = name_list.pop(i)      #删除指定索引值的列表元素
- remove():    name_list.remove(想删除的元素内容)

#### 列表的排序方法

- reverse():		# 颠倒排序name_list列表元素    name_list.reverse()
- sort():	         # 对元素由小到大排序 ，排序后原列表的元素顺序永久更改  name_list.sort()
- sorted():	    # 用新列表存储排序，原列表序列不更改      new_list.sorted(name_list)

### 进阶列表操作

- index():	# 返回特定元素内容第一次出现的索引值   name_list.index(value)
- count():     # 返回特定元素内容出现的次数 name_list.count(value)
- join():        # 将列表的元素组成一个字符串

## 循环设计

### for循环

for循环可以让程序将整个**对象**内的元素遍历（也可以迭代），在遍历期间，同时可以记录或输出每次遍历的状态或称轨迹。

#### 基本使用方法

- ```
  for var in **可迭代对象** ： # 可迭代对象 iterable object
    程序代码块
  ```

可迭代对象可以是列表、元组、字典、集合或range(),在信息科学中迭代可以解释为重复执行。上述语法可以解释为将可迭代对象的元素当作var，重复执行，直到每个元素都被执行一次，整个循环才会停止。

- ```
  for var in **可迭代对象**： 
    程序代码块
    程序代码块
  ```

#### 举例

- ```python
  files = ['da1.c','da2.py','da3.py','da4.java']
  py = []
  for file in files:
  	if file.endswith('.py'):
          py.append(file)
  print(py)
  ```
- ```python
  names = ['hong', 'hind', 'dong', 'dceing']
  lastname=[]
  for name in names:
      if name.startswith('h'):
          lastname.append(name)
  print(lastname)
  ```

### range()函数

python可以使用range()函数产生一个等差序列，我们又称这个等差序列为可迭代对象，也可以称为range对象。

- range(start, stop, step)  # stop是唯一必须的值，等差序列是产生stop的前一个值。step默认为1， start默认为0

#### 举例

- ```python
  n=5
  for i in range(n):
      print(i)
  ```
- ```python
  n= 5
  sum = 0
  for i in range(1, n):
      sum += i
  ```
- ```python
  for x in range(2, 11,2):
      print(x)
  ```

### 列表生成式

- 新列表= [ 表达式 for item in 可迭代对象], ： square = [num ** 2 for num in range(1, n+1)]

### 进阶的for循环应用

#### 嵌套循环，一个循环内有另一个循环。

- ```
  for item in a:
  	...
  	for item2 in b:
  		...
  ```
- ```python
  for i in range(1, 10):
      for j in range(1, 10):
          result = i*j
          print(i, j, i*j)
  ```

#### -break指令，强制离开for循环

如果期待某些条件发生时可以离开循环，可以在循环内执行break指令。

- ```
  for item in a:
  	程序代码块1
  	if 条件：
  		程序代码块2
  		break
  程序代码3
  ```

#### -continue指令，for循环暂时停止不往下执行

- ```
  for item in a:
  	程序代码1
  	if 条件：		#如果条件表达是True，则不执行程序代码3
  		程序代码2
  		continue
  	程序代码3
  ```

#### for...else循环

在设计for循环时，如果期待所有的if条件是False，最后一次循环后，可以执行特定程序区块指令。

- ```
  for item in a:
  	程序代码1
  	if 条件：	# 如果条件是True,则离开for循环
  		程序代码2
  		break
  	程序代码3
  else:
  	程序代码4	# 最后一次循环条件表达式是False则执行
  ```

### While循环

#### 基本while循环

- ```
  while 条件：
  	程序区块
  ```
- ```python
  answer = 30
  guess = 0
  while guess != answer:
      guess = int(input('请猜1-100间的数字'))
      if guess > answer:
          print('请猜小一点')
      elif guess < answer:
          print('请猜大一点')
      else:
          print('恭喜答对了')
  ```

#### 嵌套while循环

- ```
  while 条件：
  	...
  	while 条件1：
  		...
  ```
- ```python
  i = 1				# 设定i初始值
  while i <= 9:		# 当i大于9跳出外层循环
      j = 1			# 设定j初始值
      while j <= 9:	# 当j大于9跳出内层循环
          result = i * j
          j += 1
      print()	#换行输出
      i += 1
  ```

#### -break 指令，强制离开while循环

- ```
  while 条件1：
  	程序代码1
  	if 条件2：		# 判断条件2
  		程序代码2
  		break	# 如果条件2是True，离开while循环
  	程序代码3
  ```

#### -continue指令，while循环暂时停止不往下执行

- ```
  while 条件1：
  	程序代码1
  	if 条件2	# 如果条件是True，则不执行程序代码3
  		程序代码2
  		continue
  	程序代码3
  ```

#### pass

- pass指令是什么事也不做

### enumerate对象使用for循环


---
---
>>>>>>>>

---
---


## 8 元组

### 元组的定义

元组是另一种数据类型，这种数据类型结构和列表完全相同，但是它与列表最大的差异是它的元素值与元素个数不可更改，有时又可称为不可变列表。

- name_tuple = (item1, ... , itemn)
- 元组的每一个数据称元素，元素可以是整数、字符串或列表等

#### 读取元组元素

- 和列表一样，用中括号[]索引

#### 遍历所有元组元素

- 在python可以使用for循环遍历所有元组元素
- ```python
  keys = ('magic', 'xaab', 000)
  for key in keys:
    print(key)
  ```

#### 修改元组内容产生错误

#### 可以使用全新定义方式修改元组元素

### 元组切片（tuple slices）

元组切片与列表切片相同

- ```python
  fruits = ('apple', 'orange', 'banana', 'watermelon', 'grape')
  print(fruits[1:3])
  print(fruits[:2])
  print(fruits[1:])
  print(fruits[-2:1])
  print(fruits[0:5:2])
  ```

### 方法与函数

- len()         #
- max(tuple)    # 获得元组最大值
- min(tuple)    # 获得元组最小值

### 列表与元组数据互换

- list(tuple): 将元组数据类型改为列表
- tuple(list): 将列表数据类型改为元组

### 元组的功能

- 可以更安全的保护数据
- 增加程序执行速度
  

---
---
>>>>>>>>
---
---

## 9 字典（Dict）

---
---
>>>>>>>>
---
---


## 10 集合（Set）

---
---
>>>>>>>>
---
---


## 11 函数设计

函数设计所谓的函数(function)其实就是一系列指令语句所组成，它的目的有两个。

1. 当我们在设计一个大型程序时，若是能将这个程序依功能，将其分割成较小的功能，然后依这些较小功能要求撰写函数程序，如此，不仅使程序简单化，最后程序侦错也变得容易。另外，撰写大型程序时应该是团队合作，每一个人负责一个小功能，可以缩短程序开发的时间。
2. 在一个程序中，也许会发生某些指令被重复书写在许多不同的地方，若是我们能将这些重复的指令撰写成一个函数，需要用时再加以调用，如此，不仅减少编辑程序的时间，更可使程序精简、清晰、明了。
### 函数定义
- ```
  def 函数名称（参数1，参数2，...）：
  ''' 函数批注'''
  程序代码块
  return [返回值1， 返回值2]
  ```
- 函数名称 名称必须是唯一的，程序未来可以调用引用。
- 参数值  这是可有可无的，完全视函数设计需要，可以接收调用函数传来的变量，各参数值之间是用逗号“,”隔开。
- 函数批注 这是可有可无的，不过如果是参与大型程序设计计划，当负责一个小程序时，建议所设计的函数需要加上批注，除了自己需要也是方便他人阅读。主要是注明此函数的功能，由于可能有多行批注所以可以用3个双引号（或单引号）包夹。许多英文Python资料称此为docstring(document string的缩写)。
- return [返回值1,返回值2 , … ]不论是return或接续右边的返回值皆是可有可无，如果有返回多个数据彼此需以逗号“,”隔开。

### 函数参数设计
#### 传递一个参数
- ```python
  def greeting(name):
    print('hi', name, 'good morning')
  
  greeting('Nelson')  # 将Nelson传入函数name参数
  ```

#### 多个参数传递

- 当所设计的函数需要传递多个参数，调用此函数时就需要特别**留意传递参数的位置需要正确**，最后才可以获得正确的结果。最常见的传递参数是数值或字符串数据，有时也会需要传递列表、元组或字典。
- ```python
  def interest(interest_type, subject):
    print('my interest' + interest_type)
    print('in' + interest_type + ', my favorite is ' + subject))

  interest('travel', '敦煌')
  interest('程序设计', 'python')
  ```

#### 关键词参数 参数名称=值
- 所谓的关键词参数(keyword arguments)是指调用函数时，参数是用参数名称=值配对方式呈现。Python也允许在调用需传递多个参数的函数时，直接将参数名称=值用配对方式传送，这个时候参数的位置就不重要了。

- ```python
  def interest(interest_type, subject):
    print('my interest' + interest_type)
    print('in' + interest_type + ', my favorite is ' + subject))

  interest('travel', '敦煌')
  interest(subject = '敦煌', interest_type = 'travel')
  ```

#### 参数默认值的处理
- 在设计函数时也可以给参数默认值，如果调用的这个函数没有给参数值，函数的默认值将派上用场。特别需留意：函数设计时含有默认值的参数，必须放置在参数列的最右边。

- ```python
  def interest(interest_type, subject='张家界'):
    print('my interest' + interest_type)
    print('in' + interest_type + ', my favorite is ' + subject))

  interest('travel')
  interest('travel', '敦煌')
  interest(subject = '敦煌', interest_type = 'travel')
  ```

#### 函数返回值
##### 返回None
- 函数没有“return [返回值]”时，Python在直译时会自动返回处理成“return None”，相当于返回None，None在Python中独立成为一个数据类型NoneType。
##### 简单返回数值数据
- ```python
  def substract(x1, x2):
    result = x1 - x2
    return result

  def addition(x1, x2):
    result = x1 + x2
    return result

  a = int(input('a = '))
  b = int(input('b = '))
  print('a - b = ', substract(a, b))
  print('a + b = ', addition(a, b))
  ```

##### 返回多个数据的应用
- 使用return返回函数数据时，也允许返回多个数据，各个数据间只要以逗号隔开即可。
- ```python
  def mutifunction(x1, x2):
    addresult = x1 + x2
    subresult = x1 - x2
    mulresult = x1 * x2
    divresult = x1 / x2
    return addresult, subresult, mulresult, divresult

  x1 = x2 = 10
  add, sub, mul, div = mutifunction(x1, x2)
  print('add = ', add)
  print('sub = ', sub)
  print('mul = ', mul)
  print('div = ', div)
  ```

##### 简单返回字符串数据
- 返回字符串的方法与返回数值的方法相同

##### 函数返回字典或列表数据
- 函数除了可以返回数值或字符串数据外，也可以返回比较复杂的数据，例如，字典或列表等。

#### 参数是列表
- 在调用函数时，也可以将列表（此列表可以是由数值、字符串或字典所组成）当参数传递给函数，然后函数可以遍历列表内容，然后执行更进一步的运作。
- Python允许在函数内直接修订列表的内容，同时列表经过修正后，主程序的列表也将随之永久性更改结果。

- ```python
  def kitchen(unserved, served):
    print('handle all the meal')
    while unserved:
        current_meal = unserved.pop()
        print('menu', current_meal)
        served.append(current_meal)
  def show_unserved_meal(unserved):
    print('below are all the unserved meal')
    if not unserved:
        print('none meal')
    for unserved_meal in unserved:
        print(unserved_meal)
  def show_served_meal(served):
    print('below are all served meal')
    if not served:
        print('none meal')
    for served_meal in served:
        print(served_meal)
  unserved = ['big mike', 'super spicy chicken burg', 'mike chicken piece']
  served = []
  show_unserved_meal(unserved)
  show_served_meal(served)
  kitchen(unserved, served)
  print('kitchen handle finish')
  show_unserved_meal(unserved)
  show_served_meal(served)
  ```

#### 传递任意数量的参数
##### 基本传递处理任意数量的参数
- ```python
  def make_icecream(*toppings):
    print('this is the receipe of the ice cream')
    for topping is toppings:
      print('---', topping)

  make_icecream('strawberry juice')
  make_icecream('strawberry juice', 'saltana', 'chocolate pieces')
  ```

##### 设计含有一般参数与任意数量参数的函数
- 程序设计时有时会遇上需要传递一般参数与任意数量参数，碰上这类状况，任意数量的参数必须放在最右边。下述build_dict()函数内的参数‘**players’，这表示可以接受任意数量关键词参数。
- ```python
  def build_dict(name, age, **players):
    info = {}
    info['name'] = name
    info['age'] = age
    for key, value in players.items():
      info[key] = value
    return info

  player_dict = build_dict('james', '32',
                           City = 'Cleveland,
                           State = 'Ohio')
  print(palyer_dict)
  ```

### 递归式函数设计recursive
- 一个函数可以调用其他函数也可以调用自己，其中调用本身的动作称递归式(recursive)调用，递归式调用有下列特色：
  - 每次调用自己时，都会使范围越来越小。
  - 必须要有一个终止的条件来结束递归函数。
  - 递归函数可以使程序变得很简洁，但是设计这类程序一不小心就很容易掉入无限循环的陷阱，
  所以使用这类函数时一定要特别小心。递归函数最常见的应用是处理正整数的阶乘(factorial)，
  一个正整数的阶乘是所有小于以及等于该数的正整数的积，同时如果正整数是0则阶乘为1，依照观念正整数是1时阶乘也是1。此阶乘数字的表示法为n!。
- ```python
  def factoria(n):
    '''计算n的阶乘，n必须是正整数'''
    if n == 1:
      return 1
    else:
      return(n * factoria(n -1))

  value = 3
  print(value, '的阶乘结果是：', factoria(value))
  value = 5
  print(value, '的阶乘结果是：', factoria(value))
    ```

### 局部变量与全局变量
- 某个变量只有在该函数内使用，影响范围限定在这个函数内，这个变量称局部变量(local variable)。
如果某个变量的影响范围是在整个程序，则这个变量称全局变量(global variable)。

  - Python程序在调用函数时会建立一个内存工作区间，在这个内存工作区间可以处理属于这个函数的变量，
当函数工作结束，返回原先调用程序时，这个内存工作区间就被收回，原先存在的变量也将被销毁，
这也是为何局部变量的影响范围只限定在所属的函数内。
  - 对于全局变量而言，一般是在主程序内建立，程序在执行时，不仅主程序可以引用，
所有属于这个程序的函数也可以引用，所以它的影响范围是整个程序。

- 全局变量可以在所有函数使用

- 程序设计时建议全局变量与函数内部的局部变量不要使用相同的名称。
- 局部变量内容无法在其他函数引用。
- 局部变量内容无法在主程序引用。

### lambda匿名函数
#### 特点
- 所谓的匿名函数(anonymous function)是指一个没有名称的函数，
  Python是使用def定义一般函数，匿名函数则是使用lambda来定义，
  有的人称之为lambda表达式，也可以将匿名函数称lambda函数。
  通常会将匿名函数与Python的内置函数filter( )、map( )等共同使用，
  此时匿名函数将只是这些函数的参数。
- 匿名函数一般是用在不需要函数名称的场合，例如，
  一些高阶函数(higher-order function)的参数可能是函数，这时就很适合
  使用匿名函数，同时让程序变得更简洁。
#### lambda匿名函数定义
- lambda arg1, agr2...: expression
- ```python
  product = lambda x, y: x*y
  print(product)
  ```

#### 匿名函数与filter（）
- 内置函数filter(),将一次对iterable(可以重复执行），如：字符串，列表，元组的元素放入function中，然后将function()函数执行结果是True的元素组成新的筛选对象返回。

- ```
  filter(function, iterable)
  ```
- ```python
  mylist = [5, 10, 15, 20, 25, 30]
  oddlist = list(filter(lambda x: (x % 2 == 1), mylist))
  print('奇数列表：'， oddlist)
  ```

#### 匿名函数与map()
- ```
  map(function, iterable)
  ```
- 上述函数将一次对iterable（可以重复执行）例如：字符串，列表，元组的元素放入function内，然后将function()函数执行结果组成新的筛选对象返回。

- ```python
  mylist = [5, 10, 15, 20, 25, 30]
  squarelist = list(map(lambda x: x ** 2, mylist))

  print('列表的平方值', squarelist)
  ```

#### pass 与函数
- 不执行任何操作

#### type关键字应用在函数
- 返回函数的类型，如： 内置函数， 函数


---
---
>>>>>>>>
---
---


## 12 类-面向对象的程序设计
Python其实是一种面向对象的编程(Object Oriented Programming)，在Python中其实所有的数据类型皆是对象，Python也允许程序设计师自创数据类型，这种自创的数据类型就是本章的主题类(class)。
### 类的定义与使用
#### 定义
- ```
  class Classname()
    statement1
    ...
    statementn
  ```
- ```python
  class Banks(): # 类名
    title = 'taipei bank' # 属性
    def motto(self):    # 方法
      return '以客为尊'
  ```
#### 类的使用
- 若是想操作类的属性与方法首先需定义该类的对象(object)变量，可以简称对象，然后使用下列方式操作。
  - object.类的属性
  - object.类的方法( )
- ```python
  class Banks(): # 类名
    title = 'taipei bank' # 属性
    def motto(self):    # 方法
      return '以客为尊'
  userbank = Banks()    # 定义类的对象
  print(userbank.title())
  print(userbank.motto())
  ```

#### 类的构造函数
- 初始化类是在类内建立一个初始化方法(method)，这是一个特殊方法，
  当在程序内定义这个类的对象时将自动执行这个方法。初始化方法有一个固定名称是“__init__()”，
  写法是init左右皆是2个底线字符，init其实是initialization的缩写，
  通常又将这类初始化的方法称构造函数(constructor)。在这初始化的方法内可以执行一些属性变量设定
- ```python
  class Banks():
    title = 'taipei bank'
    def __init__(self, uname, money):
      self.name = uname
      self.money = money
    def get_balance(self):
      return self.balance
  hungbank = Banks('hung', 100)
  print(hungbank.name.title(), '存款金额', hungbank.get_balance())
  ```

#### 属性初始值的设定
- 通常Python在设初始值时是将初始值设在__init__( )方法内


### 类的访问权限--封装(encapsulation)
- 类内的属性可以让外部引用的称公有(public)属性，而可以让外部引用的方法称公有方法。
- Python也提供一个私有属性与方法的观念，这个观念的主要精神是类外无法直接更改类内的私有属性，
类外也无法直接调用私有方法，这个观念又称封装(encapsulation)。

#### 私有属性
- 为了确保类内的属性的安全，其实有必要限制外部无法直接获取类内的属性值。
  Python对于类内的属性增加了私有属性(private attribute)的观念，
  应用方式是定义时在属性名称前面增加__(2个底线)，类外的程序无法引用私有属性

#### 私有方法
- 私有方法(private method)，类外的程序无法调用。于定义方式与私有属性相同，
  只要在方法前面加上__(2个底线)符号即可。

### 类的继承
#### 类的继承
- 在面向对象程序设计中类是可以继承的，其中被继承的类称父类(parent class)或基类(base class)，
  继承的类称子类(child class)或衍生类(derived class)。类继承的最大优点是许多父类的公有方法或属性，
  在子类中不用重新设计，可以直接引用。
- ```
  class BaseClassName():
    statement
  class DerivedClassName(BaseClassName):
    statement
  ```
#### 获取基类的私有属性
- 类外是无法直接取得类内的私有属性，即使是它的衍生类也无法直接读取，
  如果真要取得可以使用return方式，传回私有属性内容。
#### 衍生类与基类有相同名称的属性
- 程序设计时，衍生类也可以有自己的初始化__init__( )方法，
  同时也有可能衍生类的属性与方法名称和基类重复，
  碰上这个状况Python会先找寻衍生类是否有这个名称，
  如果有则先使用，如果没有则使用基类的名称内容。

#### 衍生类与基类有相同名称的方法
- 程序设计时，衍生类也可以有自己的方法，
  同时也有可能衍生类的方法名称和基类方法名称重复，
  碰上这个状况Python会先找寻衍生类是否有这个名称，
  如果有则先使用，如果没有则使用基类的名称内容。

#### 衍生类引用基类的方法
- 衍生类引用基类的方法时需使用super( )

#### 三代同堂的类与取得基类的属性super( )
- super( ).__init__( )  # 将父类的属性复制

#### 兄弟类属性的取得
- 假设有一个父亲(Father)类，这个父亲类有2个儿子，
  分别是Ivan类和Ira类，如果Ivan类想取得Ira类的属性iramoney，
  可以使用下列方法。
- ```
  Ira( ).iramoney  # Ivan取得Ira的属性iramoney
  ```

### 多态(polymorphism)


### 多重继承


### type和instance


### 特殊属性

#### \__doc__ 文档字符串
- 文档字符串的英文原意是文档字符串(docstring)，
  Python鼓励程序设计师在设计函数或类时，尽量为函数或类增加文档的批注，
  未来可以使用__doc__特殊属性列出此文档批注。
#### __name__属性

- ```python
  if __name__ == '__main__':
    dosomething()
  ```
- 如果上述程序是自己执行，那么__name__就一定是__main__。

### 类的特殊方法
#### \__str__()方法
- 该方法可以协助返回易读取的字符串
  
#### \__repr__()方法
#### \__iter__()方法


---
---
>>>>>>>>
---
---


## 13 设计与应用模块

其实在大型计划的程序设计中，每个人可能只是负责一小功能的函数或类设计，为了可以让团队的其他人可以互相分享设计成果，最后每个人所负责的功能函数或类将存储在模块(module)中，然后供团队其他成员使用。在网络上或国外的技术文件常可以看到有的文章将模块(module)称为套件(package)，意义是一样的。
### 建立函数模块
- 我们会常常需要在其他程序调用函数，将函数放在一起建立成模块，
  模块的扩展名与Python程序文件一样，是py，模块可以被其他程序调用

### 应用函数模块
#### import模块名称
- ```
  import 模块名称   # 导入模块
  ```
- ```
  模块名称.函数名称   # 模块名称与函数名称之间有小数点
  ```
#### 导入模块内特定单一函数
- ```
  from 模块名称 import 函数名称
  ```
#### 导入模块内多个函数
- ```
  from 模块名称 import 函数名称1， 函数名称2， ...函数名称n
  ```
#### 导入模块所有函数
- ```
  from 模块名称 import *
  ```
#### 使用as给函数指定替代名称
- 碰上所设计程序的函数名称与模块内的函数名称相同，或是感觉模块的函数名称太长，
此时可以自行给模块的函数名称一个替代名称，未来可以使用这个替代名称代替原先模块的名称。
- ```
  from 模块名称 import 函数名称 as 代替名称
  ```
#### 使用as给模块指定替代名称
- ```
  import 模块名称 as 替代名称
  ```

### 建立类模块
- 模块的扩展名与Python程序文件一样，是py

### 应用类模块
- 导入模块内的类与导入模块内函数的方式是一致的。
#### 导入模块的单一类
- ```
  from 模块名称 import 类名称
  ```
#### 导入模块的多个类
- ```
  from 模块名称 import 类名称1， 类名称2, ...， 类名称n
  ```
#### 导入模块的所有类
- ```
  from 模块名称 import *
  ```
#### 导入模块
- ```
  import 模块名称 # 导入模块
  模块名称。类别名称 # 模块名称与类别名称间有小数点
  ```
#### 模块内导入另一个模块的类
- 如果拆成类别的模块彼此有衍生关系，则子类别也需将父类别导入，执行时才不会有错误产生。

### 随机数random模块
#### randint(): 随机产生指定区间的整数
- ```
  randint(min, max)   # 可以产生min和max之间的数值
  ```

#### choice()： 在列表(list)里随机传回一个元素

#### shuffle(): 将列表元素重新排列


### 时间time模块
#### time(): 传回自1970年1月1日00:00:00AM以来的秒数

#### sleep(): 可以让工作暂停，这个方法的参数是秒

#### asctime(): 以可以阅读方式列出当前系统时间
- ```python
  import time
  print(time.asctime())
  ```
#### localtime()： 返回目前时间的结构数据，所返回的结构可以用索引方式获得个别内容
- ```python
  import time
  xtime = time.localtime()
  print(xtime)
  print('年', xtime[0])
  print('月', xtime[1])
  print('日', xtime[2])
  print('时', xtime[3])
  print('分', xtime[4])
  print('秒', xtime[5])
  print('周几', xtime[6])
  print('第几天', xtime[7])
  print('夏令时间', xtime[8])
  ```

### 系统sys模块
#### version属性：列出python的版本信息

#### stdin对象：从屏幕输入，可以搭配readline()方法，读取屏幕输入直到按下Enter键
- ```python
  import sys
  print('请输入字符串，输入完成按Enter', end = '')
  msg = sys.stdin.readline()
  print(msg)
  ```

#### stdout对象: 从屏幕输出，可以搭配write()方法，从屏幕输出数据
- ```python
  import sys
  sys.stdout.write('i like python')
  ```

### keyword模块

#### kwlist属性 : 列出所有关键词

#### iskeyword()： 传回字符串是否是关键词


---
---
>>>>>>>>
---
---


## 14 文件的读取与写入

### 文件夹与文件路径
- 例如： D:\Python\ch14\ch14_1.py

#### 绝对路径与相对路径
- 绝对路径：路径从根目录开始表达 如：   D:\Python\ch14\ch14_1.py
- 相对路径： 相对于当前工作目录的路径
- 在操作系统处理文件夹的观念中会使用2个图书符号'.'和'..'，
    '.'指当前文件夹，'..'指上一层文件夹。
    当前文件夹可以省略'.\'。

#### OS模块与OS.path模块
- 在python内有关文件路径的模块是os，在文件操作时需导入此模块
- ```
    import os # 导入os模块
  ```
#### 检查路径方法exist/isabs/isdir/isfile
- exist(path): 如果path的文件或文件夹存在传回True，否则传回Flase
- isabs(path): 如果path的文件或文件夹是绝对路径传回True，否则传回False
- isdir(path): 如果path是文件夹传回True，否则传回False
- isfile(path): 如果path是文件传回True，否则传回False

#### 文件与目录的操作mkdir/rmdir/remove/chdir
- mkdir(path): 建立path目录
- rmdir(path): 删除path目录，限制只能是空的目录。
- remove(path): 删除path文件
- chdir(path): 将当前工作文件夹改至path。

#### 结合传回文件路径 os.path.join()
- os.path.join()参数内的字符串结合为一个文件路径
- ```python
  import os
  print(os.path.join('D:\\', 'python', 'ch14', 'ch14_1.py'))
  ```
#### 获得特定文件的大小os.path.getsize()
- os.path.getsize() 可以获得特定文件的大小 

#### 获得特定工作目录的内容os.listdir()
- os.listdir() 以列表的方式列出特定工作目录的内容
- ```python
  import os
  print(os.listdir('D:\\python\\ch14'))
  ```

#### 获得特定工作目录内容glob
- Python内还有一个模块可用于列出特定工作目录内容glob，
当导入这个模块后可以使用glob方法获得特定工作目录的内容，
这个方法最大特色是可以使用通配符' \* '，例如，可用' *.txt '获得所有txt扩展名的文件
- ```python
  import glob
  print('方法1：列出\\python\\ch14的所有文件')
  for file in glob.glob('D:\\python\\ch14\*.*'):
      print(file)
  print('方法2: 列出目前工作目录的特定文件')
  for file in glob.glob('ch14_1*.py'):
      print(file)       # ch14_1.py, ch14_10.py, ch14_11.py...
  print('方法3：列出目前工作目录的特定文件')
  for file in glob.glob('ch14_2*.*'):
      print(file)       # ch14_2.py, ch14_21.txt...
  ```

#### 遍历目录树os.walk()
- os.walk()可以遍历目录树，每次循环时传回3个值：
    - 当前工作目录名称(dirName)
    - 当前工作目录底下的子目录列表(sub_dirNames)
    - 当前工作目录底下的文件列表(fileNames)
- ```
  for dirName, sub_dirNames, fileNames in os.walk(目录路径):
    程序区块
  ```
- 上述dirName, sub_dirNames, fileNames名称可以自行命名，
顺序则不可以更改，至于目录路径可以使用绝对地址或相对地址，
如果不注明则代表当前工作目录的子目录。

#### 取得当前工作目录 os.getcwd()
- os模块内的getcwd()可以取得当前工作目录
- ```python
  import os
  print(os.getcwd())
  ```

#### 取得绝对路径 os.path.abspath
- os.path.abspath(path)会传回path的绝对路径。
- ```python
  import os
  print(os.path.abspath('.'))   # 列出当前目录的绝对路径
  print(os.path.abspath('..'))  # 列出上一层工作目录的绝对路径
  print(os.path.abspath('ch14.py')) # 列出目前文件的绝对路径
  ```

#### 传回特定路段相对路径os.path.relpath()
- os.path.relpath(path, start) 会传回从start到path的相对路径
  如果省略start，则传回当前工作目录至path的相对路径
- ```python
  import os
  print(os.path.relpath('D:\\'))    # 列出目前目录至D:\的相对路径
  print(os.path.relpath('D:\\python\\ch13'))    # 列出目前目录至特定path的相对路径
  print(os.path.relpath('D:\\', 'ch14.py')) # 列出目前文件至D:\的相对路径
  ```

### 读取文件
- Python处理读取或写入文件首先需将文件打开，
然后可以一次读取所有文件内容或是一行一行读取文件内容。
Python可以使用open( )函数打开文件，文件打开后会传回文件对象，
未来可用读取此文件对象方式读取文件内容

#### 读取整个文件read()
- read()读取打开的文件，所有的文件内容将以一个字符串方式被读取然后存入字符串变量内。
- ```python
  fn = 'ch14_15.txt'
  file_obj = open(fn)
  data = file_obj.read()
  file_obj.close()      # 文件读取完后要关闭，否则会有不可阈值的 损坏
  print(data)
  ```
- 整个文件是以字符串方式被读取与储存，所以打印字符串时最后一行的空白行也将显示出来，
不过我们可以使用rstrip( )将data字符串变量（文件）末端的空格符删除。

#### with关键词
- with关键词应用在打开文件与建立文件对象时。
- ```
  with open(file) as file_obj:
    相关系列指令
  ```
- 这种方式打开文件，可以不必在程序中关闭文件，
with指令会在结束不需要此文件时自动将它关闭，
文件经“with open( ) as文件对象”打开后会有一个文件对象，
就可以使用前一节的read( )读取此文件对象的内容

#### 逐行读取文件内容
- ```
  for line in file_obj:     # line 和 file_obj可以自行取名，file_obj是文件对象
      循环相关系列指令
  ```
- ```python
  fn = 'ch14_15.txt'
  with open(fn) as file_obj:    # 用默认mode = r 开启文件
      for line in file_obj:
          print(line)
  ```

#### 逐行读取readlines()
- 使用with关键词配合open( )时，所打开的文件对象当前只在with区块内使用，
特别是想要遍历此文件对象时。Python另外有一个方法readlines( )可以逐行读取，
同时以列表方式储存，另一个特色是读取时每行的换行字符皆会储存在列表内。
当然更重要的是我们可以在with区块外遍历原先文件对象内容。

- ```python
  fn = 'ch14_20.txt'
  with open(fn) as file_obj:
      obj_list = file_obj.readlines()  # 每次读一行
  print(obj_list)   # 打印列表
  ```
- ```python
  fn = 'ch14_20.txt'
  with open(fn) as file_obj:
      obj_list = file_obj.readlines()
  for line in obj_list:
      print(line.rstrip())      # rstrip() 将字符串末端的空格删除
  ```

#### 数据组合
- Python的多功能用途，可以让我们很轻松地组合数据
- ```python
  fn = 'ch14_20.txt'
  with open(fn) as file_obj:
      obj_list = file_obj.readlines()
  str_obj = ' '
  for line in obj_list:
      str_obj += line.rstrip()
  print(str_obj)
  ```

#### 字符串替换
- 字符串对象.replace(旧字符串， 新字符串) 
- ```python
  fn = 'ch14_20.txt'
  with open(fn) as file_obj:
      data = file_obj.read()
      new_data = data.replace('工专', '科大')
      print(new_data.rstrip())
  ```

#### 数据搜寻使用find()
- find()可以执行数据搜寻，还会传回数据的位置索引，如果没有传回-1
- ```
  index = str.find(sub[,start[,end]]) # sub是欲搜寻字符串
  ```
- ```python
  fn = 'xxx.txt'
  with open(fn) as file_obj:
      obj_list = file_obj.readlines()
  str_obj = ' '
  for line in obj_list:
      str_obj += line.rstrip()
  findstr = input('请输入欲搜寻字符串= ')
  index = str_obj.find(findstr)
  if index >=0: 
      print('搜寻%s字符串在%s文件中' % (findstr, fn))
      print('在索引%s位置出现' % index)
  else:
      print('搜寻%s字符串不在%s文件中' % (findstr, fn))
  ```

#### 普通数据的搜寻
- ```python
  fn - 'xxx.txt'
  with open(fn) as file_obj:
      obj_list = file_obj.readlines()

  str_obj = ' '
  for line in obj_list:
      str_obj += line.rstrip()
  findstr = input('请输入欲搜寻字符串=')
  if findstr in str_obj:
      print('搜寻%s字符串在%s文件中') % (findstr, fn))
  else:
      print('搜寻%s字符串不在%s文件中') % (findstr, fn))

---
---
>>>>>>>>
--- 
---

## 15 程序除错与异常处理
- 将程序错误(error)称作程序异常(exception)

### 程序异常

#### 撰写异常处理程序 try - except
- ```try - except    # 发生异常被捕捉时程序会执行异常处理程序，然后跳开异常位置，再继续往下执行。```
- ```python
  try:
    指令   # 预先设想可能引发错误异常的指令
  except 异常对象： # error名称如： ZeroDivisionError
    异常处理程序    # 通常是指出异常原因，方便修正
  ```
- ```python
  def division(x, y):
    try:    # try - except
      retrun x/y
    except ZeroDivisionError:   # 除数为0时执行
      print('除数不可为0')

  print(division(10, 2))
  print(division(5, 0))
  print(division(6, 3))
  ```

#### try-except-else
- ``` try-except-else # try内的指令正确时，可以执行else的指令区块。```
- ```
  try:
    指令  # 预先设想可能引发异常的指令
  except 异常对象：   # 
    异常处理程序
    else:
      正确处理程序    # 如果指令正确执行此区块指令
  ```

#### FileNotFoundError 找不到文件错误
- 程序设计时另一个常常发生的异常是打开文件时找不到文件，这时会产生FileNotFoundError异常。

#### 分析单一文件的字数
- ```python
  def wordsNum(fn):
    try:
      with open(fn) as file_obj:
        data = file_obj.rad()
    except FileNotFoundError:
      print('找不到%s文件'% fn)
    else:
      wordlist = data.split()
      print(fn, '文章的字数是', len(wordlist))

  file = 'ch15_6.txt'
  wordsNum(file)
  ```

#### 分析多个文件的字数
- ```python
  def wordsNum(fn):
    try:
      with open(fn) as file_obj:
        data = file_obj.rad()
    except FileNotFoundError:
      print('找不到%s文件'% fn)
    else:
      wordlist = data.split()
      print(fn, '文章的字数是', len(wordlist))

  files = ['data1.txt', 'data2.txt', 'data3.txt']
  for file in files:
    wordsNum(file)
  `````

### 设计多组异常处理程序
#### 常见的异常处理对象
- AttributeError    # 通常指对象没有这个属性
- Exception   # 一般错误皆可用
- FileNotFoundError   # 找不到open()打开的文件
- IOError     # 在输入或输出时发生错误
- IndexError    # 索引超出范围区间
- KeyError    # 在映射中没有这个键
- MemoryError   # 需求内存空间超出范围
- NameError     # 对象名称未申明
- SyntaxError   # 语法错误
- SystemError   # 直译器的系统错误
- TypeError     # 数据类型错误
- ValueError    # 传入无效参数
- ZeroDivisionError   # 除数为0

#### 设计捕捉多个异常
- ```
  try:
    指令
  except 异常对象1：
    异常处理程序1
  except 异常对象2：
    异常处理程序2
  ```
- ```python
  def division(x, y):
    try:    # try - except
      retrun x/y
    except ZeroDivisionError:   # 除数为0时执行
      print('除数不可为0')
    except TypeError:
      print('使用字符做除法运算异常')

  print(division(10, 2))
  print(division(5, 0))
  print(division(6, 3))
  ```

#### 使用except捕捉多个异常
- ```
  try:
    指令
  except (异常对象1， 异常对象2， ......):
    异常处理程序
  ```
- ```python
  def division(x, y):
    try:    # try - except
      retrun x/y
    except (ZeroDivisionError, TypeError):   # 除数为0时执行
      print('除数为0发生 或 使用字符做除法运算异常')

  print(division(10, 2))
  print(division(5, 0))
  print(division(6, 3))
  ```

#### 处理异常但是使用python内置的错误信息
- python也支持发生异常时使用系统内置的异常处理信息。
- ```
  try:
    指令
  except 异常对象 as e:
    print(e)
  ```
- ```python
  def division(x, y):
    try:    # try - except
      retrun x/y
    except (ZeroDivisionError, TypeError) as e:   # 除数为0时执行
      print('e')

  print(division(10, 2))
  print(division(5, 0))
  print(division(6, 3))
  ```

#### 捕捉所有异常
- ```
  try:
    指令
  except:
    异常处理程序
  ```
- ```python
  def division(x, y):
    try:
      return x/y
    except:
      print('异常发生')
  print(division(10, 2))
  print(division(5, 0))
  print(division('a', 'b'))
  print(division(6, 3))
  ```

### 丢出异常
- 设计程序时如果发生某些状况，我们自己将它定义为异常然后丢出异常信息，
  程序停止正常往下执行，同时让程序跳到自己设计的except去执行。
- ```
  raise Exception('msg')
  ...
  ...
  try:
    指令
  except Exception as err:
    print('messge1', + str(err))
- ```python
  def passWord(pwd):
    pwdlen = len(pwd)
    if pwdlen < 5:
      raise Exception('密码长度不足')
    if pwdlen > 8:
      raise Exception('密码长度太长')
    print('密码长度正确')
  for pwd in ('aaabbbccc', 'aaa', 'aaabbb'):
    try:
      passWord(pwd)
    except Exception as err:
      print('密码长度检查异常发生：', str(err))
  ```

### 记录Traceback字符串
- 每次错误屏幕皆出现Traceback字符串，在这个字符串中指出程序错误的原因。
 如果我们导入traceback模块，就可以使用traceback.format_exc( )记录这个Traceback字符串。
- ```python
  def passWord(pwd):
    pwdlen = len(pwd)
    if pwdlen < 5:
      raise Exception('密码长度不足')
    if pwdlen > 8:
      raise Exception('密码长度太长')
    print('密码长度正确')
  for pwd in ('aaabbbccc', 'aaa', 'aaabbb'):
    try:
      passWord(pwd)
    except Exception as err:
      errlog = open('errch15_16.txt', 'a')
      errlog.write(traceback.format_exc())
      errlog.close()
      print('将traceback写入错误文件err15_16.txt完成')
      print('密码长度检查异常发生：', str(err))
  ```

### finally
- finally和try配合使用，在try之后可以有except或else，
  这个finally关键词必须放在except和else之后，
  同时不论是否有异常发生一定会执行这个finally内的程序代码。
  这个功能主要是用在Python程序与数据库连接时，输出连接相关信息。
- ```python
  def division(x, y):
    try:
      return x/y
    except:
      print('异常发生')
    finally:
      print('阶段任务完成')
  print(division(10, 2), '\n')
  print(division(5, 0), '\n')
  print(division('a', 'b'), '\n')
  print(division(6, 3), '\n')
  ```

### 程序断言assert
#### 设计断言
- assert关键词主要功能是协助程序设计师在程序设计阶段，
对整个程序的执行状态做一个全面性的安全检查，
以确保程序不会发生语意上的错误。
- ```python
  class Banks():
    title = 'Taipei Bank'
    def __init__(self, uname, money):
      self.name = uname
      self.balance = money
    def save_money(self, money):
      assert money > 0, '存款money必须大于0'  # 如果出现该错误，报错
      self.balance += money
      print('存款'， money, '完成')
    def withdraw_money(self, money):
      assert money > 0, '提款金额必须大于0 '  # 如果小于0 ，报错
      assert money <= self.balance, '存款金额不足'
      self.balance -= money
      print('提款', money, '完成')
    def get_balance(self):
      print(self.name.title(), '目前余额：', self.balance)
  hungbank = Banks('hung', 100)
  hungbank.get_balance()
  hungbank.save_money(300)
  hungbank.get_balance()
  hungbank.save_money(-300)
  hungbank.get_balance()
  ```

#### 停用断言
- 断言assert一般是用在程序开发阶段，如果整个程序设计好了以后，
  想要停用断言assert，可以在Windows的命令提示环境（可参考附录B-2-1），
  执行程序时使用“-O”选项停用断言。

### 程序日志模块logging
- 程序日志logging功能，这个功能可以协助我们执行程序的除错,
  有了这个功能我们可以自行设定关键变量在每一个程序阶段的变化，
  由这个关键变量的变化可方便我们执行程序的除错，
  同时未来不想要显示这些关键变量数据时，可以不用删除，
  只要适度加上指令就可隐藏它们

#### logging模块
- logging模块有提供方法可以让我们使用程序日志logging功能，
  在使用前须先使用import导入此模块。
- ``` import logging ```
#### logging的等级
- DEBUG等级使用logging.debug( )显示程序日志内容，所显示的内容是程序的小细节，
  最低层级的内容，感觉程序有问题时可使用它追踪关键变量的变化过程。
- INFO等级使用logging.info( )显示程序日志内容，所显示的内容是记录程序一般发生的事件。
- WARNING等级使用logging.warning( )显示程序日志内容，所显示的内容虽然
  不会影响程序的执行，但是未来可能导致问题的发生。
- ERROR等级使用logging.error( )显示程序日志内容，通常显示程序在某些状态将引发错误的缘由。
- CRITICAL等级使用logging.critical( )显示程序日志内容，这是最重要的等级，
  通常是显示将让整个系统当掉或中断的错误。

### BUG典故

---
---
>>>>>>>>
---
---


## 16 正则表达式（Regular Express）


### 正则表达式基础
- python有关正则表达式的方法是在re模块内，所以使用时需导入re模块
- ```import re    # 导入re模块```
  

#### 建立搜寻字符串模式
- 正则表达式是一种文本模式的表达方法，在这个方法中\d表示0-9的数字字符。
- 0518-8722-1534 用正则表达式为： '\d\d\d\d-\d\d\d\d-\d\d\d\d'
- 由逸出字符的观念可知，上述表达式当字符串放入函数内需增加'\',所以整个正则表达式：
- ```'\\d\\d\\d\\d-\\d\\d\\d\\d-\\d\\d\\d\\d'```
- 字符串前加r可以防止字符串内的逸出字符被转译，所以还可以表达为：
- ```r'\d\d\d\d-\d\d\d\d-\d\d\d\d'```

#### 使用re.compile()建立Regex对象
- re模块内的compile()方法可以将正则表达式当作字符串参数，然后传回一格Reggex(**Reg**ular **ex**pression)对象
- ```phoneRule = re.compile(r'\d\d\d\d-\d\d\d\d-\d\d\d\d') ```
#### 搜寻对象 search()
- 在Regex对象内有search()方法，由Regex对象启用，然后将欲搜寻的字符串放在这个方法内：
- ```phoneNum = phoneRule.search(msg) # msg是欲搜寻的字符串```
- 如果找不到比对相符的字符串会传回None，如果找到比对相符的字符串会将结果传回所设定的phoneNum变量对象。
- 处理此对象主要是将搜寻结果传回，可以用group()方法将结果传回，不过search()将只传回第一个比对相符的字符串。
- ```python
  import re
  msg1='please call my secretary using 0930-919-919 or 0952-001-001'
  msg2='please join dinner with me tommorrow night'
  msg3= 'please join dinner with me tommorrow night, call me 0933-080-080'

  def parseString(string):
    # 解析字符串是否含有电话号码
    phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    phoneNum = phoneRule.search(string)
    if phoneNum != None:
      print('phone num is : %s' % phoneNum.group())
    else:
      print('%s there is no phone num in this string' % string)
  
  parseString(msg1)
  parseString(msg2)
  parseString(msg3)
  ```
- ```
  执行结果
  phone num is : 0930-919-919
  please join dinner with me tommorrow night there is no phone num in this string
  phone num is : 0930-080-080
  ```

#### 搜寻对象 findall()
- 可以返回所有找到的匹配项，不像search只返回第一个匹配项。
- 如果没有比对相符的就传回[ ]空列表
- phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
- phoneNum = phoneRule.findall(string)    # string是欲搜寻的字符串
- ```python
  import re
  msg1='please call my secretary using 0930-919-919 or 0952-001-001'
  msg2='please join dinner with me tommorrow night'
  msg3= 'please join dinner with me tommorrow night, call me 0933-080-080'

  def parseString(string):
    # 解析字符串是否含有电话号码
    phoneRule = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
    phoneNum = phoneRule.findall(string)
    print('phone num is:' % phoneNum)
  
  parseString(msg1)
  parseString(msg2)
  parseString(msg3)
  ```
- ```
  执行结果：
  phone num is: ['0930-919-919', '0952-001-001']
  phone num is: []
  phone num is: ['0933-080-080']
  ```

#### re模块
- python语言的re模块对于search()和findall()有提供更强的功能，可以省略使用re.compile()直接将比对模式放在各自的参数内。语法格式如下：
- re.search(pattern, string, flags)
- re.findal(pattern, string, flags)
- 上述pattern是欲搜寻的正则表达式，string是所搜寻的字符串，flags可以省略。
- ```python
  import re
  msg1='please call my secretary using 0930-919-919 or 0952-001-001'
  msg2='please join dinner with me tommorrow night'
  msg3= 'please join dinner with me tommorrow night, call me 0933-080-080'

  def parseString(string):
    # 解析字符串是否含有电话号码
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'   # re参数
    phoneNum = re.search(pattern, string)   # re参数
    if phoneNum != None:
      print('phone num is : %s' % phoneNum.group())
    else:
      print('%s there is no phone num in this string' % string)
  
  parseString(msg1)
  parseString(msg2)
  parseString(msg3)
  ```
- ```python
  import re
  msg1='please call my secretary using 0930-919-919 or 0952-001-001'
  msg2='please join dinner with me tommorrow night'
  msg3= 'please join dinner with me tommorrow night, call me 0933-080-080'

  def parseString(string):
    # 解析字符串是否含有电话号码
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d' # re参数
    phoneNum = re.findall(pattern, string)  # re参数
    print('phone num is:' % phoneNum)
  
  parseString(msg1)
  parseString(msg2)
  parseString(msg3)
  ```
### 正则表达式pattern优化

#### 重复出现的字符
- r'\d\d\d\d-\d\d\d-\d\d\d'中\d重复出现，重复出现的可以用大括号内部加上重复次数表达：
- r'\d{4}-\d{3}-\d{3}'

#### 更多搜寻比对模式
##### 使用小括号分组
- 025-28350000
- r'\d\d\d-\d\d\d\d\d\d\d\d'
- r'(\d\d\d)-(\d\d\d\d\d\d\d\d)'
- r'(\d{2})-(\d{8})' 
##### re.search()--括号分组的group()
- 当使用re.search()执行比对时，未来可以使用group()传回比对符合的不同分组，
如：group()或group(0)传回第一个比对相符的文字，group(1)传回括号的第一组文字，
group(2)传回括号的第二组文字。
- ```python
  import re
  msg = 'Please call my secretary using 025-26669999'
  pattern = r'(\d{2})-(\d{8})'
  phoneNum = re.search(pattern, msg)    # 传回搜寻结果
  print('full number is : %s' % phoneNum.group())   # 显示完整号码
  print('full number is : %s' % phoneNum.group(0))   # 显示完整号码
  print('area number is : %s' % phoneNum.group(1))   # 显示完整号码
  print('phone number is : %s' % phoneNum.group(2))   # 显示完整号码
  ```
- ```
  执行结果
  full number is : 025-26669999
  full number is : 025-26669999
  area number is : 025
  phone number is : 26669999
  ```
##### re.findall()--括号分组的group()
- 如果所搜寻比对的正则表达式字符串有用小括号分组，若是使用findall()方法处理，
会传回元组(tuple)的列表(list)，元组内的每个元素就是搜寻的分组内容。
- ```python
  import re
  msg = 'Please call my secretary using 025-26669999 or 025-24445555'
  pattern = r'(\d{2})-(\d{8})'
  phoneNum = re.search(pattern, msg)    # 传回搜寻结果
  print(phoneNum)
  ```
- `执行结果 [('025', '26669999'), ('025', '24445555')]`

#### groups()
- 注意这是groups(), 有在group后面加上s，当我们使用re.search()搜寻字符串时，可以使用这个方法取得分组的内容。
- 可以使用多重指定的观念
- areaNum, localNum = phoneNum.groups()   # 多重指定
- ```python
  import re
  msg = 'Please call my secretary using 025-26669999'
  pattern = r'(\d{2})-(\d{8})'
  phoneNum = re.search(pattern, msg)    # 传回搜寻结果
  areaNum, localNum = phoneNum.groups()   # 留意是groups()
  print('area number is : %s' % areaNum)   # 显示完整号码
  print('phone number is : %s' % localNum)   # 显示完整号码
  ```
- ```执行结果： 
  area number is : 025
  phone number is : 26669999
  ```
#### 部分字符在小括号内
- 常看到部分字符在小括号内，如： (025)-26669999
- 在处理小括号时，方法是\(和\)

#### 使用管道 | 
- | 在正在表达式称管道，使用管道可以同时搜寻对比多个字符串。
- pattern = 'Mary|Tom' # 注意单引号'或|旁不可留空白

#### 多个分组的管道搜寻
- pattern = John(son|nason|nathan)
- ```python
  import re
  msg = 'Johnson, Johnnason and Johnnathan will attend my party tonight'
  pattern = 'John(son|nason|nathan)'
  txts = re.findall(pattern, msg)   # 传回搜寻结果
  print(txts)
  for txt in txts:
    print('John' + txt)
  ```
- ```执行结果
  ['son', 'nason', 'nathan']
  Johnson
  Johnnason
  Johnnathan
  ```
#### 使用 ? 搜寻
- 在正则表达式中若某些括号内的字符串或正则表达式可有可无，执行搜寻时皆算成功
- `pattern = r'John((na)?son)'`  # ?前的na字符串可有可无
- `pattern = r'(\d\d\d-)?(\d{8})` #  ?前括号内的内容可有可无
#### 使用 * 搜寻
- 在正则表达式中某些字符串或正则表达式可从0到多次，执行搜寻时皆算成功。
- `pattern = 'John((na)*son)'` # 字符串na可以0到n次
#### 使用 + 号搜寻
- 在正则表达式中若是某些字符串或正则表达式壳可从1到多次，执行搜寻时皆算成功。
- `pattern = 'John((na)+son)'`  # 字符串na可以1到多次
#### 搜寻时忽略大小写
- 搜寻时若是在search()或findall()内增加第三个参数re.I或re.IGNORECASE,
搜寻时就会搜寻大小写，至于打印输出时将以原字符串的格式显示。
- `txt = re.findall(pattern, msg, re.I)` # 传回搜寻忽略大小写的结果
#### 贪婪与非贪婪搜寻
- pattern = `(son){3, 5}` # 代表所搜寻的字符串是'sonsonson', 'sonsonsonson', 'sonsonsonsonson'
- pattern = `(son){3, }` # 代表重复3此以上皆符合。 pattern = `(son){,10}` # 代表重复10此以下皆符合。
##### 贪婪模式（greedy）
- ```python
  import re
  def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:
      print('search failure', txt)
    else:
      print('search success', txt.group())
  msg = 'sonsonsonsonson'
  pattern = '(son){3, 5}'
  searchStr(pattern, msg)
  ```
- 由上述程序可知，搜寻模式中3，4或5个son重复就算找到了，
咳嗽python执行结果是列出最多重复的字符串，5次重复，这是python的默认模式，
这种模式又称贪婪模式（greedy）。

##### 非贪婪模式
- 非贪婪模式是列出最少重复的字符串，以这个实例而言是重复3次，方法是在正则表达式的搜寻模式右边增加？符号
- pattern = '(son){3, 5}?'    # 非贪婪模式

#### 正则表达式的特殊字符
##### 特殊字符表
- `\d`   0~9的整数子元
- `\D`  除了0~9的整数子元以外的其他字符
- `\s`  空白、定位、Tab键、换行、换页字符
- `\S`  除了空白、定位、Tab键、换行、幻夜字符以外的其他字符
- `\w`  数字、字母和底线_字符， [A-Za-z0-9_]
- `\W`  除了数字、字符、字母、底线_字符和[A-Za_z0-9_]以外的其他字符
- `pattern = '\w+'` # 意义是把不限长度的数字、字母和底线字符当作符合搜寻
- `pattern = 'John\w*'`  # John开头后面接0~多个数字、字母和底线字符
- `\d+'` 表示不限长度的数字
- `\s`  表示空格
- `\w+` 表示不限长度的数字、字母和底线字符连续字符
##### 字符分类
- 在字符分类中，中括号内可以不用放上正则表示法的反斜杠\执行.、?、*、(、)等字符的转译。
例如，[2-5.]会搜寻2-5的数字和句点，这个语法不用写成[2-5\.]。
- `[a-z]`  代表a-z的小写字符
- `[A-Z]`  代表A-Z的大写字符
- `[aeiouAEIOU]` 代表英文发音的元音字符
- `[2-5]`  代表2-5的数字

##### 字符分类的^字符
###### 中括号内的^
- 如果在中括号内的左方加上^字符，意义是搜寻不在这些字符内的所有字符。
- `pattern = '[^aeiouAEIOU]'`  返回不会出现[aeiouAEIOU]的字符
###### 正则表达式^字符
- 在正则表达式起始位置加上^字符，表示正则表达式的字符串必须出现在被搜寻字符串的起始位置，这样搜寻成功才算成功。


#### 正则表达式的$字符
- 正则表示法的末端放置$字符时，表示正则表示法的字符串必须出现在被搜寻字符串的最后位置，这样搜寻成功才算成功。

#### 单一字符使用通配符 “.”
- 正则表示法的末端放置$字符时，表示正则表示法的字符串必须出现在被搜寻字符串的最后位置，这样搜寻成功才算成功。
#### 所有字符使用通配符 "."
- “.”字符与“*”组合，可以搜寻所有字符，意义是搜寻0到多个通配符（换行字符除外）。

#### 换行字符
- “.*”搜寻时碰上换行字符，搜寻就停止。Python的re模块提供参数re.DOTALL，
功能是包括搜寻换行字符，可以将此参数放在search( )、findall( )或compile( )。
- `txt = re.search(pattern, msg, re.DOTALL)` 传回搜寻含换行字符结果





















---

---

---

---

