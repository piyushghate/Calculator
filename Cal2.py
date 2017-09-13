def add(x,y):
    z = int(x) + int(y)
    print(x + ' + ' + y + ' = ' + str(z))

def sub(x,y):
    z = int(x) - int(y)
    print(x+' - '+y+' = '+ str(z))

def multi(x,y):
    z = int(x) * int(y)
    print(x+' * '+y+' = '+ str(z))

def div(x,y):
    z = int(x) / int(y)
    print(x+' / '+y+' = '+str(z))

print('Enter the two values :')
x = input()
y = input()

print('What you want to perform:\n 1)add\n 2)sub\n 3)multi\n 4)div')
choice = input()

if choice == '1' or 'add':
    add(x,y)
elif choice == '2' or 'sub':
    sub(x,y)
elif choice == '3' or 'multi':
    multi(x,y)
elif choice == '4' or 'div':
    div(x,y)