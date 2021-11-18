"""This Program displays a bar chart of number of matches played
 in each year in IPL.
"""
import os
import csv
from matplotlib import pyplot as plt

def get_no_of_matches_played_by_year(file_path):
    """It creates and returns a dictionary that maps year to no.of matches
    played in that year in IPL.
    """
    no_of_matches_played_by_year = {}
    seasons = set()
    with open(file_path,"r",encoding="utf8") as file_object:
        matches_reader = csv.DictReader(file_object)
        for current_match_info in matches_reader:
            season = current_match_info['season']
            seasons.add(season)
            count = no_of_matches_played_by_year.get(season,0) + 1
            no_of_matches_played_by_year[season] = count
    return no_of_matches_played_by_year,seasons

def prepare_data_to_plot(no_of_matches_played_by_year,seasons):
    """It will create x-axis and y-axis values to plot."""
    x_axis_values,y_axis_values = [],[]
    for season in seasons:
        x_axis_values.append(season)
        y_axis_values.append(no_of_matches_played_by_year[season])
    return x_axis_values,y_axis_values

def plot_data(x_axis_values,y_axis_values):
    """It will create and display the bar chart."""
    plt.bar(x_axis_values,y_axis_values)
    plt.title("Number of matches played each Year in IPL")
    plt.xlabel("Year")
    plt.ylabel("No.of matches played")
    plt.show()

def execute():
    """It will prepare the data to be plotted."""
    file_path = os.getcwd()+"/../Data/mock_matches.csv"
    no_of_matches_played_by_year,seasons = get_no_of_matches_played_by_year(file_path)
    seasons = sorted(list(seasons))
    return prepare_data_to_plot(no_of_matches_played_by_year,seasons)

if __name__=="__main__":
    x_axis_values_,y_axis_values_ = execute()
    plot_data(x_axis_values_,y_axis_values_)
