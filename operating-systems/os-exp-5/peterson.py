import threading

N = 2
flag = [False] * N  
turn = 0  

def producer(j):
    while True:
        flag[j] = True
        turn = 1 - j  
        while flag[1 - j] and turn == 1 - j:
            pass
        flag[j] = False

def consumer(i):
    while True:
        flag[i] = True
        turn = i
        while flag[1 - i] and turn == i:
            pass
        flag[i] = False

producer_thread = threading.Thread(target=producer, args=(0,))
consumer_thread = threading.Thread(target=consumer, args=(1,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
