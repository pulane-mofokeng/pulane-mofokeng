# 36002887, Mofokeng PM
# Program that calculates the sum of integers

# Ask the user to put in a positive integer
def validate_input(input_str):
    try:
        num = int(input_str)
        if num <= 0:
            return False, num
        return True, num
    except ValueError:
        return False, None


# Calculate the sum of integers
valid_input = False
while not valid_input:
    n_str = input("Enter a positive integer N: ")
    valid_input, n = validate_input(n_str)
    if not valid_input:
        print("Ivalid input. Please enter a positive integer.")

# Output of the sum of positive integers
sum_even = 0
for i in range(1, n+1):
    sum_even += 2*i


print(f"The sum of the first {n} even numbers is: {sum_even}")
