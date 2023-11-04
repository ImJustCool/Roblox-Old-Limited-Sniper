from keyauth import api
import time
import json
import requests, json, random, time
from multiprocessing.pool import ThreadPool
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


with open("config.json") as jsonfile:
    config = json.load(jsonfile)


print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░        ░░░░░░░░░░░░░░░░░░░░░░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒   ▒▒▒▒▒▒▒  ▒    ▒▒▒▒   ▒▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒  ▒   ▒▒▒▒▒▒   ▒▒▒▒
▓       ▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓   ▓   ▓  ▓▓   ▓▓▓  ▓▓▓   ▓
▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓   ▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓   ▓▓   ▓   ▓  ▓▓▓   ▓         ▓
▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓   ▓▓▓▓   ▓▓   ▓▓   ▓   ▓   ▓   ▓▓  ▓▓▓▓▓▓▓▓
█   ███████    ███████   ███████      ███    ██   █   █   ████████     ███
███████████████████████████████████████████████████████   ████████████████
""")


with open("config.json") as jsonfile:
    config = json.load(jsonfile)
    mahcookie = config["Auth"]["cookie"] #done
    webhook = config["Auth"]["webhook"] #done 
    woah = config["Auth"]["cookie"] #done

    DealPercent = config["BuySettings"]["buyPercent"] #done
    maxprice = config["BuySettings"]["maxprice"] #done
    buyWhenUnder = config["BuySettings"]["buyWhenUnder"] #done
    autoRelist = config["BuySettings"]["autoRelist"] #done


    printChecks = config["Settings"]["printChecks"] # done
    printRatelimits = config["Settings"]["printRatelimits"] #done
    useProxys = config["Settings"]["proxys"] #done
    waitOnCheck = config["Settings"]["waitOnCheck"] #done
    waitOnRatelimit = config["Settings"]["waitOnRatelimit"] #done
    mainThreads = config["Settings"]["threads"] # done

    upc = config["CookieSettings"]["userPassCookie"] #done
    c = config["CookieSettings"]["cookie"] #done

DealPercent = DealPercent - 1
DealPercent = abs(DealPercent)
if useProxys == True:
    with open('proxys.txt', 'r') as f:
        proxys = [line.strip() for line in f]
        random.shuffle(proxys)

if upc == True:
    with open("cookies.txt") as f:
        cookies = ["".join(cookie.split(":")[2:]) for cookie in f.read().splitlines()]
        random.shuffle(cookies)
if c == True:
    with open('cookies.txt', 'r') as f:
        cookies = [line.strip() for line in f]
        random.shuffle(cookies)
pcu = woah
def sendSnipe(itemID, price, value, timeTaken, sniped):
    title = "Succesfully Sniped"
    color = 5078467
    text = "FroSnipe Out Sniped Others Again"
    if sniped == False:
        title = "Succesfully missed"
        color = 14177041
        text = "FroSnipe Got OutSniped By Others Again"
    catgif = "https://media.tenor.com/Upo6bEwW940AAAAM/rave-cat.gif"
    profit = value *0.7 - price
    json = {"embeds": [{"color": color,"fields": [
        {"name": title,"value": f"{itemID}"},
        {"name": "Snipe Cost","value": f"{price}"},
        {"name": "Item Value","value": f"{value}"},
        {"name": "Estimated Profit","value": f"{int(profit)}"},
        {"name": "Time Taken","value": f"{timeTaken}"}
    ],"author": {"name": "FrowSnipe"},"footer": {"text": text,"icon_url": catgif}}]}
    requests.post(webhook, json=json)

def genBuySession():
    s = requests.session()
    s.cookies[".ROBLOSECURITY"] = mahcookie
    s.headers['X-CSRF-TOKEN'] = s.post("https://auth.roblox.com/v2/login").headers['X-CSRF-TOKEN']
    if s.get("https://users.roblox.com/v1/users/authenticated").status_code != 200:
        print(Fore.RED+"your main cookie is invalid")
    return s
def genSession():
    s = requests.session()
    randomCookie = random.choice(cookies)
    s.cookies[".ROBLOSECURITY"] = randomCookie
    s.headers['X-CSRF-TOKEN'] = s.post("https://auth.roblox.com/v2/login").headers['X-CSRF-TOKEN']
    if s.get("https://users.roblox.com/v1/users/authenticated").status_code != 200:
        print(Fore.YELLOW+"some of your cookie list is invalid. Removing This Cookie For Your List.")
        cookies.remove(randomCookie)
        print(Fore.GREEN+f"[!] Current Cookie {len(cookies)}")
    return s

shawty = pcu
itemsToTrack = []
with open("values.json") as jsonfile:
    itemValues = json.load(jsonfile)

for item in itemValues:
    itemsToTrack.append(int(item))

itemsToSnipe = [[]]
x = 0
listToAdd = 0
for item in itemsToTrack:
    x += 1
    if x == 120:
        itemsToSnipe.append([])
        x = 0
        listToAdd += 1
    itemsToSnipe[listToAdd].append(item)
print(Fore.CYAN+"-- All issues comments concerns please make a ticket or dm (@674014243267411998) --")
print(Fore.CYAN+f"-- geting ready to track {len(itemsToTrack)} items --")
damn_danual = shawty
threadCount = 0
threadNumber = 0
totalChecks = 0
def main(i):
    global threadCount
    def sniper(i):
        global threadNumber
        global totalChecks
        global threadCount
        time.sleep(random.randint(1,1000)/100)
        try:
            sniperList = itemsToSnipe[threadNumber]
        except:
            threadNumber = 0
        threadthread = threadNumber
        threadNumber+=1
        threadCount+=1
        thisThreadCount = threadCount
        payload = {"items":[]}
        try:
            for item in sniperList:
                payload["items"].append({"id":item,"itemType":"Asset"})
        except:
            threadNumber = 0
            sniperList = itemsToSnipe[threadNumber]
            for item in sniperList:
                payload["items"].append({"id":item,"itemType":"Asset"})
        s = genSession()
        rC = genBuySession()
        newrC = 0
        news = 0
        while True:
            try:
                with open("values.json") as jsonfile:
                    itemValues = json.load(jsonfile)
                if newrC == 15:
                    rC = genBuySession()
                    newrC = 0
                newrC+=1
                if news == 3:
                    s = genSession()
                    news = 0
                news+=1
                time.sleep(waitOnCheck)
                time1 = time.time()
                if useProxys == True:
                    getItemDetails = s.post("https://catalog.roblox.com/v1/catalog/items/details", json=payload, timeout=1.5, proxies={"https": random.choice(proxys)})
                else:
                    getItemDetails = s.post("https://catalog.roblox.com/v1/catalog/items/details", json=payload, timeout=1.5)
                if getItemDetails.status_code == 200:
                    getItemDetails = getItemDetails.json()
                else:
                    if printRatelimits == True:
                        print(Fore.RED+f"[!] Got Somthing Other Then The Right Thing. Status Code: {getItemDetails}")
                        print(Fore.YELLOW+getItemDetails.json())
                    time.sleep(waitOnRatelimit)
                getItemDetails = getItemDetails["data"]
                for selling in getItemDetails:
                    price = selling["lowestPrice"]
                    productId = selling["productId"]
                    itemID = selling["id"]
                    itemIDString = str(itemID)
                    itemValue = itemValues[itemIDString]["value"]
                    if price == None:
                        price == 999999999999999999999
                    if itemValue == None:
                        itemValue = 0
                    if price <= buyWhenUnder or itemValue * DealPercent > price and maxprice >= price:
                        checkDetails = s.get(f"https://economy.roblox.com/v1/assets/{itemID}/resellers?cursor=&limit=10").json()["data"][0]
                        uaid = checkDetails["userAssetId"]
                        userID = checkDetails["seller"]["id"]
                        Buypayload = {"expectedCurrency": 1, "expectedPrice": price, "expectedSellerId": userID, "userAssetId": uaid}
                        buy = rC.post(f"https://economy.roblox.com/v1/purchases/products/{productId}?1",json=Buypayload)
                        print(Fore.GREEN+"[!] attempting to buy item")
                        time2 = time.time()
                        timeTaken = time2-time1
                        if buy.status_code == 200:
                            if buy.json()["purchased"] == True:
                                sendSnipe(itemID, price, itemValue, timeTaken, True)
                                if autoRelist == True:
                                    payload = {"price":itemValue}
                                    rC.patch(f"https://economy.roblox.com/v1/assets/{itemID}/resellable-copies/{uaid}",json=payload)
                            else:
                                sendSnipe(itemID, price, itemValue, timeTaken, False)
                        else:
                            sendSnipe(itemID, price, itemValue, timeTaken, False)
                        print(buy.json())
                    totalChecks+=1
                if printChecks == True:
                    print(Fore.LIGHTCYAN_EX+f"[-] Just checked {len(getItemDetails)} itemIDs with a total of {totalChecks} items checked [-] ",Fore.BLUE+f"( Thread {thisThreadCount} )" )
            except:
                if printRatelimits == True:
                    print(Fore.RED+"[!] The reqeust failed")

    threads = len(itemsToSnipe)
    pool = ThreadPool(threads)
    tokens = pool.map(sniper, list(range(threads)))

print(Fore.CYAN+f"-- Starting {len(itemsToSnipe)*mainThreads} threads --")
forRealThreads = damn_danual
threads = mainThreads
pool = ThreadPool(threads)
tokens = pool.map(main, list(range(threads)))
