def find_best_game(games):
    """
    Finds the game with the highest expected value (EV) from a list of games.

    Args:
        games: A tuple of Game namedtuples. Each Game has a name and a tuple of
               outcomes. Each outcome is a tuple (probability, reward).

    Returns:
        The name of the game with the highest EV as a string.
    """
    max_ev = float('-inf')
    best_game_name = ""

    for game in games:
        current_ev = 0
        for probability, reward in game.outcomes:
            current_ev += probability * reward
        
        if current_ev > max_ev:
            max_ev = current_ev
            best_game_name = game.name
            
    return best_game_name