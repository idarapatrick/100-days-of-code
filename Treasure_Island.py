one = input("Enter a number: ")
two = input("Enter another number: ")
sum = int(one) / int(two)
final_sum = "{:0.4f}".format(sum)
print("The sum is {0}".format(round(sum), 2))
print(final_sum)

check = input("do you want to see the last number of the second dogits?")

if check == "yes" or check == "Yes" or check == "YES":
    print(two[-1])
elif check == "no":
    print("ok")
else:
    print("error")