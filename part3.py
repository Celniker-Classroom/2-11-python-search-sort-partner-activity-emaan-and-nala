#write your python code here
from random import randint #This line imports the randint function from the random module. (generates a random integer between two specified values

ranNums = [] #name your list and make sure it is empty!

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for num in range(10): #for loop appends 5 numbers to list
    ranNums.append(randint(1, 50)) # adds a random number between 1-50 to the list


random_number = int(input("Enter a random number between 1 and 50:"))
print("generated list:", ranNums)
print("Searching for", random_number)

comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found

for num in ranNums:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if num == random_number:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

smallest = min(ranNums) # finds smallest number
biggest = max(ranNums)

sum = 0
for num in ranNums:
    sum += num

middle = int(len(ranNums) / 2)
halved = ranNums[:middle]
print("The list split in half is", halved)

ranNums.extend(ranNums)
print(ranNums)
ranNums = 
if random_number in ranNums:
    print("Number", random_number,"found in the list after", comparisons, "comparisons. The smallest number in the list is", smallest)
else:
    print("Number", random_number,"not found in the list after", comparisons, "comparisons. The smallest number in the list is", smallest)
print("The biggest number is", biggest,". The sum of the numbers in the list is", sum)

ranNums.sort()
print("This is the list sorted:", ranNums)