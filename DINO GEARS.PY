#pgzero
import random

#variaveis
cell = Actor("tile_0000", (20, 20), size = (40, 40))
cell1 = Actor("tile_0001", (20, 20), size = (40, 40))
cell2 = Actor("tile_0002", (20, 20), size = (40, 40))
background = Actor("floresta")
mode = "menu"
mortes = 0
META_MORTES = 10
controle_mortes = 0
TILE_SIZE = 40
size_w = 11 # Largura do campo em células
size_h = 12 # Altura do campo em células
WIDTH = TILE_SIZE * size_w
HEIGHT = TILE_SIZE * size_h

TITLE = "Dino Guears" # Título do jogo
FPS = 30 # Quadros por segundo
my_map = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2],
        [0, 0, 1, 1, 1, 2, 0, 2, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 2],
        [0, 1, 1, 0, 2, 0, 1, 2, 0, 2, 0],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 2, 0],
        [1, 1, 2, 0, 0, 2, 0, 2, 0, 1, 0],
        [1, 1, 0, 2, 1, 1, 0, 1, 0, 2, 0],
        [1, 1, 0, 0, 0, 1, 0, 2, 0, 1, 0],
        [1, 1, 2, 0, 2, 1, 0, 1, 0, 2, 0],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]] # linha usada pa mostrar as informações do player

#personagem
p = Actor("personagem", (50, 50), size = (70, 70))
p.top = TILE_SIZE
p.left = TILE_SIZE
p.health = 90
p.attack = 15

#dinossauros
dinos = []
for i in range(5):
    x = random.randint(0, size_w -2) * TILE_SIZE
    y = random.randint(0, size_h -3) * TILE_SIZE
    dino_t = Actor("Dinossauro", (x, y), size = (80, 50))
    dino_t.health = 100
    dino_t.attack = random.randint(5, 13)
    dinos.append(dino_t)

#mapa
def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            pos = (j * TILE_SIZE, i * TILE_SIZE)
            if my_map[i][j] == 0:
                cell.topleft = pos
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.topleft = pos
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.topleft = pos
                cell2.draw()

def draw():
        screen.clear()
        #Capa
        if mode == "menu":
            screen.clear()
            background.draw()
            screen.draw.text("Dino Guears", center=(WIDTH/2, HEIGHT/2 - 50), color="white", fontsize=50)
            screen.draw.text("Pressione I para ver como jogar", center=(WIDTH/2, HEIGHT/2 + 15), color="white", fontsize=25)
            screen.draw.text("Pressione ESPAÇO para JOGAR", center=(WIDTH/2, HEIGHT/2 + 50), color="white", fontsize=20)
            
        # Contexto
        elif mode == "instrucoes":
            screen.fill((30, 30, 30))
            screen.draw.text("COMO JOGAR", center=(WIDTH/2, 50), color="orange", fontsize=40)
            screen.draw.text("CONTEXTO: Você é o caçador de uma vila que", topleft=(30, 80), fontsize=18, width=WIDTH-60, color="white")
            screen.draw.text("existe em um mundo onde humanos e dinossauros", topleft=(30, 100), fontsize=18, width=WIDTH-60, color="white")
            screen.draw.text("vivem juntos, seu objetivo e matar os dinossauros", topleft=(30, 120), fontsize=18, width=WIDTH-60, color="white")
            screen.draw.text("para conseguir alimento ao povo da vila.", topleft=(30, 140), fontsize=18, width=WIDTH-60, color="white")
            screen.draw.text("Use as setas para mover.", midleft=(50, 200), fontsize=18)
            screen.draw.text("Encoste nos dinos para lutar.", midleft=(50, 250), fontsize=18)
            screen.draw.text("Ganhe HP ao derrotar um inimigo.", midleft=(50, 300), fontsize=18)
            screen.draw.text("Pressione ESC para voltar", center=(WIDTH/2, HEIGHT - 50), color="white", fontsize=20)
            
        #vitoria
        elif mode == "victory":
            screen.fill((0, 100, 255)) # Um fundo azul para vitória
            screen.draw.text("VOCÊ CONSEGUI!", center=(WIDTH/2, HEIGHT/2 - 20), color="yellow", fontsize=40)
            screen.draw.text("Você coletou comida suficiene para sua vila", center=(WIDTH/2, HEIGHT/2 + 30), color="white", fontsize=15)
         #derrota   
        elif mode == "gameover":
            screen.fill((100, 0, 0)) 
            screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2 - 20), color="white", fontsize=55)
            screen.draw.text("Parece que você subestimou sua presa", center=(WIDTH/2, HEIGHT/2 + 30), color="orange", fontsize=20)
            
        #modo de jogo 
        elif mode == "game":
            map_draw()
            p.draw()
            
            for dino_t in dinos:
                dino_t.draw()
            # informações do player
            screen.draw.text("HP:", center=(30, HEIGHT - 20), color='white', fontsize=20)
            screen.draw.text(str(p.health), center=(70, HEIGHT - 20), color='white', fontsize=20)
            screen.draw.text("ATK:", center=(150, HEIGHT - 20), color='white', fontsize=20)
            screen.draw.text(str(p.attack), center=(200, HEIGHT - 20), color='white', fontsize=20)
            screen.draw.text("DINOS restantes:", center=(300, HEIGHT - 20), color='white', fontsize=20)
            screen.draw.text(str(controle_mortes), center=(400, HEIGHT - 20), color='white', fontsize=20)
                
            
            
        elif mode == "victory":
            screen.fill((0, 100, 255))
            screen.draw.text("VOCÊ VENCEU!", center=(WIDTH/2, HEIGHT/2 - 20), color="yellow", fontsize=50)
            screen.draw.text("Todos os dinossauros foram derrotados", center=(WIDTH/2, HEIGHT/2 + 30), color="white", fontsize=15)
    
def on_key_down(key):
    global mode
    old_x = p.x
    old_y = p.y
    # começar o jogo
    if mode == "menu":
        if key == keys.SPACE:
            mode = "game"
        elif key == keys.I: # Aperte 'I' para ver instruções
            mode = "instrucoes"
            
    elif mode == "instrucoes":
        if key == keys.ESCAPE: # Aperte 'ESC' para voltar ao menu
            mode = "menu"
    # Movimentação
    elif mode == "game":
        if key == keys.RIGHT and p.right + TILE_SIZE <= WIDTH:
            p.x += TILE_SIZE
            p.image = "personagem-direita"
        elif key == keys.LEFT and p.left - TILE_SIZE >= 0:
            p.x -= TILE_SIZE
            p.image = "personagem-esquerda"
        elif key == keys.DOWN and p.bottom + TILE_SIZE <= HEIGHT - TILE_SIZE:
            p.y += TILE_SIZE
            p.image = "personagem"
        elif key == keys.UP and p.top - TILE_SIZE >= 0:
            p.y -= TILE_SIZE
            p.image = "personagem-cima"
            
        dino_index = p.collidelist(dinos)
        if dino_index != -1:
            dino_t = dinos[dino_index]
            dino_t.health -= p.attack
            p.health -= dino_t.attack
            p.x, p.y = old_x, old_y

            if p.health <= 0:
                mode = "gameover"
            if dino_t.health <= 0:
                global mortes
                global controle_mortes
                dinos.pop(dino_index)
                mortes += 1
                controle_mortes = META_MORTES - mortes
                # recuperar a vida 
                p.health += 65
                
                # novos inimigos
                if mortes + len(dinos) < META_MORTES:
                    new_x = random.randint(1, size_w - 2) * TILE_SIZE
                    new_y = random.randint(1, size_h - 3) * TILE_SIZE    
                    new_x = random.randint(1, size_w - 2) * TILE_SIZE
                    new_y = random.randint(1, size_h - 3) * TILE_SIZE
                    new_dino = Actor("Dinossauro", topleft=(new_x, new_y), size = (80, 50))
                    new_dino.health = 100
                    new_dino.attack = random.randint(8, 12)
                    dinos.append(new_dino)
                if mortes >= META_MORTES and len(dinos) == 0:
                    mode = "victory"
