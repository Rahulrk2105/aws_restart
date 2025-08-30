print("welcome to guess the number")
print("the rules are simple . I will think of a number , and you will try to guess it.")

import  random
number = random.randint(1,10)
isGuessRight = False

while isGuessRight!= True:
    guess = input("guess the number beteweeen 1 and 10:")
    if int (guess)== number:
        print("you guessed {}.that is corret!you win!".format (guess))
        isGuessRight=True
    else:
         print("you guessed{}.sorry, that isn't it.try again.".format(guess))
        
    
