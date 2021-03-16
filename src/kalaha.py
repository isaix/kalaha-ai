
class Kalaha:
    fields = []
    player_one = None
    player_two = None
    player_turn = None
    
    game_running = False
    won = None

    def __init__(self):
        self.fields = [4] * 14 # fields of kalaha board, index 6 and 13 are each players store, index 0-5 is player one fields, index 7-12 are player two fields
        self.fields[6] = 0 # reset the stores 
        self.fields[13] = 0

        self.player_one = self.Player(input("Enter player one name "))
        self.player_two = self.Player(input("Enter player two name "))

        self.player_turn = self.player_one

        print("The board: ", self.fields)
        print("player {} will start".format(self.player_turn.name))

        self.take_turn()

    def run_game(self):
        while game_running:
            self.take_turn()



    def change_player_turn(self):
        if self.player_turn is self.player_one:
            self.player_turn = self.player_two
        else:
            self.player_turn = self.player_one


    def take_turn(self):
        print("It is player {}'s turn".format(self.player_turn.name))
        selected_field = input("Enter selected field:\n")

        while type(selected_field) is not int:
            try:
                selected_field = int(selected_field)

                if (self.player_turn == self.player_one and 0 <= selected_field <= 6) or (self.player_turn == self.player_two and 7 <= selected_field <= 12) : # check is move valid
                    selected_field = self.move(selected_field)
                else:
                    print("Invalid field selected")
                    raise ValueError()

            except ValueError:
                print("Invalid input")
                selected_field = input("Enter selected field:\n")

        print("the field: ", self.fields)
        print("the selected field after turn finish is ", selected_field)
        if selected_field == 6 or selected_field == 13:
            return
        else:
            self.change_player_turn()



    def move(self, selected_field):

                seeds = self.fields[selected_field] # take seeds from field
                self.fields[selected_field] = 0 # set field to empty
                
                for i in range(1, seeds + 1): # iterate over fields for the number of seeds picked up
                    selected_field = (selected_field + 1) % len(self.fields) # modulo index of selected field if over the length of fields

                    if selected_field == 6 and self.player_turn == self.player_one or selected_field == 13 and self.player_turn == self.player_two: # check that player is putting seed in own store
                        self.fields[selected_field] += 1

                    elif selected_field == 6 and self.player_turn == self or selected_field == 13 and self.player_turn == self: # skip other players store
                        selected_field += 1
                        self.fields[selected_field] += 1

                    else: # regular field, always put seed
                        self.fields[selected_field] += 1

                if selected_field == 6 or selected_field == 13: # if landed in kalaha
                    return selected_field
                if fields[selected_field] == 1: # if last field was empty
                    return selected_field
                else:
                    return move(selected_field)



               

            
        


    class Player:
        def __init__(self, name):
            self.name = name



    def getPlayers(self):

        return self.player_one, self.player_two