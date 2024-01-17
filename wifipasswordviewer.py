import subprocess,time,winsound
print("\t\t WELCOME BACK ZAYYAN ")
a=str(input("enter user name: "))
password = int(input("enter password: "))
if a=="Zayyan" and password == 1234:#this is password to login this program
    print("welcome Zayyan!!!\n"
          "wifi data is being initiated plz wait it ")
    time.sleep(0.5)
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
    input("")

    print("\t\t\t\tTHANK YOU")
else:
    print("wrong identification  alarm start")
    print("alarm starts in 2 seconds")
    time.sleep(2)
    frequency = 2500
    duration = 15000
    winsound.Beep(frequency, duration)
