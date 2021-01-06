from pathlib import Path

path = Path("ecommerce")
print(path.exists())

"""p1 = Path("email")
print(p1.mkdir()) """
"""p2 = Path("email")
print(p2.rmdir()) """

pt = Path()
for file in pt.glob('*'):
    print(file)

