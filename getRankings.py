# Louis Romeo
# UFC Analytics
# Date: 11/25/2024
# Purpose: Web Scraping program that fetches updated rankings from ufc.com/rankings
#          using html parsing. Starts with Pound for Pound rankings and contains all
#          women's and men's divisions. Saves to a csv file titled ufc_rankings.csv which
#          contains fields for Division,Rank,Name,Rank Change.
from bs4 import BeautifulSoup
import requests
import csv

# Function to parse a single division's data
def parse_division(div_content):
    division_data = []
    division_name = div_content.find("div", class_="view-grouping-header").get_text(strip=True)
    is_pound_for_pound = "Pound-for-Pound" in division_name

    # Include champion for non-pound-for-pound divisions
    if not is_pound_for_pound:
        champion_div = div_content.find("div", class_="rankings--athlete--champion")
        if champion_div:
            champion_name = champion_div.find("h5").get_text(strip=True)
            division_data.append({"Rank": "Champion", "Name": champion_name, "Rank Change": ""})

    fighters = div_content.select("tbody tr")
    for fighter in fighters:
        rank = fighter.find("td", class_="views-field-weight-class-rank").get_text(strip=True)
        name = fighter.find("a").get_text(strip=True)
        rank_change_td = fighter.find("td", class_="views-field-weight-class-rank-change")
        rank_change = rank_change_td.get_text(strip=True) if rank_change_td else ""
        division_data.append({"Rank": rank, "Name": name, "Rank Change": rank_change})

    return division_name, division_data


# URL for UFC rankings
url = "https://www.ufc.com/rankings"

# Fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Select all divisions
divisions = soup.select(".view-grouping")

# Parse all divisions
all_division_data = {}
for division in divisions:
    division_name, division_data = parse_division(division)
    all_division_data[division_name] = division_data

# Save to a CSV file
with open("ufcrankings.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Division", "Rank", "Name", "Rank Change"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for division_name, fighters in all_division_data.items():
        for fighter in fighters:
            writer.writerow({"Division": division_name, **fighter})

print("UFC rankings saved to 'ufcrankings.csv'.")
