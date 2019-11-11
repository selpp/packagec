import ctypes

from invader.core.window import Window
from invader.core.maths import Vec2f
from invader.utils import bdl

bdl.createTexture.restype        = ctypes.c_void_p
bdl.createTexture.restype        = ctypes.c_void_p
bdl.createTextureManager.restype = ctypes.c_void_p

class Sprite:
    def __init__( self: 'Sprite', pos: Vec2f, scale: Vec2f, manager: 'TextureManager', idx: ctypes.c_int ) -> None:
        self.pos     = pos
        self.scale   = scale
        self.manager = manager
        self.idx     = idx

    def __call__( self: 'Sprite', window: 'Window' ) -> None:
        bdl.drawSprite( window, self.pos.to_c( ), self.scale.to_c( ), self.manager.manager, self.idx )

class TextureManager:
    def __init__( self: 'TextureManager', max_size: int ) -> None:
        self.max_size = max_size
        self.manager  = self._create_texture( )

    def _create_texture( self: 'TextureManager' ) -> ctypes.c_void_p:
        bdl.createTextureManager( ctypes.c_int( self.max_size ) )

    def __add__( self: 'TextureManager', path: str ) -> ctypes.c_int:
        texture = bdl.createTexture( ctypes.c_char_p( path.encode( ) ) )
        return bdl.addTexture( self.manager, ctypes.c_int( self.max_size ), texture )
