import random


def main():
    intentos_realizados = 0

    numero = random.randint(1, 100)
    print('Estoy pensando en un numero entre 1 y 100.')

    while intentos_realizados < 10:
        estimacion = int(input('Intenta adivinar: '))
        intentos_realizados += 1

        if estimacion < numero:
            print('Tu estimacion es muy baja.')
        if estimacion > numero:
            print('Tu estimacion es muy alta.')
        if estimacion == numero:
            break

    if estimacion == numero:
        print(
            f"!Bien! Adivinaste mi numero en {intentos_realizados} intentos.")
    else:
        print(f"No. El numero que estaba pensando era {numero}.")

    pass


if __name__ == '__main__':
    main()
