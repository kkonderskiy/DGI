import random
first = 53
last = 89
exp = 2
xer = 0

str = 23 #Число для шифрования

def shifr(first, last, exp, str):
    proizv = first * last
    eler = (first - 1)*(last - 1)
    secret = (2 * eler + 1) / exp
    #print([secret, proizv])
    #print(eler)
    modul = (exp * secret) % eler
    #print(modul)
    coddate = str**exp % proizv
    #print("начало ")
    #print(str)
    #print("kod")
    #print(coddate)
    return([coddate, int(secret), proizv, str])

def deshifr(key, date):
    a = (date**key[0]) % key[1]
    #print("итог ")
    #print(a)
    return a


def test(proizv, exp):
    check = True
    print(exp)
    critmass = 0
    for i in range(proizv):
        result = shifr(first, last, exp, i)

        if i != deshifr([result[1], result[2]], result[0]):
            check = False
            critmass = 0
            #print("Несострел")
        if i == deshifr([result[1], result[2]], result[0]):
            critmass += 1

        if critmass == 10:
            break
        if check == False:
            exp += 1
            check = True
            print(exp)

    proverka = random.randint(3, 3000)
    result = shifr(first, last, exp, proverka)
    #print(proverka)
    #print(result)
    #print(deshifr([result[1], result[2]], result[0]))
    #print(exp)
    if proverka != deshifr([result[1], result[2]], result[0]):
        test(first * last, exp)
    for i in range(proizv):
        result = shifr(first, last, exp, i)
    return exp





expert = test(first*last, exp)
result = shifr(first, last, expert, str)
print(shifr(first, last, expert, str))
print([result[1], result[2]], result[0])
print(deshifr([result[1], result[2]], result[0]))
