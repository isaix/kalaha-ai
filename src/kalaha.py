import random

class InvalidField(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)


class Kalaha:
    fields = []
    player_one = None
    player_two = None
    player_turn = None
    
    game_running = True
    won = None

    def __init__(self):
        self.fields = [4] * 14 # fields of kalaha board, index 6 and 13 are each players store, index 0-5 is player one fields, index 7-12 are player two fields
        self.fields[6] = 0 # reset the stores 
        self.fields[13] = 0

        self.player_one = self.Player(input("Enter player one name "))
        self.player_two = self.Player(input("Enter player two name "))

        self.player_turn = self.player_one if random.randint(0, 1)== 1 else self.player_two

        print("The board: ", self.fields)
        print("player {} will start".format(self.player_turn.name))

        self.run_game()

    def run_game(self):
        while self.game_running:
            self.take_turn()

        print("Game completed")
        if (self.won != None):
            print("player {} won!".format(self.won))
        else:
            print("It was a tie!")
        

    def check_result(self):
        if self.fields[6] > sum(self.fields)/2:
            self.won = self.player_one
            self.game_running = False
            return True
        elif self.fields[13] > sum(self.fields)/2:
            self.won = self.player_two
            self.game_running = False
            return True
        elif(self.fields[6] == sum(self.fields)/2 and self.fields[13] == sum(fields)/2):
            self.game_running = False
            return True
        else:
            return False


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

                if (((self.player_turn == self.player_one and 0 <= selected_field <= 6) or 
                    (self.player_turn == self.player_two and 7 <= selected_field <= 12)) and
                    (self.fields[selected_field] > 0)): # check if move is valid
                    selected_field = self.move(selected_field)
                    if selected_field == None:
                        return
                else:
                    raise InvalidField()

            except ValueError:
                print("Invalid input")
                selected_field = input("Enter selected field:\n")
            except InvalidField:
                print("Invalid field selected")
                selected_field = input("Enter selected field:\n")


        print("the field: ", self.fields)
        print("the selected field after turn finish is ", selected_field)
        if selected_field == 6 or selected_field == 13:
            return
        else:
            self.change_player_turn()


    def move(self, selected_field):

                seeds = self.fields[selected_field] # take seeds from selected field
                self.fields[selected_field] = 0 # set selected field to empty
                
                for i in range(1, seeds + 1): # iterate over fields for the number of seeds picked up
                    selected_field = (selected_field + 1) % len(self.fields) # modulo index of selected field is over the length of fields

                    if selected_field == 6 and self.player_turn == self.player_one or selected_field == 13 and self.player_turn == self.player_two: # check that player is putting seed in own store
                        self.fields[selected_field] += 1

                    elif selected_field == 6 and self.player_turn == self.player_two or selected_field == 13 and self.player_turn == self.player_one: # skip other players store
                        selected_field += 1
                        selected_field = selected_field % len(self.fields) # check again if modulo index of selected field is over the length of fields
                        self.fields[selected_field] += 1

                    else: # regular field, always put seed
                        self.fields[selected_field] += 1


                if sum(self.fields[0:6]) == 0:
                    self.fields[6] += sum(self.fields[7:13])
                    self.fields[7:13] = [0]*6

                elif sum(self.fields[7:13]) == 0:
                    self.fields[13] += sum(self.fields[0:6])
                    self.fields[0:6] = [0]*6

                print("the field: ", self.fields)
                print("the selected field after turn finish is ", selected_field)

                if self.check_result():
                    return None

                if selected_field == 6 or selected_field == 13: # if landed in kalaha
                    return selected_field
                if self.fields[selected_field] == 1: # if last field was empty
                    return selected_field
                else:
                    return self.move(selected_field)

    class Player:
        def __init__(self, name):
            self.name = name
