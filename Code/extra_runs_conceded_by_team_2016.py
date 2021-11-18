"""This Program displays a bar chart of Total no.of extra runs
conceded by Each Team in 2016.
"""
import os
import csv
from matplotlib import pyplot as plt

def get_extra_runs_conceded_by_team_2016(file_path):
    """It creates and returns a dictionary that maps team to total
    no.of extra runs conceded in 2016.
    """
    extra_runs_conceded_by_team = {}
    with open(file_path,"r",encoding="utf8") as file_object:
        matches_reader = csv.DictReader(file_object)
        for current_match_info in matches_reader:
            season = current_match_info["season"]
            if season == "2016":
                team1 = current_match_info["team1"]
                team2 = current_match_info["team2"]
                team1_extra_runs = int(current_match_info['extra_conceded_runs_team1'])
                team2_extra_runs = int(current_match_info['extra_conceded_runs_team2'])
                count = extra_runs_conceded_by_team.get(team1,0) + team1_extra_runs
                extra_runs_conceded_by_team[team1] = count
                count = extra_runs_conceded_by_team.get(team2,0) + team2_extra_runs
                extra_runs_conceded_by_team[team2] = count
    return extra_runs_conceded_by_team

def plot_data(extra_runs_conceded_by_team):
    """It will create and display the bar chart."""
    # preparing x-axis and y-axis values to plot.
    x_axis_values,y_axis_values = [],[]
    for team,extra_runs in extra_runs_conceded_by_team.items():
        x_axis_values.append(team)
        y_axis_values.append(extra_runs)
    # creating and displaying bar chart
    figure_width = 15
    figure_height = 10
    plt.figure(figsize=(figure_width,figure_height))
    plt.barh(x_axis_values,y_axis_values)
    plt.title("Total Number of Extra runs conceded by Each Team in 2016")
    plt.ylabel("Team")
    plt.xlabel("Total No.of extra runs conceded")
    plt.show()

def execute():
    """It will prepare the data to be plotted."""
    file_path = os.getcwd()+"/../Data/mock_matches.csv"
    return get_extra_runs_conceded_by_team_2016(file_path)

if __name__=="__main__":
    extra_runs_conceded_by_team_ = execute()
    plot_data(extra_runs_conceded_by_team_)
