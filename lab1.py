file_in = open('in.txt', 'r')
file_out = open('out.txt', 'w')

def read_matrix(s):
    n = int(data[s][0])
    m = int(data[s][1])
    a = [[0 for el in range(0, m)] for els in range(0, n)]
    data2 = data[s+1]
    for i in range(0, n):
        for j in range(0, m):
            a[i][j] = data2[(i*n) + j]
            a[i][j] = int(a[i][j])
    return a

def sum(a, b):
    c = [[0 for el in range(0, len(a[0]))] for els in range(0, len(a))]
    if (len(a) == len(b)) and (len(a[0]) == len(b[0])) :
        for i in range(0, len(a)):
            for j in range(0, len(a[0])):
                c[i][j] = a[i][j] + b[i][j]
        return c
    else:
        return 0

def mult_num (alpha, a):
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            a[i][j] *= alpha
    return a

def transp(a):
    c = [[0 for el in range(0, len(a))] for els in range(0, len(a[0]))]
    for i in range(0, len(a)):
        for j in range(0, len(a[0])):
            c[j][i] = a[i][j]
    return c

def mult_matrix(a,b):
    c = [[0 for el in range(0, len(b[0]))] for els in range(0, len(a))]
    if len(a[0]) == len(b):
        for i in range(0, len(c)) :
            for j in range(0, len(c[i])):
                for t in range(0, len(b)):
                    c[i][j] += a[i][t] * b[t][j]
        return c
    else:
        return 0

data = file_in.readlines()
for i in range(0, len(data)):
    data[i] = data[i].split()

alpha = int(data[0][0])
beta = int(data[0][1])

A = read_matrix(1)
B = read_matrix(3)
C = read_matrix(5)
D = read_matrix(7)
F = read_matrix(9)

X = sum(mult_matrix(mult_matrix(C, transp(sum(mult_num(alpha, A) ,mult_num(beta, transp(B))))), D), mult_num(-1, F))

x = ''
for i in range(0, len(X)):
    for j in range(0, len(X[0])):
        x += str(X[i][j])
        x += ' '
if X != 0:
    file_out.write('1' + '\n')
    file_out.write(str(len(X)) + ' ' + str(len(X[0])) + '\n')
    file_out.write(x)
else:
    file_out.write('0')

file_in.close()
file_out.close()
