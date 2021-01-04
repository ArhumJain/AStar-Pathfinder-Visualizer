array = [
    [0,0,0,0,0],
    [0,2,3,4,0],
    [0,9,1,5,0],
    [0,8,7,6,0],
    [0,0,0,0,0]
]


"""
result = []

def findAdjacent(x, y):
    for dx in range(-1, 2):
        for dy in range(-1,2):
            if dx != 0 or dy != 0:
                if (x + dx > -1) and (x+dx < int(len(array[0]))) and (y+dy > -1) and (y+dy < int(len(array))):
                    result.append(array[x + dx][y + dy])

findAdjacent(4, 4)
print(result)
"""
while True:
    x = input("Grocery Store\n--------\nChoose the following:\n--------\nBuy Item\nSee Items\n\n")
    print(x)
    print(x.lower())
    if x.lower() == "buy items":
        print("yes")
        item_buy = input(f"Balance: 123456\n--------\nWhat would you like to buy")