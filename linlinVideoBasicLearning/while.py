import re

print("this is a calculate a average number program!")
input_result = input("please only input number until input 'q' to finish, your number: ")

total = 0
count = 0
average = 0

while input_result != 'q':
    if re.match(r'^-?\d+(\.\d+)?$', input_result):
        number = float(input_result)
        total += number
        count += 1
    input_result = input("please only input number until input 'q' to finish, your number: ")

if count > 0:
    average = total / count

print("your average number is : " + str(average))
