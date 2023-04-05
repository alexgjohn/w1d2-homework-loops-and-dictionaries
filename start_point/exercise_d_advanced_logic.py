# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

# 2. Print the difference between the largest and smallest value:
# numbers_difference = max(numbers) - min(numbers)
# print(numbers_difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
# got_it = False
# for i in range(len(numbers) - 1):
#     if numbers[i] == 2 and numbers[i + 1] == 2:
#         got_it = True
#         break
# print(got_it)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

# total_of_numbers = 0
# ignore_start = numbers.index(6)
# ignore_end = numbers.index(7) + 1
# new_numbers = numbers[:ignore_start] + numbers[ignore_end:]
# for new_number in new_numbers:
#     total_of_numbers = total_of_numbers + new_number

# print(total_of_numbers)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

# for i, num in enumerate(numbers):
#     if num == 13 or (i > 0 and numbers[i-1] = 13) or (i < len(numbers) -1 and numbers[i+1] == 13):
#         continue
#     print(num)

#the above didn't work, so I'm going to copy/paste some chatgpt code and see if that runs without error

# for i, num in enumerate(numbers):
#     if num == 13 or (i > 0 and numbers[i-1] == 13) or (i < len(numbers)-1 and numbers[i+1] == 13):
#         continue
#     print(num)

sum_of_numbers = 0
for i, num in enumerate(numbers):
    if num == 13 or (i > 0 and numbers[i-1] == 13) or (i < len(numbers)-1 and numbers[i+1] == 13):
        sum_of_numbers = sum_of_numbers + num
        continue
print(sum_of_numbers)

#the above isn't exactly it, i know, but i'm happy i got that far!




