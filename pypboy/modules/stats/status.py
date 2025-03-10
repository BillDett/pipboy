from game.core import Entity
import pypboy
import pygame
import game
import settings
import pypboy.ui
import os
import time
global STATION

class Module(pypboy.SubModule):
    global STATION
    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        
        self.label = "STATUS"
        self.images = []

        self.topmenu = pypboy.ui.TopMenu()
        self.add(self.topmenu)
        self.topmenu.label = "STAT"
        self.topmenu.title = settings.MODULE_TEXT


        self.health = Health()
        self.health.rect[0] = 0
        self.health.rect[1] = 131
        self.add(self.health)
        
        self.animation = Animation()
        self.animation.rect[0] = 296
        self.animation.rect[1] = 190
        self.add(self.animation)

        self.prev_time = 0

        self.footer = pypboy.ui.Footer(settings.STATUS_FOOTER)
        self.footer.rect[0] = settings.footer_x
        self.footer.rect[1] = settings.footer_y
        self.add(self.footer)
        # STATUS_FOOTER = ["HP 115/115", "LEVEL 66", "AP 90/90", 90, True]

    #     self.menu = pypboy.ui.Menu(["CND", "RAD", "EFF"], [self.show_cnd, self.show_rad, self.show_eff], 0)
    #     self.menu.rect[0] = settings.menu_x
    #     self.menu.rect[1] = settings.menu_y
    #     self.add(self.menu)

    # def show_cnd(self):
    #     print("CND")

    # def show_rad(self):
    #     print("RAD")

    # def show_eff(self):
    #     print("EFF")

    def render(self, *args, **kwargs):
        global STATION
        if settings.glitch == True:
            self.current_time = time.time()
            self.delta_time = self.current_time - self.prev_time

            if self.delta_time >= settings.glitch_time:
                if settings.glitch_next == 0 or settings.glitch_next == 2 or settings.glitch_next == 4:
                    self.health.rect[1] = -69
                    self.footer.rect[1] = 62
                    self.animation.rect[1] = -10
                    self.prev_time = self.current_time
                elif settings.glitch_next == 1 or settings.glitch_next == 3 or settings.glitch_next == 5:
                    self.health.rect[1] = 331
                    self.footer.rect[1] = 531
                    self.animation.rect[1] = 390
                    self.prev_time = self.current_time
                elif settings.glitch_next == 6:
                    self.health.rect[1] = 131
                    self.animation.rect[1] = 190
                    self.footer.rect[1] = settings.footer_y
                    self.prev_time = self.current_time
                elif settings.glitch_next >= 7:
                    settings.glitch_next = 0
                    settings.glitch = False
                settings.glitch_next += 1

    # def handle_resume(self):
    #     pass
    #     super(Module, self).handle_resume()

class Animation(game.Entity):

    def __init__(self):
        super(Animation, self).__init__()

        self.image = pygame.Surface((120,250))   
        #self.animation_time = 0.125 # 8 fps
        self.animation_time = 0 # 8 fps
        self.steps = list(range(4)) + list(range(4, 0, -1))
        self.index = 0                
        self.images = []
        self.prev_time = 0
        self.prev_fps_time = 0

        path = "./images/stats/legs1"
        for f in  sorted(os.listdir(path)):
            if f.endswith(".png"):
                image = pygame.image.load(path + "/" + f).convert_alpha()
                self.images.append(image)
        self.head = pygame.image.load("images/stats/head1/1.png").convert_alpha()

    def render(self, *args, **kwargs):

        self.current_time = time.time()
        self.delta_time = self.current_time - self.prev_time

        # #FPS debugging
        # self.fps_delta_time = self.current_time - self.prev_fps_time
        # if self.fps_delta_time:
        #     self.fps = round(1/self.fps_delta_time,1)
        # self.prev_fps_time = time.time()

        if self.delta_time >= self.animation_time:
            self.prev_time = self.current_time

            self.image.fill((0,0,0))

            if self.index >= len(self.images):
                self.index = 0
            self.file = self.images[self.index]

            self.image.blit((self.file),(1 + self.steps[self.index] // 2,68 + self.steps[self.index]))
            self.image.blit((self.head),(29 + self.steps[self.index] // 2,0 + self.steps[self.index]))
            # settings.FreeRobotoB[24].render_to(self.image, (0, 0), str(self.fps), settings.bright) #FPS

            self.index += 1


class Health(game.Entity):

    def __init__(self):
        super(Health, self).__init__()

        self.image = pygame.Surface((settings.WIDTH, settings.HEIGHT - 180))
        self.image.fill((0,0,0))
        #
        # # Bottom Boxes
        # pygame.draw.rect(self.image, settings.dim, (0, 501, 166, 38)) #Hit point background
        # pygame.draw.rect(self.image, settings.dim, (170, 501, 370, 38)) #Level bar background
        # pygame.draw.lines(self.image, settings.mid,True,[(282,515),(529,515),(529,529),(282,529)], 3) #Level bar surround
        # pygame.draw.rect(self.image, settings.bright, (285, 517, 179, 11)) #Level bar fill
        # pygame.draw.rect(self.image, settings.dim, (544, 501, 176, 38)) #Actiion background
        

        # Middle Boxes
        pygame.draw.rect(self.image, settings.dim, (203, 358, 64, 62)) #Gun box
        pygame.draw.rect(self.image, settings.dim, (273, 358, 38, 62)) #Ammo box
        pygame.draw.rect(self.image, settings.dim, (328, 358, 64, 62)) #Helmet box
        pygame.draw.rect(self.image, settings.dim, (398, 358, 38, 62)) #Armor box
        pygame.draw.rect(self.image, settings.dim, (440, 358, 38, 62)) #Energy box
        pygame.draw.rect(self.image, settings.dim, (483, 358, 38, 62)) #Radiation box

        # Icons
        self.image.blit(pygame.image.load('images/stats/gun.png').convert_alpha(),(210,374))
        self.image.blit(pygame.image.load('images/stats/reticle.png').convert_alpha(),(284,363))
        self.image.blit(pygame.image.load('images/stats/helmet.png').convert_alpha(),(338,373))
        self.image.blit(pygame.image.load('images/stats/shield.png').convert_alpha(),(410,362))
        self.image.blit(pygame.image.load('images/stats/bolt.png').convert_alpha(),(453,362))
        self.image.blit(pygame.image.load('images/stats/radiation.png').convert_alpha(),(491,363))

        # Health Bars
        pygame.draw.line(self.image, settings.bright, (344, 32), (379, 32), 9)
        pygame.draw.line(self.image, settings.bright, (465, 134), (500, 134), 9)
        pygame.draw.line(self.image, settings.bright, (465, 266), (500, 266), 9)
        pygame.draw.line(self.image, settings.bright, (344, 318), (379, 318), 9)
        pygame.draw.line(self.image, settings.bright, (216, 266), (251, 266), 9)
        pygame.draw.line(self.image, settings.bright, (216, 134), (251, 134), 9)
        
        #Stat text
        settings.FreeRobotoB[24].render_to(self.image, (281, 395), "18", settings.bright) # Ammo count
        settings.FreeRobotoB[24].render_to(self.image, (406, 395), "10", settings.bright) # Armor count
        settings.FreeRobotoB[24].render_to(self.image, (447, 395), "20", settings.bright) # Energy count
        settings.FreeRobotoB[24].render_to(self.image, (490, 395), "10", settings.bright) # Rad count
        #
        # # Bottom text
        # settings.FreeRobotoB[30].render_to(self.image, (7, 509), "HP 115/115", settings.bright)
        # settings.FreeRobotoB[24].render_to(self.image, (188, 513), "LEVEL 66", settings.bright)
        # settings.FreeRobotoB[30].render_to(self.image, (602, 509), "AP 90/90", settings.bright)

        #User name
        settings.FreeRobotoB[24].render_to(self.image, (301, 448), settings.name, settings.bright)

    # def handle_resume(self):
    #     pass
    #     super(Module, self).handle_resume()
