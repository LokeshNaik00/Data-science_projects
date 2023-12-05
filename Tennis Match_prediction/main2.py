from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fractions import Fraction
import pickle
import pandas as pd
from fastapi.encoders import jsonable_encoder

class InputData(BaseModel):
    surface: int
    player_one_ht: float
    player_two_ht: float
    player_one_age: float
    player_two_age: float
    player_one_hand: int
    player_two_hand: int
    player_one_ace: float
    player_two_ace: float
    player_one_df: float
    player_two_df: float
    player_one_break_point_saved: float
    player_two_break_point_saved: float
    player_one_break_point_faced: float
    player_two_break_point_faced: float
    player_one_rank: float
    player_two_rank: float
    player_one_rank_points: float
    player_two_rank_points: float
    player_one_win_percentage: float
    player_two_win_percentage: float

with open('xgb_tennis_model.pkl', 'rb') as f:
    model1 = pickle.load(f)

app = FastAPI()

@app.post('/prediction')
def get_prediction(data: InputData):
    received = pd.DataFrame(jsonable_encoder(data), index=[0])
    cols_new = ['surface', 'player_one_ht', 'player_two_ht', 'player_one_age','player_two_age', 'player_one_hand', 'player_two_hand','player_one_ace', 'player_two_ace', 'player_one_df', 'player_two_df','player_one_break_point_saved', 'player_two_break_point_saved', 'player_one_break_point_faced', 'player_two_break_point_faced','player_one_rank', 'player_two_rank', 'player_one_rank_points','player_two_rank_points', 'player_one_win_percentage','player_two_win_percentage']

    received = received[cols_new]
    pred_name = model1.predict(received)[0]
    Prob = model1.predict_proba(received) * 100
    probability_percent = {
			"Loss": round(Prob.tolist()[0][0], 2),
			"Win": round(Prob.tolist()[0][1], 2)
	}
    decimal_odds = {
		"Loss_odds": round(100/Prob.tolist()[0][0], 2),
		"Win_odds": round(100/Prob.tolist()[0][1], 2)
    }

    return {'prediction': pred_name,
			'probability_percent': probability_percent,
			"predicted_decimal_odds": decimal_odds
			
			}
