```python
import pandas as pd
url = 'http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/dzjy/index.phtml'
table = pd.read_html(url)[0]
table
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>交易日期</th>
      <th>证券代码</th>
      <th>证券简称</th>
      <th>成交价格(元)</th>
      <th>成交量(万股)</th>
      <th>成交金额(万元)</th>
      <th>买方营业部</th>
      <th>卖方营业部</th>
      <th>证券类型</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2022-04-26</td>
      <td>836239</td>
      <td>长虹能源</td>
      <td>47.68</td>
      <td>21340.0</td>
      <td>0.0</td>
      <td>中信证券股份有限公司深圳福田南证券营业部</td>
      <td>长城证券股份有限公司前海分公司</td>
      <td>A股</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2022-04-26</td>
      <td>832566</td>
      <td>梓</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### 6.1.2　pandas库在爬虫领域的核心代码知识
read_html()函数只是pandas库强大功能的冰山一角，本节将讲解pandas库在爬虫领域的更多核心代码知识。
#### 1.创建DataFrame
DataFrame是pandas库用于组织和管理数据的一种二维表格数据结构，可以将其看成一个Excel工作表。创建DataFrame常用的方法有两种：通过列表创建和通过字典创建。
##### （1）通过列表创建DataFrame
通过列表创建DataFrame有两种方法。第1种方法的代码如下：


```python
import pandas as pd
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



我们还可以在创建DataFrame时自定义列索引和行索引，其中columns代表列索引，index代表行索引，此时a的打印输出结果如下：
代码如下：


```python
import pandas as pd
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['A', 'B', 'C'])
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>B</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>C</th>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



通过DataFrame的columns属性可以查看和修改列索引，代码如下：


```python

import pandas as pd
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['date', 'score'], index=['A', 'B', 'C'])
print(a.columns)    # 查看列索引
a.columns = ['日期', '分数']    # 修改列索引
a
```

    Index(['date', 'score'], dtype='object')
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>日期</th>
      <th>分数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>B</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>C</th>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



第2种方法较为灵活，无须知道数据的具体数量，直接将列表拼接成列即可。该方法在实战中很常用


```python
import pandas as pd
a = pd.DataFrame()  # 创建一个空DataFrame，用于存储之后要拼接的列数据
data = [1, 3, 5]
score = [2, 4, 6]
a['data'] = data
a['score'] = score
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



##### （2）通过字典创建DataFrame
通过字典创建DataFrame的代码如下：


```python
import pandas as pd
b = pd.DataFrame({'data': [1, 3, 5], 'score': [2, 4, 6]})
b
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>data</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



#### 2.数据文件的读取和写入
pandas库可以从多种类型的数据文件中读取数据，并且可以将数据写入这些文件中。本节以Excel工作簿和CSV文件为例进行讲解。
##### （1）文件读取
用read_excel()函数可以读取Excel工作簿中的数据，代码如下：


```python
import pandas as pd
data = pd.read_excel('.\\data.xlsx')
data.head() # 写成（10）则可查看前10行数据，以此类推
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>date</th>
      <th>score</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2018-09-03</td>
      <td>70</td>
      <td>23.55</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2018-09-04</td>
      <td>75</td>
      <td>24.43</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2018-09-05</td>
      <td>65</td>
      <td>23.41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2018-09-06</td>
      <td>60</td>
      <td>22.81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2018-09-07</td>
      <td>70</td>
      <td>23.21</td>
    </tr>
  </tbody>
</table>
</div>




```python
import pandas as pd
data = pd.read_excel('.\\data.xlsx', sheet_name=0)
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>date</th>
      <th>score</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2018-09-03</td>
      <td>70</td>
      <td>23.55</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2018-09-04</td>
      <td>75</td>
      <td>24.43</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2018-09-05</td>
      <td>65</td>
      <td>23.41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2018-09-06</td>
      <td>60</td>
      <td>22.81</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2018-09-07</td>
      <td>70</td>
      <td>23.21</td>
    </tr>
  </tbody>
</table>
</div>



这里的参数sheet_name用于指定要读取的工作表，其值可以是工作表名称，也可以是数字（默认为0，即第1个工作表）。此外，还可用参数index_col来指定以某一列作为行索引。
CSV文件也是一种常见的数据文件格式，它在本质上是一个文本文件，可以用Excel或文本编辑器（如“记事本”）打开。CSV文件中存储的是用逗号分隔的数据，但不包含格式、公式、宏等，因而占用的存储空间通常较小。用read_csv()函数可以读取CSV文件中的数据，其中参数delimiter用于指定数据的分隔符，默认为逗号；参数encoding用于设置编码格式，如果出现中文乱码，则需要设置为'utf-8'或'gbk'。此外，还可以通过参数index_col设置索引列。
代码如下：


```python
import pandas as pd
data = pd.read_csv('.\\data.csv')
data.head()
```

read_csv()函数也可以指定参数，代码如下：


```python
import pandas as pd
data = pd.read_csv('.\\data.csv', delimiter=',', encoding='utf-8')
data.head()
```

##### （2）文件写入
用to_excel()函数可以将DataFrame中的数据写入Excel工作簿，代码如下：

运行之后，将在代码文件所在的文件夹下生成一个Excel工作簿“data_new.xlsx”，其内容如下图所示。


```python
import pandas as pd
data = pd.DataFrame({'unnamed': [0, 1, 2, 3, 4], 'data':['2018-09-03','2018-09-04', '2018-09-05', '2018-09-06','2018-09-07'], 'score': [70, 75, 65, 60, 70], 'price':[23.55, 24.43, 23.41, 22.81, 23.21]})
data.to_excel('.\\data.xlsx')
```


```python
import pandas as pd
data = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A列', 'B列'])
data.to_excel('.\\data1.xlsx')
```

从上图可以看出，工作表的第1列还保留了行索引信息，如果想在写入数据时不保留行索引信息，可以将to_excel()函数的参数index设置为False（设置为True则表示保留行索引信息），代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A列', 'B列'])
data.to_excel('.\\data1.xlsx', sheet_name = '1', index= False)
```

to_excel()函数还有一些常用的参数：sheet_name用于指定工作表名称；columns用于指定要写入的列。
用to_csv()函数可以将DataFrame中的数据写入CSV文件，代码如下：

#### 3.DataFrame中数据的常用操作
创建了DataFrame之后，就可以根据需要操作其中的数据。首先创建一个3行3列的DataFrame用于演示，行索引设定为r1、r2、r3，列索引设定为c1、c2、c3，代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r1</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>r2</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>r3</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



下面讲解数据的选取、筛选、整体情况查看等常用操作。
##### （1）按列选取数据
先从简单的选取单列数据入手，代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
a = data['c1']
a
```




    r1    1
    r2    4
    r3    7
    Name: c1, dtype: int64



可以看到返回的结果不包含列索引信息，这是因为通过data['c1']选取单列时返回的是一个一维的Series格式的数据。如果要返回二维的DataFrame格式的数据，可以使用如下代码：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
b = data[[ 'c1' ]]
b
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>r2</th>
      <td>4</td>
    </tr>
    <tr>
      <th>r3</th>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



如果要选取多列，则需要在中括号[]中以列表的形式给出列索引值。例如，选取c1和c3列的代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
c = data[[ 'c1', 'c3']] # 不能写错data['c1', 'c3']
c
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r1</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>r2</th>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <th>r3</th>
      <td>7</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



##### （2）按行选取数据
可以根据行序号选取数据，代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
# 选取第2行和第3行的数据，注意序号从0开始，左闭右开
a = data[1:3]
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r2</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>r3</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



而pandas库的官方文档推荐使用iloc方法来根据行序号选取数据，这样更直观，而且不像data[1:3]可能会引起混淆报错。代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
b = data.iloc[1:3]
b
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r2</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>r3</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



而且如果要选取单行，就必须使用iloc方法。例如，选取倒数第1行，代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
c = data.iloc[-1]
c
```




    c1    7
    c2    8
    c3    9
    Name: r3, dtype: int64



此时如果使用data[-1]，那么pandas库可能会认为-1是列索引，导致混淆报错。
除了根据行序号选取数据外，还可以使用loc方法根据行索引选取数据，代码如下：



```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
d = data.loc[['r2', 'r3']]
d
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r2</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>r3</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



如果行数很多，可以用head()函数选取前5行数据，代码如下：


```python
e = data.head()
```

这里因为data中只有3行数据，所以data.head()会选取所有数据。如果只想选取前两行数据，可以写成data.head(2).

##### （3）按区块选取数据
按区块选取是指选取某几行的某几列数据。例如，选取c1和c3列的前两行数据，代码如下：


```python
a = data[['c1', 'c3']][0:2] # 也可写成data[0:2][['c1', 'c3']]
```

##### （4）数据筛选
通过在中括号里设置条件可以对行数据进行筛选。例如，选取c1列中数字大于1的行，代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
a = data[data['c1'] > 1]
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r2</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>r3</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



如果有多个筛选条件，可用“&”（表示“且”）或“|”（表示“或”）连接。例如，筛选c1列中数字大于1且c2列中数字等于5的行，代码如下（在筛选条件两侧要加上小括号）：


```python
b = data[(data['c1'] > 1) & (data['c2'] == 5)]  # 用“==”而不是“=”来判断是否相等
```

##### （5）数据整体情况查看
通过DataFrame的shape属性可以获取表格的行数和列数，从而快速了解表格的数据量大小，代码如下：


```python
data.shape
```

运行结果如下，其中第1个数字为行数，第2个数字为列数。因此，通过data.shape[0]和data.shape[1]可分别获取行数和列数。此外，通过len(data)也可获取行数。

##### （6）数据运算
通过数据运算可利用已有的列创建新的一列，运行结果如下，因为表格只有3行，所以data.head()会输出所有行。代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
data['c4'] = data['c3'] - data['c1']
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
      <th>c4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r1</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>r2</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>r3</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



##### （7）数据排序
用sort_values()函数可以将数据按列排序。例如，按c2列进行降序排序的,参数by用于指定按哪一列来排序；参数ascending默认为True，表示升序排序，若设置为False则表示降序排序。a的打印输出结果如下。
代码如下：


```python
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
a = data.sort_values(by='c2', ascending=False)
a
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>c1</th>
      <th>c2</th>
      <th>c3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>r3</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>r2</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>r1</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



##### （8）数据删除
用drop()函数可以删除指定的列或行，其常用语法格式如下：
DataFrame.drop(index=None, columns=None, inplace=False)
这里列出的几个常用参数的含义为：index用于指定要删除的行；columns用于指定要删除的列；inplace默认为False，表示该删除操作不改变原DataFrame，而是返回一个执行删除操作后的新DataFrame，如果设置为True，则会直接在原DataFrame中执行删除操作。
删除单列，如c1列，代码如下：


```python
a = data.drop(columns='c1')
```

删除多列，如c1和c3列，可以通过列表的方式声明，代码如下：


```python
b = data.drop(columns=['c1', 'c3'])
```

删除行，如第1行和第3行，代码如下：


```python
c = data.drop(index=['r1', 'r3'])
```

注意：删除行时要输入行索引而不是行序号，除非行索引本来就是数字，才可以输入对应的数字。
用drop_duplicates()函数可以删除内容重复的行，代码如下：


```python
d = data.drop_duplicates()  # 默认保留首次出现的行，删除之后重复的行
```

用dropna()函数可以删除空行（含有空值的行），代码如下：


```python
e = data.dropna()
```

这种删除方法是只要含有空值的行都会被删除。如果只想删除全为空值的行，可以写成：


```python
data.dropna(how='all')
```

还可用参数thresh来限定非空值的个数，代码如下：


```python
data.dropna(thresh=2)  # 表示行内至少要有两个非空值，否则删除该行
```

上面的代码都是删除数据后又赋给新的变量，不会改变data的内容。如果想要改变data的内容，可以删除数据后重新赋给data，或者将参数inplace设置为True，代码如下：


```python
data = data.dropna()
data.dropna(inplace=True)
```

### 4.DataFrame拼接
pandas库提供的数据合并与重塑功能极大地方便了两个DataFrame的拼接，主要涉及merge()、concat()、append()等函数。这里主要介绍append()函数，它可以方便地将结构相同的DataFrame拼接起来，在爬虫任务中经常会用到。
先创建两个DataFrame用于演示，代码如下：


```python
import pandas as pd
df1 = pd.DataFrame({'公司':['万科', '阿里'], '分数':[90, 95]})
df2 = pd.DataFrame({'公司':['百度', '京东'], '分数':[80, 90]})
df1
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>公司</th>
      <th>分数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>百度</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>京东</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>



现在需要对df1和df2进行上下合并，核心代码如下：


```python
import pandas as pd
df1 = pd.DataFrame({'公司':['万科', '阿里'], '分数':[90, 95]})
df2 = pd.DataFrame({'公司':['百度', '京东'], '分数':[80, 90]})
df3 = df1.append(df2)
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>公司</th>
      <th>分数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>万科</td>
      <td>90</td>
    </tr>
    <tr>
      <th>1</th>
      <td>阿里</td>
      <td>95</td>
    </tr>
    <tr>
      <th>0</th>
      <td>百度</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>京东</td>
      <td>90</td>
    </tr>
  </tbody>
</table>
</div>



可以看到行索引还是原DataFrame的行索引，如果想忽略原DataFrame的行索引，可以将参数ignore_index设置为True，代码如下：


```python
df3 = df1.append(df2, ignore_index=True)
```

也可以不设置ignore_index，在用to_excel()函数导出Excel工作簿时设置index=False来忽略行索引。爬虫实战中，通常是创建一个空的DataFrame，然后用append()函数依次添加每个表格的数据（参见6.3.2节的具体应用）。
实际上，排序、删除、拼接等操作都不会改变原DataFrame的内容，笔者推荐使用重新赋值的方式来获取修改后的DataFrame。