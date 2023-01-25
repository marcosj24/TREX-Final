import requests
import time
from colorama import init, Fore, Back, Style
import socket
def checkproxy():
    proceed = str(input("Do you wish to proceed to check your proxies?(y/n)"))
    if proceed.lower() == "y":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        localip = s.getsockname()[0]
        s.close()
        def timeit(proxy):
            data=proxy.split(":")
            ip=data[0]
            port=data[1]
            user=data[2]
            pwd=data[3]

            try:
                proxies = {
                "http": f"http://{user}:{pwd}@{ip}:{port}",
                "https": f"http://{user}:{pwd}@{ip}:{port}",
                }
                # ip = get('https://api.ipify.org').text
                # print('My public IP address is: {}'.format(ip))
                resp=requests.get("https://api.ipify.org", proxies=proxies)
                return resp.text,"HTTP(s)"
            except:
                proxies = {
                "http": f"http://{user}:{pwd}@{ip}:{port}",
                # "https": f"https://{user}:{pwd}@{ip}:{port}",
                }
                resp=requests.get("https://api.ipify.org", proxies=proxies)
                return resp.text,"HTTP"


        file=open("Accounts\Toolbox\Proxies\proxies.txt")
        proxies=file.read()
        file.close()
        proxies=proxies.split("\n")



        for proxy in proxies:
            start_time=time.time()
            ip,protocol=timeit(proxy)
            end_time=time.time()
            total_time=int((end_time-start_time)*1000)
            if ip == localip:
                print(Fore.WHITE + proxy,"",Fore.RED + "PROXY NOT WORKING")
            else:
                print(Fore.WHITE + proxy,"",ip,"",str(total_time)+"ms","",protocol)



        print(Fore.GREEN + "Completed" + Fore.WHITE)




