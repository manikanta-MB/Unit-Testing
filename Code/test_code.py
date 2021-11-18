import unittest
import no_of_matches_played_by_year
import no_of_matches_won_by_team_by_year
import extra_runs_conceded_by_team_2016
import top_economic_bowlers_2015


class UnitTest(unittest.TestCase):
    """It is a Unit Testing Class having all the powers to test the cases
        given by programmer.
    """
    def test_no_of_matches_played_by_year(self):
        x_axis_values = ["2016","2017","2018"]
        y_axis_values = [11,10,9]
        self.assertEqual(no_of_matches_played_by_year.execute(),(x_axis_values,y_axis_values))
    def test_no_of_matches_won_by_team_by_year(self):
        seasons_original = ["2016","2017","2018"]
        team_season_matches_original = {
            'Chennai Super Kings':[3,3,2],
            'Kolkata Knight Riders':[2,1,2],
            'Delhi Capitals':[2,2,2],
            'Royal Challengers Bangalore':[1,1,1],
            'Mumbai Indians':[1,1,1],
            'Kings XI Punjab':[1,1,1],
            'Rajastan Royals':[1,1,0]
        }
        team_season_matches,seasons = no_of_matches_won_by_team_by_year.execute()
        self.assertEqual(seasons_original,seasons)
        self.assertEqual(len(team_season_matches_original),len(team_season_matches))
        for team,season_wise_data in team_season_matches.items():
            self.assertEqual(season_wise_data,team_season_matches_original[team])
    def test_extra_runs_conceded_by_team(self):
        teams_and_extra_runs_original = {
            'Chennai Super Kings':32,
            'Mumbai Indians':20,
            'Kolkata Knight Riders':21,
            'Delhi Capitals':20,
            'Royal Challengers Bangalore':40,
            'Rajastan Royals':55,
            'Kings XI Punjab':45
        }
        extra_runs_conceded_by_team = extra_runs_conceded_by_team_2016.execute()
        self.assertEqual(len(teams_and_extra_runs_original),len(extra_runs_conceded_by_team))
        for team,extra_runs in extra_runs_conceded_by_team.items():
            self.assertEqual(extra_runs,teams_and_extra_runs_original[team])
    def test_top_economic_bowlers(self):
        bowler_names_original = [
            "Jadeja","Kuldeep Yadav","Ashwin","Chahal",
            "Shami","B Kumar","Bumrah","Hardik Pandya"
            ]
        economic_rates_original = [
            3.17,4.75,5.08,5.78,
            5.83,6.0,6.69,7.92
        ]
        bowler_names,economic_rates = top_economic_bowlers_2015.execute()
        self.assertEqual(bowler_names_original,bowler_names)
        self.assertEqual(economic_rates_original,economic_rates)



if __name__=="__main__":
    unittest.main()
