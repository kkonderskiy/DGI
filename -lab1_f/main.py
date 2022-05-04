import math
from PIL import Image, ImageDraw

n_mas = 10
size = 10
matrix = [0.0] * n_mas

for i in range(n_mas):
    matrix[i] = [0.0] * size

for j in range(n_mas):
    for k in range(size):
        matrix[j][k] = [0.0] * size

test_matrix = [0] * size
for i in range(size):
    test_matrix[i] = [0.0] * size

def crete_matrix_BW(matrix, test_matrix):
    for i in range(n_mas + 1):
        if i == n_mas:
            image = Image.open(f'test.jpg')  # Открываем изображение
        else:
            image = Image.open(f'mas{i+1}.jpg')  # Открываем изображение

        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
        width = image.size[0]  # Определяем ширину
        height = image.size[1]  # Определяем высоту
        pix = image.load()  # Выгружаем значения пикселей

        for j in range(width):
            for k in range(height):
                if i == n_mas:
                    if pix[j, k] < (10, 10, 10):
                        test_matrix[k][j] = 1
                    else:
                        test_matrix[k][j] = -1
                else:
                    if pix[j, k] < (10, 10, 10):
                        matrix[i][k][j] = 1
                    else:
                        matrix[i][k][j] = -1
    return matrix, test_matrix


def crete_matrix_G(matrix, test_matrix):
    for i in range(n_mas + 1):
        if i == n_mas:
            image = Image.open(f'test.jpg')  # Открываем изображение
        else:
            image = Image.open(f'mas{i + 1}.jpg')  # Открываем изображение

        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
        width = image.size[0]  # Определяем ширину
        height = image.size[1]  # Определяем высоту
        pix = image.load()  # Выгружаем значения пикселей

        for j in range(width):
            for k in range(height):
                if i == n_mas:
                    test_matrix[k][j] = pix[j, k][0] / 255
                else:
                    matrix[i][k][j] = pix[j, k][0] / 255
    return matrix, test_matrix

coef = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]


#for i in range(size):
#   print(test_matrix[i])

def trans_matrix(matrix):
    matrix_trans = [0.0] * n_mas
    for i in range(n_mas):
        matrix_trans[i] = [0.0] * size

    for j in range(n_mas):
        for k in range(size):
            matrix_trans[j][k] = [0.0] * size

    for i in range(n_mas):
        for j in range(size):
            for k in range(size):
                matrix_trans[i][j][k] = matrix[i][k][j]
    return matrix_trans

def sum_matrix_step(matrix, matrix_trans, coef):
    sum_matrix = [0.0] * n_mas
    print(coef)
    for i in range(n_mas):
        sum_matrix[i] = [0.0] * size

    for j in range(n_mas):
        for k in range(size):
            sum_matrix[j][k] = [0.0] * size

    for i in range(n_mas):
        for j in range(size):
            for k in range(size):
                for u in range(size):
                    sum_matrix[i][j][k] += matrix_trans[i][u][k] * matrix[i][j][u] * coef[i]
    return sum_matrix

def matrix_weight(result):
    matrix_W = [0] * size
    for i in range(size):
        matrix_W[i] = [0] * size

    for i in range(n_mas):
        for j in range(size):
            for k in range(size):
                matrix_W[j][k] += result[i][j][k]
                matrix_W[j][k] = round(matrix_W[j][k], 1)

    return matrix_W

def norm_matrix(matrix_W, test_matrix):
    test_matrix_exit = [0] * size

    for i in range(size):
        test_matrix_exit[i] = [0] * size

    for j in range(size):
        for k in range(size):
            for u in range(size):
                test_matrix_exit[j][k] += matrix_W[j][u] * test_matrix[u][k]
    matrix_Y_norm = test_matrix_exit

    for i in range(size):
        for j in range(size):
            if matrix_Y_norm[i][j] > 0:
                matrix_Y_norm[i][j] = 1
            else:
                matrix_Y_norm[i][j] = 0
    return matrix_Y_norm

def matrix_dist(matrix, matrix_Y_norm):
    sum_dist = [0] * n_mas
    matrix_start_dist = [0] * n_mas

    for i in range(n_mas):
        matrix_start_dist[i] = [0] * (size * size)

    for i in range(n_mas):
        u = 0
        for j in range(size):
            for k in range(size):
                matrix_start_dist[i][u] = matrix[i][j][k]
                u += 1

    matrix_Y_norm_start_dist = [0] * (size * size)

    u = 0
    for i in range(size):
        for j in range(size):
            matrix_Y_norm_start_dist[u] = matrix_Y_norm[i][j]
            u += 1

    for i in range(n_mas):
            sum_dist[i] += math.dist(matrix_start_dist[i], matrix_Y_norm_start_dist)
    return sum_dist

matrix, test_matrix = crete_matrix_BW(matrix, test_matrix)

matrix_trans = trans_matrix(matrix)

result = sum_matrix_step(matrix, matrix_trans, coef)

matrix_W = matrix_weight(result)

matrix_Y_norm = norm_matrix(matrix_W, test_matrix)

print(matrix_dist(matrix, matrix_Y_norm))
print(min(matrix_dist(matrix, matrix_Y_norm)))


