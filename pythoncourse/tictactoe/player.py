import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
        
        
    def get_move(self):
        pass
    
  #am yusing inheritance to create random computer player and human computer player
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
        
    def get_move(self, game):
        #the available_moves function called returns a list of indices of empty squares
        square = random.choice(game.available_moves())
        
        return square
    
class  HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
        
    def get_move(self, game):
       
        valid_square = False
        val = None#if the user has not yet typed anything
        
        
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            
            try:
                val = int(square)
                if val not in game.available_moves():
                    return ValueError
                valid_square = True
            except ValueError:
                print("Invalid square, try again amigo.")
            
                
                
        return val
    
class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
        
    def get_move(self,game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
            
        else:
            #get the square based on minimax algorithimn
            
            square = self.minimax(game, self.letter)['position']
        return square
    def minimax(self, state, player):
        max_player = self.letter#yourself
        other_player = 'O' if player == 'X' else 'X'
        
        #first we want to check if previous move is a winner
        #this is our bestcase
        
        if  state.current_winner == other_player:
            return {'position': None,'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
            
            
            
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        
        if player == max_player:
            best  = {'position': None, 'score': -math.inf}
            
            
        else:
            best = {'postion': None, 'score': math.inf}#each score should minimise
            
            
            
        for possible_move in state.available_moves():
            
            #make a move and try that spot
            state.make_move(possible_move, player)
           
           
            #recurse using minimax to simulate a move after making that move
            sim_score = self.minimax(state, other_player)#now alternate other player
           
            
            #undo the move
            state.board[possible_move]= ''
            state.current_winner = None
            sim_score['position'] = possible_move
            
            #update the dictionary if neccessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                   best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                    
                    
        return best
                        
            
    
    
    
