def calculate_capacitor_parameters(voltage, distance, dielectric_constant, is_connected):
    epsilon_0 = 8.854e-12  # Фарад/метр
    electric_field = voltage / distance
    capacitance = dielectric_constant * epsilon_0 / distance
    charge = capacitance * voltage
    if not is_connected:
        distance *= 2
    return {
        "electric_field_initial": electric_field,
        "charge": charge,
    }

def main():
    print("Расчет параметров плоского конденсатора")

    # Ввод данных от пользователя
    try:
        voltage = float(input("Напряжение на пластинах (В): "))
        distance = float(input("Расстояние между пластинами (м): "))
        dielectric_constant = float(input("Относительная диэлектрическая проницаемость: "))
        connection_input = input("Конденсатор подключен к источнику питания? (да/нет): ").strip().lower()
        
        if connection_input == "да":
            is_connected = True
        elif connection_input == "нет":
            is_connected = False
        else:
            print("Неверный ответ на вопрос о подключении")
            return

        # Расчет параметров конденсатора
        results = calculate_capacitor_parameters(voltage, distance, dielectric_constant, is_connected)
        
        # Вывод результатов
        print(f"\nРезультаты расчета:")
        print(f"Напряженность электрического поля: {results['electric_field_initial']:.2e} В/м")
        print(f"Заряд на пластинах: {results['charge']:.2e} Кл")
    
    except ValueError:
        print("Ошибка: введены некорректные числовые значения.")

if __name__ == "__main__":
    main()
