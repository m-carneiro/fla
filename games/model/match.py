"""Match model"""


class Match:
    def __init__(self, championship, home, away, date, hour):
        self.championship = championship
        self.home = home
        self.away = away
        self.date = date
        self.hour = hour

    def __str__(self):
        return f'{self.championship} - {self.home} vs {self.away} - {self.date} - {self.hour}'

    def __repr__(self):
        return f'{self.championship} - {self.home} vs {self.away} - {self.date} - {self.hour}'

    def json(self):
        return {
            'championship': self.championship,
            'home': self.home,
            'away': self.away,
            'date': self.date,
            'hour': self.hour
        }
