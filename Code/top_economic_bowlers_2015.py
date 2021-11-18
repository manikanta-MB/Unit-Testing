"""This Program displays a bar chart of Top Economic Bowlers in 2015."""
import os
import csv
from matplotlib import pyplot as plt

def get_economy_by_player_2015(file_path):
    """It creates and returns a dictionary that maps bowler name to
     economy on each match that bowler plays in 2015.
    """
    economy_by_player = {}
    with open(file_path,"r",encoding="utf8") as file_object:
        bowler_reader = csv.DictReader(file_object)
        for current_bowler_info in bowler_reader:
            season = current_bowler_info['season']
            if season == "2015":
                bowler_name = current_bowler_info["bowler_name"]
                conceded_runs = int(current_bowler_info["conceded_runs"])
                no_of_overs = int(current_bowler_info["no_of_overs"])
                economy = round(conceded_runs / no_of_overs, 2)
                if bowler_name not in economy_by_player:
                    economy_by_player[bowler_name] = []
                economy_by_player[bowler_name].append(economy)
    return economy_by_player
def calculate_average_economy(economy_by_player):
    """It will calculate the average economy for each player and then
    returns a list of bowler names sorted according to their economy rate.
    """
    player_names = list(economy_by_player.keys())
    for player_name,economies in economy_by_player.items():
        economy_by_player[player_name] = round(sum(economies)/len(economies), 2)
    player_names.sort(key = lambda player_name:economy_by_player[player_name])
    return player_names

def prepare_data_to_plot(economy_by_player,player_names):
    """It will create x-axis and y-axis values to plot."""
    x_axis_values,y_axis_values = [],[]
    for player_name in player_names:
        x_axis_values.append(player_name)
        y_axis_values.append(economy_by_player[player_name])
    return x_axis_values,y_axis_values

def plot_data(x_axis_values,y_axis_values):
    """It will create and display the bar chart."""
    figure_width = 15
    figure_height = 10
    plt.figure(figsize=(figure_width,figure_height))
    plt.barh(x_axis_values,y_axis_values)
    plt.title("Top Economic Bowlers in 2015")
    plt.ylabel("Player Name")
    plt.xlabel("Economy Rate")
    plt.show()

def execute():
    """It will prepare the data that to be plotted."""
    file_path = os.getcwd()+"/../Data/mock_deliveries.csv"
    economy_by_player = get_economy_by_player_2015(file_path)
    player_names = calculate_average_economy(economy_by_player)
    return prepare_data_to_plot(economy_by_player,player_names)

if __name__=="__main__":
    x_axis_values_,y_axis_values_ = execute()
    plot_data(x_axis_values_,y_axis_values_)
