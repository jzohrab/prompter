import time
import yaml
# import pyttsx3
import os
import threading
import random

def read_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def speak(text):
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()
    print(text)
    os.system(f"say -v Daniel \"{text}\"")

def start_prompt(period, phrases):
    while True:
        random.shuffle(phrases)
        for phrase in phrases:
            time.sleep(period)

            # Repeat after a brief pause.
            speak(phrase)
            time.sleep(4)
            speak(phrase)


def main(duration_mins):
    config = read_config('config.yaml')
    threads = []

    for entry in config:
        period = entry['period']
        phrases = entry['say']
        thread = threading.Thread(target=start_prompt, args=(period, phrases))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    time.sleep(duration_mins * 60)
    speak("All done.")

    for thread in threads:
        thread.join(0)  # Terminate threads after the duration is up

if __name__ == "__main__":
    duration_mins = int(input("Enter the duration to run the program (minutes): "))
    main(duration_mins)
