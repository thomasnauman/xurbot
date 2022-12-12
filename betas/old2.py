import requests
from bs4 import BeautifulSoup

# Use requests library to get the HTML from the website
response = requests.get("https://whereisxur.com/")

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Use BeautifulSoup to find the relevant information on the page
planet = soup.find(id="planet").text.strip()
planet_location = soup.find(id="planet-location").text.strip()
weapon = soup.find(id="weapon").text.strip()
weapon_type_and_slot = soup.find(id="weapon-type-and-slot").text.strip()
hunter_armor = soup.find(id="hunter-armor").text.strip()
hunter_armor_slot = soup.find(id="hunter-armor-slot").text.strip()
warlock_armor = soup.find(id="warlock-armor").text.strip()
warlock_armor_slot = soup.find(id="warlock-armor-slot").text.strip()
titan_armor = soup.find(id="titan-armor").text.strip()
titan_armor_slot = soup.find(id="titan-armor-slot").text.strip()

# Print the results to the console
print(f"Planet: {planet}")
print(f"Planet location: {planet_location}")
print(f"Weapon: {weapon}")
print(f"Weapon type and slot: {weapon_type_and_slot}")
print(f"Hunter armor: {hunter_armor}")
print(f"Hunter armor slot: {hunter_armor_slot}")
print(f"Warlock armor: {warlock_armor}")
print(f"Warlock armor slot: {warlock_armor_slot}")
print(f"Titan armor: {titan_armor}")
print(f"Titan armor slot: {titan_armor_slot}")
