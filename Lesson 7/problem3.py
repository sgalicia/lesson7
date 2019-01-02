print('-' * 64)
print ('100th Birthday Program: ')
print()
print("Description: This program asks you for you current age and tells you the year that you will turn 100.")

age = input('What is your age today? ')
age = int(age)

year = (100 - age) + 2018
year = str(year)
year = input('You will turn 100 in the year ' + year)

print(year)
print('-' * 64)
print()