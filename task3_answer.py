money = [1000, 1200, 800, 1500, 1100]

print(money)

total = money[0]+money[1]+money[2]+money[3]+money[4]

#print(f"total ammont recieved so far: ", money[0]+money[1]+money[2]+money[3]+money[4])

print(f"\ntotal ammont recieved so far is = ", total) 

print(f"\nchecking the most recent transaction: ", money[-1:-6:-1])

recent = money[-1]

print(f"\nthe most recent amount sent is:  ", recent)
