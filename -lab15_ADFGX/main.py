import string
import math
import random
mas_chifr = ["A", "D", "F", "G", "X"]
mas_elem = [0] * 5
maska = {0: "A", 1: "D", 2: "F", 3: "G", 4: "X"}
invert_mask = {"A": "0", "D": "1", "F": "2", "G": "3", "X": "4"}



key = "battle"
mas_index = [0] * len(key)

str_alf_last = list(string.ascii_lowercase)
str_alf_last.remove("i")
str_alf_last[str_alf_last.index("j")] = "i"

for i in range(len(key)):
    mas_index[i] = (i, key[i])

print(mas_index)

shifr = ""
message = "hello"
def size_step_two_mas(shifr_text):
    if (len(shifr_text) / len(key) % 1) != 0:
        step_two_counter = int(len(shifr_text) / len(key)) + 1
    else:
        step_two_counter = len(shifr_text) / len(key)
    return int(step_two_counter)

def step_two(shifr_text):
    step_two_counter = size_step_two_mas(shifr_text)

    mas_start_chifr = [0] * (step_two_counter + 1)
    for i in range(step_two_counter + 1):
        mas_start_chifr[i] = [0] * len(key)

    return mas_start_chifr


for i in range(5):
    mas_elem[i] = [0] * 5

 #строк для заполнения массива

def add_elem(mas, str):
    k = 0
    for i in range(5):
        for j in range(5):
            rand_int = random.randint(0, len(str) - 1)
            mas[i][j] = str[rand_int]
            str.pop(rand_int)
            k += 1
    print(mas)
    return mas


def new_mask():
    result = []
    for i in range(5):
        for j in range(5):
            result += [maska[i]+maska[j]]
    return result

def shifr(message, slovar):
    y = True
    v = ""

    for i in message:
        if i == "j":
            i = "i"
        if i == " ":
            y = False
        else:
            y = True
            v += slovar[i]
    return v


def slovarik(result):
    slovar = {}
    i = 0

    for letter in str_alf_last:
        slovar[letter] = result[i]
        i +=1
    return slovar

def create_new_mas(shifr_text, step_two_result, result):
    x = size_step_two_mas(shifr_text)
    y = 0
    t = False
    for i in range(1, x + 1):
        for j in range(len(key)):
            if y == len(shifr_text) or y > len(shifr_text):
                step_two_result[i][j] = "0"
                t = True
            else:
                step_two_result[i][j] = shifr_text[y]
            y += 1

    return step_two_result



def sort_step_two(shifr_text, new_mas_step_two):
    y = size_step_two_mas(shifr_text)
    sert = list(key)
    for i in range(len(sert) - 1):
        for j in range(len(sert) - i - 1):
                    if sert[j] > sert[j + 1]:
                        x = sert[j]
                        sert[j] = sert[j + 1]
                        sert[j + 1] = x
                        for k in range(y+1):
                            v = new_mas_step_two[k][j]
                            new_mas_step_two[k][j] = new_mas_step_two[k][j + 1]
                            new_mas_step_two[k][j + 1] = v

    return new_mas_step_two

def cout_mas_res(shifr_text, step_two_mas_shifr):
    str_f = ""
    y = size_step_two_mas(shifr_text)

    for i in range(len(key)):
        for j in range(1, y+1):
            str_f += step_two_mas_shifr[j][i]
    return str_f



mas_elem = add_elem(mas_elem, str_alf_last)


jeronimo = 0
for i in range(5):
    for j in range(5):
        str_alf_last.append(mas_elem[i][j])
        jeronimo += 1

print(str_alf_last)
result = new_mask()


slovar = slovarik(result)
print(slovar)
shifr_text = shifr(message, slovar)
print(shifr_text)

step_two_result = step_two(shifr_text)
print(step_two_result)
step_two_result[0] = list(mas_index)
print(step_two_result)

new_mas_step_two = create_new_mas(shifr_text, step_two_result, result)

print(new_mas_step_two)

step_two_mas_shifr = sort_step_two(shifr_text, new_mas_step_two)
print(step_two_mas_shifr)
shifr_str = cout_mas_res(shifr_text, step_two_mas_shifr)
print(shifr_str)

def cout_mas_deshifr(shifr_text, shifr_str):
    y = size_step_two_mas(shifr_text)
    k = 0
    new_mass = step_two(shifr_text)
    for i in range(len(key)):
        for j in range(1, y+1):
            new_mass[j][i] = shifr_str[k]
            k += 1

    new_mass[0] = step_two_mas_shifr[0]
    sert = list(key)

    for i in range(len(sert)):
        if new_mass[0][i][0] != i:
            for j in range(len(sert)):
                if new_mass[0][j][0] == i:
                    for k in range(y+1):
                        v = new_mass[k][i]
                        new_mass[k][i] = new_mass[k][j]
                        new_mass[k][j] = v

    slovar_deshifr = {}
    i = 0
    new_mask_slovar = new_mask()
    for letter in str_alf_last:
        slovar_deshifr[new_mask_slovar[i]] = letter
        i += 1
    print(slovar_deshifr)

    str_f = ""
    y = size_step_two_mas(shifr_text)

    for i in range(1, y + 1):
        for j in range(len(key)):
            str_f += new_mass[i][j]
    print(str_f)
    y = True
    v = ""
    start_deshifr = ""
    str_f = str_f.replace("0", "1")
    print(str_f)
    check = False
    for i in str_f:
        start_deshifr += i
        if start_deshifr == "11":
            start_deshifr = ""
            check = False
        if check == True and len(start_deshifr) == 2:
            if i == 0:
                y = False
            else:
                y = True
                v += slovar_deshifr[start_deshifr]
            start_deshifr = ""
            check = False
        else:
            check = True
    print(v)
    return new_mass

masssss = cout_mas_deshifr(shifr_text, shifr_str)


