import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/boggio-analytics/api/football-prediction'

mcp = FastMCP('football-prediction')

@mcp.tool()
def predictions(market: Annotated[Union[str, None], Field(description='Shows the predictions for a certain market. Defaults to "classic" if not provided')] = None,
                iso_date: Annotated[Union[str, None], Field(description='Will filter the results by date. Can be used to show past results.')] = None,
                federation: Annotated[Union[str, None], Field(description='Filter the predictions by federation')] = None) -> dict: 
    '''This endpoint returns a list of the football predictions scheduled to start in the next 48hours. URL parameters can be specified to show past predictions or to filter by federation and prediction market.'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/predictions'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'market': market,
        'iso_date': iso_date,
        'federation': federation,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def prediction_details(id: Annotated[Union[int, float], Field(description='Default: 99999')]) -> dict: 
    '''Grab all available predictions for a match id'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/predictions/99999'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def performance_stats_for_past_predictions(market: Annotated[Union[str, None], Field(description='Show stats for a different prediction market. Defaults to "classic" if not provided')] = None,
                                           federation: Annotated[Union[str, None], Field(description='Filter stats by federation')] = None) -> dict: 
    '''Returns information about the accuracy of past predictions. (in the last day, 7 days, 14 days and 30 days) Can be additionally filtered by federation and market. If no market filter is provided it defaults to classic'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/performance-stats'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'market': market,
        'federation': federation,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def head_to_head(limit: Annotated[Union[int, float, None], Field(description='Limit the search to only X previous encounters. (max is 10) Default: 10')] = None) -> dict: 
    '''Shows head to head stats and previous encounters for the home and away team of an upcoming match.'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/head-to-head/81930'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def home_team_league_stats(id: Annotated[Union[int, float], Field(description='(use predictions endpoint to get list of IDs) Default: 81930')]) -> dict: 
    '''Shows the league table and stats for the home team of an upcoming match.'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/home-league-stats/81930'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def home_team_last10_matches(id: Annotated[Union[int, float], Field(description='(use predictions endpoint to get list of IDs) Default: 81930')]) -> dict: 
    '''Grab the statistics and list of the last 10 matches played by the home team for a certain ID'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/home-last-10/81930'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def away_team_last10_matches(id: Annotated[Union[int, float], Field(description='(use predictions endpoint to get list of IDs) Default: 81930')]) -> dict: 
    '''Grab the statistics and list of the last 10 matches played by the away team for a certain ID'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/away-last-10/81930'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def away_team_league_stats(id: Annotated[Union[int, float], Field(description='(use predictions endpoint to get list of IDs) Default: 86397')]) -> dict: 
    '''Shows the league table and stats for the away team of an upcoming match.'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/away-league-stats/86397'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_available_markets() -> dict: 
    '''List all available markets and the ones that are enabled for your subscription plan'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/list-markets'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_available_federations() -> dict: 
    '''Returns an array of all the available federations.'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/list-federations'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_list_of_fixture_ids() -> dict: 
    '''Returns a list of fixture IDs that can be used to make requests to endpoints expecting a ID url parameter. Can be filtered by: - iso_date - market - federation'''
    url = 'https://football-prediction-api.p.rapidapi.com/api/v2/get-list-of-fixture-ids'
    headers = {'x-rapidapi-host': 'football-prediction-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
