def call():
    print("Calling someone")
    return "call done"


class Phone:
    price = 14000
    color = "blue"
    brand = "Redmi"
    features = ["camera", "speaker", "hamer"]

    def call(self):  # kono parameter na thakly o self dithy hoby
        print("Calling One Person")

    def send_sms(
        self, phone, sms
    ):  # method add korar somoi extra ak ta self parameter dithy hoby
        text = f"Sending sms to : {phone} and message : {sms}"
        return text


my_phone = Phone()
# print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(4145, "Good Morning")
print(result)
