from games.api import get_all_matches, get_recent_matches


def beautify_matches() -> list[str]:
    all_matches = []
    with open('matches.json', 'r') as file:
        matches = get_all_matches()
        for match in matches:
            message = f"""
                Campeonato: {match.championship}
                
                {match.home} vs {match.away}
                
                {match.date} às {match.hour}
            """
            all_matches.append(message)

    return all_matches


def next_match() -> str:
    matches = get_all_matches()
    next_game = matches[0]
    message = f"""
        Campeonato: {next_game.championship}
        
        {next_game.home} vs {next_game.away}
        
        {next_game.date} às {next_game.hour}
    """
    return message


def recent_matches() -> list[str]:
    all_messages = []
    latest_matches = get_recent_matches()
    for match in latest_matches:
        results = match.result.split('-')

        message = f"""
            Campeonato: {match.championship}
            
            {match.home} {results[0]} vs {results[1]} {match.away}
            {match.date}
            """

        all_messages.append(message)

    return all_messages
