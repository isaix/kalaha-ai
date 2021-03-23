import math

def findMiniMax(kalaha, max_depth, maximizing_player):
    if max_depth == 0 or kalaha.game_running == False:
        # evaluate board state
        return kalaha.fields[13] - kalaha.fields[6], None

    
    if maximizing_player:
        max_value = math.inf
        selected_field = None
        # find alle states vi kan komme itl herfra, med moves
        # loop igennem de states og kør minimax rekursivt
        for field in range(7, 13): # iterate over all possible moves to make
            if kalaha.fields[field] > 0: # check if move is valid
                kalaha.move(kalaha.fields, field) # perform move
                value, value_field = findMiniMax(kalaha, max_depth - 1, True if kalaha.player_turn == kalaha.player_two else False) # run minimax on new game state
                if (value > max_value):
                    max_value = value
                    selected_field = value_field
                else:
                    selected_field = field
                # max_value = max(max_value, value)
        return max_value, selected_field
    
    else:
        min_value = -math.inf
        selected_field = None

        # find alle states vi kan komme itl herfra, med moves
        # loop igennem de states og kør minimax rekursivt
        for field in range(0, 6):
            if kalaha.fields[field] > 0:
                value, value_field = findMiniMax(kalaha, max_depth - 1, True if kalaha.player_turn == kalaha.player_two else False)
                if (value < min_value):
                    min_value = value
                    selected_field = value_field
                else:
                    selected_field = field
                # min_value = min(min_value, value)
        return min_value, selected_field







        
        


    # def minimax(state, max_depth, is_player_minimizer):
    #     if max_depth == 0 or state.is_end_state():
    #         # We're at the end. Time to evaluate the state we're in
    #         return evaluation_function(state)
    #     # Is the current player the minimizer?
    #     if is_player_minimizer:
    #         value = -math.inf
    #         for move in state.possible_moves():
    #             evaluation = minimax(move, max_depth - 1, False)
    #             min = min(value, evaluation)
    #         return value
    #     # Or the maximizer?
    #     value = math.inf
    #     for move in state.possible_moves():
    #         evaluation = minimax(move, max_depth - 1, True)
    #         max = max(value, evaluation)
    #     return value