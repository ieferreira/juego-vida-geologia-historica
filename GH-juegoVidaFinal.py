
import numpy as np
import pygame,sys, time, csv, datetime
import matplotlib.pyplot as plt
        
# este es un cambio para github!!
# para probar conexión
pygame.init()
historialCeldasVivas = []
width, height = 800,800

screen = pygame.display.set_mode((height,width))

bg = 25,25,25
screen.fill(bg)


dimension1, dimension2 = 50,50

dimensionW = width / dimension1
dimensionH = height / dimension2

estadoJuego = np.zeros((dimension1, dimension2))


# stick 
estadoJuego[5,3] = 1
estadoJuego[5,4] = 1
estadoJuego[5,5] = 1

# glider
estadoJuego[21,21] = 1
estadoJuego[22,22] = 1
estadoJuego[22,23] = 1
estadoJuego[21,23] = 1
estadoJuego[20,23] = 1

estadoJuego[21+5,21+5] = 1
estadoJuego[22+5,22+5] = 1
estadoJuego[22+5,23+5] = 1
estadoJuego[21+5,23+5] = 1
estadoJuego[20+5,23+5] = 1

#estadoJuego = np.random.randint(2, size=(dimension1, dimension2))       
pauseExect = False
k, b, n = 0, 0, 0
while True:

    newestadoJuego = np.copy(estadoJuego)

    screen.fill(bg)
    time.sleep(0.000001)

    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pauseExect = not pauseExect
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            estadoJuego = np.random.randint(2, size=(dimension1, dimension2))          
        mouseClick = pygame.mouse.get_pressed()
        print(mouseClick)

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimensionW)), int(np.floor(posY/dimensionH))
            newestadoJuego[celX, celY] = not mouseClick[2]

    for y in range(0,dimension1):
        for x in range(0,dimension2):



            if not pauseExect:
                n_neigh = estadoJuego[(x-1)%dimension1, (y-1)%dimension2] + \
                        estadoJuego[(x)%dimension1, (y-1)%dimension2] + \
                        estadoJuego[(x+1)%dimension1, (y-1)%dimension2] + \
                        estadoJuego[(x-1)%dimension1, (y)%dimension2] + \
                        estadoJuego[(x+1)%dimension1, (y)%dimension2] + \
                        estadoJuego[(x-1)%dimension1, (y+1)%dimension2] + \
                        estadoJuego[(x)%dimension1, (y+1)%dimension2] + \
                        estadoJuego[(x+1)%dimension1, (y+1)%dimension2]
            
            poly = [((x)*dimensionW,y*dimensionH),
                    ((x+1)*dimensionW,y*dimensionH),
                    ((x+1)*dimensionW,(y+1)*dimensionH),
                    ((x)*dimensionW,(y+1)*dimensionH)]

            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                if estadoJuego[x,y] == 0 and n_neigh ==4:
                    newestadoJuego[x,y]=1
                elif estadoJuego[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newestadoJuego[x,y]=0
                k = 255
                b, n = 0, 128
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                if estadoJuego[x,y] == 0 and n_neigh ==2:
                    newestadoJuego[x,y]=1
                elif estadoJuego[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newestadoJuego[x,y]=0   
                b = 255
                k, n = 128, 0  
            else: 
                if estadoJuego[x,y] == 0 and n_neigh ==3:
                    newestadoJuego[x,y]=1
                elif estadoJuego[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newestadoJuego[x,y]=0
                if newestadoJuego[x,y]==0:
                    pygame.draw.polygon(screen, (128,128,128),poly, 1)
                else:
                    pygame.draw.polygon(screen, (0,0,255),poly,0)

                n = 255
                k, b = 255, 255


            if newestadoJuego[x,y]==0:
                pygame.draw.polygon(screen, (128,128,128),poly, 1)
            else:
                pygame.draw.polygon(screen, (k,b,n),poly,0)
            vivas = np.count_nonzero(newestadoJuego)

    estadoJuego = np.copy(newestadoJuego)
    historialCeldasVivas.append(vivas)    
    pygame.display.flip()

# mora, 2013; Faccena, 2017, mora, 2006
        

        #file = open('historial.csv', 'w+', newline ='') 
    if event.type == pygame.QUIT: 
        # writing the data into the file 
        #with file:     
            #write = csv.writer(file) 
            #write.writerows(historialCeldasVivas)
        hora = str(datetime.datetime.now().time())
        hora = list(hora)

        for i in range(len(hora)):
            if hora[i] == ":":
                hora[i] = "-"
        hora = "".join(hora)[-3:]
        np.savetxt(f"hist{hora}.csv", historialCeldasVivas, delimiter=",", fmt='%s')
        pygame.display.quit()
       
        exit()


