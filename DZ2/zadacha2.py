# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление. Функцию hex
# используйте для проверки своего результата.

a = int(input("Введите целое число: "))

print("USING HEX: ", hex(a))


def convert_to(n):
    s = ''
    h = '0123456789abcdef'
    while n > 0:
        s = h[n % 16] + s
        n = n // 16
    print("NO HEX: 0x"+s)

convert_to(a)