#The classical fizzbuzz exercise from my python course. Not a big deal,
#but I upload this in order to compare python with bash, as I recreated
#the same script. You can find it in the bash repository.



choice = int(input("Enter the number: "))
def function(choice):
    for num in range(1, choice):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num} = fizzbuzz")
        elif num % 3 == 0:
            print(f"{num} = fizz")
        elif num % 5 == 0:
            print(f"{num} = buzz")

function(choice)
