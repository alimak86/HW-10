from collections import UserDict

NOT_DEFINED = "not defined"

class AddressBook(UserDict):
    def add_record(self,record): ## adding record type Record into the dictionary
        self.data[record.name.value] = record

    def print(self):
        for name in self.data:
            self.data[name].print()

class Record: ## responsible for the record manipulation
     
    def __init__(self,name,phone = [], email = []):
        self.name = name ## type of Name
        self.phone = phone
        self.email = email

    def add_phone(self,phone):
        self.phone.append(phone)
        return (f"add phone: {phone.value}")
    
    def find_phone(self,phone):
        for ph in self.phone:
            if ph.value == phone:
                return ph
        return Phone()

    def find_email(self,email):
        for ph in self.email:
            if ph.value == email:
                return ph
        return Email()

    def remove_phone(self,strphone):
        try:
            phone = self.find_phone(strphone)
            self.phone.remove(phone)
            return f"{phone.value} removed"
        except ValueError:
            return f"can not remove phone {strphone}: does not exist"
        
    def edit_phone(phone): ## to be defined in next H/W
        pass

    def add_email(self,email):
        self.email.append(email)
        return(f"add email: {email.value}")
    
    def remove_email(self,stremail):
        try:
            email = self.find_email(stremail)
            self.email.remove(email)
            return f"{email.value} removed"
        except ValueError:
            return f"can not remove email {stremail}: does not exist"
        
    def edit_email(email): ## to be defined in next H/W
        pass

    def print_phones(self):
        print("Phones: ")
        for phone in self.phone:
            print(phone.print())

    def print_emails(self):
        print("Emails: ")
        for email in self.email:
            print(email.print())

    def print(self):
        print("Name: " + self.name.print())
        self.print_phones()
        self.print_emails()


class Field: ## defines general fields properties TBD
    def __init__(self,value):
        self.value = value

    def print(self):
        return self.value

class Name(Field): ## mandatory field
    def __init__(self,value):
        self.value = value

class Phone(Field): ## nonmandatory field
    def __init__(self,phone = NOT_DEFINED):
        self.value = phone

class Email(Field): ## nonmandatory field
    def __init__(self,email = NOT_DEFINED):
        self.value = email

def do_something():
    output = """ here we created the following classes:\n 
    - AdressBook \n 
    - Record \n 
    - Field \n 
    - Name \n 
    - Phone \n 
    - Email \n
    and added some functionality which will be developed in the next H/Ws"""
    print(output)

if __name__ =="__main__":
    do_something()


##print("------------------------------")
##name = Name("alisa")
##print(name.print())
##phone = Phone("6478619006")
###print(phone.print())
##email = Email("put_nik4@mail.ru")
###print(email.print())
###print("------------------------------")

###record = Record(name)
##print(record.add_phone(phone))
###print(record.add_phone(Phone("6478617006")))
##print(record.add_email(email))
#print(record.remove_phone(Phone("sdfsdfsdfsfd")))
#print(record.remove_email(Phone("sdfsdfsdfsfd")))
#record.print()

##book = AddressBook()
##book.add_record(record)
##book.print()

###print(record.remove_email("put_nik4kk@mail.ru"))
