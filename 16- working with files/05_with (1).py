# f = open("harry.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("16- working with files/harry.txt", "r") as f:
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with synax