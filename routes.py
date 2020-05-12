import requests as r

def get_team(team_name):
    url = f"https://api-football-beta.p.rapidapi.com/teams?name={team_name}"

    headers = {
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
    'x-rapidapi-key': "370ba1b368msh3d4b495ab10e060p1cd375jsn03d308d545b2"
    }

    response = r.get(url, headers=headers).json()
    return response