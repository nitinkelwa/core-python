for num in range(1, 12):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print( " The  prime numbers is =",num)

