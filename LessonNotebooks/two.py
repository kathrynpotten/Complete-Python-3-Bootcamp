import one

print('TOP LEVEL IN TWO.PY')

one.func()

if __name__ == "__main__":
    print('TWO.PY is being run directly!')
else:
    print('TWO.PY has been imported!')


""" conventional usage for if __name__ == "__main__"
def func1():
    pass

def func2():
    pass

if __name__ == "__main__":
    #run the script
    func1()
    func2() """

