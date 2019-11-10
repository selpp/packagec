#include "draw.h"

// ========= DRAW ===============
void drawCircle( sfRenderWindow* window, sfVector2f position, float radius, sfColor color, int outline_thickness, sfColor outline_color ) {
  sfCircleShape* circle = sfCircleShape_create( );
  sfCircleShape_setPosition( circle, position );
  sfCircleShape_setRadius( circle, radius );
  sfCircleShape_setFillColor( circle, color );
  sfCircleShape_setOutlineThickness( circle, outline_thickness );
  sfCircleShape_setOutlineColor( circle, outline_color );
  sfRenderWindow_drawShape( window, ( sfShape* ) circle, NULL );
}

void drawRectangle( sfRenderWindow* window, sfVector2f position, sfVector2f size, sfColor color, int outline_thickness, sfColor outline_color ) {
  sfRectangleShape* rectangle = sfRectangleShape_create( );
  sfRectangleShape_setPosition( rectangle, position );
  sfRectangleShape_setSize( rectangle, size );
  sfRectangleShape_setFillColor( rectangle, color );
  sfRectangleShape_setOutlineThickness( rectangle, outline_thickness );
  sfRectangleShape_setOutlineColor( rectangle, outline_color );
  sfRenderWindow_drawShape( window, ( sfShape* ) rectangle, NULL );
}

void drawConvexPolygone( sfRenderWindow* window, sfVector2f* positions, int size, sfColor color, int outline_thickness, sfColor outline_color ) {
  sfConvexShape* convex_polygone = sfConvexShape_create( );
  sfConvexShape_setPointCount( convex_polygone, size );

  for( int i = 0; i < size; i++ )
    sfConvexShape_setPoint( convex_polygone, i, *( positions + i ) );

  sfConvexShape_setFillColor( convex_polygone, color );
  sfConvexShape_setOutlineThickness( convex_polygone, outline_thickness );
  sfConvexShape_setOutlineColor( convex_polygone, outline_color );
  sfRenderWindow_drawShape( window, ( sfShape* ) convex_polygone, NULL );
}
