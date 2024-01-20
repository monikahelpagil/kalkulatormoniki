def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Dzielenie przez zero!"
    return x / y

def main():
    while True:
        print("\nProsty Kalkulator")
        print("Wybierz operację.")
        print("1.Dodaj")
        print("2.Odejmij")
        print("3.Pomnóż")
        print("4.Podziel")

        wybor = input("Wybierz (1/2/3/4): ")

        if wybor in ('1', '2', '3', '4'):
            num1 = float(input("Wprowadź pierwszą liczbę: "))
            num2 = float(input("Wprowadź drugą liczbę: "))

            if wybor == '1':
                print("Wynik:", add(num1, num2))

            elif wybor == '2':
                print("Wynik:", subtract(num1, num2))

            elif wybor == '3':
                print("Wynik:", multiply(num1, num2))

            elif wybor == '4':
                print("Wynik:", divide(num1, num2))

            kolejna_operacja = input("Czy chcesz wykonać kolejną operację? (tak/nie): ")
            if kolejna_operacja.lower() != "tak":
                break
        else:
            print("Nieprawidłowy wybór")

if __name__ == "__main__":
    main()
