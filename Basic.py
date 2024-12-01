import time
import webbrowser

alarm_time = input("Enter the web alarm as Hr:Min:Sec 12hour formate\n")
print("Alarm is set for", alarm_time)

url = input("Enter the Url of the Website\n")

Sys_time = time.strftime("%I:%M:%S")

while(Sys_time != alarm_time):
    print("Remainig sec are" + Sys_time)
    Sys_time = time.strftime("%I:%M:%S")
    time.sleep(1)

if(Sys_time == alarm_time):
     print("Web page Opend")
     webbrowser.open(url)
