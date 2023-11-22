class Phone:
    manufactures = "China"

    def __init__(self, owner, brand, price):  # init as same as constructor
        # pass  # khali bujai
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f"Sending to : {phone} message to : {sms}"
        print(text)


myPhone = Phone("Sharmin", "Redmi", 14000)
print(myPhone.owner, myPhone.brand, myPhone.price)

hisPhone = Phone("Rahaman", "Samsung", 15000)
print(hisPhone.owner, hisPhone.brand, hisPhone.price)

myPhone.send_sms(2242, "HII")
hisPhone.send_sms(4232, "hlw")
