# PYTHON ALARM CLOCK

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = ".mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 😊")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()  

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        else:
            time.sleep(1)  

if __name__ == "__main__":
    alarm_time = input("Enter your alarm time (HH:MM:SS): ")
    try:
        # Validate time format
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")























































































