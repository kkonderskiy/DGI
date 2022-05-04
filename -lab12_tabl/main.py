str1 = "nivalabators12366"
coefbig_j = round(len(str1)/4 + 0.5)
coefbig_i = round(len(str1) / coefbig_j + 0.5)


matrix = [0] * coefbig_i
rang = 0
str2 = ""
random = "10243"
str3 = ""
strdeshifr = ""

for i in range(coefbig_i):
    matrix[i] = [0] * coefbig_j

for i in range(coefbig_i):
    for j in range(coefbig_j):
        if j + rang < len(str1):
            matrix[i][j] = str1[j + rang]
        else:
            matrix[i][j] = " "
    rang += coefbig_j

for i in range(coefbig_j):
    for j in range(coefbig_i):
        str2 += str(matrix[j][i])

print("shifr")
for i in range(len(str2)):
    if str2[i] == " ":
        print("", end="")
    else:
        print(str2[i], end="")
print(" ")

for i in random:
    for j in range(coefbig_i):
        str3 += str(matrix[j][int(i)])

print("rand")
for i in range(len(str3)):
    if str3[i] == " ":
        print("", end="")
    else:
        print(str3[i], end="")
print(" ")

def deshifr(strmy):
    for i in range(coefbig_i):
        rang = 0
        for j in range(coefbig_j):
            matrix[i][j] = str(strmy[i + rang])

            rang += coefbig_i
    print("deshifr")
    print(matrix)

def deshifrRand(strmy, key):
    for i in range(coefbig_i):
        rang = 0
        for j in key:

            matrix[i][int(j)] = str(strmy[i + rang])

            rang += coefbig_i
    print("deshifrRAND")
    print(matrix)

print("Startmatrix")
print(matrix)





deshifr(str2)
deshifrRand(str3, random)

