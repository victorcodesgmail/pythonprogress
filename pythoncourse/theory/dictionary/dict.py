capitals = {"USA":"Washington DC", "China":"Beijing", "Nairobi":"Kenya"}

# print(capitals['USA'])
# not safe 

print(capitals.get('USA')) 
print(capitals.get('Kenya'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())


for key, value in capitals:
    print(key, value)
    
    
    
capitals.update({'Germany':'NATO'})

capitals.pop('USA')

capitals.remove()