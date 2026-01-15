import os

print(os.name)
# print(os.getcwd())

# print(os.listdir())

# os.rename("os_module.py", "os_module_learning.py")

# os.remove("useless.py")

# print(os.environ.get("HOME"))

# print(os.system("ls -la"))

# print(os.getpid())

# print(os.cpu_count())

# print(os.stat("/home/divyansh/oke.txt"))

# print(os.sep)

# for root, dirs, files in os.walk("/home/divyansh"):
#     print(root, files)

print(os.environ.get("USER"))

print(os.path.split("/home/divyansh/oke.txt"))

print(os.path.exists("/home/divyansh"))