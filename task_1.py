# Найти НОК двух чисел

def search_NOK(a:int , b:int):
    minimum = min(a, b)
    maximum = max(a, b)

    while True:
        rem = maximum % minimum

        if rem == 0:
            return minimum
            
        maximum = max(rem, minimum)
        minimum = min(rem, minimum)
        
print(search_NOK(33, 55))