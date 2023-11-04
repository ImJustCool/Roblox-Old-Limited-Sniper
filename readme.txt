Config -
    This will be used for editing settings on how the bot runs and peforms.
    The bot genrates threads for each item list. If you want to check the same items faster just open the bot again. (If you are checking for a freind everything they get is somthing you could of gotten insted)
    key: put your key there
    webhook: put your webhook there
    cookie: put your roblox cookie WITH robux there
    printChecks: wether or not you want the bot to print every time it scrapes the catalog
    printRatelimits: Wether or not you want the bot to print ratelimits AND errors
    proxys: using proxys is completly up to you but im paying $20 a month for 10 RESEDENTIAL proxys. I am using proxys from https://proxysocks5.com/ .
    waitOnCheck: how long you want the bot on each check. (If you have enough proxys you dont need to use this)
    waitOnRateLimit: how long you want the bot to wait when it gets ratelimited 
    buyPercent: the deals you are trying to snipe. 0.1 = 10% deals 0.3 = 30% deals. Setting 0.3 and bellow will result in losses. The max deal percent (and still be able to snipe) is 0.99 the min is 0.01
    maxprice: max amount of robux you are willing to spend on one snipe
    itemsToBuy: keep it in increments of 120 since thats the max items i can get in one request. Just the items the bot will be tracking (itemIDS)
    userPassCookie: user:pass:cookie next line 
    cookie: cookie next line
    --new features
    maxRapRaise: This is a feature in the value algorythm witch is the max amount of rap a item can raise untill its marked as projected by it, be defualt its set to 0.07 (7%)
    buyWhenUnder: This will buy anything under that threshold, by defualt the bot will buy anything under 44 robux
    autoRelist: This will automaticly relist your items for there set Value by the bot witch will allow the bot to run fully automaticly     
Cookies -
    paste your cookies in here. the bot only accepts cookie next line and user:pass:cookie next line
main/FroSnipe -
    run this file only when you have the cookie file filled out. the config filled out. and value.json finished
ProductIDs -
    this is just a file to get the productIDs of each item. 
Proxys -
    proxy next line. The only accepted proxy format is ip auth
ValueAlgo - 
    you MUST run this 24/7. This is the only reason you can sefley snipe 35% deals without the values going wack. You must run it before your first time running FrowSnipe.py
    you will know when its first time is not when values is filled out
    if it crashes set your value file to {}
Values -
    where the custom values are stored
KeyAuth-
    ignoor