out = []

def split(number):
    found = False
    for i in range(2, int(number / 2) + 1, 1):
        if(number % i == 0 and not found):
            split(number / i)
            out.append(int(i))
            found = True
    if(not found):
            out.append(int(number))
    
split(156)
print(out)