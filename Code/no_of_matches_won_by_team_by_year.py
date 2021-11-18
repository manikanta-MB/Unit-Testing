"""
This Program displays the Stacked bar chart for the no.of matches won by each
team in each IPL Season.
To solve this problem first i divided it into 3 modules.
    1.getting no.of matches won by each team seasonwise
     (but not ordered in ascending order of season year)
    2.ordering the data(got in 1st module) in ascending order of season year.
    3.Plotting the data(got in 2nd module) with the help of matplotlib library.
"""

# importing the required libraries to deal with csv files and to plot the data.
import csv
import os
from matplotlib import pyplot as plt

def get_team_season_matches(filename):
    """Creating the data of no.of matches won by each team in
    each season, from scratch data file, and returning it.
    """
    team_season_matches={}
    seasons = set()
    with open(filename,"r",encoding="utf8") as file_obj:
        matches_reader = csv.DictReader(file_obj)
        for current_match_info in matches_reader:
            season = current_match_info["season"].strip()
            seasons.add(season)
            won_team = current_match_info["winner"].strip()
            if won_team not in team_season_matches:
                team_season_matches[won_team] = {}
            team_season_matches[won_team][season] = team_season_matches[won_team].get(season,0)+1
    seasons = sorted(list(seasons))
    return team_season_matches,seasons

def order_matches_seasonwise(team_season_matches,seasons):
    """ordering the teams and correpsonding no.of won matches by Seasonwise"""
    teams_and_matches_seasonwise = {}
    for team,season_data in team_season_matches.items():
        teams_and_matches_seasonwise[team] = []
        for season in seasons:
            teams_and_matches_seasonwise[team].append(season_data.get(season,0))
    return teams_and_matches_seasonwise

def plot_the_data(teams_and_matches_seasonwise,seasons):
    """Plotting the Sorted data"""
    no_seasons = len(seasons)
    # it will be useful for calculating the ending position of the previous bar.
    prev_list = [0]*no_seasons
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(10)
    fig_obj = fig.add_subplot(111)
    # Shrink current axis by 20%
    box = fig_obj.get_position()
    fig_obj.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    #Hardcoding the names of colors for each team
    colors = [
                "fuchsia","maroon","red","yellow","blue","lime","purple",
                "black","green","olive","teal","aqua","navy","grey"
            ]
    # Creating the bar and Placing it to the right of previous team bar in each season.
    color_index=0
    for team,current_team_matches in teams_and_matches_seasonwise.items():
        color_name = colors[color_index]
        fig_obj.bar(seasons,current_team_matches,bottom=prev_list,label = team,color=color_name)
        prev_list = [prev_list[i]+current_team_matches[i] for i in range(no_seasons)]
        color_index += 1
    plt.title("Number of matches won by each team Seasonwise",fontweight='bold',fontsize=20)
    plt.xlabel("Seasons",fontweight='bold',fontsize=15)
    plt.ylabel("number of matches won",fontweight='bold',fontsize=15)
    # Put a legend to the right of the current axis
    fig_obj.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def execute():
    """It will prepare the data to be plotted."""
    team_season_matches,seasons = get_team_season_matches(os.getcwd()+"/../Data/mock_matches.csv")
    teams_and_matches_seasonwise = order_matches_seasonwise(team_season_matches,seasons)
    return teams_and_matches_seasonwise,seasons

if __name__=="__main__":
    teams_matches_season_wise,seasons_ = execute()
    plot_the_data(teams_matches_season_wise,seasons_)
