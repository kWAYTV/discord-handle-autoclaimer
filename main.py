import threading
import requests
import json
from colorama import Fore, Style
import time
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import random
disable_warnings(InsecureRequestWarning)

class PomeloSender:
    def __init__(self, endpoint="pomelo"):
        self.endpoint = endpoint
        self.tokenlist = []
        self.wordlist = []
        self.proxylist = []

        print(f"{Fore.YELLOW}⏰ Warning: This will put your account at risk for temporary (or possibly permanent) terminations. Use an alt to stay safe.")
        print(f"{Fore.BLUE}Created by Jam (jaa.am)")

        with open('tokens.txt', 'r') as f:
            self.tokenlist = [line.strip() for line in f.readlines()]
            print(f"{Fore.GREEN}✔ Loaded {len(self.tokenlist)} tokens successfully.")

        with open('words.txt', 'r') as f:
            self.wordlist = [line.strip() for line in f.readlines()]
            print(f"{Fore.GREEN}✔ Loaded {len(self.wordlist)} words successfully.")

        with open('proxies.txt', 'r') as f:
            self.proxylist = [line.strip() for line in f.readlines()]
            print(f"{Fore.GREEN}✔ Loaded {len(self.proxylist)} proxies successfully.")
        
    def send(self, token):
        session = requests.Session()
        session.verify = False
        while True:
            for username in self.wordlist:
                url = f"https://discord.com/api/v9/users/@me/{self.endpoint}"
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": token
                }
                data = {
                    "username": username 
                }
                proxy = random.choice(self.proxylist)
                proxies = {
                    "http": f"http://{proxy}", 
                    "https": f"http://{proxy}"
                }
                session.proxies.update(proxies)
                try:
                    response = session.post(url, headers=headers, json=data)

                    if response.status_code != 429:
                        print(f"{Fore.GREEN}✔ Sent username '{username}' to endpoint '{self.endpoint}' successfully. Token: {token[-5:]} Proxy: {proxy} Response: {response.json()}{Style.RESET_ALL}")
                    else:
                        
                        if "retry_after" in response.json():
                            print(f"{Fore.YELLOW}⏰ Rate-limit Detected! Sleeping {int(response.json()['retry_after'])+1} seconds before retrying.{Style.RESET_ALL}")
                            time.sleep(int(response.json()['retry_after'])+1)
                        else:
                            print(f"{Fore.RED}✘ Failed to send username '{username}' to endpoint '{self.endpoint}'. Proxy: {proxy} Response: {response.json()}{Style.RESET_ALL}")
                except:

                    
                    print(f"{Fore.RED}✘ Failed to send username '{username}' to endpoint '{self.endpoint}'. Removing proxy from list. Proxy: {proxy}")
                    self.proxylist = [p for p in self.proxylist if p != proxy]

    def start_sending(self):
        threads = []
        for token in self.tokenlist:
            t1 = threading.Thread(target=self.send, args=(token,))
            threads.append(t1)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

if __name__ == "__main__": 
    pomeloSender = PomeloSender()
    pomeloSender.start_sending()
