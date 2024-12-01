# 🕒 Web Alarm for Browser

This project provides a simple yet versatile **Web Alarm** system that opens a browser to a specified URL at a scheduled time. It includes both a **basic** and an **advanced** version to cater to different user needs.

---

## ✨ Features

### Basic Version
- Set a single alarm to open a website.
- Simple and minimalistic functionality.
- Alarm time in 12-hour format (HH:MM:SS).
- Continually checks system time until the alarm triggers.

### Advanced Version
- Set multiple alarms with different URLs.
- Accepts alarm time in both 12-hour and 24-hour formats.
- **Snooze Functionality**: Allows users to snooze alarms for 5 minutes.
- **Sound Notification**: Plays a beep sound when the alarm goes off.
- Automatically adjusts for alarms set in the past (triggers the next day).

---

## 🖥️ How to Use

### Basic Version
1. Run the basic script.
2. Enter the alarm time in **12-hour format (HH:MM:SS)**.
3. Provide the URL of the website to open at the scheduled time.
4. Wait for the alarm to trigger and the webpage to open.

### Advanced Version
1. Run the advanced script.
2. Enter the alarm time in **12-hour (HH:MM AM/PM)** or **24-hour (HH:MM:SS)** format.
3. Provide the URL of the website for the alarm.
4. Optionally, set multiple alarms.
5. When an alarm triggers:
   - The URL opens in a browser.
   - A sound plays (if on Windows).
   - Choose to snooze the alarm for 5 minutes or dismiss it.

---

## 📋 Prerequisites

### Libraries Used
- **Basic Version**:
  - `time`: For system time management.
  - `webbrowser`: To open the URL.
- **Advanced Version**:
  - `time`: For system time management.
  - `webbrowser`: To open the URL.
  - `winsound`: For sound notification (Windows only).
  - `datetime`: To handle date and time calculations.

### Installation
No external libraries are required. Python's built-in modules handle all functionality.

---

## 🚀 Running the Code

### Basic Version
```bash
python basic_web_alarm.py
```

### Advanced Version
```bash
python advanced_web_alarm.py
```

---

## 🛠️ Code Overview

### Basic Version
```python
import time
import webbrowser

alarm_time = input("Enter the web alarm as Hr:Min:Sec 12hour format\n")
print("Alarm is set for", alarm_time)

url = input("Enter the Url of the Website\n")

Sys_time = time.strftime("%I:%M:%S")

while(Sys_time != alarm_time):
    print("Remaining seconds are " + Sys_time)
    Sys_time = time.strftime("%I:%M:%S")
    time.sleep(1)

if(Sys_time == alarm_time):
     print("Web page opened")
     webbrowser.open(url)
```

### Advanced Version
Refer to the detailed code in the repository for features like snoozing and multiple alarms.

---

## 📅 Example Usage

### Basic Version
- Input:
  ```
  Enter the web alarm as Hr:Min:Sec 12hour format
  07:30:00
  Enter the Url of the Website
  https://example.com
  ```
- Output:
  ```
  Alarm is set for 07:30:00
  Web page opened
  ```

### Advanced Version
- Input:
  ```
  Enter the alarm time (HH:MM AM/PM):
  7:30 AM
  Enter the URL of the website to open:
  https://example.com
  ```
- Output:
  ```
  Alarm set for 07:30:00 to open https://example.com
  Alarm! Opening https://example.com at 07:30:00
  ```

---

## 🛡️ Limitations
- **Basic Version**:
  - No error handling for invalid time inputs.
  - No sound notification.
- **Advanced Version**:
  - Sound notifications work only on Windows.
  - Alarm snoozing is limited to manual confirmation.

---

## ✍️ Author

- **Dhairya Vora**  
  📧 **Email**: voradhairya22@gmail.com  
  🖇️ **LinkedIn**: https://www.linkedin.com/in/dhairya-vora-475577275

Feel free to reach out for suggestions, improvements, or feedback! 😊
