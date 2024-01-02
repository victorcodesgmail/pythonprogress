list = ["fish", "python", "fish", "python","fish", "python"]
#This code is not working I had intended to print the list without printind the [ or ] or ,
#debug if you can

print(list)
obj = str(list)

for i in obj:
    if i == '[' or  ']' or ',':
    #   pass  
        print(i ,end = "")
        
    pass
    
print()
        
    
    
