







class player:
 def play(self):
  print("The player in playing cricket.")
    
#Define the derived class Batsman
class Batsman(player):
 def play(self):
  print("The batsman is batting.")
     
#Define the derived class Bowler
class Bowler(player):
 def play(self):
 
   print("the bowler is bowling.")
          
#create objects of batsman and bowler
batsman=Batsman()
bowler=Bowler()