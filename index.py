import module as md
name = int(input("Your name: "))

try:
    print(md.mIsqrt(name))
except NameError:
    print('import error')