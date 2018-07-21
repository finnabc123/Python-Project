import time
from datetime import datetime as dt

# host_temp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_List = ["www.facebook.com", "facebook.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Time.....")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_List:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Fun Hours.....")
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_List):
                    file.write(line)
            file.truncate()
    time.sleep(5)
