import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def book(self):
        """
        Book a hotel by changing availability from 'yes' to 'no'
        """
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

    def available(self):
        """Checks if hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for you reservation!
        Here is your booking data:
        Name = {self.customer_name}
        Hotel name = {self.hotel.name}"""
        return content


print(df)
hotel_id = input('Enter the ID of the hotel: ')
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    customer_name = input('Enter your name: ')
    reservation_ticket = ReservationTicket(customer_name, hotel)
    print(reservation_ticket.generate())
else:
    print('Hotel is not available')
