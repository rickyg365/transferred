import os
import sys
import requests

from bs4 import BeautifulSoup

"""
Metrolink Train Schedule Web Data Scraper
Author: Rickyg3

source: https://covid19.ca.gov/state-dashboard/
"""


class Metrolink():
    def __init__(self, origin, destination, weekend=0):
        self.station_map = {'Upland': '125', 'Montclair': '118', 'L.A. Union Station': '107'}
        self.weekend = weekend

        self.origin = self.get_id(origin)
        self.destination = self.get_id(destination)

        self.schedule = []

        self.url = f"https://metrolinktrains.com/schedules/?type=station&originId={self.origin}&destinationId={self.destination}&weekend={self.weekend}"

        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def __str__(self):
        temp_str = ""
        title = "Metrolink Schedule Finder: Upland -> LA"

        temp_str += f".-{len(title) * '-'}-."
        temp_str += f"\n| {title} |"
        temp_str += f"\n'-{len(title) * '-'}-'"
        temp_str += f"\n \n"
        temp_str += f"\nTrips:"
        temp_str += f"\n{65 * '-'}"

        count = 1
        for trip in self.schedule:
            temp_str += f"\n|  #{count}:\t Departure(Upland): {trip[0]}\tArrival(LA): {trip[1]}\t|"
            temp_str += f"\n{65*'-'}"
            count += 1

        temp_str += f"\n"

        return temp_str

    def get_id(self, station_name):
        if station_name in self.station_map.keys():
            return self.station_map[station_name]
        else:
            print(f"Error, {station_name.title()} not Found!")

    def get_schedule(self):
        schedule = self.soup.find_all('tr', class_='stationToStation__trip scheduleTrip')

        for item in schedule:
            trip = []
            raw_departure = item.find('td', class_='scheduleTrip__item scheduleTrip__item--depart scheduleTrip__item--SB')
            raw_arrival = item.find('td', class_='scheduleTrip__item scheduleTrip__item--arrive scheduleTrip__item--SB')

            departure = raw_departure.find('span', class_='scheduleTrip__time').get_text()
            arrival = raw_arrival.find('span', class_='scheduleTrip__time').get_text()

            trip.append(departure)
            trip.append(arrival)

            # print(departure)
            # print(arrival)

            self.schedule.append(trip)


m = Metrolink("Upland", 'L.A. Union Station')
m.get_schedule()
print(m)

