

def n_bottles(n):
    while n>99:
        print("I want to sing a funnier song than", n, ",bottles.")
        n = n - 1
    while n>5 & n<=99:
        print(n, "bottles of beer on the wall,", n, ",bottles of beer.")
        n = n-1
        print("take one down pass it around,", n,"bottles of beer on the wall.")
    while n>1 & n<=5:
        print("I want to sing a funnier song than", n, ",bottles.")
        n = n - 1
    while n==1:
        print("One bottle of beer on the wall, One bottle of beer.")
        print("Take one down, pass it around, no more bottles of beer on the wall.")
        n = n - 1
    if n==0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store, buy some more, 99 bottles of beer on the wall.")
        n = n - 1
    
        
        

if __name__ == "__main__":
    n_bottles(100)
