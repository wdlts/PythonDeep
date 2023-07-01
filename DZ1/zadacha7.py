while True:
    try:
        number = int(input("Input num: "))
    except ValueError:
        print("This is not a number")
        exit()
    if number < 1 or number > 999:
        print("Number should be not less than 1 and not more than 999")
    else:
        numlength = len(str(number))
        match numlength:
            case 1:
                result = number * number
            case 2:
                result = number - 75
            case 3:
                result = ''.join(reversed(str(number)))
                for item in result:
                    minus = 0
                    if item == "0":
                        minus += 1
                        result = result[minus:]
        print(result)
        exit()
