# Using the match case in python.

command = "hello world"
match command:
    case "Hello World":
        print("It is Proper")
    case "hello world":
        print("It is in small case")
    case other:
        print("Nothing do so.")
