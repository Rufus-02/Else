import time
from threading import Thread


def remind():
    print("О чём вам напомнить?")
    text = str(input())
    print("Через сколько минут?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    print(text)


th = Thread(target=remind, args=())
th.start()
time.sleep(10)
print("Пока поток работает, мы можем сделать что-нибудь ещё.\n")
