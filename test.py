from ctypes import *
import ctypes

lib = cdll.LoadLibrary("./build/bdl.so")

class RGBA(ctypes.Structure):
   _fields_ = [('r', c_char), ('g', c_char), ('b', c_char), ('a', c_char)]

class sfVector2f(ctypes.Structure):
    _fields_ = [('x', c_float), ('y', c_float)]

origin = sfVector2f()
origin.x = 0.0
origin.y = 0.0

black = RGBA()
black.r = 0
black.g = 0
black.b = 0
black.a = 255

red = RGBA()
red.r = 255
red.g = 0
red.b = 0
red.a = 255

windowFlags = 6

lib.createWindow.restype = ctypes.c_void_p
# lib.createWindow.argtype = [c_int, c_int, c_int, c_char_p, c_int, c_void_p]
window = lib.createWindow(c_int(800), c_int(600), c_int(32), c_char_p(b"test"), c_int(6), c_void_p(0))
window = c_void_p(window)

# lib.setFPSCapWindow.argtype = [c_void_p, c_int]
lib.setFPSCapWindow(window, 60);

while(lib.isOpenWindow(window)):
    lib.handleDefaultEvents(window)
    lib.clearWindow(window, black);
    lib.drawCircle(window, origin, c_float(50.0), red, c_int(1), black);
    lib.displayWindow(window);
