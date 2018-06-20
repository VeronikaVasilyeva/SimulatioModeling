import argparse
import os
import shutil
import time
import numpy
from queue import Queue

#from file import

parser = argparse.ArgumentParser(description='PyTorch CelebA Training')
parser.add_argument('-j', '--workers', default=16, type=int, metavar='N',
                    help='number of data loading workers (default: 4)')
parser.add_argument('--epochs', default=60, type=int, metavar='N',
                    help='number of total epochs to run')
parser.add_argument('--lr', '--learning-rate', default=0.1, type=float,
                    metavar='LR', help='initial learning rate')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('--pretrained', default='', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')
parser.add_argument('--end2end', action='store_true', \
                    help='if true, using end2end with dream block, else, using naive architecture')

seed = 0                # начальное значение гсч
appear_time = 0         # среднее время появления между заявками
service_time = 0        # среднее время обслуживания
loss_probability = 0    # коэффициент (вероятность) потерь
len_queue = 0           # средняя длина очереди
L_queue = 0             # ёмкость буфера
model_time = 0          # абсолютное время жизни модели
queue = Queue()         # буфер сообщений q.put('eat') print(q.get())
message_number = 0      # количество сообщений в модели, переменная состояния

def main():
    global args
    args = parser.parse_args()

    print('img_dir:', args.img_dir)
    print('end2end?:', args.end2end)



if __name__ == '__main__':
    main()
