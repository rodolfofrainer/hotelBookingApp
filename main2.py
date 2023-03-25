import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv('hotels.csv', dtype={'id': str})


class Hotel:
    watermark = 'The Real Estate Company'

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        """Book a hotel by changing availability from 'yes' to 'no'"""
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Checks if hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False

    # class method
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # Magic method(overriding python's function)
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for you reservation!
        Here is your booking data:
        Name = {self.the_customer_name}
        Hotel name = {self.hotel.name}
        """
        return content

    # class property
    @property
    def the_customer_name(self):
        name = self.customer_name.strip().title()
        return name

    # class static method
    @staticmethod
    def convert(amount):
        return amount*1.2


class DigitalTicket(Ticket):
    def generate(self):
        return 'Hello, this is your digital ticket'

    def download(self):
        pass
