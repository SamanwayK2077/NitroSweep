from time import localtime, strftime, sleep
from colorama import Fore
import requests
import random
import string
from pyfiglet import Figlet

def print_ascii_art(text):
    custom_fig = Figlet(font='standard')
    ascii_art = custom_fig.renderText(text)
    print(ascii_art)

print_ascii_art("NitroSweep")

class NitroSweep:
    def __init__(self, code_type: str, prox=None, codes=None):
        self.type = code_type
        self.codes = codes
        self.proxies = prox
        self.session = requests.Session()
        self.prox_api = (
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
        )

    def __proxies__(self):
        req = self.session.get(self.prox_api).text
        if req is not None:
            open("./data/proxies.txt", "a+").truncate(0)
            for proxy in req.split("\n"):
                proxy = proxy.strip()
                proxy = f"https://{proxy}"
                open("./data/proxies.txt", "a").write(f"{proxy}\n")

    def generate(self, scrape=None):
        if scrape == "True" or (scrape is None and self.proxies is None):
            self.__proxies__()

        print_ascii_art("[NitroSweep] is ready to find codes.")

        for _ in range(int(self.codes)):
            try:
                if self.proxies == "True":
                    prox = {
                        "http": random.choice(
                            open("./data/proxies.txt", "r").read().splitlines()
                        )
                    }
                else:
                    prox = None

                if self.type == "boost":
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
                req = self.session.get(
                    f"https://discordapp.com/api/entitlements/gift-codes/{code}",
                    proxies=prox,
                    timeout=10,
                ).status_code

                if req == 200:
                    print(
                        f"{Fore.GREEN}[NitroSweep] discord.gift/{code} | {Fore.GREEN}Valid code"
                    )
                    open("./data/valid.txt", "a").write(f"{code}\n")
                elif req == 404:
                    print(
                        f"{Fore.RED}[NitroSweep] discord.gift/{code} | {Fore.RED}Invalid code"
                    )
                elif req == 429:
                    print(
                        f"{Fore.YELLOW}[NitroSweep] discord.gift/{code} | {Fore.YELLOW}Rate Limited"
                    )

            except Exception as e:
                print(f"{Fore.RED}[NitroSweep] {e}")

        print(
            f"{Fore.LIGHTMAGENTA_EX}[NitroSweep] NitroSweep has successfully checked {self.codes} codes."
        )
        sleep(1.5)

if __name__ == "__main__":
    while True:
        code_type = input(
            f"{Fore.LIGHTMAGENTA_EX}[NitroSweep] Code Type (boost, classic): "
        )
        prox=True

        codes = input(f"{Fore.LIGHTMAGENTA_EX}[NitroSweep] Number of codes to test (Higher number=Higher chance to find \nanswer but means higher time): "
        )
        NitroSweep(code_type, prox, codes).generate()
