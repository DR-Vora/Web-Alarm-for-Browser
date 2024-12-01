import time
import webbrowser
import winsound  # For sound notification (Windows only)
from datetime import datetime, timedelta

def play_sound():
    # Play a simple beep sound (Windows only)
    frequency = 2000
    duration = 1000   # 1 second
    winsound.Beep(frequency, duration)

def get_alarm_time():
    while True:
        alarm_time_input = input("Enter the alarm time (HH:MM:SS or HH:MM AM/PM): ")
        try:
            # Try parsing in 24-hour format
            alarm_time = datetime.strptime(alarm_time_input, "%H:%M:%S")
            return alarm_time
        except ValueError:
            try:
                # Try parsing in 12-hour format
                alarm_time = datetime.strptime(alarm_time_input, "%I:%M %p")
                return alarm_time
            except ValueError:
                print("Invalid format. Please try again.")

def main():
    alarms = []
    
    while True:
        alarm_time = get_alarm_time()
        url = input("Enter the URL of the website to open: ")
        
        # Adjust the alarm time to today's date
        now = datetime.now()
        alarm_time = alarm_time.replace(year=now.year, month=now.month, day=now.day)

        # If the alarm time is in the past, set it for the next day
        if alarm_time < now:
            alarm_time += timedelta(days=1)

        alarms.append((alarm_time, url))
        
        more_alarms = input("Do you want to set another alarm? (yes/no): ").strip().lower()
        if more_alarms != 'yes':
            break

    print("Alarms set:")
    for alarm in alarms:
        print(f"Alarm set for {alarm[0].strftime('%H:%M:%S')} to open {alarm[1]}")

    while True:
        current_time = datetime.now()
        
        for alarm_time, url in alarms:
            # Check if the alarm time is reached
            if current_time >= alarm_time and current_time < alarm_time + timedelta(seconds=1):
                print(f"Alarm! Opening {url} at {current_time.strftime('%H:%M:%S')}")
                webbrowser.open(url)
                play_sound()
                
                # Ask for snooze
                snooze = input("Do you want to snooze for 5 minutes? (yes/no): ").strip().lower()
                if snooze == 'yes':
                    alarm_time += timedelta(minutes=5)
                    print(f"Snoozed! Next alarm set for {alarm_time.strftime('%H:%M:%S')}")
                    alarms.append((alarm_time, url))  # Add the snoozed alarm
                else:
                    alarms.remove((alarm_time, url))  # Remove the alarm if not snoozed

        time.sleep(1)

if __name__ == "__main__":
    main()