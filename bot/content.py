import json
from games.api import get_all_matches
from games.model.match import Match


def beautify_matches():
    all_matches = []
    with open('matches.json', 'r') as file:
        matches = get_all_matches()
        for match in matches:
            for i, j in match:
                print(i, j)
