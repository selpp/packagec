import ctypes

from typing import Any

class _Vec2f( ctypes.Structure ):
    _fields_ = [ ( 'x', ctypes.c_float ), ( 'y', ctypes.c_float ) ]

class Vec2f:
    def __init__( self: 'Vec2f', x: float, y: float ) -> None:
        self.x = x
        self.y = y

    def to_c( self: 'Vec2f' ) -> '_Vec2f':
        return _Vec2f( ctypes.c_float( self.x ), ctypes.c_float( self.y ) )

    def __add__( self: 'Vec2f', other: Any ) -> 'Vec2f':
        if type( other ) == float or type( other ) == int:
            return Vec2f( self.x + other, self.y + other )
        elif type( other ) == Vec2f:
            return Vec2f( self.x + other.x, self.y + other.y )
        else:
            return None

    def __sub__( self: 'Vec2f', other: Any ) -> 'Vec2f':
        if type( other ) == float or type( other ) == int:
            return Vec2f( self.x - other, self.y - other )
        elif type( other ) == Vec2f:
            return Vec2f( self.x - other.x, self.y - other.y )
        else:
            return None

    def __mul__( self: 'Vec2f', other: Any ) -> 'Vec2f':
        if type( other ) == float or type( other ) == int:
            return Vec2f( self.x * other, self.y * other )
        elif type( other ) == Vec2f:
            return Vec2f( self.x * other.x, self.y * other.y )
        else:
            return None

    def __div__( self: 'Vec2f', other: Any ) -> 'Vec2f':
        if type( other ) == float or type( other ) == int:
            return Vec2f( self.x / other, self.y / other )
        elif type( other ) == Vec2f:
            return Vec2f( self.x / other.x, self.y / other.y )
        else:
            return None
