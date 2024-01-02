payinfo = [
    
    ("Eric", 50.0),
    ("Elvis", 60.0),
    ("James", 40.0),
     ("Simon", 5.0),
     ("Risper", 100.0)
]
# map(function, iterable)
to_dollars = lambda payinfo: (payinfo[0], payinfo[1]/150)


listdollar = list(map(to_dollars, payinfo))

print(listdollar)
for i in listdollar:
    print(i)
    
    
    