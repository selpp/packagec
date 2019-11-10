#ifndef _lcsfml
#define _lcsfml
#include <SFML/Graphics.h>
#include <SFML/System.h>
#endif

void drawCircle( sfRenderWindow* window, sfVector2f position, float radius,
                 sfColor color, int outline_thickness, sfColor outline_color );

void drawRectangle( sfRenderWindow* window, sfVector2f position,
                    sfVector2f size, sfColor color, int outline_thickness,
                    sfColor outline_color );

void drawConvexPolygone( sfRenderWindow* window, sfVector2f* positions,
                         int size, sfColor color, int outline_thickness,
                         sfColor outline_color );

void drawSprite( sfRenderWindow* window, sfVector2f position, sfVector2f scale,
                 sfTexture** manager, int idx );
