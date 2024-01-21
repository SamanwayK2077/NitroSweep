from time import localtime, strftime
import time
from colorama import Fore
import requests
import random
import string
import os
from pyfiglet import Figlet

def print_ascii_art(text):
    custom_fig = Figlet(font='standard')
    ascii_art = custom_fig.renderText(text)
    print(ascii_art)

print_ascii_art("NitroSweep")

class NitroSweep:
    def __init__(this, code_type: str, prox=None, codes=None):
        this.type = code_type
        this.codes = codes
        this.proxies = prox
        this.session = requests.Session()
        this.prox_api = (
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
        )

    def __proxies__(this):
        req = this.session.get(this.prox_api).text
        if req != None:
            open("./data/proxies.txt", "a+").truncate(0)
            for proxy in req.split("\n"):
                proxy = proxy.strip()
                proxy = f"https://{proxy}"
                open("./data/proxies.txt", "a").write(f"{proxy}\n")

    def generate(this, scrape=None):
        this.__proxies__()
        for _ in range(int(this.codes)):
            try:
                if this.proxies == "True":
                    prox = {
                        "http": random.choice(
                            open("./data/proxies.txt", "r").read().splitlines()
                        )
                    }
                else:
                    prox = None

                if this.type == "boost":
                    code = "".join(
                        [
                            random.choice(string.ascii_letters + string.digits)
                            for i in range(24)
                        ]
                    )
                else:
                    code = "".join(
                        [
                            random.choice(string.ascii_letters + string.digits)
                            for i in range(16)
                        ]
                    )
                req = this.session.get(
                    f"https://discordapp.com/api/entitlements/gift-codes/{code}",
                    proxies=prox,
                    timeout=10,
                ).status_code
                if req == 200:
                    print(
                        f"{Fore.GREEN}[NitroSweep] discord.gift/{code} | valid")
                    print(f"{Fore.MAGENTA}[NitroSweep] Found in "+ (time.time() - stime)+" seconds.")
                    open("./data/valid.txt", "a").write(f"{code}\n")
                if req == 404:
                    print(
                        f"{Fore.RED}[NitroSweep] discord.gift/{code} | invalid"
                    )

                if req == 429:
                    print(
                        f"{Fore.YELLOW}[NitroSweep] discord.gift/{code} | ratelimited"
                    )

            except Exception as e:
                print(f"{Fore.RED}[NitroSweep] {e}")

        print(
            f"{Fore.LIGHTMAGENTA_EX}[NitroSweep] Successfully checked {this.codes} codes."
        )

if __name__ == "__main__":
    while True:
        code_type = input(
            f"{Fore.LIGHTMAGENTA_EX}[NitroSweep] Code Type (boost, classic): "
        )
        prox=True
        scrape_proxy=True
        codes = input(
            f"{Fore.LIGHTMAGENTA_EX}[NitroSweep] Number of codes to sweep: "
        )
        NitroSweep(code_type, prox, codes).generate(scrape=scrape_proxy)
        stime=time.time()
