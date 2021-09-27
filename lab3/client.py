import Pyro4

server = Pyro4.Proxy("PYRONAME:server")

name = input("What is your name? ").strip()

def inputNumbers():
    while(True):
        try:
            a = int(input('Input first number: '))
            b = int(input('Input second number: '))
            return a,b
        except:
            print("Please input only numbers!")

def inputStrings():
    a = input('Input first string: ')
    b = input('Input second string: ')
    return a, b

def inputBinNumber():
    while(True): 
        a, b = inputNumbers()
        if (isBinary(a) and isBinary(b)):
            return str(a), str(b)
        else:
            print("Input number(-es) is (are) not binary.")
            

def isBinary(num):
    for i in str(num):
        if (i in ("0","1")):
            return True
        else:
            return False


        

print(server.welcomeMessage(name))



print('Multiplication &:')
a,b = inputBinNumber()
print(server.multiplication(a,b))

print('Comprassion:')
a,b = inputNumbers()
print(server.comprassion(a,b))

print('Evaluate even or not:')
a,b = inputNumbers()
print(server.evaluate(a,b))

print('Comprassion string:')
a,b = inputStrings()
print(server.stringComprassion(a,b))
