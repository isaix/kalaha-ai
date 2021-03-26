from kalaha import Kalaha

# importing the sys module 
import sys 
  
# the setrecursionlimit function is 
# used to modify the default recursion
# limit set by python. Using this,  
# we can increase the recursion limit 
# to satisfy our needs 
  
sys.setrecursionlimit(100000) 

if __name__ == "__main__":
    kalaha = Kalaha()
    kalaha.run_game()