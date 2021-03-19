class Search:

    def findMiniMax
        
        


    def minimax(state, max_depth, is_player_minimizer):
        if max_depth == 0 or state.is_end_state():
            # We're at the end. Time to evaluate the state we're in
            return evaluation_function(state)
        # Is the current player the minimizer?
        if is_player_minimizer:
            value = -math.inf
            for move in state.possible_moves():
                evaluation = minimax(move, max_depth - 1, False)
                min = min(value, evaluation)
            return value
        # Or the maximizer?
        value = math.inf
        for move in state.possible_moves():
            evaluation = minimax(move, max_depth - 1, True)
            max = max(value, evaluation)
        return value