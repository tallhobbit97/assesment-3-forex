import requests

def check_currency(curr):
    """Checks to make sure the user has input a valid currency code."""
    file = open('currencies.txt', 'r')
    for line in file:
        line = line[0:3:]
        if line == curr:
            return True
    file.close()
    return False

def make_exchange(curr_1, curr_2, amt):
    """Makes a request from the exchangerate API to actually make the currency exchange."""
    url = f'https://api.exchangerate.host/convert?from={curr_1}&to={curr_2}&amount={amt}'
    response = requests.get(url)
    data = response.json()
    new_amt = data['result']
    return str(round(float(new_amt), 2))