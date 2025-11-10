def summation(n: int) -> int:
    if n < 0:
        return None # no devuelvo nada??
    return n * (n + 1) // 2  # acordarse de poner el doble / para que sea el ntero

def show_user():
    number = -1
    while number < 0:
        try:
            number = int(input("Please enter a positive number: "))
            if number < 0:
                print("The number must be positive:/")
        except ValueError:
            print("Please enter a valid integer.")

    result = summation(number)
    print(f"The result is: {result}")
