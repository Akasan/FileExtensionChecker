from FunctionChecker.FunctionAnnotationChecker import annotation_checker


@annotation_checker
def hoge(x: int, y: float, z: str) -> str:
    return z


print(hoge(1, 2.0, "3.0"))
