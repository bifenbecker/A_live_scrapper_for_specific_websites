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
        json.dump(data, write_file)




def SellMyMobile_Price_Json():
    url = {
        'IPhone11':'https://www.sellmymobile.com/phones/apple/iphone-11-64gb/',
        'Iphone11pro':'https://www.sellmymobile.com/phones/apple/iphone-11-pro-256gb/',
        'Iphone11proMax':'https://www.sellmymobile.com/phones/apple/iphone-11-pro-max-64gb/',
        'Iphone12':'https://www.sellmymobile.com/phones/apple/iphone-12-64gb/',
        'Iphone12mini:':'https://www.sellmymobile.com/phones/apple/iphone-12-mini-64gb/',
        'Iphone12pro':'https://www.sellmymobile.com/phones/apple/iphone-12-pro-128gb/',
        'Iphone12proMax':'https://www.sellmymobile.com/phones/apple/iphone-12-pro-max-128gb/',

    }
    try:
        data = {}
        for key in url:
            capacities = returnGb(url[key])
            condition = {'good': {}}
            data_capacity = {}
            for capacity in capacities:
                currentUrl = url[key].replace(re.search(r"\d+gb", url[key]).group(), capacity)
                price = getPrice(currentUrl)
                data_capacity[capacity] = price
            condition['good'] = data_capacity
            data[key] = condition

        with open("SellMyMobile.json", "w") as file:
            json.dump(data, file)
    except:
        raise ExceptionBreak("Error in SellMyMobile")





def returnGb(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r,'html.parser')
    return [n.text.replace('\n','').lower() for n in soup.find_all('li',class_ = 'device-to-results__variant')]

def getPrice(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    return float(soup.find('span', class_='device-results-table__deal-price').text[1:])

