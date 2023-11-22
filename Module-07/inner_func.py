# function is a first class object
# decorator : ak ta funtion er moddy parameter hiseby onno ak ta function ky o pataty pari
def double_decker():
    print("Starting the double decker")

    def inner_func():
        print("inside the inner")

    return inner_func


# # print(double_decker())
# print(
#     double_decker()()
# )  # ak ta function er bitor theky onno ak ta function k return kora


def do_something(work):
    print("work started")
    # print(work)
    work()  # fucntion ta ky patalam
    print("work ended")


# do_something(2)
# do_something("Now i am busy")


def coding():
    print("coding in python")


# do_something(coding)


def sleeping():
    print("sleeping and dreaming")


do_something(sleeping)
