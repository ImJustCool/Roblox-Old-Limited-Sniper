import requests, json, random, time


with open("config.json") as jsonfile:
    config = json.load(jsonfile)
    key = config["Auth"]["key"]
    mahcookie = config["Auth"]["cookie"]

    maxRapRaise = config["Settings"]["maxRapRaise"]
    maxRapRaise = maxRapRaise - 1
    maxRapRaise = abs(maxRapRaise)
    itemsToTrack = config["BuySettings"]["itemsToBuy"]
    upc = config["CookieSettings"]["userPassCookie"]
    c = config["CookieSettings"]["cookie"]

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

def genSession():
    s = requests.session()
    s.cookies[".ROBLOSECURITY"] = random.choice(cookies)
    s.headers['X-CSRF-TOKEN'] = s.post("https://auth.roblox.com/v2/login").headers['X-CSRF-TOKEN']
    return s
while True:
    with open("values.json", "r") as infile:
        oldValues = json.load(infile)
    ItemFinishedValues = []
    for itemID in itemsToTrack:
        try:
            itemValues = []
            s = genSession()
            getResellData = s.get(f"https://economy.roblox.com/v1/assets/{itemID}/resale-data")
            getResellers = s.get(f"https://economy.roblox.com/v1/assets/{itemID}/resellers?cursor=&limit=100") 
            valueItem = False
            projected = False
            if getResellData.status_code == 200 and getResellers.status_code == 200:
                itemRap = getResellData.json()["recentAveragePrice"]
                itemValues.append(itemRap)
                last15 = []
                last16to30 = []
                x = 1
                for dataPoint in getResellData.json()["priceDataPoints"]:
                    point = dataPoint["value"]
                    if x <= 15:
                        last15.append(point)
                    if x <= 30 and x >= 16:
                        last16to30.append(point)
                    if x == 31:
                        break
                    x+=1
                avg15 = sum(last15)/len(last15)
                avg30 = sum(last16to30)/len(last16to30)
                if avg15 * 1.35 < avg30 or avg30 * 1.35 < avg15:
                    projected = True
                totalSales = 0
                for dataPoint in getResellData.json()["volumeDataPoints"]:
                    point = dataPoint["value"]
                    totalSales+=point
                if totalSales == 120:
                    valueItem == True
                if projected == True:
                    itemValues.append(min([avg15, avg30]))
                bestPrice = getResellers.json()["data"][0]["price"]
                itemValues.append(bestPrice)
                if valueItem == False:
                    itemValues.append(min(itemValues) * 0.8)
                try:
                    oldValue = oldValues[str(itemID)]["value"]
                except:
                    print("[!] New item detected. ignoring maxRapRaise")
                    oldValue = itemRap
                itemValue = min(itemValues)
                itemValue = int(itemValue)
                if itemValue * maxRapRaise <= oldValue:
                    productID = 0
                    with open("productIDs.json") as jsonfile:
                        api = json.load(jsonfile)
                        productID = api[str(itemID)]["productId"]
                    if productID == 0:
                        print(f"[!] Unable to save new items {itemID}. Please update productIDs.json to use new items")
                    else:
                        print(f"[-] Giving {itemID} a value of {itemValue}")
                        itemValue = {"itemID": itemID, "itemValue": itemValue, "productID": productID}
                        ItemFinishedValues.append(itemValue)      
                else:
                    print(f"[!] This item is defo projected {itemID}. Keeping old value")
            else:
                print(f"Unable to value item {itemID}", getResellData.status_code, getResellers.status_code)
        except:
            print(f"[!] unable to value {itemID} due to lack of data")
        time.sleep(1)
    with open("values.json", "r") as infile:
        SavedValues = json.load(infile)

    for item in ItemFinishedValues:
        itemID = item['itemID']
        productID = item['productID']
        itemValue = item['itemValue']
        
        if str(itemID) not in SavedValues:
            SavedValues[itemID] = {
                'id': itemID,
                'value': None,
                'productId': productID
            }
        
        elif SavedValues[str(itemID)]['productId'] == productID:
            SavedValues[str(itemID)]['value'] = itemValue

        transformed_data_list = list(SavedValues.values())

    with open('values.json', 'w') as outfile:
        json.dump(SavedValues, outfile)
    print("[!] Finished Batch Of Values. Starting next batch!")

    with open("values.json", "r") as infile:
        SavedValues = json.load(infile)

    for item in ItemFinishedValues:
        itemID = item['itemID']
        productID = item['productID']
        itemValue = item['itemValue']
        
        if str(itemID) not in SavedValues:
            SavedValues[itemID] = {
                'id': itemID,
                'value': None,
                'productId': productID
            }
        
        elif SavedValues[str(itemID)]['productId'] == productID:
            SavedValues[str(itemID)]['value'] = itemValue

        transformed_data_list = list(SavedValues.values())

    with open('values.json', 'w') as outfile:
        json.dump(SavedValues, outfile)
