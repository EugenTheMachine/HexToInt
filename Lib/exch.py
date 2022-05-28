# модуль с функциями для перевода чисел в разные системы исчисления

# функция перевода элементов hex-строки в целочисленные значения
def str_init(str_):
    div = 0
    if str_ == '0':
        div = 0
    elif str_ == '1':
        div = 1
    elif str_ == '2':
        div = 2
    elif str_ == '3':
        div = 3
    elif str_ == '4':
        div = 4
    elif str_ == '5':
        div = 5
    elif str_ == '6':
        div = 6
    elif str_ == '7':
        div = 7
    elif str_ == '8':
        div = 8
    elif str_ == '9':
        div = 9
    elif str_ == 'a' or str_ == 'A':
        div = 10
    elif str_ == 'b' or str_ == 'B':
        div = 11
    elif str_ == 'c' or str_ == 'C':
        div = 12
    elif str_ == 'd' or str_ == 'D':
        div = 13
    elif str_ == 'e' or str_ == 'E':
        div = 14
    elif str_ == 'f' or str_ == 'F':
        div = 15
    return div


# функция перевода целочисленных значений в элементы hex-строки
def str_init_reverse(s):
    div = 0
    if s == 0:
        div = '0'
    elif s == 1:
        div = '1'
    elif s == 2:
        div = '2'
    elif s == 3:
        div = '3'
    elif s == 4:
        div = '4'
    elif s == 5:
        div = '5'
    elif s == 6:
        div = '6'
    elif s == 7:
        div = '7'
    elif s == 8:
        div = '8'
    elif s == 9:
        div = '9'
    elif s == 10:
        div = 'A'
    elif s == 11:
        div = 'B'
    elif s == 12:
        div = 'C'
    elif s == 13:
        div = 'D'
    elif s == 14:
        div = 'E'
    elif s == 15:
        div = 'F'
    return div


# функция перевода hex-числа в целочисленное little-endian
def hex_to_int_litend(s):
    leng = len(s)
    sum = 0
    for i in range(0, leng, +1):
        num = str_init(s[i])
        temp = 16**i * num
        sum += temp
    return sum


# функция перевода hex-числа в целочисленное big-endian
def hex_to_int_bigend(s):
    leng = len(s)
    sum = 0
    for i in range(0, leng, +1):
        num = str_init(s[i])
        temp = 16**(leng - i - 1) * num
        sum += temp
    return sum


# функция перевода целочисленного big-endian значения в hex
def bigend_int_to_hex(s):
    st = ''
    leng = len(s)
    sum = 0
    for i in range(0, leng, +1):
        num = str_init(s[i])
        temp = 10 ** (leng - i - 1) * num
        sum += temp
    i = 1
    while sum // (16 ** i) != 0:
        i += 1
    glob = i
    i -= 1
    temp_val = sum // 16 ** i
    sum -= temp_val * 16 ** i
    st += str_init_reverse(temp_val)
    while sum != 0:
        i = 1
        while sum // (16 ** i) != 0:
            i += 1
        i -= 1
        # print(i)
        temp_val = sum // 16 ** i
        sum -= temp_val * 16 ** i
        st += str_init_reverse(temp_val)
    if len(st) < glob:
        h = glob - len(st)
        # print("h is", h)
        for j in range(h, 0, -1):
          st += '0'
    st = '0x' + st
    return st


# функция перевода целочисленного little-endian значения в hex
def litend_int_to_hex(s):
    st = bigend_int_to_hex(s)
    st = st.replace('0x', '')
    st = st[::-1]
    st = '0x' + st
    return st
