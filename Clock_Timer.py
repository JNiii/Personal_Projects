#A program that simulates the countdown and stopwatch function of
#Clock Timer


import time

def get_user_input():
    sec = int(input('Enter time in seconds: '))
    return sec

def count_down(seconds):
    while seconds != 0:
        minute, sec = seconds // 60, seconds % 60
        time.sleep(1)
        print(minute,'min', sec,'sec')
        seconds -= 1
    print('Time is up!')

def stop_watch():
    seconds = 0
    try:
        while True:
            minute, sec = seconds // 60, seconds % 60
            time.sleep(1)
            print(minute, 'min', sec, 'sec')
            seconds += 1
    except:
        print('Time taken before stopping:', minute, 'min', sec, 'sec')



 
