from FileExtensionChecker import extension_checker, InvalidExtensionException


@extension_checker(filename="xml")
def hoge(filename):
    print(filename)


try:
    hoge("hoge.pdf")
except InvalidExtensionException:
    print("error")
