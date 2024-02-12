"""Latest Match model"""


class LatestMatch:
    def __init__(self, championship: str, home: str, away: str, result: str, date: str):
        self.championship = championship
        self.home = home
        self.away = away
        self.result = result
        self.date = date

    def __str__(self):
        return f'{self.championship} - {self.home} vs {self.away} - {self.date} - {self.result}'

    def __repr__(self):
        return f'{self.championship} - {self.home} vs {self.away} - {self.date} - {self.result}'

    def json(self):
        return {
            'championship': self.championship,
            'home': self.home,
            'away': self.away,
            'date': self.date,
            'result': self.result
        }
