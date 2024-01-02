friends = [
    
    ("Eric", 18.0),
    ("Elvis", 17.0),
    ("James", 20.0),
     ("Simon", 16.0),
     ("Risper", 10.0)
]


hackers = lambda friends:friends[1] >= 18

hacker_buddies = list(filter(hackers, friends))


for i in hacker_buddies:
    print(i)

