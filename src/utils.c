#include "utils.h"

  sfRenderWindow* createWindow(int width, int height, int depth, char* title, char flags, void* chepa) {
  return _createWindow(Mode(width, height, depth), title, flags, chepa);
}

void setFPSCapWindow(sfWindow* window, int cap) {
  _setFPSCapWindow(window, cap);
}

char isOpenWindow(sfRenderWindow* window) {
  return _isOpenWindow(window);
}

char pollEventWindow(sfRenderWindow* window, sfEvent* event) {
  return _pollEventWindow(window, event);
}

void closeWindow(sfRenderWindow* window) {
  _closeWindow(window);
}

void clearWindow(sfRenderWindow* window, sfColor color) {
  _clearWindow(window, color);
}

void displayWindow(sfRenderWindow* window) {
  _displayWindow(window);
}

void destroyWindow(sfRenderWindow* window) {
  _destroyWindow(window);
}

void handleDefaultEvents(sfRenderWindow* window) {
  sfEvent event;
  while( pollEventWindow( window, &event ) )
    if( event.type == sfEvtClosed )
      closeWindow( window );
}
