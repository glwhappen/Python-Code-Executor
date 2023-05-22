# Python Code Executor

> Execute Python code seamlessly

[English Doc](README.md) | [中文文档](README_CN.md)

## Use Cases

If you find yourself in a situation where you need to execute Python code on a machine without a Python environment, this tool is for you.

This utility is incredibly compact, resulting in a single file when packed. It can be easily copied and used anywhere.

For instance, if you need to execute a POST request and inspect the result in a remote environment, this tool comes in handy. You can generate the specific POST request code directly from Postman, insert it into the tool, and run it effortlessly.

## Advanced Usage

The tool's source code includes only a few commonly used libraries. If you require additional libraries, you can modify the code accordingly and then repack it.

Currently imported modules are:
1. requests
2. json

## Packaging Commands

Once you've installed pyinstaller in your environment, you can use the following commands to package the tool:
```shell
pip install pyinstaller
```
```shell
pyinstaller -F manage.py
```

This tool is designed to streamline the process of running Python code in environments where a Python setup is not readily available. Enjoy coding on the go!