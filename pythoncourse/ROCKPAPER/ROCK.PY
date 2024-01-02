import random

def play():
    use = input(f"'r' for rock , 'p' for paper, 's' for scissor\n" )
    print(f"You chose {use}")
    comput = random.choice(['r', 's', 'p'])
    print(f"HA! HA! AI chose {comput}")
    
    if use == comput:
        print("Its a tie")
        
    if is_win(use, comput):
        return "You won"
    
    return "Computer won"

    
    def is_win(user , computer):
        if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
            return True


    
print(play())