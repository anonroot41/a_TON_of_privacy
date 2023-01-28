from colorama import Fore, Style
import requests
import telethon
import re
import json
import argparse
import random
import time
from datetime import datetime

delays = [0.2, 0.5, 0.6, 0.5, 0.1, 0.4, 1]

uapools = [
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79",
]


def gdelay():
    return random.choice(delays)


def print_banner():
    print(
        """
Welcome in the realm of....."""
        + Fore.RED
        + """

 ▄▄▄         ▄▄▄█████▓ ▒█████   ███▄    █     ▒█████    █████▒   
▒████▄       ▓  ██▒ ▓▒▒██▒  ██▒ ██ ▀█   █    ▒██▒  ██▒▓██   ▒    
▒██  ▀█▄     ▒ ▓██░ ▒░▒██░  ██▒▓██  ▀█ ██▒   ▒██░  ██▒▒████ ░    
░██▄▄▄▄██    ░ ▓██▓ ░ ▒██   ██░▓██▒  ▐▌██▒   ▒██   ██░░▓█▒  ░    
 ▓█   ▓██▒     ▒██▒ ░ ░ ████▓▒░▒██░   ▓██░   ░ ████▓▒░░▒█░       
 ▒▒   ▓▒█░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ░ ▒░▒░▒░  ▒ ░       
  ▒   ▒▒ ░       ░      ░ ▒ ▒░ ░ ░░   ░ ▒░     ░ ▒ ▒░  ░         
  ░   ▒        ░      ░ ░ ░ ▒     ░   ░ ░    ░ ░ ░ ▒   ░ ░       
      ░  ░                ░ ░           ░        ░ ░             
                                                                 
 ██▓███   ██▀███   ██▓ ██▒   █▓ ▄▄▄       ▄████▄▓██   ██▓        
▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▒████▄    ▒██▀ ▀█ ▒██  ██▒        
▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒██  ▀█▄  ▒▓█    ▄ ▒██ ██░        
▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░░██▄▄▄▄██ ▒▓▓▄ ▄██▒░ ▐██▓░        
▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░   ▓█   ▓██▒▒ ▓███▀ ░░ ██▒▓░        
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░   ▒▒   ▓▒█░░ ░▒ ▒  ░ ██▒▒▒         
░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░    ▒   ▒▒ ░  ░  ▒  ▓██ ░▒░         
░░         ░░   ░  ▒ ░     ░░    ░   ▒   ░       ▒ ▒ ░░          
            ░      ░        ░        ░  ░░ ░     ░ ░             
                           ░             ░       ░ ░             
v 0.0.1 """
        + Style.RESET_ALL
    )


class Ton_retriever:

    step = 10000
    offset = 0
    target = ""
    # comprensive scan use Telethon api to retrieve info about users
    comprehensive = False
    currentua = ""
    address = ""
    nft_name = ""
    is_scam = ""
    owner_name = ""
    info = None
    transactions = None
    nfts = None
    type = ""
    kind = ""

    def __init__(self, _telephone_num, _comprehensive):
        self.comprehensive = _comprehensive
        if not self.check_format(_telephone_num):
            print("\n [!] WRONG INPUT FORMAT")
            return 1
        self.stop_cycle = False
        self.refreshUA()
        self.header = {"User-Agent": self.ua()}
        print(f"\n [!] START CRAWLING.... {self.kind}: {self.target} \n")

    """
        TON DNS 0:b774d95eb20543f186c06b371ab88ad704f7e256130caf96189368a7d0cb6ccf
        TON NICKNAME 0:80d78a35f955a14b679faa887ff4cd5bfc0f43b4a4eea2a7e6927f3701b273c2
        TON NUMBERS 0:0e41dc1dc3c9067ed24248580e12b3359818d83dee0304fabcf80845eafafdb2
    """

    def check_format(self, _string):
        status = False
        if re.match(r"\+?888[0-9\s]{0,12}", _string.strip()):
            status = True
            if _string[0] != "+":
                _string = "+" + _string
            self.target = _string.replace(" ", "")
            self.kind = "NUMBER"
            self.type = (
                "0e41dc1dc3c9067ed24248580e12b3359818d83dee0304fabcf80845eafafdb2"
            )
        if re.match(r"[a-z0-9-_]+\.ton", _string.strip()):
            status = True
            self.target = _string.strip()
            self.kind = "DOMAIN"
            self.type = (
                "b774d95eb20543f186c06b371ab88ad704f7e256130caf96189368a7d0cb6ccf"
            )
        if re.match(r"@[a-z0-9]", _string.strip()):
            status = True
            self.target = _string.strip()
            self.kind = "NICKNAME"
            self.type = (
                "80d78a35f955a14b679faa887ff4cd5bfc0f43b4a4eea2a7e6927f3701b273c2"
            )
        return status

    @staticmethod
    def sleeping_time():
        time.sleep(gdelay(delays))

    def refreshUA(self):
        try:
            template = re.compile("<li><a[^>]*>([^<]*)<\/a><\/li>")
            for browser in ["chrome", "edge", "firefox", "safari", "opera"]:
                with requests.get(
                    f"http://useragentstring.com/pages/useragentstring.php?name={browser}"
                ) as response:
                    temp = response.content.decode("utf-8")
                    count = 10
                    for item in template.findall(temp):
                        if item not in self.user_agents:
                            self.user_agents.append(item)
                        count -= 1
                        if count == 0:
                            break
        except Exception as exx:
            self.user_agents = uapools

    def ua(self):
        return random.choice(self.user_agents)

    def print_info(self):
        balance = "N/A"
        last_date = datetime.min

        print(" [+] ", f"Details for {self.kind.lower()}: " + self.target)
        print("  ├  Owner address: ", str(self.address))
        print("  ├  Is scam: ", str(self.is_scam))
        if self.owner_name != "":
            print("  ├  Owner name: ", str(self.owner_name))

        if self.info:
            if "result" in self.info.keys():
                balance = str(int(self.info["result"]["balance"]) / 1000000000)

        if self.transactions and len(self.transactions):
            last_date = datetime.fromtimestamp(self.transactions[0]["utime"])

        print("  ├  Last activity: ", last_date.strftime("%Y-%m-%d %H:%M:%S"))
        print("  ├  Balance: ", str(balance))
        print("  └  ------------------------------------\n")

        processnft = False
        if self.nfts:
            if "data" in self.nfts.keys():
                if "nftItemsByOwner" in self.nfts["data"].keys():
                    print(
                        " [+] ",
                        "NFTs found: %s"
                        % len(self.nfts["data"]["nftItemsByOwner"]["items"]),
                    )
                    processnft = True

        if processnft:
            first = True
            for nftff in self.nfts["data"]["nftItemsByOwner"]["items"]:
                if not first:
                    print("  |")
                print("  ├  Address: %s" % (nftff["address"]))
                print("  |  Name: %s, Kind: %s" % (nftff["name"], nftff["kind"]))
                if "collection" in nftff.keys():
                    print("  |  Collection: %s" % (nftff["collection"]["name"]))
                if "image" in nftff.keys():
                    print("  |  Url: %s" % (nftff["image"]["originalUrl"]))
                first = False
            print("  └  ------------------------------------")

    def request_address_nft(self, addr):
        request_api = "https://api.getgems.io/graphql"
        req_body = {
            "query": "\nquery NftItemConnection($ownerAddress: String!, $first: Int!, $after: String) {\n nftItemsByOwner(ownerAddress: $ownerAddress, first: $first, after: $after) {\n cursor\n items {\n id\n name\n address\n index\n kind\n image: content {\n type: __typename\n ... on NftContentImage {\n originalUrl\n thumb: image {\n sized(width: 480, height: 480)\n }\n }\n ... on NftContentLottie {\n preview: image {\n sized(width: 480, height: 480)\n }\n }\n ... on NftContentVideo {\n cover: preview(width: 480, height: 480)\n }\n }\n collection {\n address\n name\n isVerified\n }\n sale {\n ... on NftSaleFixPrice {\n fullPrice\n }\n }\n }\n }\n}",
            "variables": {"first": 100, "ownerAddress": addr},
        }
        try:
            res = requests.post(request_api, json=req_body, headers=self.header).text
            self.nfts = json.loads(res)
        except Exception as exx:
            print("[-] AN ISSUE OCCURRED DURING RETRIEVING NFT INFO...")

    def request_address_info(self, addr):
        c_addr = addr.split(":")[1]
        request_api = (
            "https://api.ton.cat/v2/explorer/getWalletInformation?address=0%3A" + c_addr
        )
        try:
            res = requests.get(request_api, headers=self.header).text
            self.info = json.loads(res)
        except Exception as exx:
            print(" [-] AN ISSUE OCCURRED DURING RETRIEVING ADDRESS INFO...")

    def request_address_transctions(self, addr):
        c_addr = addr.split(":")[1]
        request_api = f"https://toncenter.com/api/index/getTransactionsByAddress?address=0%3A{c_addr}&limit=20&offset=0&include_msg_body=true"
        try:
            res = requests.get(request_api, headers=self.header).text
            self.transactions = json.loads(res)
        except Exception as exx:
            print(" [-] AN ISSUE OCCURRED DURING RETRIEVING TRANSACTIONS INFO...")

    def request_info(self):
        count = 0
        request_api = f"https://tonapi.io/v1/nft/searchItems?collection=0%3A{self.type}&include_on_sale=false&limit={self.step}&offset={self.offset}"
        try:
            res = requests.get(request_api, headers=self.header).text
            obj = json.loads(res)
            if "message" in obj.keys():
                if obj["message"] == "rate limit exceeded":
                    print(
                        f" [-] RATE LIMIT EXCEEDED... {self.offset} NUMBERS CHECKED.."
                    )
                    exit(1)

            for element in obj["nft_items"]:
                count += 1
                search_field = ""
                if "name" in element["metadata"].keys():
                    search_field = element["metadata"]["name"].replace(" ", "")
                    if self.kind == "NICKNAME":
                        search_field = "@" + element["metadata"]["name"]

                elif "dns" in element.keys():
                    if element["dns"]:
                        search_field = element["dns"]

                if search_field == self.target:
                    self.nft_name = search_field
                    self.address = element["owner"]["address"]
                    self.is_scam = element["owner"]["is_scam"]
                    if "name" in element["owner"].keys():
                        self.owner_name = element["owner"]["name"]

                    self.request_address_info(element["owner"]["address"])
                    self.request_address_transctions(element["owner"]["address"])
                    self.request_address_nft(element["owner"]["address"])
                    self.stop_cycle = True
                    break
        except Exception as exx:
            print(
                f" [-] THERE WAS SOME ISSUE DURING REQUESTING INFO ABOUT TON {self.kind} ..."
            )
            exit(1)
        return count

    def start_searching(self):
        self.offset = 0
        current_finding = self.step
        while not self.stop_cycle and current_finding == self.step:
            current_finding = self.request_info()
            self.offset += current_finding
            time.sleep(gdelay())
        if not self.address:
            print(f" [-] {self.kind} NOT FOUND, {self.offset} {self.kind} PROCESSED...")
        else:
            self.print_info()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Launch me, and u'll receive a TON of privacy..."
    )
    parser.add_argument(
        "--target",
        required=True,
        help="[?] TON number, nickname or domain to analyze ...",
    )
    parser.add_argument(
        "-c",
        "--comprehensive",
        required=False,
        default=False,
        help="[?] Exhaustive research [work in progress] ...",
        action="store_true",
    )
    parser.add_argument(
        "--apiid",
        required=False,
        help="[?] Exhaustive research [work in progress] ...",
    )
    parser.add_argument(
        "--apihash",
        required=False,
        help="[?] Exhaustive research [work in progress] ...",
    )
    print_banner()
    args = parser.parse_args()
    ton_ret = Ton_retriever(args.target, args.comprehensive)
    ton_ret.start_searching()
