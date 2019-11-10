// ========= LIBRARIES ==========
#include <stdio.h>
#include <stdlib.h>

#include <SFML/Graphics.h>
#include <SFML/System.h>

#include "utils.h"
#include "draw.h"

// ========= WINDOW =============
#define TITLE          "SFML Window"
#define WIDTH          800
#define HEIGHT         600
#define BITS_PER_PIXEL 32
#define FPS_CAP        60

// ========= VARIABLES ==========
sfVideoMode     mode;
sfRenderWindow* window;
sfEvent         event;

// ========= LOOP ===============
int main( int args, char* argv[ ] ) {
  mode   = Mode( WIDTH, HEIGHT, BITS_PER_PIXEL );
  window = sfRenderWindow_create( mode, TITLE, sfResize | sfClose, NULL );
  if( !window ) FAILURE( "window" );

  setFPSCapWindow( ( sfWindow* ) window, FPS_CAP );

  while( isOpenWindow( window ) ) {

    while( pollEventWindow( window, &event ) )
      if( event.type == sfEvtClosed )
        closeWindow( window );

    clearWindow( window, sfBlack );

    drawCircle( window, Vec2f(  0.f, 0.f ), 30.0f, WHITE, 0, BLACK );
    drawRectangle( window, Vec2f( 50.f, 50.f ), Vec2f( 50.f, 50.f ), WHITE, 0, BLACK );

    sfVector2f points[ ] = { Vec2f( 100.f, 100.f ), Vec2f( 100.f, 150.f ), Vec2f( 150.f, 125.f ) };
    drawConvexPolygone( window, points, 3, RGB( 255, 0, 0 ), 0, BLACK );

    displayWindow( window );
  }

  destroyWindow( window );

  return 0;
}
