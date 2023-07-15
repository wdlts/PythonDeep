# 4. Создайте функцию генератор чисел Фибоначчи

def fibonaccigenerator(n):
    fib1 = 0
    fib2 = 1
    i = 0
    while i<n-2:
        sum = fib1+fib2
        fib1=fib2
        fib2=sum
        i = i+1
        print(sum)

fibonaccigenerator(500)