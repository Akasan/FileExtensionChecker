# UsefulDecorators
## What is this?
UsefulDecorators is for checking file extension of function's arguments.

## How to install
You can install FileExtensionChecker by pip

`pip install FileExtensionChecker`


## How to use
```python
from FileNameChecker import extension_checker

@extension_checker(filename1="xml")
def hoge(filename1):
    print(filename1)

hoge("hoge.xml")
# hoge.xml
hoge(filename1="hoge.xml")
# hoge.xml
hoge("hoge.pdf")
# AssertionError: filename1 requires extension xml. You specified the argument as hoge.pdf
```
