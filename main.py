1.1
n=5
for i in range(1,n+1):
    print ((n-i)*(" ")+(i*" *"))

for i in range(n-1,0,-1):
    print((n-i)*(" ")+(i*" *"))

1.2
h = eval(input("Enter diamond's height: "))

for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
    

1.3
a = int(input("Enter the maximum value.: "))
x = input("Enter O/E/B (Odd or Even or Both): ")
r = input("Y/N (OnlyPrime?): ")
def Odd():
    prime = real
    for number in range(a+1):
        if number == 0 or number == 1 : prime = False
        if prime:
            for i in range(2,number):
                if number % i == 0:
                    prime = False
                    break
        if prime:
            if number % 2 == 0:
                print(number,"Is prime number")
        else:
            ()
            prime = real
def Odd_N():
    prime = real
    for number in range(a+1):
        if number == 0 or number == 1 : prime = False
        if prime:
            for i in range(2,number):
                if number % i == 0:
                    prime = False
                    break
        if prime:
            if number % 2 == 0:
                print(number,"Is prime number")
        else:
            if number % 2 == 0:
              print(number,"Isn't prime number")
            prime = real

def Even():
  prime = real
  for number in range(a+1):
        if number == 0 or number == 1 : prime = False
        if prime:
            for i in range(2,number):
                if number % i == 0:
                    prime = False
                    break
        if prime:
            if number % 2 == 1:
                print(number,"Is prime number")
        else:
            ()
            prime = real
def Even_N():
  prime = real
  for number in range(a+1):
        if number == 0 or number == 1 : prime = False
        if prime:
            for i in range(2,number):
                if number % i == 0:
                    prime = False
                    break
        if prime:
            if number % 2 == 1:
                print(number,"Is prime number")
        else:
            if number % 2 == 1:
              print(number,"Isn't prime number")
            prime = real
def fn():
    #if r == ("Y"):
        prime = real
        for number in range(a+1):
            if number == 0 or number == 1 : prime = False
            if prime:
                for i in range(2,number):
                    if number % i == 0:
                        prime = False
                        break
          
            if prime:
                print(number,"Is prime number")
            else:
                prime = real
      

def fn1():
    #if r == ("N"):        
        prime = real
        for number in range(a+1):
            if number == 0 or number == 1 : prime = False
            if prime :
                for i in range(2,number):
                    if number % i == 0:
                        prime = False
                        break

            if prime:
                print(number,"is prime number")
            else:
                print(number,"isn't prime number")
    
            prime = real
    
if x == ("O"):
    if r == ("Y"):
        Odd()
    elif r ==("N"):
      Odd_N()
if x == ("E"):
  if r == ("Y"):
    Even()
  elif r == ("N"):
    Even_N() 
if x == ("B"):
  if r == ("Y"):
    fn()
  elif r == ("N"):
    fn1()





1.4
a = int(input("Enter Harmonic step: "))        
def sum(a):
    if a < 2:
        return 1
    else:
        return 1 / a + (sum(a-1))
        
for number in range(1,a+1):
    if number == number:
        print("limit = ",number,"Value = ",sum(number))

    
