str = "zello"
rang = 31
first = ord("a")
last = ord("z")
print(first)
print(last)
if rang > (last - first):
    rang -= last - first
    
def shifr(str, rang, first, last):
    result = ""
    for i in str:

        if ord(i) + rang > last:
            result += chr(first + ((ord(i) + rang) % last) - 1)
            print(1)
        else:
            result += chr(first + ((ord(i) + rang) % first))
    print(result)
    return result


def deshifr(str, rang, first, last):
    result = ""
    for i in str:

        if ord(i) - rang < first:
            result += chr(last - (rang - (ord(i) % first)) + 1)

        else:
            result += chr(ord(i) - rang)
    return result




print(deshifr(shifr(str, rang, first, last), rang, first, last))
