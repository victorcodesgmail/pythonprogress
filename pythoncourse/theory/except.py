#handle errors 

try:
    result = 5 / 0
    print(result)
except Exception:
    print("Something is wrong")