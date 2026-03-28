import time
from datetime import datetime
import winsound

def play_alarm():
    for _ in range(5):
        winsound.Beep(1000, 800)  # frequency, duration(ms)

def alarm_clock(alarm_time, snooze_minutes):
    print(f"\n⏰ Alarm set for {alarm_time}")

    while True:
        current_time = datetime.now().strftime("%H:%M")

        if current_time == alarm_time:
            print("\n🔔 ALARM RINGING 🔔")
            play_alarm()

            choice = input("Press S to snooze or any key to stop: ").lower()

            if choice == "s":
                print(f"😴 Snoozing for {snooze_minutes} minutes...")
                time.sleep(snooze_minutes * 60)
                play_alarm()

            break

        time.sleep(10)

def main():
    print("⏰ Simple Python Alarm Clock ⏰")

    alarm_time = input("Enter alarm time (HH:MM): ").strip()
    snooze_minutes = int(input("Enter snooze time (minutes): "))

    alarm_clock(alarm_time, snooze_minutes)
    print("✅ Alarm stopped. Have a good day!")

main()
