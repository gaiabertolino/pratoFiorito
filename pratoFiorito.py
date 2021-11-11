import pygame
from pygame import *
from random import *
font.init()
font = font.SysFont("Times New Roman", 30)

##funzione che inizializza la matrice nascosta celle e la matrice stato che verrà in seguito aggiornata per indicare le caselle da scoprire
#restituisce la matrice stato o la matrice celle in base al terzo argomento
def inizializza(righe,colonne,numMine,risultato):
    stato = emptyMatrix(righe,colonne)
    celle = emptyMatrix(righe,colonne)
    posizionaMine(celle,numMine)
    for i in range(righe):
        for j in range(colonne):
            if celle[i][j] != -1:
                celleVicine = vicini(celle,(i,j))
                num = 0
                for(x,y) in celleVicine:
                    if celle[x][y] == -1:
                        num += 1
                celle[i][j] = num
    if risultato == "stato":
        return stato
    else:
        return celle
    
def imitMatrix(r,c,v):
    m = [[v]*c for i in range(r)]
    return m
    
def emptyMatrix(r,c):
    return imitMatrix(r,c,0)


def vicini(m,pos):
    r = pos[0]
    c = pos[1]
    v = []
    ultimaRiga = len(m) - 1
    ultimaCol = len(m[0]) -1
    i = max(0,r-1)
    while i <= r+1 and i <= ultimaRiga:
        j = max(0,c-1)
        while j <= c+1 and j <= ultimaCol:
            if (i,j) != (r,c):
                v.append((i,j))
            j += 1
        i += 1
    return v

##funzione legata a inizializza() che posiziona le mine nella matrice
def posizionaMine(matrix,numMine):
    mineAsseg = 0
    while mineAsseg < numMine:
        i = randint(0,len(matrix)-1)
        j = randint(0,len(matrix)-1)
        if matrix[i][j] != -1:
            matrix[i][j] = -1
            mineAsseg += 1

## funzione che cambia la corrispettiva casella di stato rispetto alla matrice celle in 1 se in celle è -1 (una bomba) o maggiore di 0
## nel caso in cui è 0, non solo la cella con lo 0 cambia la corrispettiva cella in stato in 1 ma anche quelle dei vicini
## diventano 1 (cioè sono da scoprire) se contengo un numero maggiore di 0
def scopri(r,c,stato):
    if celle[r][c] == -1 or celle[r][c] > 0:
        stato [r][c] = 1
    else:
        coppie = [(r,c)]
        while len(coppie) > 0:
            (r,c) = coppie.pop()
            stato[r][c] = 1
            celleVicine = vicini(celle,(r,c))
            for (x,y) in celleVicine:
                    if celle[x][y] >= 0:
                        stato[x][y] = 1
    return stato

## le due funzioni successive restituiscono le posizioni delle celle in base al click dell'utente
# valgono per la modalità facile con matrice 4x4
def coordinataXFacile(x):
    if 300 < x <= 400:
        xCella = 0
    elif 400 < x <= 500:
        xCella = 1
    elif 500 < x <= 600:
        xCella = 2
    elif 600 < x <= 700:
        xCella = 3
    return xCella

def coordinataYFacile(y):
    if 50 < y <= 150:
        yCella = 0
    elif 150 < y <= 250:
        yCella = 1
    elif 250 < y <= 350:
        yCella = 2
    elif 350 < y <= 450:
        yCella = 3
    return yCella

##le due funzioni successive indicano il punto di partenza per la copiatura della Surface sul mainScreen
# valgono per la modalità facile con matrice 4x4
def copiaturaXFacile(xCella):
    coorX = 300
    if xCella == 1:
        coorX = 400
    elif xCella == 2:
        coorX = 500
    elif xCella == 3:
        coorX = 600
    return coorX

def copiaturaYFacile(yCella):
    coorY = 50
    if yCella == 1:
        coorY = 150
    elif yCella == 2:
        coorY = 250
    elif yCella == 3:
        coorY = 350
    return coorY

## la funzione restituisce l'immagine corrispondente al contenuto di ciascuna cella
# vale per la modalità facile con matrice 4x4
def immagineCorrispondenteFacile(x,y):
    if celle[x][y] == -1:
        mostra = image.load('bomba.png')
    elif celle[x][y] == 0:
        mostra = image.load('zero.png')
    elif celle[x][y] == 1:
        mostra = image.load('uno.png')
    elif celle[x][y] == 2:
        mostra = image.load('due.png')
    elif celle[x][y] == 3:
        mostra = image.load('tre.png')
    elif celle[x][y] == 4:
        mostra = image.load('quattro.png')
    elif celle[x][y] == 5:
        mostra = image.load('cinque.png')
    elif celle[x][y] == 6:
        mostra = image.load('sei.png')
    elif celle[x][y] == 7:
        mostra = image.load('sette.png')
    else:
        mostra = image.load('otto.png')
    return mostra

## le due funzioni successive restituiscono le posizioni delle celle in base al click dell'utente
# valgono per la modalità difficile con matrice 8x8
def coordinataXDifficile(x):
    if 300 < x <= 350:
        xCella = 0
    elif 350 < x <= 400:
        xCella = 1
    elif 400 < x <= 450:
        xCella = 2
    elif 450 < x <= 500:
        xCella = 3
    elif 500 < x <= 550:
        xCella = 4
    elif 550 < x <= 600:
        xCella = 5
    elif 600 < x <= 650:
        xCella = 6
    elif 650 < x <= 700:
        xCella = 7  
    return xCella

def coordinataYDifficile(y):
    if 50 < y <= 100:
        yCella = 0
    elif 100 < y <= 150:
        yCella = 1
    elif 150 < y <= 200:
        yCella = 2
    elif 200 < y <= 250:
        yCella = 3
    elif 250 < y <= 300:
        yCella = 4
    elif 300 < y <= 350:
        yCella = 5
    elif 350 < y <= 400:
        yCella = 6
    elif 400 < y <= 450:
        yCella = 7
    return yCella

##le due funzioni successive indicano il punto di partenza per la copiatura della Surface sul mainScreen
# valgono per la modalità difficile con matrice 8x8
def copiaturaXDifficile(xCella):
    coorX = 300
    if xCella == 1:
        coorX = 350
    elif xCella == 2:
        coorX = 400
    elif xCella == 3:
        coorX = 450
    elif xCella == 4:
        coorX = 500
    elif xCella == 5:
        coorX = 550
    elif xCella == 6:
        coorX = 600
    elif xCella == 7:
        coorX = 650
    return coorX

def copiaturaYDifficile(yCella):
    coorY = 50
    if yCella == 1:
        coorY = 100
    elif yCella == 2:
        coorY = 150
    elif yCella == 3:
        coorY = 200
    elif yCella == 4:
        coorY = 250
    elif yCella == 5:
        coorY = 300
    elif yCella == 6:
        coorY = 350
    elif yCella == 7:
        coorY = 400
    return coorY

## la funzione restituisce l'immagine corrispondente al contenuto di ciascuna cella
# vale per la modalità difficile con matrice 8x8
def immagineCorrispondenteDifficile(x,y):
    if celle[x][y] == -1:
        mostra = image.load('bombaDiff.png')
    elif celle[x][y] == 0:
        mostra = image.load('zeroDiff.png')
    elif celle[x][y] == 1:
        mostra = image.load('unoDiff.png')
    elif celle[x][y] == 2:
        mostra = image.load('dueDiff.png')
    elif celle[x][y] == 3:
        mostra = image.load('treDiff.png')
    elif celle[x][y] == 4:
        mostra = image.load('quattroDiff.png')
    elif celle[x][y] == 5:
        mostra = image.load('cinqueDiff.png')
    elif celle[x][y] == 6:
        mostra = image.load('seiDiff.png')
    elif celle[x][y] == 7:
        mostra = image.load('setteDiff.png')
    else:
        mostra = image.load('ottoDiff.png')
    return mostra
##creo un ciclo infinito di while per far funzionare il gioco fino all'interruzione da parte dell'utente
index = 0
while index != 1:
    ##creo la finestra di scelta iniziale
    init()
    mainScreen = display.set_mode((1000,500))
    mainScreen.fill((128,128,128))
    easy = image.load('Facile.png')
    mainScreen.blit(easy,(150,270))
    difficult = image.load('Difficile.png')
    mainScreen.blit(difficult,(550,270))
    benvenuto = image.load('benvenuto2.png')
    mainScreen.blit(benvenuto,(300,100))
    display.set_caption("Prato fiorito")
    display.update()

    ##per far fare una scelta all'utente metto windows in ascolto degli eventi
    scelta = False
    while not scelta:
        for ev in event.get():
            if ev.type == MOUSEBUTTONDOWN:
                x = ev.pos[0]
                y = ev.pos[1]
                if 150 < x < 450 and 270 < y < 370:
                    modalità = "facile"
                    scelta = True
                elif 550 < x < 850 and 270 < y < 370:
                    modalità = "difficile"
                    scelta = True


    ##creo i due ambienti di gioco in base alla scelta
                    
    ##modalità facile con matrice 4x4 e 3 bombe
    if modalità == "facile":
        stato = inizializza(4,4,3,"stato")
        celle = inizializza(4,4,3,"celle")
        finale = inizializza(4,4,3,"stato")
        mainScreen.fill((128,128,128))
        #creo la matrice coperta in grafica
        posy = 50
        for i in range(4):
            posx = 300
            for i in range(4):
                cella = image.load('coperta.png')
                mainScreen.blit(cella,(posx, posy))
                display.update()
                posx += 100
            posy += 100
        display.update()
        ##rimetto la finestra di windows in ascolto per ottenere le coordinate di ciascun clic
        #il ciclo successivo crea per ogni clic una matrice nuovostato che indica con 1 le celle da scoprire
        finito = False
        while not finito:
            for ev in event.get():
                if ev.type == MOUSEBUTTONDOWN:
                    x = ev.pos[0]
                    y = ev.pos[1]
                    if 300 < x < 700 and 50 < y < 450:
                        xCella = coordinataXFacile(x)
                        yCella = coordinataYFacile(y)
                        nuovostato = scopri(xCella,yCella,stato)
                        scoperte = 0
                        for i in range(4):
                            for j in range(4):
                                if nuovostato[i][j] == 1:
                                    scoperte += 1
                                    xCellaCop = i
                                    yCellaCop = j
                                    finale[i][j] = 1
                                    mainScreen.blit(immagineCorrispondenteFacile(xCellaCop,yCellaCop),(copiaturaXFacile(xCellaCop),copiaturaYFacile(yCellaCop)))
                                    display.update()
                        ##esito del gioco in base alla casella cliccata 
                        if celle[xCella][yCella] == -1:
                            mixer.music.load('pioggia.mp3')
                            mixer.music.play()
                            finito = True
                            perso = font.render("Hai trovato una bomba! Partita terminata", True, (255,255,255))
                            for i in range(4):
                                for j in range(4):
                                    if celle[i][j] == -1:
                                        mainScreen.blit(immagineCorrispondenteFacile(i,j),(copiaturaXFacile(i),copiaturaYFacile(j)))
                                    if celle[i][j] != -1:
                                        fioreBruciato = image.load('fioreBruciato.png')
                                        mainScreen.blit(fioreBruciato,(copiaturaXFacile(i),copiaturaYFacile(j)))
                            noncontinua = font.render("Per terminare premi un tasto", True, (122,0,92))
                            continua = font.render("Per una nuova partita clicca sullo schermo", True, (122,0,92))
                            mainScreen.blit(continua,(20,455))
                            mainScreen.blit(noncontinua,(600,455))
                            mainScreen.blit(perso, (250,10))
                            display.update()
                        elif scoperte == 13:
                            mixer.music.load('fioritura.mp3')
                            mixer.music.play()
                            finito = True
                            for i in range(4):
                                for j in range(4):
                                    fiore = image.load('fiore.png')
                                    mainScreen.blit(fiore,(copiaturaXFacile(i),copiaturaYFacile(j)))
                                        
                            vinto = font.render("Non hai trovato nessuna bomba! Hai vinto!", True, (255,255,255))
                            noncontinua = font.render("Per terminare premi un tasto", True, (122,0,92))
                            continua = font.render("Per una nuova partita clicca sullo schermo", True, (122,0,92))
                            mainScreen.blit(continua,(20,455))
                            mainScreen.blit(noncontinua,(600,455))
                            mainScreen.blit(vinto, (250,10))
                            display.update()

    ##modalità difficile con matrice 8x8 e 15 bombe
    if modalità == "difficile":
        stato = inizializza(8,8,15,"stato")
        celle = inizializza(8,8,15,"celle")
        mainScreen.fill((128,128,128))
        #creo la matrice coperta in grafica
        posy = 50
        for i in range(8):
            posx = 300
            for i in range(8):
                cella = image.load('copertaDiff.png')
                mainScreen.blit(cella,(posx, posy))
                display.update()
                posx += 50
            posy += 50
        display.update()
        ##rimetto la finestra di windows in ascolto per ottenere le coordinate di ciascun clic
        #il ciclo successivo crea per ogni clic una matrice nuovostato che indica con 1 le celle da scoprire
        finito = False
        while not finito:
            for ev in event.get():
                if ev.type == MOUSEBUTTONDOWN:
                    x = ev.pos[0]
                    y = ev.pos[1]
                    if 300 < x < 700 and 50 < y < 450:
                        xCella = coordinataXDifficile(x)
                        yCella = coordinataYDifficile(y)
                        nuovostato = scopri(xCella,yCella,stato)
                        scoperte = 0
                        for i in range(8):
                            for j in range(8):
                                if nuovostato[i][j] == 1:
                                    scoperte += 1
                                    xCellaCop = i
                                    yCellaCop = j
                                    mainScreen.blit(immagineCorrispondenteDifficile(xCellaCop,yCellaCop),(copiaturaXDifficile(xCellaCop),copiaturaYDifficile(yCellaCop)))
                                    display.update()
                        ##esito del gioco in base alla casella cliccata 
                        if celle[xCella][yCella] == -1:
                            finito = True
                            for i in range(8):
                                for j in range(8):
                                    if celle[i][j] == -1:
                                        mainScreen.blit(immagineCorrispondenteDifficile(i,j),(copiaturaXDifficile(i),copiaturaYDifficile(j)))
                                    elif celle[i][j] != -1:
                                        fioreBruciato = image.load('fioreBruciatoDiff.png')
                                        mainScreen.blit(fioreBruciato,(copiaturaXDifficile(i),copiaturaYDifficile(j)))
                            mixer.music.load('pioggia.mp3')
                            mixer.music.play()
                            perso = font.render("Hai trovato una bomba! Partita terminata", True, (255,255,255))
                            noncontinua = font.render("Per terminare premi un tasto", True, (122,0,92))
                            continua = font.render("Per una nuova partita clicca sullo schermo", True, (122,0,92))
                            mainScreen.blit(continua,(20,455))
                            mainScreen.blit(noncontinua,(600,455))
                            mainScreen.blit(perso, (250,10))
                            display.update()
                        elif scoperte == 49:
                            finito = True
                            for i in range(8):
                                for j in range(8):
                                    fiore = image.load('fioreDiff.png')
                                    mainScreen.blit(fiore,(copiaturaXDifficile(i),copiaturaYDifficile(j)))
                            mixer.music.load('fioritura.mp3')
                            mixer.music.play()
                            vinto = font.render("Non hai trovato nessuna bomba! Hai vinto!", True, (255,255,255))
                            noncontinua = font.render("Per terminare premi un tasto", True, (122,0,92))
                            continua = font.render("Per una nuova partita clicca sullo schermo", True, (122,0,92))
                            mainScreen.blit(continua,(20,455))
                            mainScreen.blit(noncontinua,(600,455))
                            mainScreen.blit(vinto, (250,10))
                            display.update()
    ##variabile booleana e ciclo che interrompe lo script se l'utente clicca un tasto qualsiasi della tastiera o lo riporta alla schermata iniziale se clicca sullo schermo
    ricomincia = False
    while not ricomincia:
        for ev in event.get():
            if ev.type == MOUSEBUTTONDOWN:
                ricomincia = True
            elif ev.type == KEYDOWN:
                quit()
                exit()
            
