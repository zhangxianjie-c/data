### 概述
C++是以[[C]]语言为基础发展而来，与[[Java]]一样是面向对象的高级程序设计语言。一般用于底层开发/系统开发：比如Android [[Framework]]、JVM、C#的CLR、Python编译器；游戏开发：比如UE5；网络开发；服务端开发；嵌入式开发；
C++几乎完全兼容C语言，即保持的C的优点，又对C的类型进行了改革和扩充，他们的关系类似[子集](语言#子集)(C语言)和[超集](语言#超集)(C++)的概念。
优点：
* C++的编译系统能检查出更多的类型错误。
* [面向对象](语言#面向对象)
* 凭借对C的兼容可以嵌入汇编语言，调用底层

### 关键字
```
//宏定义
/宏名全部用字符串代替，宏名一般用大写字母，类似JAVA的静态常量
# define PI 3.14159

//文件包含
# include<文件名>
# include"[路径]文件名"
第一种直接到C++系统目录查找被包含文件
第二种首先回去指定路径查找，其次再去系统目录
```

### 数据类型

____
<table>
	<tr>
		<td>类别</td>
		<td>数据类型</td>
		<td>字节数</td>
		<td>数据表达范围</td>
	</tr>
	<tr>
	    <td>bool布尔型</td>
	    <td>bool</td>
	    <td>1</td>
	    <td>false,true(0,1)</td>
	</tr>
  <tr>
    <td rowspan="9"; style="text-align: center; vertical-align: middle;">int整型</td>
    <td>基本型(int)</td>
    <td>4</td>
    <td>-2147483648~2147483647</td>
  </tr>
  <tr>
    <td>短整型(short)</td>
    <td>2</td>
    <td>-32768~32767</td>
  </tr>
  <tr>
    <td>长整型(long)</td>
    <td>4</td>
    <td>-2147483648~2147483647</td>
  </tr>
  <tr>
    <td>无符号整型(unsigned [int])</td>
    <td>4</td>
    <td>0~4294967295</td>
  </tr>
  <tr>
    <td>无符号短整型(unsigned short [int])</td>
    <td>2</td>
    <td>0~65535</td>
  </tr>
  <tr>
    <td>无符号长整型(unsigned long [int])</td>
    <td>4</td>
    <td>0~4294967295</td>
  </tr>
  <tr>
    <td>有符号整形(signed [int])</td>
    <td>4</td>
    <td>-2147483648~2147483647</td>
  </tr>
  <tr>
    <td>有符号短整型([signed] short [int])</td>
    <td>2</td>
    <td>-32768~32767</td>
  </tr>
  <tr>
    <td>有符号长整型([signed] long [int])</td>
    <td>4</td>
    <td>-2147483648~2147483647</td>
  </tr>
  <tr>
	<td rowspan="3"; style="text-align: center; vertical-align: middle;">char 字符</td>
    <td>无符号 unsigned char</td>
    <td>1</td>
    <td>0~255</td>
  </tr>
  <tr>
	<td>有符号 [signed] char</td>
    <td>1</td>
    <td>-128~127</td>
  </tr>
   <tr>
	<td>wchar_t 宽字符</td>
    <td>2</td>
    <td>0~65 535</td>
  </tr>
   <tr>
    <td rowspan="3"; style="text-align: center; vertical-align: middle;">float 实型</td>
    <td>单精度浮点型(float)</td>
    <td>4</td>
    <td>-3.4x1038~3.4x1038</td>
  </tr>
  <tr>
	<td>双精度浮点型(double)</td>
    <td>8</td>
    <td>-1.7x10308~1.7x10308</td>
  </tr>
   <tr>
	<td>长双精度浮点型(long double)</td>
    <td>10 or 8</td>
    <td>-1.7x10308~1.7x10308</td>
  </tr>
</table>
表中的[]表示默认，代表括号中的内容可选，如为空，默认就是括号内数据。

