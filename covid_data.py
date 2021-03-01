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

# Make into CLI
# if len(sys.argv) >= 2:
#     word = sys.argv[1]
# else:
#     word = 'brand'
#


def clear_screen():
    os.system("clear")


class Covid:
    def __init__(self):
        self.url = 'https://covid19.ca.gov/state-dashboard/'

        self.total_cases = 0
        self.daily_cases = 0
        self.delta = 0

        self.total_deaths = 0
        self.daily_deaths = 0
        self.delta_d = 0

        self.vaccine_given = 0

        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def __str__(self):
        temp_str = ""
        title = "California Covid Information"

        temp_str += f".-{len(title) * '-'}-."
        temp_str += f"\n| {title} |"
        temp_str += f"\n'-{len(title) * '-'}-'"

        temp_str += f"\n"
        temp_str += f"\n Total Cases: {self.total_cases}"
        temp_str += f"\n Daily Cases: {self.daily_cases}"
        temp_str += f"\n [Delta Cases]: {self.delta}"

        temp_str += f"\n"
        temp_str += f"\n Total Deaths: {self.total_deaths}"
        temp_str += f"\n Daily Deaths: {self.daily_deaths}"
        temp_str += f"\n [Delta Deaths]: {self.delta_d}"

        temp_str += f"\n"
        temp_str += f"\n Vaccines Administered: {self.vaccine_given}"
        temp_str += f"\n"

        return temp_str

    def update_data(self):
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

        ''' Change '''
        # Cases Delta
        change_cases = self.soup.find('div', id='total-cases-increase')
        self.delta = change_cases.get_text().strip()

        # Deaths Delta
        change_deaths = self.soup.find('div', id='total-deaths-increase')
        self.delta_d = change_deaths.get_text().strip()

        ''' Total Cases '''
        # Find div containing total cases
        raw_total = self.soup.find('div', id='total-cases-number')
        self.total_cases = raw_total.get_text()

        ''' Daily Cases '''
        # Find div containing total cases
        raw_daily = self.soup.find('div', id='total-cases-today')
        self.daily_cases = raw_daily.get_text()

        ''' Total Deaths '''
        # Find div containing total cases
        raw_deaths = self.soup.find('div', id='total-deaths-number')
        self.total_deaths = raw_deaths.get_text()

        ''' Daily Deaths '''
        # Find div containing total cases
        raw_daily_deaths = self.soup.find('div', id='total-deaths-today')
        self.daily_deaths = raw_daily_deaths.get_text()

        ''' Vaccines '''
        raw_vaccine = self.soup.find('div', class_='text-white font-size-1-2em my-4')
        self.vaccine_given = raw_vaccine.get_text()


if __name__ == '__main__':
    current = Covid()
    current.update_data()
    clear_screen()

    print(current)


''' First Attempt '''
# URL = 'https://covid19.ca.gov/state-dashboard/'
#
# page = requests.get(URL)
#
# soup = BeautifulSoup(page.content, 'html.parser')
#
#
# '''
# Change
# '''
# # Find div containing total cases
# change_cases = soup.find('div', id='total-cases-increase')
#
# # # Best Item
# delta = change_cases.get_text().strip()
#
#
# # Find div containing total cases
# change_deaths = soup.find('div', id='total-deaths-increase')
#
# # # Best Item
# delta_d = change_deaths.get_text().strip()
#
#
# '''
# Total Cases
# '''
# # Find div containing total cases
# raw_total = soup.find('div', id='total-cases-number')
#
# # # Best Item
# total_cases = raw_total.get_text()
#
# print(f"Total Cases: {total_cases}")
#
# '''
# Daily Cases
# '''
# # Find div containing total cases
# raw_daily = soup.find('div', id='total-cases-today')
#
# # # Best Item
# daily_cases = raw_daily.get_text()
#
# print(f"Daily Cases: {daily_cases}")
#
# print(f"[Delta Cases]: {delta}")
#
# '''
# Total Deaths
# '''
# # Find div containing total cases
# raw_deaths = soup.find('div', id='total-deaths-number')
#
# # # Best Item
# total_deaths = raw_deaths.get_text()
#
# print(f"\nTotal Deaths: {total_deaths}")
#
# '''
# Daily Deaths
# '''
# # Find div containing total cases
# raw_daily_deaths = soup.find('div', id='total-deaths-today')
#
# # # Best Item
# daily_deaths = raw_daily_deaths.get_text()
#
# print(f"Daily Deaths: {daily_deaths}")
#
# print(f"[Delta Deaths]: {delta_d}")
#
# '''
# Vaccines
# '''
# raw_vaccine = soup.find('div', class_='text-white font-size-1-2em my-4')
#
# vaccine_number = raw_vaccine.get_text()
#
# print(f"\nVaccines Administered: {vaccine_number}")
