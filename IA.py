import sys
from PyQt5.QtWidgets import *
from random import *
from mouvement import *
from bombe import *


class ia(QWidget) :
    def __init__(self, Map) :
        super(ia, self).__init__()
        self.map = Map
        self.mouvement = mouvement(Map)
        self.bombe = bombe(Map)

    def moveIA2(self) :
        if self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2]] == 74 :
            if self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] != 0 and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] != 2 and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] != 4 :
                if self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 2][self.map.findJoueur(2)[2]] != 4 and self.map.Map1[self.map.findJoueur(2)[1] + 2][self.map.findJoueur(2)[2]] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(2)[1] + 2][self.map.findJoueur(2)[2]] == 1 or self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1]): 
                    self.mouvement.moveDown(7, 74)
                    self.map.var.posJ2 = 1
            elif self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] != 0 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] != 2 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] != 4 :
                if self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] - 2][self.map.findJoueur(2)[2]] != 4 and self.map.Map1[self.map.findJoueur(2)[1] - 2][self.map.findJoueur(2)[2]] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(2)[1] - 2][self.map.findJoueur(2)[2]] == 1 or self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1]): 
                    self.mouvement.moveTop(7, 74)
                    self.map.var.posJ2 = 0

            elif self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] != 0 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] != 2 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] != 4 :
                if self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] + 1] != 4  and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 2] != 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 2] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 2] == 1 or self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] + 1]): 
                    self.mouvement.moveRight(7, 74)
                    self.map.var.posJ2 = 3
                    
            elif self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] != 0 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] != 2 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] != 4 :
                if self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 2] != 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 2] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 2] == 1 or self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1]): 
                    self.mouvement.moveLeft(7, 74)
                    self.map.var.posJ2 = 2
                    
        elif self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2]] == 7 :
            if self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] == 0 or self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] == 0 or self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] == 0 or self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] == 0:
                if self.map.var.bombeJ1 == "pyke" :
                    self.bombe.posePikeBombe(7, 74)
                else :
                    self.bombe.poseBombe(7, 74)
            elif (self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] == 4 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] == 1) or (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] == 1) or (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] == 1):
                self.mouvement.moveTop(7, 74)
                self.map.var.posJ2 = 0
                
            elif (self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] == 4 and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] == 1) or (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] == 1) or (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] == 1):
                self.mouvement.moveDown(7, 74)
                self.map.var.posJ2 = 1
                
            elif (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] == 1) or  (self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] == 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] == 1) or (self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] == 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] == 1):
                self.mouvement.moveLeft(7, 74)
                self.map.var.posJ2 = 2
                
            elif (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] == 1) or (self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] == 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] == 1) or (self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] == 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] == 1):
                self.mouvement.moveRight(7, 74)
                self.map.var.posJ2 = 3
                
            else :
                ia = random()
                if ia < 0.25 :
                    if (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 1] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 2] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] + 2] != 4):
                        if self.map.var.stateJ2 == "skull" :
                            self.mouvement.moveLeft(7, 74)
                            self.map.var.posJ2 = 2


                elif ia >= 0.25  and ia < 0.5:
                    if (self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2 - 1]] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 2] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1]][self.map.findJoueur(2)[2] - 2] != 4):
                        if self.map.var.stateJ2 == "skull" :
                            self.mouvement.moveRight(7, 74)
                            self.map.var.posJ2 = 3
                            
                        else :
                            self.mouvement.moveLeft(7, 74)
                            self.map.var.posJ2 = 2

                
                elif ia >= 0.5 and ia < 0.75:
                    if (self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] == 1 or self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2]] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] - 2][self.map.findJoueur(2)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] - 1][self.map.findJoueur(2)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] - 2][self.map.findJoueur(2)[2]] != 4):
                        if self.map.var.stateJ2 == "skull" :
                            self.mouvement.moveDown(7, 74)
                            self.map.var.posJ2 = 1
                            
                        else :
                            self.mouvement.moveTop(7, 74)
                            self.map.var.posJ2 = 1

                
                else :
                    if self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2]] == 1 and (self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 2][self.map.findJoueur(2)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] + 1][self.map.findJoueur(2)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(2)[1] + 2][self.map.findJoueur(2)[2]] != 4):
                        if self.map.var.stateJ2 == "skull" :
                            self.mouvement.moveTop(7, 74)
                            self.map.var.posJ2 = 0
                            
                        else :
                            self.mouvement.moveDown(7, 74)
                            self.map.var.posJ2 = 1

    
    def moveIA3(self) :
        if self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2]] == 84 :
            if self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] != 0 and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] != 2 and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] != 4 :
                if self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 2][self.map.findJoueur(3)[2]] != 4 and self.map.Map1[self.map.findJoueur(3)[1] + 2][self.map.findJoueur(3)[2]] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(3)[1] + 2][self.map.findJoueur(3)[2]] == 1 or self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1]): 
                    self.mouvement.moveDown(8, 84)
                    self.map.var.posJ3 = 1
                    if self.map.var.movementJ3 == 0:
                        self.map.var.movementJ3 = 1
                    elif self.map.var.movementJ3 == 1:
                        self.map.var.movementJ3 = 2
                    elif self.map.var.movementJ3 == 2:
                        self.map.var.movementJ3 = 3
                    elif self.map.var.movementJ3 == 3:
                        self.map.var.movementJ3 = 0
            elif self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] != 0 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] != 2 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] != 4 :
                if self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] - 2][self.map.findJoueur(3)[2]] != 4 and self.map.Map1[self.map.findJoueur(3)[1] - 2][self.map.findJoueur(3)[2]] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(3)[1] - 2][self.map.findJoueur(3)[2]] == 1 or self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1]): 
                    self.mouvement.moveTop(8, 84)
                    self.map.var.posJ3 = 0
                    if self.map.var.movementJ3 == 0:
                        self.map.var.movementJ3 = 1
                    elif self.map.var.movementJ3 == 1:
                        self.map.var.movementJ3 = 2
                    elif self.map.var.movementJ3 == 2:
                        self.map.var.movementJ3 = 3
                    elif self.map.var.movementJ3 == 3:
                        self.map.var.movementJ3 = 0
            elif self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] != 0 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] != 2 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] != 4 :
                if self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] + 1] != 4  and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 2] != 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 2] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 2] == 1 or self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] + 1]): 
                    self.mouvement.moveRight(8, 84)
                    self.map.var.posJ3 = 3
                    if self.map.var.movementJ3 == 0:
                        self.map.var.movementJ3 = 1
                    elif self.map.var.movementJ3 == 1:
                        self.map.var.movementJ3 = 2
                    elif self.map.var.movementJ3 == 2:
                        self.map.var.movementJ3 = 3
                    elif self.map.var.movementJ3 == 3:
                        self.map.var.movementJ3 = 0
            elif self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] != 0 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] != 2 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] != 4 :
                if self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 2] != 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 2] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 2] == 1 or self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1]): 
                    self.mouvement.moveLeft(8, 84)
                    self.map.var.posJ3 = 2
                    if self.map.var.movementJ3 == 0:
                        self.map.var.movementJ3 = 1
                    elif self.map.var.movementJ3 == 1:
                        self.map.var.movementJ3 = 2
                    elif self.map.var.movementJ3 == 2:
                        self.map.var.movementJ3 = 3
                    elif self.map.var.movementJ3 == 3:
                        self.map.var.movementJ3 = 0

        elif self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2]] == 8 :
            if self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] == 0 or self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] == 0 or self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] == 0 or self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] == 0:
                if self.map.var.bombeJ1 == "pyke" :
                    self.bombe.posePikeBombe(8, 84)
                else :
                    self.bombe.poseBombe(8, 84)
            elif (self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] == 4 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] == 1) or (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] == 1) or (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] == 1):
                self.mouvement.moveTop(8, 84)
                self.map.var.posJ3 = 0
                if self.map.var.movementJ3 == 0:
                    self.map.var.movementJ3 = 1
                elif self.map.var.movementJ3 == 1:
                    self.map.var.movementJ3 = 2
                elif self.map.var.movementJ3 == 2:
                    self.map.var.movementJ3 = 3
                elif self.map.var.movementJ3 == 3:
                    self.map.var.movementJ3 = 0
            elif (self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] == 4 and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] == 1) or (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] == 1) or (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] == 1):
                self.mouvement.moveDown(8, 84)
                self.map.var.posJ3 = 1
                if self.map.var.movementJ3 == 0:
                    self.map.var.movementJ3 = 1
                elif self.map.var.movementJ3 == 1:
                    self.map.var.movementJ3 = 2
                elif self.map.var.movementJ3 == 2:
                    self.map.var.movementJ3 = 3
                elif self.map.var.movementJ3 == 3:
                    self.map.var.movementJ3 = 0
            elif (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] == 1) or  (self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] == 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] == 1) or (self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] == 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] == 1):
                self.mouvement.moveLeft(8, 84)
                self.map.var.posJ3 = 2
                if self.map.var.movementJ3 == 0:
                    self.map.var.movementJ3 = 1
                elif self.map.var.movementJ3 == 1:
                    self.map.var.movementJ3 = 2
                elif self.map.var.movementJ3 == 2:
                    self.map.var.movementJ3 = 3
                elif self.map.var.movementJ3 == 3:
                    self.map.var.movementJ3 = 0
            elif (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] == 1) or (self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] == 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] == 1) or (self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] == 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] == 1):
                self.mouvement.moveRight(8, 84)
                self.map.var.posJ3 = 3
                if self.map.var.movementJ3 == 0:
                    self.map.var.movementJ3 = 1
                elif self.map.var.movementJ3 == 1:
                    self.map.var.movementJ3 = 2
                elif self.map.var.movementJ3 == 2:
                    self.map.var.movementJ3 = 3
                elif self.map.var.movementJ3 == 3:
                    self.map.var.movementJ3 = 0
            else :
                ia = random()
                if ia < 0.25 :
                    if (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 1] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 2] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] + 2] != 4):
                        if self.map.var.stateJ3 == "skull" :
                            self.mouvement.moveLeft(8, 84)
                            self.map.var.posJ3 = 2
                            if self.map.var.movementJ3 == 0:
                                self.map.var.movementJ3 = 1
                            elif self.map.var.movementJ3 == 1:
                                self.map.var.movementJ3 = 2
                            elif self.map.var.movementJ3 == 2:
                                self.map.var.movementJ3 = 3
                            elif self.map.var.movementJ3 == 3:
                                self.map.var.movementJ3 = 0
                        else :
                            self.mouvement.moveRight(8, 84)
                            self.map.var.posJ3 = 3
                            if self.map.var.movementJ3 == 0:
                                self.map.var.movementJ3 = 1
                            elif self.map.var.movementJ3 == 1:
                                self.map.var.movementJ3 = 2
                            elif self.map.var.movementJ3 == 2:
                                self.map.var.movementJ3 = 3
                            elif self.map.var.movementJ3 == 3:
                                self.map.var.movementJ3 = 0


                elif ia >= 0.25  and ia < 0.5:
                    if (self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2 - 1]] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 2] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1]][self.map.findJoueur(3)[2] - 2] != 4):
                        if self.map.var.stateJ3 == "skull" :
                            self.mouvement.moveRight(8, 84)
                            self.map.var.posJ3 = 3
                            if self.map.var.movementJ3 == 0:
                                self.map.var.movementJ3 = 1
                            elif self.map.var.movementJ3 == 1:
                                self.map.var.movementJ3 = 2
                            elif self.map.var.movementJ3 == 2:
                                self.map.var.movementJ3 = 3
                            elif self.map.var.movementJ3 == 3:
                                self.map.var.movementJ3 = 0
                        else :
                            self.mouvement.moveLeft(8, 84)
                            self.map.var.posJ3 = 2
                            if self.map.var.movementJ3 == 0:
                                self.map.var.movementJ3 = 1
                            elif self.map.var.movementJ3 == 1:
                                self.map.var.movementJ3 = 2
                            elif self.map.var.movementJ3 == 2:
                                self.map.var.movementJ3 = 3
                            elif self.map.var.movementJ3 == 3:
                                self.map.var.movementJ3 = 0

                
                elif ia >= 0.5 and ia < 0.75:
                    if (self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] == 1 or self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2]] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] - 2][self.map.findJoueur(3)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] - 1][self.map.findJoueur(3)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] - 2][self.map.findJoueur(3)[2]] != 4):
                        if self.map.var.stateJ3 == "skull" :
                            self.mouvement.moveDown(8, 84)
                            self.map.var.posJ3 = 1
                            if self.map.var.movementJ3 == 0:
                                self.map.var.movementJ3 = 1
                            elif self.map.var.movementJ3 == 1:
                                self.map.var.movementJ3 = 2
                            elif self.map.var.movementJ3 == 2:
                                self.map.var.movementJ3 = 3
                            elif self.map.var.movementJ3 == 3:
                                self.map.var.movementJ3 = 0
                        else :
                            self.mouvement.moveTop(8, 84)
                            self.map.var.posJ3 = 0
                            if self.map.var.movementJ3 == 0:
                                self.map.var.movementJ3 = 1
                            elif self.map.var.movementJ3 == 1:
                                self.map.var.movementJ3 = 2
                            elif self.map.var.movementJ3 == 2:
                                self.map.var.movementJ3 = 3
                            elif self.map.var.movementJ3 == 3:
                                self.map.var.movementJ3 = 0

                
                else :
                    if self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2]] == 1 and (self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 2][self.map.findJoueur(3)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] + 1][self.map.findJoueur(3)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(3)[1] + 2][self.map.findJoueur(3)[2]] != 4):
                        if self.map.var.stateJ3 == "skull" :
                            self.mouvement.moveTop(8, 84)
                            self.map.var.posJ3 = 0
                            if self.map.var.movementJ3 == 0:
                                self.map.var.movementJ3 = 1
                            elif self.map.var.movementJ3 == 1:
                                self.map.var.movementJ3 = 2
                            elif self.map.var.movementJ3 == 2:
                                self.map.var.movementJ3 = 3
                            elif self.map.var.movementJ3 == 3:
                                self.map.var.movementJ3 = 0
                        else :
                            self.mouvement.moveDown(8, 84)
                            self.map.var.posJ3 = 1
                            if self.map.var.movementJ3 == 0:
                                self.map.var.movementJ3 = 1
                            elif self.map.var.movementJ3 == 1:
                                self.map.var.movementJ3 = 2
                            elif self.map.var.movementJ3 == 2:
                                self.map.var.movementJ3 = 3
                            elif self.map.var.movementJ3 == 3:
                                self.map.var.movementJ3 = 0

    
    def moveIA4(self) :
        if self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2]] == 94 :
            if self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] != 0 and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] != 2 and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] != 4 :
                if self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 2][self.map.findJoueur(4)[2]] != 4 and self.map.Map1[self.map.findJoueur(4)[1] + 2][self.map.findJoueur(4)[2]] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(4)[1] + 2][self.map.findJoueur(4)[2]] == 1 or self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1]): 
                    self.mouvement.moveDown(9, 94)
                    self.map.var.posJ4 = 1
                    if self.map.var.movementJ4 == 0:
                        self.map.var.movementJ4 = 1
                    elif self.map.var.movementJ4 == 1:
                        self.map.var.movementJ4 = 2
                    elif self.map.var.movementJ4 == 2:
                        self.map.var.movementJ4 = 3
                    elif self.map.var.movementJ4 == 3:
                        self.map.var.movementJ4 = 0
            elif self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] != 0 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] != 2 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] != 4 :
                if self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] - 2][self.map.findJoueur(4)[2]] != 4 and self.map.Map1[self.map.findJoueur(4)[1] - 2][self.map.findJoueur(4)[2]] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(4)[1] - 2][self.map.findJoueur(4)[2]] == 1 or self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1]): 
                    self.mouvement.moveTop(9, 94)
                    self.map.var.posJ4 = 0
                    if self.map.var.movementJ4 == 0:
                        self.map.var.movementJ4 = 1
                    elif self.map.var.movementJ4 == 1:
                        self.map.var.movementJ4 = 2
                    elif self.map.var.movementJ4 == 2:
                        self.map.var.movementJ4 = 3
                    elif self.map.var.movementJ4 == 3:
                        self.map.var.movementJ4 = 0
            elif self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] != 0 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] != 2 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] != 4 :
                if self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] + 1] != 4  and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 2] != 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 2] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 2] == 1 or self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] + 1]): 
                    self.mouvement.moveRight(9, 94)
                    self.map.var.posJ4 = 3
                    if self.map.var.movementJ4 == 0:
                        self.map.var.movementJ4 = 1
                    elif self.map.var.movementJ4 == 1:
                        self.map.var.movementJ4 = 2
                    elif self.map.var.movementJ4 == 2:
                        self.map.var.movementJ4 = 3
                    elif self.map.var.movementJ4 == 3:
                        self.map.var.movementJ4 = 0
            elif self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] != 0 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] != 2 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] != 4 :
                if self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1] != 4  and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 2] != 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 2] not in self.map.var.listeBombeJ and (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 2] == 1 or self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1]): 
                    self.mouvement.moveLeft(9, 94)
                    self.map.var.posJ4 = 2
                    if self.map.var.movementJ4 == 0:
                        self.map.var.movementJ4 = 1
                    elif self.map.var.movementJ4 == 1:
                        self.map.var.movementJ4 = 2
                    elif self.map.var.movementJ4 == 2:
                        self.map.var.movementJ4 = 3
                    elif self.map.var.movementJ4 == 3:
                        self.map.var.movementJ4 = 0

        elif self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2]] == 9 :
            if self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] == 0 or self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] == 0 or self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] == 0 or self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] == 0:
                if self.map.var.bombeJ1 == "pyke" :
                    self.bombe.posePikeBombe(9, 94)
                else :
                    self.bombe.poseBombe(9, 94)
            elif (self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] == 4 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] == 1) or (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] == 1) or (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] == 1):
                self.mouvement.moveTop(9, 94)
                self.map.var.posJ4 = 0
                if self.map.var.movementJ4 == 0:
                    self.map.var.movementJ4 = 1
                elif self.map.var.movementJ4 == 1:
                    self.map.var.movementJ4 = 2
                elif self.map.var.movementJ4 == 2:
                    self.map.var.movementJ4 = 3
                elif self.map.var.movementJ4 == 3:
                    self.map.var.movementJ4 = 0
            elif (self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] == 4 and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] == 1) or (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] == 1) or (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] == 1):
                self.mouvement.moveDown(9, 94)
                self.map.var.posJ4 = 1
                if self.map.var.movementJ4 == 0:
                    self.map.var.movementJ4 = 1
                elif self.map.var.movementJ4 == 1:
                    self.map.var.movementJ4 = 2
                elif self.map.var.movementJ4 == 2:
                    self.map.var.movementJ4 = 3
                elif self.map.var.movementJ4 == 3:
                    self.map.var.movementJ4 = 0
            elif (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] == 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] == 1) or  (self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] == 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] == 1) or (self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] == 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] == 1):
                self.mouvement.moveLeft(9, 94)
                self.map.var.posJ4 = 2
                if self.map.var.movementJ4 == 0:
                    self.map.var.movementJ4 = 1
                elif self.map.var.movementJ4 == 1:
                    self.map.var.movementJ4 = 2
                elif self.map.var.movementJ4 == 2:
                    self.map.var.movementJ4 = 3
                elif self.map.var.movementJ4 == 3:
                    self.map.var.movementJ4 = 0
            elif (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] == 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] == 1) or (self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] == 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] == 1) or (self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] == 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] == 1):
                self.mouvement.moveRight(9, 94)
                self.map.var.posJ4 = 3
                if self.map.var.movementJ4 == 0:
                    self.map.var.movementJ4 = 1
                elif self.map.var.movementJ4 == 1:
                    self.map.var.movementJ4 = 2
                elif self.map.var.movementJ4 == 2:
                    self.map.var.movementJ4 = 3
                elif self.map.var.movementJ4 == 3:
                    self.map.var.movementJ4 = 0
            else :
                ia = random()
                if ia < 0.25 :
                    if (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] == 1 or self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 1] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 2] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] + 2] != 4):
                        if self.map.var.stateJ4 == "skull" :
                            self.mouvement.moveLeft(9, 94)
                            self.map.var.posJ4 = 2
                            if self.map.var.movementJ4 == 0:
                                self.map.var.movementJ4 = 1
                            elif self.map.var.movementJ4 == 1:
                                self.map.var.movementJ4 = 2
                            elif self.map.var.movementJ4 == 2:
                                self.map.var.movementJ4 = 3
                            elif self.map.var.movementJ4 == 3:
                                self.map.var.movementJ4 = 0
                        else :
                            self.mouvement.moveRight(9, 94)
                            self.map.var.posJ4 = 3
                            if self.map.var.movementJ4 == 0:
                                self.map.var.movementJ4 = 1
                            elif self.map.var.movementJ4 == 1:
                                self.map.var.movementJ4 = 2
                            elif self.map.var.movementJ4 == 2:
                                self.map.var.movementJ4 = 3
                            elif self.map.var.movementJ4 == 3:
                                self.map.var.movementJ4 = 0

                elif ia >= 0.25  and ia < 0.5:
                    if (self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 1] == 1 or self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2 - 1]] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 2] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1]][self.map.findJoueur(4)[2] - 2] != 4):
                        if self.map.var.stateJ4 == "skull" :
                            self.mouvement.moveRight(9, 94)
                            self.map.var.posJ4 = 3
                            if self.map.var.movementJ4 == 0:
                                self.map.var.movementJ4 = 1
                            elif self.map.var.movementJ4 == 1:
                                self.map.var.movementJ4 = 2
                            elif self.map.var.movementJ4 == 2:
                                self.map.var.movementJ4 = 3
                            elif self.map.var.movementJ4 == 3:
                                self.map.var.movementJ4 = 0
                        else :
                            self.mouvement.moveLeft(9, 94)
                            self.map.var.posJ4 = 2
                            if self.map.var.movementJ4 == 0:
                                self.map.var.movementJ4 = 1
                            elif self.map.var.movementJ4 == 1:
                                self.map.var.movementJ4 = 2
                            elif self.map.var.movementJ4 == 2:
                                self.map.var.movementJ4 = 3
                            elif self.map.var.movementJ4 == 3:
                                self.map.var.movementJ4 = 0
                
                elif ia >= 0.5 and ia < 0.75:
                    if (self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] == 1 or self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2]] in self.map.var.listePowerUp) and (self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] - 2][self.map.findJoueur(4)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] - 1][self.map.findJoueur(4)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] - 2][self.map.findJoueur(4)[2]] != 4):
                        if self.map.var.stateJ4 == "skull" :
                            self.mouvement.moveDown(9, 94)
                            self.map.var.posJ4 = 1
                            if self.map.var.movementJ4 == 0:
                                self.map.var.movementJ4 = 1
                            elif self.map.var.movementJ4 == 1:
                                self.map.var.movementJ4 = 2
                            elif self.map.var.movementJ4 == 2:
                                self.map.var.movementJ4 = 3
                            elif self.map.var.movementJ4 == 3:
                                self.map.var.movementJ4 = 0
                        else :
                            self.mouvement.moveTop(9, 94)
                            self.map.var.posJ4 = 0
                            if self.map.var.movementJ4 == 0:
                                self.map.var.movementJ4 = 1
                            elif self.map.var.movementJ4 == 1:
                                self.map.var.movementJ4 = 2
                            elif self.map.var.movementJ4 == 2:
                                self.map.var.movementJ4 = 3
                            elif self.map.var.movementJ4 == 3:
                                self.map.var.movementJ4 = 0

                
                else :
                    if self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2]] == 1 and (self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] + 1] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 2][self.map.findJoueur(4)[2]] not in self.map.var.listeBombeJ and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] - 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] + 1][self.map.findJoueur(4)[2] + 1] != 4 and self.map.Map1[self.map.findJoueur(4)[1] + 2][self.map.findJoueur(4)[2]] != 4):
                        if self.map.var.stateJ4 == "skull" :
                            self.mouvement.moveTop(9, 94)
                            self.map.var.posJ4 = 0
                            if self.map.var.movementJ4 == 0:
                                self.map.var.movementJ4 = 1
                            elif self.map.var.movementJ4 == 1:
                                self.map.var.movementJ4 = 2
                            elif self.map.var.movementJ4 == 2:
                                self.map.var.movementJ4 = 3
                            elif self.map.var.movementJ4 == 3:
                                self.map.var.movementJ4 = 0
                        else :
                            self.mouvement.moveDown(9, 94)
                            self.map.var.posJ4 = 1
                            if self.map.var.movementJ4 == 0:
                                self.map.var.movementJ4 = 1
                            elif self.map.var.movementJ4 == 1:
                                self.map.var.movementJ4 = 2
                            elif self.map.var.movementJ4 == 2:
                                self.map.var.movementJ4 = 3
                            elif self.map.var.movementJ4 == 3:
                                self.map.var.movementJ4 = 0

