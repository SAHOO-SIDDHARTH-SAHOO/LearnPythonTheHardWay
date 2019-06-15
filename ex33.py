i = 0
numbers = []
def increment(value):
    return value+1

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    #i = i + 1
    i= increment(i)
    print("Number now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
