from random import randint

class De:
    
    def __init__(self):
        self.de = randint(1,6)
        
    def __repr__(self):
        return f"{self.de}"
    

class player:
    
    def __init__(self,pseudo):
        self.player_1 = pseudo
        self.jetons = 0
        
    def __repr__(self):
        return f"{self.player_1} - {self.jetons}"
    
    def lancer_de(self):
        de1 = De()
        de2 = De()
        de3 = De()
        return sorted([de1.de, de2.de, de3.de])
    
 
        
    
    
class Lancer:
    
    def __init__(self,lancer):
        self.combinaison = lancer
        
               
    def points_combinaison(self):
        if self.combinaison == [1,2,4]:
            return  10
        elif self.combinaison == [1,1,1]:
            return  7
        elif self.combinaison == [1,1,6] or self.combinaison == [6,6,6]:
            return  6
        elif self.combinaison == [1,1,5] or self.combinaison == [5,5,5]:
            return  5
        elif self.combinaison == [1,1,4] or self.combinaison == [4,4,4]:
            return  4
        elif self.combinaison == [1,1,3] or self.combinaison == [3,3,3]:
            return  3
        elif self.combinaison == [1,1,2] or self.combinaison == [2,2,2]:
            return  2
        elif self.combinaison == [1,2,3] or self.combinaison == [2,3,4]:
            return  2
        elif self.combinaison == [3,4,5] or self.combinaison == [3,4,5]:
            return  2
        
        elif self.combinaison == [1,2,2]:
            return  2
        
        else:
            return  1
    
    
    
    
class jeux:
    
    def __init__(self,nom):
        self.partie = nom
        self.joueurs = {}
        self.lance  = None
        self.pot = 21
        
    def add_player(self,pseudo):
        self.joueurs[pseudo] = player(pseudo)
    
    def __repr__(self):
        res = ''
        for j in self.joueurs:
            res += repr(self.joueurs[j]) + '\n'
        return res 

    
from time import sleep    
    

j1 = jeux('j1')
j1.add_player('momo')
j1.add_player('sam')
j1.add_player('hacene')
while not j1.pot == 0:    
    a = j1.joueurs['momo'].lancer_de()   
    b = j1.joueurs['hacene'].lancer_de()
    print (a)
    print(b)
    
    
    l = Lancer(a).points_combinaison()
    
    if j1.pot < l:
        j1.joueurs['momo'].jetons += j1.pot
        break
    
    j1.joueurs['momo'].jetons += l
    print(j1.joueurs['momo'].jetons)
    j1.pot -= Lancer(a).points_combinaison()
    
    l2 = Lancer(b).points_combinaison()
    
    if j1.pot < l2:
        j1.joueurs['hacene'].jetons += j1.pot
        break
    
    j1.joueurs['hacene'].jetons += l2
    print(j1.joueurs['hacene'].jetons )
    j1.pot -= Lancer(b).points_combinaison()
    
    print(j1.pot)
    sleep(0.1)
    
g = j1.joueurs['momo'].jetons
h = j1.joueurs['hacene'].jetons
if g < h:
    print ('hacene a gagné',h,g)
else:
    print('momo a gagné',g,h)