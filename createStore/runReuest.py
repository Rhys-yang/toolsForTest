import create_store

class createManyStore():
    phoneNumber = 18009611556
    realName = "橘猫"
    storeName = "共享店铺"
    phoneCode = "3679"
    ruleId = "RULE_A4707107_R2486459"
    cookies = "_ga=GA1.3.1936891217.1626229210; gauserid=qm59433c6o; qmuid=-1710029240; cxuid=1801556; UM_distinctid=17aa918a4b3286-08e91f8dd2e04e-34647600-1fa400-17aa918a4b4ee4; SSOTICKET=; SSOEXPIRES=; SSOTHRESHOLD=; _gid=GA1.3.1375423225.1626660282; a9a68f4fefd3b693f10be4a89799dc48=8fc3f53594934398a0b0cc154b313c2c; sxuid=2139692685; _gat=1"
    
    def lootCreatStore(self):
        number = 9
        for i in range(1,100):
            result = create_store.createStoreRequest(mobilePhone=self.phoneNumber,realName=self.realName,storeName=self.storeName,number=number,phoneCode=self.phoneCode,ruleId=self.ruleId,cookies=self.cookies)
            number+=1
            print(result)

if __name__ == '__main__':
    createManyStore().lootCreatStore()