def add(x,y):
    z = int(x) + int(y)
    print(x + ' + ' + y + ' = ' + str(z))

def sub(x,y):
    z = int(x) - int(y)
    print(x+' - '+y+' = '+ str(z))

def multi(x,y):
    z = int(x) * int(y)
    print(x+' * '+y+' = '+ str(z))

print('Enter the two values :')
x = input()
y = input()

add(x,y)
sub(x,y)
multi(x,y)