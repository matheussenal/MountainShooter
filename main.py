import pygame

pygame.init()
print('Setup Start')
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    # Check for all events / checando todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close window / fechar janela
            quit()  # end pygame
