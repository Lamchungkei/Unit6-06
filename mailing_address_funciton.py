# Created by: Kay Lin
# Created on: Dec-12th 2017
# Created for: ICS3U
# This program displays mailing address information

from enum import Enum

province_initials_choice = Enum('ON', 'QC', 'AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'PE', 'SK', 'YT')

street_type_choice = Enum('DR', 'ST', 'LANE', 'BLVD', 'RD','AVE','CRT')

class MailAddress():
    def __init__(self, first_name, last_name, house_number, street_name, street_type, city_name, province_initials, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        self.city_name = city_name
        self.province_initials = province_initials
        self.postal_code = postal_code

    def information(self):
        #return your address to 911
        
        self.information_string = "\n" + a_mailing_address.first_name + " " + a_mailing_address.last_name + "\n" + str(a_mailing_address.house_number) + " " + a_mailing_address.street_name + " " + str(a_mailing_address.street_type) + "\n" + a_mailing_address.city_name + ", " + a_mailing_address.province_initials + " " + a_mailing_address.postal_code + "\n"
        
        return self.information_string

province_initials = raw_input('Province: ')
while province_initials not in province_initials_choice:
    province_initials = raw_input('Please input valid province initials: ')
province_initials = province_initials

street_type = raw_input('street type: ')
while street_type not in street_type_choice:
    street_type = raw_input('Please input valid street type: ')
street_type = street_type

house_number = int(input('house number: '))
while house_number < 0:
    house_number = int(input('Please input an actual house number: '))
house_number = house_number

a_mailing_address = MailAddress(raw_input("First Name: "), raw_input("Last Name: "), house_number, raw_input("Street Name: "), street_type, raw_input("City Name: "), province_initials, raw_input("Postal Code: "))

print(a_mailing_address.information())

