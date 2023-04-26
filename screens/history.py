import pygame
from classes.Button import Button
from constants.images import space_background_img
from constants.buttons import button_return
from constants.fonts import history_font

def render_history_screen(surface, scroll_y = 0):

    surface.blit(space_background_img.get("space_background"), (0, 0))

    text = '''
    Era o ano de 2150 e a humanidade havia coloni-
    zado diversos planetas e luas dentro do nosso
    sistema solar. Uma dessas colônias era uma es-
    tação espacial construída em uma órbita próxi-
    ma a um cinturão de asteróides. Essa estação 
    era responsável por extrair minérios dos aste-
    róides próximos e abastecer outras colônias
    espalhadas pelo sistema solar. O piloto de na-
    ve responsável pela defesa da estação era um
    homem chamado David. Ele era militar e havia
    passado a maior parte de sua vida defendendo
    interesses humanos no espaço. David sabia que
    a estação espacial era uma parte vital da infra-
    estrutura humana no espaço e que sua defesa era
    essencial para manter o abastecimento de recur-
    sos em outras colônias.

    Em uma noite tranquila, David estava fazendo
    sua ronda de rotina ao redor da estação espa-
    cial quando detectou a presença de naves inimi-
    gas se aproximando. Ele sabia que os inimigos
    eram piratas espaciais que atacavam colônias
    humanas em busca de recursos. David prontamente
    alertou a equipe de defesa da estação e prepa-
    rou sua nave de combate para enfrentar os ini-
    migos. Os piratas espaciais chegaram rapidamen-
    te e iniciaram seu ataque à estação. David ma-
    nobrou sua nave habilmente para interceptar os
    ataques inimigos e proteger a estação espacial.
    Ele usou todas as habilidades que aprendeu du-
    rante sua carreira para enfrentar os inimigos
    e proteger a estação. A batalha foi intensa,
    durou horas e há boatos de que ainda esteja
    ocorrendo.
    '''

    # Split the text into lines
    lines = text.split('\n')

    # Render each line of the text
    text_surfaces = []
    for line in lines:
        text_surface = history_font.render(line, True, (255, 255, 255))
        text_surfaces.append(text_surface)

    # Calculate the height of each text surface
    text_heights = [text_surface.get_height() for text_surface in text_surfaces]

    # Calculate the y position of the first line of text

    text_y = 50
    text_x = -20
    # Blit each line of text to the screen, justified
    for text_surface, text_height in zip(text_surfaces, text_heights):
        surface.blit(text_surface, (text_x, text_y))
        text_y += text_height

    button_return.draw(surface)

    pygame.display.update()
