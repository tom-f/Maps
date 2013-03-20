from pyglet.sprite import Sprite

class Tile(Sprite):
    """ A basic square shaped 'block' which is the base unit of any map or item"""

    _height = 0
    _width = 0

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def set_height(self, height):
        self._height = height
        self.update()

    def set_width(self, width):
        self._width = width
        self.update()

    def __init__(self, *args, **kwargs):
        self.set_height = kwargs.get('tile_height', 0)
        self.set_width = kwargs.get('tile_width', 0)
        if self._tile_width or self._tile_height:
            del kwargs['tile_width']
            del kwargs['tile_height']
        super(TileableSprite, self).__init__(*args, **kwargs)
        if self._tile_width == 0 or self._tile_height == 0:
            self._tile_width, self._tile_height = self.width, self.height
        self._update_position()


    def update_tile(self):
        if not self._visible:
            # Hide 
            self._vertex_list.vertices[:] = [0, 0, 0, 0, 0, 0, 0, 0]
        else:
            x, y = int(self._x), int(self._y)
            h, w = self._get_height(), self._get_width()
            u1 = self._texture.anchor_x / float(self._texture.width)
            v1 = self._texture.anchor_y / float(self._texture.height)
            u2 = u1 + w / float(self._texture.width)
            v2 = v1 + h / float(self._texture.height)
            t = self._texture.tex_coords
            # update square coords - the [:] notation 
            self._vertex_list.vertices[:] = 
                [x, y, x + w, y, x + w, y + h, x, y + h]
            self._vertex_list.tex_coords[:] = 
                [u1, v1, t[2], u2, v1, t[5], u2, v2, t[8], u1, v2, t[11]]
            
