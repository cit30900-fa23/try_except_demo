x = 4/0
# print(x)

try:
    # Code you want to run
    x = 4/0
    # print(x)
    # y = 4/0
    # print(y)

except ZeroDivisionError as e:
    # Code that will run if the "try" code has an exception
    # Call a function that emails the error to the developer; or logs it in a database
    print(f'An error occurred: {e}')

else:
    # Code that will run if the "try" code succeeds
    print(x)

finally:
    # Code that will run no matter what
    print('This was a program to divide two numbers.')