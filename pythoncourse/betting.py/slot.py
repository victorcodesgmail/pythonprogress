import random



ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#to keep this program nice and dynamic  am gonna put what we call a global variable

MAX_LINES = 3

MAX_BET = 100
MIN_BET = 1


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
            
    columns = []
    
      

def deposit():
    
    while True:
        amount = input("Happy new year! what would you like to deposit? $")
        if amount.isdigit(): # we check if they did enter a valid number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than  0,  Amigo")
                
        else:
            print("Please enter a valid amount")
            
    return amount
            

def get_number_of_lines():
    #since we are asking them to enter number of lines we are going to copy everthing we have in function 1 and ask them to enter 
    #Hello copying is not a crime
        while True:
            #Added max lines in string concatenation
            lines = input("Enter the number of lines? #1 - "+ str(MAX_LINES)+" #")
            
            if lines.isdigit(): # we check if they did enter a valid number
                lines = int(lines)
                if 0 < lines  <= MAX_LINES:
                    break
                else:
                    print("Amount must be greater than  0,  Amigo")
                    
            else:
                print("Please enter a valid amount")
                
        return lines


def get_number_of_bets():
    while True:
            #Added max lines in string concatenation
        bet = input(f"Enter  bet ON EACH LINE?Amount beetween {MIN_BET} and {MAX_BET} $ ")
        
        if bet.isdigit(): # we check if they did enter a valid number
            bet = int(bet)
            if MIN_BET <= bet  <= MAX_BET:
                break
            else:
                print(f"Amount must be beetween {MIN_BET} and {MAX_BET},  Amigo")
                
        else:
            
            print("Please enter a valid amount")
            
    return bet

       

    
    
    
def main():
    balance =deposit()
    lines = get_number_of_lines()
    
    
    while True:
        bet = get_number_of_bets()  
        total_bet = bet * lines
        
        
        
        
        
        if total_bet > balance:
            print(f"You do not have enough money. Your balance is {balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines}. Total bet is equal to ${total_bet}")
    
    print(balance,  lines, bet)
main()