# Program to find the position of the first set bit (rightmost 1) in a number

def find_first_set_bit(n):
    if n == 0:
        return -1  # No set bits
    
    position = 0
    while n > 0:
        if n & 1 == 1:
            return position
        n = n >> 1
        position += 1

# Take input from user
num = int(input("Enter a number: "))
result = find_first_set_bit(num)
if result == -1:
    print("No set bits in the number.")
else:
    print(f"The position of the first set bit is: {result}")