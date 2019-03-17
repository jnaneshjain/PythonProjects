from pathlib import Path

path = Path("email")
print(path.exists())
path.mkdir()
path.rmdir()

path1 = Path()
for file in path1.glob('*.py'):
    print(file)