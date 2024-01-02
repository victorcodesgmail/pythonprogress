import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        guess = random.randint(low, high)
        if low == high:
            guess = low
        feedback = input(f'Is {guess} too HIGH(H) too low(L) or correct(C)')
        
        if feedback == 'h':
            high = guess - 1
            
        elif feedback == 'l':
            low = guess + 1
    print(f"You got it, Number is {guess}")
    print("Hello {name}, Its time you rewrite the program by yourself:These are the instructions \ Imagine you know a number but you want the computer to guess sodeign the program so that the computer knows when the number is high or low and if correct write the number down")
    
computer_guess(10)
    
    
    
    #wri