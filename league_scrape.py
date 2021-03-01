#!/bin/python
import os
import sys
import requests

from bs4 import BeautifulSoup


"""
Covid 19 - California Web Data Scraper
Author: Rickyg3

source: https://covid19.ca.gov/state-dashboard/
"""


def clear_screen():
    os.system("clear")


class Ability():
    """ Storage Class for Champion abilities """
    def __init__(self, ability_name, ability_key, ability_description):
        self.name = ability_name
        self.symbol = ability_key
        self.description = ability_description

    def __str__(self):
        txt = '\n'
        txt += f"{self.name} [{self.symbol}]:\n {self.description}\n"
        return txt


class League:
    def __init__(self, champion_name):
        self.url = f"https://na.leagueoflegends.com/en-us/champions/{champion_name}/"

        self.champion_name = champion_name
        self.abilities = []

        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def __str__(self):
        temp_str = ""
        title = "League Champion Information Finder"

        temp_str += f".-{len(self.champion_name) * '-'}-."
        temp_str += f"\n| {self.champion_name.upper()} |"
        temp_str += f"\n'-{len(self.champion_name) * '-'}-'"
        temp_str += f"\n"

        for ability in self.abilities:
            temp_str += ability.__str__()

        temp_str += f"\n"

        return temp_str

    def update_data(self):
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

        # Haven't tried it don't really need it though
        # ''' Champ name  '''
        # champ = self.soup.find('strong', class_='style__Title-sc-14gxj1e-3 iLTyui')
        # self.champion_name = champ.get_text().strip()

        ''' Abilities '''
        ability_list = self.soup.find('ol', class_='style__AbilityInfoList-ulelzu-7 kAlIxD')
        raw_abilities = ability_list.find_all('li', class_='style__AbilityInfoItem-ulelzu-8 ldXivP false')

        # Passive
        raw_passive = ability_list.find('li', class_='style__AbilityInfoItem-ulelzu-8 ldXivP is-active')
        passive_ability = raw_passive.find('h6').get_text()
        passive_symbol = raw_passive.find('h5').get_text()
        passive_desc = raw_passive.find('p').get_text()

        self.abilities.append(Ability(passive_ability, passive_symbol, passive_desc))

        for raw_ability in raw_abilities:
            ability = raw_ability.find('h6').get_text()
            symbol = raw_ability.find('h5').get_text()
            desc = raw_ability.find('p').get_text()

            self.abilities.append(Ability(ability, symbol, desc))


if __name__ == '__main__':
    # Make into CLI
    if len(sys.argv) >= 2:
        champion = sys.argv[1]
    else:
        champion = input("Champion to search: ")

    # champion = input("Champion to search: ")

    current = League(champion)
    current.update_data()
    clear_screen()

    print(current)
