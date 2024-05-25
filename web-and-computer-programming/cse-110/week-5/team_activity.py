# print('Enter a list of numbers, type - when finished.')
# numbers = []
# number = -1
# while number != 0:
#     number = int(input('Enter number: '))
#     numbers.append(number)

# sum_numbers = 0
# average = 0
# largest = 0
# for number in numbers:
#     sum_numbers += number
#     if number > largest:
#         largest = number

# average = sum(numbers)/(len(numbers)-1)
# print(len(numbers))
# print(f'The sum is: {sum_numbers}')
# print(f'The aver is: {average}')
# print(f'The largest number is: {largest}')

#Stretch challenge 1
print('Enter a list of numbers, type 0 when finished.')
numbers = []
number = -1
while number != 0:
    number = int(input('Enter number: '))
    if (number != 0):
        numbers.append(number)

sum_numbers = 0
average = 0
largest = 0
smallest = 999

for number in numbers:
    sum_numbers += number
    if number > largest:
        largest = number
    if number < smallest and number > 0:
        smallest = number

average = sum(numbers)/len(numbers)
print(len(numbers))
print(f'The sum is: {sum_numbers}')
print(f'The aver is: {average}')
print(f'The largest number is: {largest}')
print(f'The smallest number is: {smallest}')
print('The sorted list is:')
sorted_list = sorted(numbers)
for i in sorted_list:
    print(i)
