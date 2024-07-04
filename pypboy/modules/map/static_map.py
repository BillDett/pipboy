import pygame
import pypboy
import settings
import game
import io
import numpy as np

class Module(pypboy.SubModule):
    label = "WORLD MAP"
    zoom = settings.WORLD_MAP_ZOOM
    map_top_edge = 128
    map_type = settings.MAP_TYPE
    map_width = 720
    map_height = 545
    map_rect = pygame.Rect(0, (map_width - 720) / 2, map_width, map_height - 45)

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.mapgrid = Map(self.map_width,self.map_height, self.map_rect)
        self.add(self.mapgrid)
        self.mapgrid.rect[0] = 0
        self.mapgrid.rect[1] = self.map_top_edge

        self.topmenu = pypboy.ui.TopMenu()
        self.add(self.topmenu)
        self.topmenu.label = "MAP"
        self.topmenu.title = settings.MODULE_TEXT

        settings.FOOTER_TIME[2] = "He's such a good boy!"
        self.footer = pypboy.ui.Footer(settings.FOOTER_TIME)
        self.footer.rect[0] = settings.footer_x
        self.footer.rect[1] = settings.footer_y
        self.add(self.footer)

class Map(game.Entity):
    _mapper = None
    _transposed = None
    _size = 0
    _fetching = None
    _map_surface = None
    _loading_size = 0
    _render_rect = None

    def __init__(self, width, height, render_rect=None, loading_type="Loading map...", *args, **kwargs):
        super(Map, self).__init__((width, height), *args, **kwargs)
        self._size = width
        self._map_surface = pygame.Surface((width, height))
        self._render_rect = render_rect
        #text = settings.RobotoB[14].render(loading_type, True, settings.bright, (0, 0, 0))
        image = pygame.image.load('boston.png').convert()

        arr = pygame.surfarray.pixels3d(image)

        mean_arr = np.dot(arr[:, :, :], [0.216, 0.587, 0.144])
        mean_arr3d = mean_arr[..., np.newaxis]
        new_arr = np.repeat(mean_arr3d[:, :, :], 3, axis=2)
        map_surf = pygame.surfarray.make_surface(arr)

        map_surf.fill(settings.bright, None, pygame.BLEND_RGBA_MULT)

        self._map_surface.blit(map_surf, (0, 0))

        # svg_surface = load_svg("./images/map_icons/Player_Marker.svg", 40, 40)
        svg_surface = pygame.image.load("./images/map_icons/Player_Marker.svg").convert_alpha()
        svg_surface.fill(settings.bright, None, pygame.BLEND_RGBA_MULT)
        self._map_surface.blit(svg_surface, (settings.WIDTH / 2 - 20, self._render_rect.centery - 20))
        # redraw
        self.image.blit(self._map_surface, (0, 0), area=self._render_rect)
