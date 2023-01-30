# A TON of privacy
## ATOP - A tool for investigating TON network and its NFT.

"A TON of Privacy" formally called ATOP ... is a tool for conducting OSINT investigations on TON (Telegram 🙃) NFTs.  
  
The TON network is increasingly integrated with the Telegram ecosystem, via NFT. Telegram allows people to purchase numbers, domains and nicknames through cryptocurrency.  
  
ATOP aims to give visibility into the addresses and details of the holders of these assets. Using this tool you will be able to retrieve:
- Address of the owner
- Scam status
- Balance
- Other related NFT
  
ATOP supports:
- TON DNS
- TON NICKNAME
- TON PHONE NUMBERS (+888)

## INSTALLATION
Install dependencies using pip and the file requirements.
```
pip install -r requirements.txt
```
### USAGE 
Retrieve information about a:
- Telephone numbers
```
python atop.py --target +888 12345678
```
- Nickname 
```
python atop.py --target @telegram_nickname
```
- Domain 
```
python atop.py --target atop.ton
```
The OUTPUT will contain information about the owner of the asset.
```
Welcome in the realm of.....

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
v 0.0.1 

 [!] START CRAWLING.... NUMBER: +888XXXXXXXXXXXX

 [+]  Details for number: +8880XXXXXXXXXXXXXXXXX
  ├  Owner address:  0:c8351922XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  ├  Is scam:  False
  ├  Last activity:  2023-XXXXXXXXXXXXx
  ├  Balance:  0.9XXXXXXXXXX
  └  ------------------------------------

 [+]  NFTs found: 2
  ├  Address: EQCJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  |  Name: +888 XXXXXX, Kind: CollectionItem
  |  Collection: Anonymous Telegram Numbers
  |  Url: https://nft.fragment.com/number/XXXXX.webp
  |
  ├  Address: EQCnIG-ZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  |  Name: +888 XXXXXXX, Kind: CollectionItem
  |  Collection: Anonymous Telegram Numbers
  |  Url: https://nft.fragment.com/number/XXXXXX.webp
  └  ------------------------------------

Process finished with exit code 0
```
The flag `-c` supports pivots and in depth analysis, ATM it helps to correlate TON domains to ENS domains, simply pivoting on the second-level domain.
```
[+]  Details for domain ENS domain: xxxxxx.eth
  ├  Owner address:  0xd8xxxxxxxxxxxxxxxxxxxxxxx
  ├  Registration:  2020-xxxxxxxxxxxxxxxx
  ├  Expiry:  2034-xxxxxxxxxxxxxxxxxxxxxx
  └  ------------------------------------
```
