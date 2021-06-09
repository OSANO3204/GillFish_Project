import datetime
def ageinyears(name, age):
    year=datetime.datetime.now().year
    remaining = 100-age

    return year + remaining


name=input("Enter your name : ")
age= int(input("Enter your age : "))

print(ageinyears(name,age))


