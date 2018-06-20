import argparse
import random

parser = argparse.ArgumentParser(description='Simulation model')
parser.add_argument('--L', default=200, type=int)  # ёмкость буфера
parser.add_argument('--Nmax', default=100000, type=int)

appear_time = 3  # среднее время появления между заявками
service_time = 9  # среднее время обслуживания
loss_probability = 0  # коэффициент (вероятность) потерь
len_queue = 0  # средняя длина очереди
model_time = 0  # абсолютное время жизни модели
n = 0  # количество заявок в модели, переменная состояния
current_issue_number = 0  # текущее кол-во поступивших заявок
loss_issue_number = 0  # кол-во потерянных заявок
Tin = 0  # время вхда
Tout = 0  # время выхода
Nmax = 0
L = 0


def increment_state():
    global n
    n += 1


def is_end():
    global n, current_issue_number, Tin, Tout, loss_issue_number, loss_probability, Nmax, L

    if current_issue_number == Nmax:
        loss_probability = loss_issue_number / Nmax
        return True
    else:
        return False


def handle_issues():
    global L, Tin, Tout, n, loss_issue_number
    if Tin < Tout:
        if n == L + 1:
            loss_issue_number += 1
        else:
            increment_state()
        create_issue()
        return
    else:
        n -= 1
        if n == 0:
            Tout = Tin + random.expovariate(1 / service_time)
            increment_state()
            create_issue()
            return
        else:
            Tout = Tout + random.expovariate(1 / service_time)
            handle_issues()


def create_issue():
    global current_issue_number, Tin
    current_issue_number += 1
    Tin = Tin + random.expovariate(1 / appear_time)

# ======================MAIN=============================
args = parser.parse_args()
Nmax, L = args.Nmax, args.L
Tin = random.expovariate(1 / appear_time)
Tout = Tin + random.expovariate(1 / service_time)

increment_state()
create_issue()
i = 1
while not is_end():
    len_queue += n
    i += 1
    handle_issues()

print('Общее число заявок:', Nmax)
print('Размер буффера:', L)
print('Коэффициент(вероятность) потерь:', float(loss_probability))
print('Средняя длина очереди:', len_queue / i)
exit()

