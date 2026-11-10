# Smart Alarm System (Beginner Friendly with Random Math Challenge)

import time
import random
from datetime import datetime

print("=== Smart Alarm System ===")
alarm_time = input("Enter alarm time in HH:MM format (24-hour): ")

print("Alarm set for", alarm_time)

snooze_count = 0
MAX_SNOOZE = 2
SNOOZE_TIME = 60  # 1 minute snooze time

def ring_alarm():
    print("\n⏰ Wake up! It's time!")
    for i in range(5):
        print("Beep! Beep! Beep!")
        time.sleep(1)

def challenge_to_stop():
    # generate random numbers and operator
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/', '%'])

    # avoid division by zero
    if operator in ['/', '%'] and num2 == 0:
        num2 = 1

    question = f"{num1} {operator} {num2}"
    correct = round(eval(question), 2)  # round for division results

    print("\nTo stop the alarm, solve this problem:")
    ans = input(f"What is {question}? ")

    try:
        if abs(float(ans) - correct) < 0.01:
            print("✅ Correct! Alarm dismissed.")
            return True
        else:
            print(f"❌ Wrong! Correct answer was {correct}")
            return False
    except:
        print("Invalid input! Try again.")
        return False

# main alarm loop
while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == alarm_time:
        ring_alarm()
        while True:
            choice = input("\nEnter 's' to snooze or 'a' to answer challenge: ").lower()
            if choice == 'a':
                if challenge_to_stop():
                    break
            elif choice == 's':
                if snooze_count < MAX_SNOOZE:
                    snooze_count += 1
                    print(f"Snoozed for 1 minute. (Snooze {snooze_count}/{MAX_SNOOZE})")
                    time.sleep(SNOOZE_TIME)
                    ring_alarm()
                else:
                    print("❗ Snooze limit reached. Answer the challenge to stop.")
            else:
                print("Invalid choice. Try again.")
        break
    time.sleep(1)
