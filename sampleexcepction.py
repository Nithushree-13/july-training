#raise an exception if the input is not a number
num=input("Enter a number:")
try:
    if not num.isnumeric():
        raise ValueError("input is not valid number.")
    else:
        print(num)
except ValueError as e:
    print(e)