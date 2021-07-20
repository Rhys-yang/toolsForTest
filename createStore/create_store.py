import requests

host = "http://member-api.1000.com.pw.ck"
    
def createStoreRequest(mobilePhone,realName,storeName,number,phoneCode,ruleId,cookies):
    createStoreUrl = host + "/crm/supervision/store/add"
    
    headers = { "Connection": "keep-alive",
                "reqId": "347a3fe0-e865-11eb-a193-c7fc6c95bbb2", 
                "Accept": "application/json",
                "Platform-No": "", 
                "Platform": "pc", 
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
                "systemId": "0031",
                "Content-Type": "application/json", 
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Cookie":cookies
            }
    bodyJson = {
                "msgCode": phoneCode,
                "bindMobilePhone": mobilePhone,
                "realName": realName + str(number) + "号",
                "ruleId": ruleId,
                "companyName": storeName + str(number) + "号",
                "o2oShopType":"direct",
                "jobType":"1",
                "province":"江苏省",
                "city":"南京市",
                "area":"秦淮区",
                "street":"朝天宫街道",
                "addressDetail":"汉中门广场",
                "longitude":118.767398,
                "latitude":32.041662
            }
    response = requests.post(url=createStoreUrl,headers=headers,json=bodyJson).json()
    return response