import ctypes

from invader.core.window import Window
from invader.core.maths import _Vec2f
from invader.core.maths import Vec2f
from invader.core.utils import Color
from typing import List

bdl                      = ctypes.cdll.LoadLibrary( 'packagepython/res/bdl.so' )
bdl.createWindow.restype = ctypes.c_void_p
c_float_p                = ctypes.POINTER( ctypes.c_float )

class Shape:
    def __init__( self: 'Shape' ) -> None:
        pass

    def __call__( self: 'Shape', window: 'Window' ) -> None:
        pass

class Circle( Shape ):
    def __init__( self: 'Circle', pos: 'Vec2f', rad: float, color: 'Color', outline: int, outline_color: 'Color' ) -> None:
        super( Circle, self ).__init__( )
        self.pos           = pos
        self.rad           = rad
        self.color         = color
        self.outline       = outline
        self.outline_color = outline_color

    def __call__( self: 'Circle', window: 'Window' ) -> None:
         bdl.drawCircle( window.window, self.pos.to_c( ), ctypes.c_float( self.rad ), self.color.to_c( ), ctypes.c_int( self.outline ), self.outline_color.to_c( ) )

class Rectangle( Shape ):
    def __init__( self: 'Rectangle', pos: 'Vec2f', size: 'Vec2f', color: 'Color', outline: int, outline_color: 'Color' ) -> None:
        super( Rectangle, self ).__init__( )
        self.pos           = pos
        self.size          = size
        self.color         = color
        self.outline       = outline
        self.outline_color = outline_color

    def __call__( self: 'Rectangle', window: 'Window' ) -> None:
         bdl.drawRectangle( window.window, self.pos.to_c( ), self.size.to_c( ), self.color.to_c( ), ctypes.c_int( self.outline ), self.outline_color.to_c( ) )

class Polygone( Shape ):
    def __init__( self: 'Polygone', pos: List[ 'Vec2f' ], color: 'Color', outline: int, outline_color: 'Color' ) -> None:
        super( Polygone, self ).__init__( )
        self.pos           = pos
        self.color         = color
        self.outline       = outline
        self.outline_color = outline_color

    def __call__( self: 'Polygone', window: 'Window' ) -> None:
        pos = [ p.to_c( ) for p in self.pos ]
        n   = len( pos )
        pos = ( _Vec2f * n )( *pos )
        bdl.drawConvexPolygone( window.window, pos, ctypes.c_int( n ), self.color.to_c( ), ctypes.c_int( self.outline ), self.outline_color.to_c( ) )
