print("yasmina")


print(42+96)

print(42*96)
print(42>96)

def add (a,b):
    print(a+b)
    add(42+96)

def prod(a,b):
    print(a*b)
    prod(42,96)

def sup(a,b):
    print(a>b)
    sup(42,96)

# Day 1#
# t °F = -17,22 °C#
# t °C = 33,8 °F#

def temper(temp,temp_type):
    if type(temp) is int:
        print("farenheit")
        if(temp_type=='C'):
            print('#t °F=-17.22 °C#')
        elif(temp_type=='F'):
            print('#t°C=33,8 °F#')
    else:
        print ('erreur')
temper(15,"C")

def convert_emp(temp,type):
    if type =='C':
        a=(temp*9/5)+32
        return a
    #cas de fehreneit
    elif type == 'F':
        a=(temp-32)*5/9
        return a
    #cas de ni celsius ni fehreneit
    else:
        print('donne le bon type')

#result = convert_temp(25,'F')

# print(result)



string="en forme"
print(string[0],string[-1])
