rows = int(input("Enter loop"))
collumns = int(input("Enter collumns"))

symbol = input("Enter symbol to use")



for i in range(rows):
    for j in range(collumns):
        print(symbol, end="")
        
    print()
    
        