'''age=int(input("enter age of child:"))
if age<10 :
     print("not eligible")
else:
        print("eligible")'''
'''number=int(input("enter the number to reach:"))
for i in range(number):
    ''''''
# create an array only within range
arr = list(range(1,25))
print(arr)'''
user_input = input("enter some text to save file:")
from datetime import datetime
current_datetime=datetime.now()
with open("user_input.txt","w")as file:
    file.write(user_input)
print("your input has been saved to 'user_input.txt'.")