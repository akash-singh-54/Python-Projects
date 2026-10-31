import random
ucount = 0 
ccount =0

for i in range(1,4):
    print("round", i,":")
    user = int(input("Guess a number between 1 to 100: "))
    computer = random.randint(1,100)
    if (user > computer):
        print("Computer Choice: ", computer)
        print("User is the Winner")
        ucount+=1
    elif (user < computer):
        print("Computer Choice: ", computer)
        print("Computer is the Winner")
        ccount +=1
    else:
        print("Computer Choice: ", computer)
        print("Match is draw")
        i -= 1
    print("\n")


if (ucount > ccount):
    print("User is the Winner")

elif (ucount < ccount):
    print("Computer is the Winner")

else:
    print("Match is draw")