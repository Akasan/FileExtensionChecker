from udeco.FileExtensionChecker import extension_checker, InvalidExtensionException


@extension_checker(filename="xml,pdf,jpg")
def hoge(filename):
    print(filename)


