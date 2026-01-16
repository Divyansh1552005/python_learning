from pathlib import Path

path = Path("/home/divyansh")

print(path)

print(Path.cwd())

user_home = Path.home()

file_path =  user_home / "oke.txt"

print(file_path.exists())
print(file_path.is_file())

project_dir = Path("/home/divyansh/Programming/Projects")

# for item in project_dir.iterdir():
#     if(item.is_dir()):
#         print(item)
    
    
# content = Path("loops.py").read_text()
# print(content)

new_file = Path("wow.txt")
print(new_file.resolve())

print(__file__)

print(new_file.cwd())