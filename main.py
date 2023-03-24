import pandas as pd

df = pd.read_csv('hotels.csv', dtype={'id': str})
df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
df_cards_security = pd.read_csv('card_security.csv', dtype=str)


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


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


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


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {'number': self.number,
                     'expiration': expiration, 'holder': holder, 'cvc': cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number']
                                         == self.number, 'password'].squeeze()
        if password == given_password:
            return True
        else:
            return False


class SpaTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for you Spa reservation!
        Here is your Spa booking data:
        Name = {self.customer_name}
        Hotel name = {self.hotel.name}"""
        return content


print(df)
hotel_id = input('Enter the ID of the hotel: ')
hotel = SpaHotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard(number='1234567890123456')
    if credit_card.validate(expiration='12/26', holder='JOHN SMITH', cvc='123'):
        if credit_card.authenticate(given_password='mypass'):
            hotel.book()
            customer_name = input('Enter your name: ')
            reservation_ticket = ReservationTicket(customer_name, hotel)
            print(reservation_ticket.generate())
            spa = input('Would you like to add a Spa package to your order? ')
            if spa == 'yes':
                hotel.book_spa_package()
                spa_package = SpaTicket(
                    customer_name=customer_name, hotel_object=hotel)
                print(spa_package.generate())
        else:
            print('Card authentication failed')
    else:
        print('There was something wrong with the payment')
else:
    print('Hotel is not available')
