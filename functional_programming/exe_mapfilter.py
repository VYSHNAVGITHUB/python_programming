products=[
    [1,"hide&seek",30],
    [2,"oreo",25],
    [3,"dark fntsy",40],
    [4,"parle-g",10],
    [5,"tiger",20]
]
print(products)
proname=list(map(lambda n:n[1],products))   #pro name
print(proname)
price=list(filter(lambda n:n[2]<30,products))    #price<30
print(price)
print(list(map(lambda n:n[1],price)))        #name of price less than 30