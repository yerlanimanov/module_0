import numpy as np

def score_game(game_core_v):
    '''��������� ���� 1000 ���, ���� ������ ��� ������ ���� ��������� �����'''
    count_ls = [] #����������� ������ �������
    np.random.seed(1)  # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
    random_array = np.random.randint(1, 101, size=(1000)) #������ �� 1000 ������������ ����� ����� �� 1 �� 100
    for number in random_array:
        count_ls.append(game_core_v(number)) #�������� �� ����� ���������� ������� ������� game_core_v3 ����� ���� �����
    score = int(np.mean(count_ls)) #������� ������� �������������� �������� ���������� ������� ����� �����
    print(f"��� �������� ��������� ����� � ������� �� {score} �������")
    return(score)

def game_core_v3(number):
    import math #��������� ���������� math, ��� ���������� � ������� �������
    count = 1 #���������� ������� ����� �����
    predict = 50 #�������������� �����
    uplim=100 #������� ����� ������
    downlim=1 #������ ����� ������
    while number != predict: #���� �� ������� ����� ��������� ���
        count+=1 
        if number > predict: 
            downlim=predict 
            predict += math.ceil((uplim-downlim)/2) #����������� �������������� ����� �� �������� ���������� ���������
        elif number < predict: #
            uplim=predict #
            predict -= math.ceil((uplim-downlim)/2) #��������� �������������� ����� �� �������� ���������� ���������
    return(count) # ����� �� �����, ���� �������
score_game(game_core_v3)