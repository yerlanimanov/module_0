import numpy as np

def score_game(game_core_v):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = [] #опеределяем список попыток
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000)) #список из 1000 произвольных целых чисел от 1 до 100
    for number in random_array:
        count_ls.append(game_core_v(number)) #получаем за какое количество попыток функция game_core_v3 нашло наше число
    score = int(np.mean(count_ls)) #находим среднее арифметическое значение количества попыток найти число
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v3(number):
    import math #открываем библиотеку math, для округления в большую сторону
    count = 1 #количество попыток найти число
    predict = 50 #предполагаемое число
    uplim=100 #верхний лимит поиска
    downlim=1 #нижний лимит поиска
    while number != predict: #пока не угадали число выполняем код
        count+=1 
        if number > predict: 
            downlim=predict 
            predict += math.ceil((uplim-downlim)/2) #увеличиваем предполагаемое число на половину возможного диапозона
        elif number < predict: #
            uplim=predict #
            predict -= math.ceil((uplim-downlim)/2) #уменьшаем предполагаемое число на половину возможного диапозона
    return(count) # выход из цикла, если угадали
score_game(game_core_v3)