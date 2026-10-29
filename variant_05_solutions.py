"""
Лабораторна робота: Варіант 5
Студент: Рубцов Михаїл
Група: EIP30
"""

# Задача 1: Аварійна посадка БПЛА (складені умови)
def landing_decision(thrust: float, fuel: float, dist_to_runway: float) -> str:
    if fuel < 5 or thrust < 20:
        return "Аварійна посадка в полі"
    elif dist_to_runway <= 10:
        return "Посадка на ЗПС"
    else:
        return "Продовження місії"
    """
    - fuel < 5 або thrust < 20 -> "Аварійна посадка в полі"
    - dist_to_runway <= 10 -> "Посадка на ЗПС"
    - інакше -> "Продовження місії"
    """
    ...

# Задача 2: Класифікація подій "чорної скриньки" (match-case)
def classify_blackbox_event(event: tuple) -> str:
    event_type = event[0]
    priority = event[1]
    payload = event[2]
    match priority:
        case 1:
            return(f"Критична подія ({event_type}): {payload}")
        case 2 | 3 as p:
            return(f"Звичайна подія [пріоритет {p}] ({event_type}): {payload}")
    """
    Приймає (event_type, priority, payload).
    - priority == 1 -> "Критична подія ({type}): {payload}"
    - priority == 2 або 3 (з виразом as p) -> "Звичайна подія [пріоритет {p}] ({type}): {payload}"
    """
    ...

# Задача 3: Моніторинг рівнів кисню (while / continue / break)
def monitor_oxygen(initial_o2: float) -> str:
    o2 = initial_o2
    while True:
        o2 -= 2.0
        if o2 <= 5:
            break
        elif o2 < 20:
            print("Низький рівень кисню")
            continue
    return(f"Аварійна зупинка: O2 = {o2}%")
    """
    У циклі while зменшує рівень кисню на 2.0%.
    - o2 <= 5% -> перериває break і повертає "Аварійна зупинка: O2 = {o2}%"
    - o2 < 20% -> пропускає розрахунок через continue
    """
    ...

# Задача 4: Пошук максимального споживача (zip / dict)
def find_max_power_system(systems: list, powers: list) -> tuple:
    systems_dict = dict(zip(systems, powers))
    power_max = powers[0]
    system_max = systems[0]
    for sys, pow in systems_dict.items():
        if pow > power_max:
            power_max = pow
            system_max = sys
    return(system_max, power_max)
    """
    Створює словник з систем та їх споживання за допомогою zip.
    Знаходить і повертає кортеж (назва_системи, макс_споживання).
    """
    ...
