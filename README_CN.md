# Python 代码执行器

> 轻松执行Python代码

[English Doc](README.md) | [中文文档](README_CN.md)

## 应用场景

如果你发现自己在一个没有Python环境的机器上需要执行Python代码，那么这个工具就是为你准备的。

这个工具非常小巧，打包后只有一个文件，可以轻松复制并在任何地方使用。

例如，如果你需要在一个远程环境中执行一个POST请求并查看结果，这个工具就非常方便。你可以直接从Postman中生成特定的POST请求代码，然后插入到这个工具中运行。

## 高级用法

工具的源代码只包含了一些常用的库。如果你需要其他库，可以自行修改代码，然后重新打包。

目前已导入的模块包括：
1. requests
2. json

## 打包命令

在你的环境中安装pyinstaller后，你可以使用下面的命令来打包这个工具：
```shell
pip install pyinstaller
```
```shell
pyinstaller -F manage.py
```

这个工具旨在简化在没有现成Python环境的地方运行Python代码的过程。尽享移动编程的乐趣！