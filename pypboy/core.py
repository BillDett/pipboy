import time

import pcf8574_io

import pygame
import game
import pypboy.ui
import settings
from math import atan2, pi, degrees

from pypboy.modules import data
from pypboy.modules import items
from pypboy.modules import stats
from pypboy.modules import boot
from pypboy.modules import map
from pypboy.modules import onyx
from pypboy.modules import lili
from pypboy.modules import radio
from pypboy.modules import passcode

class Pypboy(game.core.Engine):
    currentModule = 0
    prev_fps_time = 0

    def __init__(self, *args, **kwargs):
        # Support rescaling
        # if hasattr(settings, 'OUTPUT_WIDTH') and hasattr(settings, 'OUTPUT_HEIGHT'):
        #     self.rescale = False

        # Initialize modules
        super(Pypboy, self).__init__(*args, **kwargs)
        self.init_persitant()
        self.init_modules()

        self.gpio_actions = {}
        # if settings.GPIO_AVAILABLE:
        self.init_gpio_controls()

        self.prev_fps_time = 0

    def init_persitant(self):
        # self.background = pygame.image.load('images/background.png')
        overlay = pypboy.ui.Overlay()
        self.root_persitant.add(overlay)
        scanlines = pypboy.ui.Scanlines()
        self.root_persitant.add(scanlines)
        pass

    def init_modules(self):
        self.modules = {
            "lili": lili.Module(self),
            "onyx": onyx.Module(self),
            "map": map.Module(self),
            "data": data.Module(self),
            "items": items.Module(self),
            "stats": stats.Module(self),
        }
        self.switch_module(settings.STARTER_MODULE)  # Set the start screen

    def init_gpio_controls(self):
        self.gpio = pcf8574_io.PCF(0x20)

        self.gpio.pin_mode("p0", "INPUT")
        self.gpio.pin_mode("p1", "INPUT")
        self.gpio.pin_mode("p2", "INPUT")
        self.gpio.pin_mode("p3", "INPUT")
        self.gpio.pin_mode("p4", "INPUT")
        self.gpio.pin_mode("p5", "INPUT")
        self.gpio.pin_mode("p6", "INPUT")
        self.gpio.pin_mode("p7", "INPUT")

        self.last_seen_gpio = 0


    def check_gpio_input(self):
        self.current_gpio = self.last_seen_gpio
        if self.gpio.read("p0") == False:
            self.current_gpio = 0
        elif self.gpio.read("p1") == False:
            self.current_gpio = 1
        elif self.gpio.read("p2") == False:
            self.current_gpio = 2
        elif self.gpio.read("p3") == False:
            self.current_gpio = 3
        elif self.gpio.read("p4") == False:
            self.current_gpio = 4
        elif self.gpio.read("p5") == False:
            self.current_gpio = 5
        elif self.gpio.read("p6") == False:
            self.current_gpio = 6
        elif self.gpio.read("p7") == False:
            self.current_gpio = 7
	    
        if self.current_gpio != self.last_seen_gpio:
            self.last_seen_gpio = self.current_gpio
            print("Switching based on gpio now " + str(self.current_gpio))
            if self.current_gpio == 1:
                self.switch_module("stats")
            elif self.current_gpio == 2:
                self.switch_module("items")
            elif self.current_gpio == 3:
                self.switch_module("data")
            elif self.current_gpio == 4:
                self.switch_module("map")
            elif self.current_gpio == 5:
                self.switch_module("onyx")
            elif self.current_gpio == 6:
                self.switch_module("lili")
   

    def switch_module(self, module):
        # if not settings.hide_top_menu:
        if module in self.modules:
            if hasattr(self, 'active'):
                self.active.handle_action("pause")
                self.remove(self.active)
            self.active = self.modules[module]
            self.active.parent = self
            self.active.handle_action("resume")
            self.add(self.active)
        else:
            print("Module '%s' not implemented." % module)

    def handle_action(self, action):
        if action.startswith('module_'):
            self.switch_module(action[7:])
        else:
            if hasattr(self, 'active'):
                self.active.handle_action(action)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:  # Some key has been pressed
            # Persistent Events:
            if event.key == pygame.K_ESCAPE:  # ESC
                self.running = False

            elif event.key == pygame.K_PAGEUP:  # Volume up
                settings.radio.handle_radio_event(event)
            elif event.key == pygame.K_PAGEDOWN:  # Volume down
                settings.radio.handle_radio_event(event)
            elif event.key == pygame.K_END:  # Next Song
                settings.radio.handle_radio_event(event)
            elif event.key == pygame.K_HOME:  # Prev Song
                settings.radio.handle_radio_event(event)
            elif event.key == pygame.K_DELETE:
                settings.radio.handle_radio_event(event)
            elif event.key == pygame.K_INSERT:
                settings.radio.handle_radio_event(event)
            else:
                if event.key in settings.ACTIONS:  # Check action based on key in settings
                    self.handle_action(settings.ACTIONS[event.key])

        elif event.type == pygame.QUIT:
            self.running = False

        elif event.type == settings.EVENTS['SONG_END']:
            if settings.SOUND_ENABLED:
                if hasattr(settings, 'radio'):
                    settings.radio.handle_radio_event(event)
        elif event.type == settings.EVENTS['PLAYPAUSE']:
            if settings.SOUND_ENABLED:
                if hasattr(settings, 'radio'):
                    settings.radio.handle_radio_event(event)
        else:
            if hasattr(self, 'active'):
                self.active.handle_event(event)

    def inRange(self, angle, init, end):
        return (angle >= init) and (angle < end)

    def run(self):
        self.running = True
        while self.running:
            self.check_gpio_input()
            #for event in pygame.event.get():
            #    self.handle_event(event)
            #    if hasattr(self, 'active'):
            #        self.active.handle_event(event)

            # slow code debugger
            # debug_time = time.time()

            self.render()
            #
            # time_past = time.time() - debug_time
            # if time_past:
            #     max_fps = int(1 / time_past)
            #     print("self.render took:", time_past, "max fps:", max_fps)

        #try:
        #    pygame.mixer.quit()
        #except Exception as e:
        #    print(e)
