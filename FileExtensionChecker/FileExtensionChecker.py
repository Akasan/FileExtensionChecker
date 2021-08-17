class InvalidExtensionException(Exception):
    def __init__(self, arg_name, valid_extension, value):
        msg = f"{arg_name} requires extension {valid_extension}. You specified the argument as {value}"
        super().__init__(msg)


def extension_checker(**vkwargs):
    def _check_filename(func):
        func_varnames = list(func.__code__.co_varnames[:func.__code__.co_argcount])
        args_index = {k: i for i, k in enumerate(func_varnames)}

        def wrapper(*args, **kwargs):
            for varname, extension in vkwargs.items():
                if varname in kwargs:
                    if not kwargs[varname].split(".")[-1] == extension:
                        raise InvalidExtensionException(varname, extension, kwargs[varname])
                elif varname in func_varnames:
                    idx = args_index[varname]
                    if not args[idx].split(".")[-1] == extension:
                        raise InvalidExtensionException(varname, extension, args[idx])

            return func(*args, **kwargs)

        return wrapper

    return _check_filename
