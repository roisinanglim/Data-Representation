import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.myhome.ie/residential/mayo/property-for-sale?page=2"
page = requests.get(url)
print(page.content)
soup = BeautifulSoup(page.content,'html.parser')
home_file = open('week04myhome.csv',mode='w')
home_writer = csv.writer(home_file, delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)

# Find the div where the class is equal to Property card listing
listings = soup.findAll("div", class_="PropertyListingCard" )
print(listings)

# Within the page retrn the price and address for each listing
for listing in listings:
    entrylist = []
    price = listing.find(class_="PropertyListingCard__Price").text
    entrylist.append(price)
    address = listing.find(class_="PropertyListingCard__Address")
    entrylist.append(address)
    home_writer.writerow(entrylist)
print(entrylist)
home_file.close()