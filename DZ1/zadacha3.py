def primeorcomposite(number):
    if number < 0 or number > 100_000:
        print("Only numbers from 0 to 100_000")
        exit()
    if number == 0 or number == 1:
        print("Not a prime or composite number")
        exit()

    composite = False
    for i in range(2, number):
        if number % i == 0:
            composite = True
    print("Input number is prime" if composite == False else "Input number is composite")

primeorcomposite(int(input("Input number: ")))
