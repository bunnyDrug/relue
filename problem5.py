#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

numbers = range(20,2,-1)
test_num = 2
iterator = 0

while iterator < len(numbers):
    if test_num % numbers[iterator] == 0:
        iterator +=1
    else:
        test_num +=1
        iterator = 0
        
print(test_num) # 232792560
