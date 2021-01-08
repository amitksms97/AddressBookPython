class Person:

    def __init__(self, first_name, second_name, email_address, city, state, zip_code, phone):
        self.first_name = first_name
        self.second_name = second_name
        self.email_address = email_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone

    def get_first_name(self):
        return self.first_name

    def get_second_name(self):
        return self.second_name

    def get_email_address(self):
        return self.email_address

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip_code

    def get_phone(self):
        return self.phone

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_second_name(self, second_name):
        self.second_name = second_name

    def set_email_address(self, email_address):
        self.email_address = email_address

    def set_state(self, state):
        self.state = state

    def set_zip(self, zip_code):
        self.zip_code = zip

    def set_phone(self, phone):
        self.phone = phone


print("Welcome to Address Book Program")
