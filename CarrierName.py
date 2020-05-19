import phonenumbers
from phonenumbers import carrier

N = input("Enter The phone number : ")
Service = phonenumbers.parse(N)
print(carrier.name_for_number(Service, 'en'))
