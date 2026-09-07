print("Welcome to the Prime number checker!")

lower_limit = int(input("\nPlease enter the lower limit of your range: "))

upper_limit = int(input("Please enter the upper limit of your range: "))

print("\nThe prime numbers between " + str(lower_limit) + " and " + str(upper_limit) + " are: ")

for num in range(lower_limit, upper_limit + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

print("\nThank you for using the Prime number checker!")