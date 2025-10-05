def calculator():
    print("Доступні операції: +, -, *, /")
    print("Щоб вийти, введіть 'exit'")
    while True:
        res = input("\nВиберіть операцію (+ - * / або exit): ")
        if res.lower() == "exit":
            print("Вихід з калькулятора. До побачення!")
            break
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        if res == "+":
            print("Результат:", a + b)
        elif res == "-":
            print("Результат:", a - b)
        elif res == "*":
            print("Результат:", a * b)
        elif res == "/":
            if b != 0:
                print("Результат:", a / b)
            else:
                print("Помилка: ділення на нуль!")
        else:
            print("Невідома операція")
calculator()