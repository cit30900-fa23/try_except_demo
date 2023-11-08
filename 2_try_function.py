def divide(a,b):
    try:
        z = a/b
    except ZeroDivisionError as e:
        return None
    else:
        return z

def main():
    # try:
    #     x = divide(6,3)
    # except ZeroDivisionError as e:
    #     print(e)
    # else:
    #     print(x)

    x = divide(6,0)

    ## THREE WAYS TO WRITE THE IF STATEMENT
    if x != None:
        print(x)
    else:
        print('An error has occurred.')

    if x:
        print(x)
    else:
        print('An error has occurred.')

    # Ternary operator
    # [on_true] if [expression] else [on_false]
    print(x) if x != None else print('An error has occurred.')
    print(x) if x else print('An error has occurred.')


if __name__ == "__main__":
    main()