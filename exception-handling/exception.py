# the error that can be controlled through program is called exception

# in try block we write code which can throw error

# in except block we tell the program what to do if there is any exception occour

# else: block will run if there is no exception

# finally will execute if ther eis or there is no exception

try:
    a=int(input())
    b=int(input())
    c=a//b
except Exception as e:
    print(e)
else:
    print("a//b: ",c)

finally:
    print("Hello")
