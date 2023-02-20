# This is how the django per view caching works from the urls.py file
def decor(timer):
    def func(code):
        print("func")
        print(code)
    return func


def thunder():
    pass


decor(60)(thunder)
