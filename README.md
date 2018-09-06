# Word-Counter

### 简介

统计文本文件的字符数、单词数和行数的程序，以及还具备其他扩展功能，并能够快速地处理多个文件。 

### 程序的处理模式：

```py
wordCounter.py [parameter] [filename]
```

### 基本功能列表

1. wordCounter.py  -c  file.c      //返回文件 file.c 的字符数（实现）
2. wordCounter.py  -w  file.c     //返回文件 file.c 的词的数目  （实现）
3. wordCounter.py  -l  file.c       //返回文件 file.c 的行数（实现）

### 扩展功能

1. wordCounter.py  -s   file       //递归处理目录下符合条件的文件。（实现）

2. wordCounter.py   -a  file.c   //返回更复杂的数据（代码行 / 空行 / 注释行）。（未实现）

   **空行：**本行全部是空格或格式控制字符，如果包括代码，则只有不超过一个可显示的字符，例如“{”。

   **代码行**：本行包括多于一个字符的代码。

   **注释行：**本行不是代码行，并且本行包括注释。一个有趣的例子是有些程序员会在单字符后面加注释：

   ​		`} // 注释`，在这种情况下，这一行属于注释行。

   **`fileName`**  	文件或目录名，可以处理一般通配符

3. -x 参数。这个参数单独使用。如果命令行有这个参数，则程序会显示图形界面，用户可以通过界面选取单个文件，程序就会显示文件的字符数、行数等全部统计信息。（未实现）
