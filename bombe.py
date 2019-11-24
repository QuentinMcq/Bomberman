from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from random import *
import os

class bombe(QWidget) :
    def __init__(self, Map) :
        super(bombe, self).__init__()
        self.map = Map
    
    def poseBombe(self, n, nb):
        if self.map.var.checkbombe(n) != self.map.var.allowedBomb(n):
            for i in range(len(self.map.Map1)):
                for j in range(len(self.map.Map1[i])):
                    if self.map.Map1[i][j] == n:
                        self.map.Map1[i][j] = nb
                        self.map.var.addBomb(n)
                        i1 = i
                        j1 = j
                        self.map.update()

                        def explosion():
                            stopDroite = False
                            stopGauche = False
                            stopBas = False
                            stopHaut = False
                            k = 1
                            while k < self.map.var.range(n) + 1 and k != self.map.var.MAXFIRE and not stopDroite:
                                if self.map.Map1[i1][j1 + k] == 2:
                                    stopDroite = True
                                    break

                                if self.map.Map1[i1][j1 + k] == 0 or self.map.Map1[i1][j1 + k] in self.map.var.listePowerUp or self.map.Map1[i1][j1 + k] == 4 or self.map.Map1[i1][j1 + k] in self.map.var.listeBombeJ or self.map.Map1[i1][j1 + k] in self.map.var.listeJoueur:

                                    if self.map.Map1[i1][j1 + k] in self.map.var.listeJoueur:
                                        if self.map.Map1[i1][j1 + k] == 8:
                                            self.map.var.gainPointKill(n, 8)

                                        if self.map.Map1[i1][j1 + k] == 7:
                                            self.map.var.gainPointKill(n, 7)

                                        if self.map.Map1[i1][j1 + k] == 9:
                                            self.map.var.gainPointKill(n, 9)

                                        if self.map.Map1[i1][j1 + k] == 3:
                                            self.map.var.gainPointKill(n, 3)
                                    powerup = -1
                                    if self.map.Map1[i1][j1 + k] == 0:
                                        powerup = random()
                                    self.map.Map1[i1][j1 + k] = 1
                                    self.map.Map1[i1][j1] = 1
                                    stopDroite = True
                                    if powerup > 0.4 and powerup <= 0.6:
                                        choix = random()
                                        if choix < 0.45:
                                            self.map.Map1[i1][j1 + k] = 6.1
                                        elif choix > 0.45 and choix <= 0.55:
                                            self.map.Map1[i1][j1 + k] = 6.2
                                        elif choix > 0.55 and choix <= 0.775:
                                            self.map.Map1[i1][j1 + k] = 6.4
                                        elif choix > 0.775 and choix <= 0.90:
                                            self.map.Map1[i1][j1 + k] = 6.6
                                        elif choix > 0.90 and choix <= 0.95:
                                            self.map.Map1[i1][j1 + k] = 6.5
                                        elif choix > 0.95:
                                            self.map.Map1[i1][j1 + k] = 6.3
                                    self.map.var.gainPoint(n)
                                k += 1

                            k = 1
                            while k < self.map.var.range(n) + 1 and k != self.map.var.MAXFIRE and not stopGauche:
                                if self.map.Map1[i1][j1 - k] == 2:
                                    stopGauche = True
                                    break

                                if self.map.Map1[i1][j1 - k] == 4 or self.map.Map1[i1][j1 - k] in self.map.var.listeBombeJ or self.map.Map1[i1][j1 - k] == 0 or self.map.Map1[i1][j1 - k] in self.map.var.listePowerUp or self.map.Map1[i1][j1 - k] in self.map.var.listeJoueur:

                                    if self.map.Map1[i1][j1 - k] == 8:
                                        self.map.var.gainPointKill(n, 8)

                                    if self.map.Map1[i1][j1 - k] == 7:
                                        self.map.var.gainPointKill(n, 7)

                                    if self.map.Map1[i1][j1 - k] == 3:
                                        self.map.var.gainPointKill(n, 3)

                                    if self.map.Map1[i1][j1 - k] == 9:
                                        self.map.var.gainPointKill(n, 9)
                                    powerup = -1
                                    if self.map.Map1[i1][j1 - k] == 0:
                                        powerup = random()
                                    self.map.Map1[i1][j1 - k] = 1
                                    self.map.Map1[i1][j1] = 1
                                    stopGauche = True
                                    if powerup > 0.4 and powerup <= 0.6:
                                        choix = random()
                                        if choix < 0.45:
                                            self.map.Map1[i1][j1 - k] = 6.1
                                        elif choix > 0.45 and choix <= 0.55:
                                            self.map.Map1[i1][j1 - k] = 6.2
                                        elif choix > 0.55 and choix <= 0.775:
                                            self.map.Map1[i1][j1 - k] = 6.4
                                        elif choix > 0.775 and choix <= 0.90:
                                            self.map.Map1[i1][j1 - k] = 6.6
                                        elif choix > 0.90 and choix <= 0.95:
                                            self.map.Map1[i1][j1 - k] = 6.5
                                        elif choix > 0.95:
                                            self.map.Map1[i1][j1 - k] = 6.3
                                    self.map.var.gainPoint(n)
                                k += 1

                            k = 1
                            while k < self.map.var.range(n) + 1 and k != self.map.var.MAXFIRE and not stopBas:
                                if self.map.Map1[i1 + k][j1] == 2:
                                    stopBas = True
                                    break
                                if self.map.Map1[i1 + k][j1] == 4 or self.map.Map1[i1 + k][j1] in self.map.var.listeBombeJ or self.map.Map1[i1 + k][j1] == 0 or self.map.Map1[i1 + k][j1] in self.map.var.listePowerUp or self.map.Map1[i1 + k][j1] in self.map.var.listeJoueur:

                                    if self.map.Map1[i1 + k][j1] == 9:
                                        self.map.var.gainPointKill(n, 9)

                                    if self.map.Map1[i1 + k][j1] == 8:
                                        self.map.var.gainPointKill(n, 8)

                                    if self.map.Map1[i1 + k][j1] == 3:
                                        self.map.var.gainPointKill(n, 3)

                                    if self.map.Map1[i1 + k][j1] == 7:
                                        self.map.var.gainPointKill(n, 7)
                                    powerup = -1
                                    if self.map.Map1[i1 + 1][j1] == 0:
                                        powerup = random()
                                    self.map.Map1[i1 + k][j1] = 1
                                    self.map.Map1[i1][j1] = 1
                                    stopBas = True
                                    if powerup > 0.4 and powerup <= 0.6:
                                        choix = random()
                                        if choix < 0.45:
                                            self.map.Map1[i1 + k][j1] = 6.1
                                        elif choix > 0.45 and choix <= 0.55:
                                            self.map.Map1[i1 + k][j1] = 6.2
                                        elif choix > 0.55 and choix <= 0.775:
                                            self.map.Map1[i1 + k][j1] = 6.4
                                        # elif choix > 0.775 and choix <= 0.90:
                                        #   self.map.Map1[i1 + k][j1] = 6.6
                                        elif choix > 0.90 and choix <= 0.95:
                                            self.map.Map1[i1 + k][j1] = 6.5
                                        elif choix > 0.95:
                                            self.map.Map1[i1 + k][j1] = 6.3
                                    self.map.var.gainPoint(n)
                                k += 1

                            k = 1
                            while k < self.map.var.range(n) + 1 and k != self.map.var.MAXFIRE and not stopHaut:
                                if self.map.Map1[i1 - k][j1] == 2:
                                    stopHaut = True
                                    break
                                if self.map.Map1[i1 - k][j1] == 0 or self.map.Map1[i1 - k][j1] in self.map.var.listePowerUp or self.map.Map1[i1 - k][j1] in self.map.var.listeJoueur or self.map.Map1[i1 - k][j1] in self.map.var.listeBombeJ:
                                    if self.map.Map1[i1 - k][j1] == 7:
                                        self.map.var.gainPointKill(n, 7)

                                    if self.map.Map1[i1 - k][j1] == 8:
                                        self.map.var.gainPointKill(n, 8)

                                    if self.map.Map1[i1 - k][j1] == 3:
                                        self.map.var.gainPointKill(n, 3)

                                    if self.map.Map1[i1 - k][j1] == 9:
                                        self.map.var.gainPointKill(n, 9)
                                    powerup = -1
                                    if self.map.Map1[i1 - k][j1] == 0:
                                        powerup = random()
                                    self.map.Map1[i1 - k][j1] = 1
                                    self.map.Map1[i1][j1] = 1
                                    stopHaut = True
                                    powerup = random()
                                    if powerup > 0.4 and powerup <= 0.6:
                                        choix = random()
                                        if choix < 0.45:
                                            self.map.Map1[i1 - k][j1] = 6.1
                                        elif choix > 0.45 and choix <= 0.55:
                                            self.map.Map1[i1 - k][j1] = 6.2
                                        elif choix > 0.55 and choix <= 0.775:
                                            self.map.Map1[i1 - k][j1] = 6.4
                                        elif choix > 0.775 and choix <= 0.90:
                                            self.map.Map1[i1 - k][j1] = 6.6
                                        elif choix > 0.90 and choix <= 0.95:
                                            self.map.Map1[i1 - k][j1] = 6.5
                                        elif choix > 0.95:
                                            self.map.Map1[i1 - k][j1] = 6.3
                                    self.map.var.gainPoint(n)
                                k += 1

                            if self.map.Map1[i1][j1] == nb:
                                self.map.Map1[i1][j1] = 1

                            self.map.Map1[i1][j1] = 1
                            self.map.var.removeBomb(n)
                            self.map.updateScore()
                            self.map.update()
                            test1 = QMediaPlaylist(self)
                            test = QUrl.fromLocalFile(os.getcwd() + "/Musiques/explosion.wav")
                            test1.addMedia(QMediaContent(test))
                            test2 = QMediaPlayer(self)
                            test2.setPlaylist(test1)
                            test2.play()

                        timer = QTimer(self)
                        timer.timeout.connect(explosion)
                        timer.setSingleShot(True)
                        timer.start(3000)

    # Et celle la une pyke bombe

    def posePikeBombe(self, n, nb):
        if self.map.var.checkbombe(n) != self.map.var.allowedBomb(n):
            for i in range(len(self.map.Map1)):
                for j in range(len(self.map.Map1[i])):
                    if self.map.Map1[i][j] == n:
                        self.map.Map1[i][j] = nb
                        self.map.var.addBomb(n)
                        self.map.update()
                        i1 = i
                        j1 = j

                        def explosion():
                            stopDroite = False
                            stopGauche = False
                            stopBas = False
                            stopHaut = False
                            k = 1
                            while k < self.map.var.range(n) + 1 and k != self.map.var.MAXFIRE and not stopDroite:
                                if self.map.Map1[i1][j1 + k] == 2:
                                    stopDroite = True
                                    break

                                if self.map.Map1[i1][j1 + k] == 0 or self.map.Map1[i1][j1 + k] == 6.2 or self.map.Map1[i1][j1 + k] == 6.1 or self.map.Map1[i1][j1 + k] == 4 or self.map.Map1[i1][j1 + k] == 34 or self.map.Map1[i1][j1 + k] == 74 or self.map.Map1[i1][j1 + k] == 84 or self.map.Map1[i1][j1 + k] == 94 or self.map.Map1[i1][j1 + k] == 7 or self.map.Map1[i1][j1 + k] == 8 or self.map.Map1[i1][j1 + k] == 9 or self.map.Map1[i1][j1 + k] == 3:

                                    if self.map.Map1[i1][j1 + k] == 7 or self.map.Map1[i1][j1 + k] == 8 or self.map.Map1[i1][j1 + k] == 9 or self.map.Map1[i1][j1 + k] == 3:
                                        if self.map.Map1[i1][j1 + k] == 8:
                                            self.map.var.gainPointKill(n, 8)

                                        if self.map.Map1[i1][j1 + k] == 7:
                                            self.map.var.gainPointKill(n, 7)

                                        if self.map.Map1[i1][j1 + k] == 9:
                                            self.map.var.gainPointKill(n, 9)

                                        if self.map.Map1[i1][j1 + k] == 3:
                                            self.map.var.gainPointKill(n, 3)
                                    powerup = -1
                                    if self.map.Map1[i1][j1 + k] == 0:
                                        powerup = random()
                                    self.map.Map1[i1][j1 + k] = 1
                                    self.map.Map1[i1][j1] = 1
                                    if powerup > 0.4 and powerup <= 0.6:
                                        choix = random()
                                        if choix < 0.45:
                                            self.map.Map1[i1][j1 + k] = 6.1
                                        elif choix > 0.45 and choix <= 0.55:
                                            self.map.Map1[i1][j1 + k] = 6.2
                                        elif choix > 0.55 and choix <= 0.775:
                                            self.map.Map1[i1][j1 + k] = 6.4
                                        elif choix > 0.775 and choix <= 0.90:
                                            self.map.Map1[i1][j1 + k] = 6.6
                                        elif choix > 0.90 and choix <= 0.95:
                                            self.map.Map1[i1][j1 + k] = 6.5
                                        elif choix > 0.95:
                                            self.map.Map1[i1][j1 + k] = 6.3
                                    self.map.var.gainPoint(n)
                                k += 1

                            k = 1
                            while k < self.map.var.range(n) + 1 and k != self.map.var.MAXFIRE and not stopGauche:
                                if self.map.Map1[i1][j1 - k] == 2:
                                    stopGauche = True
                                    break

                                if self.map.Map1[i1][j1 - k] == 4 or self.map.Map1[i1][j1 - k] == 34 or self.map.Map1[i1][j1 - k] == 74 or self.map.Map1[i1][j1 - k] == 84 or self.map.Map1[i1][j1 - k] == 94 or self.map.Map1[i1][j1 - k] == 0 or self.map.Map1[i1][j1 - k] == 6.1 or self.map.Map1[i1][j1 - k] == 6.2 or self.map.Map1[i1][j1 - k] == 7 or self.map.Map1[i1][j1 - k] == 8 or self.map.Map1[i1][j1 - k] == 9 or self.map.Map1[i1][j1 - k] == 3:

                                    if self.map.Map1[i1][j1 - k] == 8:
                                        self.map.var.gainPointKill(n, 8)

                                    if self.map.Map1[i1][j1 - k] == 7:
                                        self.map.var.gainPointKill(n, 7)

                                    if self.map.Map1[i1][j1 - k] == 3:
                                        self.map.var.gainPointKill(n, 3)

                                    if self.map.Map1[i1][j1 - k] == 9:
                                        self.map.var.gainPointKill(n, 9)
                                    powerup = -1
                                    if self.map.Map1[i1][j1 - k] == 0:
                                        powerup = random()
                                    self.map.Map1[i1][j1 - k] = 1
                                    self.map.Map1[i1][j1] = 1
                                    if powerup > 0.4 and powerup <= 0.6:
                                        choix = random()
                                        if choix < 0.45:
                                            self.map.Map1[i1][j1 - k] = 6.1
                                        elif choix > 0.45 and choix <= 0.55:
                                            self.map.Map1[i1][j1 - k] = 6.2
                                        elif choix > 0.55 and choix <= 0.775:
                                            self.map.Map1[i1][j1 - k] = 6.4
                                        elif choix > 0.775 and choix <= 0.90:
                                            self.map.Map1[i1][j1 - k] = 6.6
                                        elif choix > 0.90 and choix <= 0.95:
                                            self.map.Map1[i1][j1 - k] = 6.5
                                        elif choix > 0.95:
                                            self.map.Map1[i1][j1 - k] = 6.3
                                    self.map.var.gainPoint(n)
                                k += 1

                            k = 1
                            while k < self.map.var.range(n) + 1 and k != self.map.var.MAXFIRE and not stopBas:
                                if self.map.Map1[i1 + k][j1] == 2:
                                    stopBas = True
                                    break
                                if self.map.Map1[i1 + k][j1] == 4 or self.map.Map1[i1 + k][j1] == 34 or self.map.Map1[i1 + k][j1] == 74 or self.map.Map1[i1 + k][j1] == 84 or self.map.Map1[i1 + k][j1] == 94 or self.map.Map1[i1 + k][j1] == 0 or self.map.Map1[i1 + k][j1] == 6.1 or self.map.Map1[i1 + k][j1] == 6.2 or self.map.Map1[i1 + k][j1] == 7 or self.map.Map1[i1 + k][j1] == 8 or self.map.Map1[i1 + k][j1] == 9 or self.map.Map1[i1 + k][j1] == 3:

                                    if self.map.Map1[i1 + k][j1] == 9:
                                        self.map.var.gainPointKill(n, 9)

                                    if self.map.Map1[i1 + k][j1] == 8:
                                        self.map.var.gainPointKill(n, 8)

                                    if self.map.Map1[i1 + k][j1] == 3:
                                        self.map.var.gainPointKill(n, 3)

                                    if self.map.Map1[i1 + k][j1] == 7:
                                        self.map.var.gainPointKill(n, 7)
                                    powerup = -1
                                    if self.map.Map1[i1 + 1][j1] == 0:
                                        powerup = random()
                                    self.map.Map1[i1 + k][j1] = 1
                                    self.map.Map1[i1][j1] = 1

                                    if powerup > 0.4 and powerup <= 0.6:
                                        choix = random()
                                        if choix < 0.45:
                                            self.map.Map1[i1 + k][j1] = 6.1
                                        elif choix > 0.45 and choix <= 0.55:
                                            self.map.Map1[i1 + k][j1] = 6.2
                                        elif choix > 0.55 and choix <= 0.775:
                                            self.map.Map1[i1 + k][j1] = 6.4
                                        elif choix > 0.775 and choix <= 0.90:
                                            self.map.Map1[i1 + k][j1] = 6.6
                                        elif choix > 0.90 and choix <= 0.95:
                                            self.map.Map1[i1 + k][j1] = 6.5
                                        elif choix > 0.95:
                                            self.map.Map1[i1 + k][j1] = 6.3
                                    self.map.var.gainPoint(n)
                                k += 1

                            k = 1
                            while k < self.map.var.range(n) + 1 and k != self.map.var.MAXFIRE and not stopHaut:
                                if self.map.Map1[i1 - k][j1] == 2:
                                    stopHaut = True
                                    break
                                if self.map.Map1[i1 - k][j1] == 0 or self.map.Map1[i1 - k][j1] == 6.2 or self.map.Map1[i1 - k][j1] == 6.1 or self.map.Map1[i1 - k][j1] == 7 or self.map.Map1[i1 - k][j1] == 8 or self.map.Map1[i1 - k][j1] == 9 or self.map.Map1[i1 - k][j1] == 3:
                                    if self.map.Map1[i1 - k][j1] == 7 :
                                        self.map.var.gainPointKill(n, 7)

                                    if self.map.Map1[i1 - k][j1] == 8:
                                        self.map.var.gainPointKill(n, 8)

                                    if self.map.Map1[i1 - k][j1] == 3:
                                        self.map.var.gainPointKill(n, 3)

                                    if self.map.Map1[i1 - k][j1] == 9:
                                        self.map.var.gainPointKill(n, 9)
                                    powerup = -1
                                    if self.map.Map1[i1 - k][j1] == 0:
                                        powerup = random()
                                    self.map.Map1[i1 - k][j1] = 1
                                    self.map.Map1[i1][j1] = 1
                                    powerup = random()
                                    if powerup > 0.4 and powerup <= 0.6:
                                        choix = random()
                                        if choix < 0.225:
                                            self.map.Map1[i1 - k][j1] = 6.1
                                        elif choix > 0.225 and choix <= 0.45:
                                            self.map.Map1[i1 - k][j1] = 6.2
                                        elif choix > 0.45 and choix <= 0.675:
                                            self.map.Map1[i1 - k][j1] = 6.4
                                        elif choix > 0.675 and choix <= 0.90:
                                            self.map.Map1[i1 - k][j1] = 6.6
                                        elif choix > 0.90 and choix <= 0.95:
                                            self.map.Map1[i1 - k][j1] = 6.5
                                        elif choix > 0.95:
                                            self.map.Map1[i1 - k][j1] = 6.3
                                    self.map.var.gainPoint(n)
                                k += 1

                            if self.map.Map1[i1][j1] == nb:
                                self.map.Map1[i1][j1] = 1

                            self.map.Map1[i1][j1] = 1
                            self.map.var.removeBomb(n)
                            self.map.updateScore()
                            self.map.update()
                            test1 = QMediaPlaylist(self)
                            test = QUrl.fromLocalFile(os.getcwd() + "/Musiques/explosion.wav")
                            test1.addMedia(QMediaContent(test))
                            test2 = QMediaPlayer(self)
                            test2.setPlaylist(test1)
                            test2.play()

                        timer = QTimer(self)
                        timer.timeout.connect(explosion)
                        timer.setSingleShot(True)
                        timer.start(3000)