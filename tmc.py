import time

df_counter = 0

def start():
    global tm_counter
    tm_counter = time.perf_counter()

def end():
    global tm_counter, df_counter
    df_counter = time.perf_counter() - tm_counter
    echo()

def echo():
    tm_h = int(df_counter / (60 * 60))
    tm_m = int(df_counter % (60 * 60) / 60)
    tm_s = int(df_counter % 60)
    print(f'{tm_h}[h] {tm_m}[m] {tm_s}[s]')

start()
