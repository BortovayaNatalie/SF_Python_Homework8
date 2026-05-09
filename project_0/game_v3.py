import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Используем алгоритм бинарного поиска: диапазон делится пополам и, 
    в зависимости от полученной подсказки переносим левую или правую границы диапазона
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Счетчик попыток
    count = 0
    low = 1  # присваиваем значение, соответствующее нижней границе диапазона поиска
    high = 101  # присваиваем значение, соответствующее верхней границе диапазона поиска +1

   # Формируем условие цикла - пока диапазон без остатка делится на два
    while True:
        middle = (low + high)//2
        count += 1 # увеличиваем счетчик на каждой итерации
        if middle == number:
            break  # выход из цикла если угадали
        elif number > middle:
            low = middle + 1  # перезаписываем переменную левую границу массива
        else:
            high = middle - 1 # перезаписываем переменную правую границу массива

    
    # Ваш код заканчивается здесь

    return count

#print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

# RUN
if __name__ == '__main__':
    score_game(game_core_v3)