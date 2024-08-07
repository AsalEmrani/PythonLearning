import time 
from playsound import playsound

def my_countdown() :
    my_time  = int(input("Enter you'r time in seconds :"))

    for x in range(my_time, 0, -1):
        seconds = x % 60 
        minutes = int(x / 60) % 60 
        hours = int(x / 3600)
        print(f"{hours:02} : {minutes:02} : {seconds:02}")
        time.sleep(1)

    print("Time's up")
    playsound('C:/Users/leyla/Desktop/alarm.mp3')

def main():
    while True:
        current_time = time.strftime("%H:%M:%S")
     
        print(current_time)

        # 1 ثانیه صبر کنید
        time.sleep(1)


if __name__ == "__main__":
    choice = input("what do you what 1 time / 2 count down ")
    if choice == "1" :
        main()
    if choice == "2" :
        my_countdown()
