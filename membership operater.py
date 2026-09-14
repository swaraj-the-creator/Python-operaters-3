print("Enter marks obtained in 5 subjects")
mark1 = int( input())
mark2 = int( input())
mark3 = int( input())
mark4 = int( input())
mark5 = int( input())
tot = mark1 + mark2 + mark3 + mark4 + mark5
avg = int(tot / 5)
valran = range(0,101)
if avg not in valran:
    print("invalid input")
elif avg in range(91,101):
    print("Your grade is A1")
elif avg in range(81,91):
    print("Your grade is A2")
elif avg in range(71,81):
    print("Your grade is B1")
elif avg in range(61,71):
    print("Your grade is B2")
elif avg in range(51,61):
    print("Your grade is C1")
elif avg in range(41,51):
    print("Your grade is C2")



