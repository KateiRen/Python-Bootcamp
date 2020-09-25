

cart_prices = [20, 3.5, 6.49, 8.99, 9.99, 14.98]

def list_sum(l):
    totalprice=0
    for price in l:
        totalprice+=price
    print(totalprice)    
    # alternativ einfach: 
    print(sum(l))    
    
list_sum(cart_prices)
        



def prices_list(name, price):
    # hier kommt dein Code hin, das "pass" kannst du durch deinen Code ersetzen
    preistabelle=[]
    for i in range(1,11):
        preistabelle.append(str(i)+" x "+name+": "+str(i*price))
    return preistabelle

print(prices_list("Wunderkeks", 0.79))


shelf = ["Zaubersäge", "leer", "Wunderkekse", "Trickarten", "leer"]

def add_shelf(article):
    # hier kommt dein Code hin. 
    # Du darfst von innerhalb der Funktion direkt auf die Variable "shelf"
    # zugreifen, diese muss nicht als Parameter übergeben werden, da sie
    # schon außerhalb der Funktion existiert.
    print("Hier kommt dein Code hin")
    for i in range(0, len(shelf)):
        if shelf[i]=="leer":
            shelf[i]=article
            break
            

add_shelf("Rubik's Cube")
print(shelf)


xs=[]
ys=[]
with open("Kursmaterialien/data/names.csv","r") as file:
    counter = 0
    numMax = 0
    for line in file:
        data = line.split(",")
        #print(line)
        #print(data)
        if data[1]!="Max" or int(data[2])<1950  or int(data[2])>2000 or data[3]!="M" or data[4]!="CA":
            continue
        numMax += int(data[5])
        xs.append(int(data[2]))
        ys.append(int(data[5]))

print(numMax)
