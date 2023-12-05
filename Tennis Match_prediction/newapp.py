import requests
import json
from datetime import datetime
# import pandas as pd
import time
from re import search



with open('backtesting.json', 'r') as f:
		team_details = json.load(f)
print(len(team_details))

# function to get the prediction of tennis event from goal serve for yesterday
#http://127.0.0.1:8000/prediction
def test2(team_details):
	dataList = []
	for info in team_details:
		url = "http://127.0.0.1:8000/prediction"
		if (info["player_one_win_percentage"] == "0.0") or (info["player_one_win_percentage"] == "0.0"):
			dataList.append(info)
		else:
			payload = json.dumps({
			  "surface": info["surface"],
			  "player_one_ht": info["player_one_ht"],
			  "player_two_ht": info["player_two_ht"],
			  "player_one_age": info["player_one_age"],
			  "player_two_age": info["player_two_age"],
			  "player_one_hand": info["player_one_hand"],
			  "player_two_hand": info["player_two_hand"],
			  "player_one_ace": info["player_one_ace"],
			  "player_two_ace": info["player_two_ace"],
			  "player_one_df": info["player_one_df"],
			  "player_two_df": info["player_two_df"],
			  "player_one_break_point_saved"  : info["player_one_break_point_saved"],
			  "player_two_break_point_saved"  : info["player_two_break_point_saved"],
			  "player_one_break_point_faced"  : info["player_one_break_point_faced"],
			  "player_two_break_point_faced"  : info["player_two_break_point_faced"],
			  "player_one_rank"  : info["player_one_rank"],
			  
			
			  "player_two_rank" : info["player_two_rank"],
			  "player_one_rank_points" : info["player_one_rank_points"],
			  "player_two_rank_points" : info["player_two_rank_points"],
			  "player_one_win_percentage" : info["player_one_win_percentage"],
			  "player_two_win_percentage" : info["player_two_win_percentage"]
			})
			headers = {
			  'Content-Type': 'application/json'
			}
			response = requests.request("POST", url, headers=headers, data=payload)
			data = response.json()
			info.update(data)
			dataList.append(info)
			print(dataList)


	return dataList

raw_data_1 = test2(team_details)

with open("tennis_predictions.json", 'w') as f:
 	f.write(json.dumps(raw_data_1, indent=3))

#import pandas as pd
#df = pd.read_json("tennis_for_september27.json")
#df.to_csv("tennis_matches prediction september27.csv",index=False)


