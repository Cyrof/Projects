import time
from datetime import datetime as dt

hosts_temp = "website_blocker\hosts_copy"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,17) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        print("Not allowed")
        with open(hosts_temp, 'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    f.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
            f.truncate()
        print("Allowed")
    time.sleep(5)
