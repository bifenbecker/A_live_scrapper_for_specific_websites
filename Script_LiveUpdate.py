import json, requests, re, time
from bs4 import BeautifulSoup
from ExceptionBreak import ExceptionBreak
from IPhone11 import IPhone11
from IPhone12pro import IPhone12pro
from IPhone12mini import IPhone12mini
from IPhone11proMax import IPhone11proMax
from IPhone12 import IPhone12
from IPhone12proMax import IPhone12proMax
from IPhone11pro import IPhone11pro
from fake_useragent import UserAgent

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'upgrade-insecure-requests': '1',
'cookie': 'mos_id=CllGxlx+PS20pAxcIuDnAgA=; session-cookie=158b36ec3ea4f5484054ad1fd21407333c874ef0fa4f0c8e34387efd5464a1e9500e2277b0367d71a273e5b46fa0869a; NSC_WBS-QUBG-jo-nptsv-WT-443=ffffffff0951e23245525d5f4f58455e445a4a423660; rheftjdd=rheftjddVal; _ym_uid=1552395093355938562; _ym_d=1552395093; _ym_isad=2'
}

def Update():
    iphone11 = IPhone11()
    iphone12pro = IPhone12pro()
    iphone12mini = IPhone12mini()
    iphone11proMax = IPhone11proMax()
    iphone12 = IPhone12()
    iphone12proMax = IPhone12proMax()
    iphone11pro = IPhone11pro()

    data1 = iphone11.getData_BrandNew() + iphone11.getData_Renewed()
    data2 = iphone12pro.getData_BrandNew()
    data3 = iphone12mini.getData_BrandNew()
    data4 = iphone11proMax.getData_BrandNew() + iphone11proMax.getData_Renewed()
    data5 = iphone12.getData_BrandNew()
    data6 = iphone12proMax.getData_BrandNew()
    data7 = iphone11pro.getData_BrandNew() + iphone11pro.getData_Renewed()

    data = data1 + data2 + data3 + data4 + data5 + data6 + data7
    with open("config.txt") as file:
        path = file.readlines()[0]
    with open(path, "w") as write_file:
        json.dump(data, write_file,indent=1)

def GenDict(*args):
    res = {}
    for dict in args:
        for key in dict:
            res[key] = dict[key]
    return res

def GetDictPhone(phones,url,flak):
    domen = 'https://www.sellmymobile.com'
    soap = BeautifulSoup(requests.get(url,headers = headers).text, 'html.parser')
    links = soap.find_all('a', class_='cta cta--tertiary')

    res = {}
    for l in links:
        a = l.get('href')
        for i in phones:
            flag = flak + '-' + i
            if flag in a:
                if flak == "ipad-pro":
                    if flag in a and 'data' not in a:
                        r = a.split('/')[3].split('-')[:-1]
                        name = " ".join(r[:3]).title().replace(' ', '') + "-" + "-".join(r[3:])
                        res[name] = domen + a
                else:
                    name = " ".join(a.split('/')[3].split('-')[:-1]).title().replace(' ', '')
                    res[name] = domen + a

    return res

def getDataForSellMyMobile():
    url = {
        'iphone': 'https://www.sellmymobile.com/phones/apple/',
        'galaxy': 'https://www.sellmymobile.com/phones/samsung/',
        'ipad-pro': 'https://www.sellmymobile.com/tablets/apple/',
    }
    phones = [
        ['7', '8', 'x', 'xr', 'xs', '11', 'se-2020', '12'],
        ['s8', 's9', 's10-5g', 's20', 'fold', 'z-fold2'],
        ['12-9-2018', '11-2018'],
    ]
    data = {}
    for i in range(len(url.keys())):
        data_n = GetDictPhone(phones[i], url[list(url.keys())[i]], list(url.keys())[i])
        data = GenDict(data, data_n)
    data["OnePlus8Pro"] = "https://www.sellmymobile.com/phones/oneplus/8-pro-128gb/"
    return data

def SellMyMobile_Price_Json():
    url = getDataForSellMyMobile()
    url["Galaxy Fold"] = url.pop("Galaxy")
    data = {}
    for key in url:
        try:
            capacities = returnGb(url[key])
        except:
            raise ExceptionBreak(f"Error in {key}(SellMyMobile)")
        condition = {'good': {}}
        data_capacity = {}
        if len(capacities) == 0:
            try:
                price = getPrice(url[key])
            except:
                raise ExceptionBreak(f"Error in {key}(SellMyMobile)")
            c = url[key].split("-")[-1][:-1]
            if c == "fold":
                c = "512gb"
            data_capacity[c] = price
        for capacity in capacities:
            currentUrl = url[key].replace(re.search(r"\d+gb", url[key]).group(), capacity)
            try:
                price = getPrice(currentUrl)
            except:
                raise ExceptionBreak(f"Error in {key}(SellMyMobile)")
            data_capacity[capacity] = price
        condition['good'] = data_capacity
        data[key] = condition
    with open("SellMyMobile.json", "w") as file:
        json.dump(data, file, indent=2)

def returnGb(url):
    r = requests.get(url,headers = headers).text
    soup = BeautifulSoup(r,'html.parser')
    return [n.text.replace('\n','').lower() for n in soup.find_all('li',class_ = 'device-to-results__variant')]

def getPrice(url):
    r = requests.get(url,headers = headers).text
    soup = BeautifulSoup(r, 'html.parser')
    return float(soup.find('span', class_='device-results-table__deal-price').text[1:])

