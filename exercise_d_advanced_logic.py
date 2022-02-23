# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

for number in numbers:
  if number % 2 ==0:
    print (number)


# 2. Print the difference between the largest and smallest value: 

smallest_number = min(numbers)
largest_number = max(numbers)

difference = largest_number - smallest_number

print (f'The difference between the largest and smallest number is {difference}.')


# 3. Print True if the list contains a 2 next to a 2 somewhere. 

single_two = False # Initilise single_two boolean to false
double_two = False # Initilise double_two boolean to false

for number in numbers:
    if single_two == False:
        if number == 2:
            single_two = True
    if single_two == True:
        if number == 2:
            double_two = True
            print (f'Yes, the number list does contain a 2 next to a 2!')
            break


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

sum_of_numbers = 0
cogs_are_spinning = True # A boolean that will stop and start counting - initially set to true :)

for number in numbers:
    if cogs_are_spinning == True:
        if number != 6:
            sum_of_numbers += number
        else:
            cogs_are_spinning = False # stop adding numbers to number total
    else:
        if number == 7:
            cogs_are_spinning = True  # start adding numbers to number total

print (f'The total sum of numbers, ignoring those between 6 and 7, is {sum_of_numbers}.')

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

sum_of_numbers = 0
after_13 = False
for number in numbers:
    if after_13 == False and number != 13:
            sum_of_numbers += number
            after_13 = False
    else:
            after_13 = True
        

print (f'The total sum of numbers until 13 is {sum_of_numbers}.')






