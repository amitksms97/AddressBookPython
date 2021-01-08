class Person:

    def __init__(self, first_name, second_name, email_address, city, state, zip_code, phone):
        self.first_name = first_name
        self.second_name = second_name
        self.email_address = email_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

    def first_name(self):
        return self.first_name

    def second_name(self):
        return self.second_name

    def email_address(self):
        return self.email_address

    def state(self):
        return self.state

    def zip(self):
        return self.zip_code

    def phone(self):
        return self.phone


print("Welcome to Address Book Program")
