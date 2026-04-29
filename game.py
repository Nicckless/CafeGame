import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAP_X = 5
MAP_Y = 10

window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,"Facebook Cooking Game")
window.center_window()
window.background_color = arcade.color.AMAZON

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.sprite_list = arcade.SpriteList()

        start_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT // 2
        TILE_WIDTH = 64
        TILE_HEIGHT = 32

        mapa = [
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,0,0,0,0],
        ]

        tiles = {
            0: "media.png",
            1: "woodFloor.png",
            2: "dirt.png",
}
        
        for row in range(len(mapa)):
            for col in range(len(mapa[0])):
                center_col = (MAP_X - 1) / 2
                center_row = (MAP_Y - 1) / 2
                cx = start_x + (col - center_col - (row - center_row)) * TILE_WIDTH // 2
                cy = start_y + (col - center_col + (row - center_row)) * TILE_HEIGHT // 2

                # p1 = (cx,cy)
                # p2 = (cx + size,cy - size / 2)
                # p3 = (cx,cy - size)
                # p4 = (cx - size,cy - size / 2)

                sprite = arcade.Sprite(tiles[mapa[row][col]])
                sprite.center_x = cx
                sprite.center_y = cy
                sprite.width = TILE_WIDTH
                sprite.height = TILE_HEIGHT

                self.sprite_list.append(sprite)
                # arcade.draw_polygon_filled([p1,p2,p3,p4],arcade.color.GRAY)

                # arcade.draw_polygon_outline([p1,p2,p3,p4],arcade.color.WHITE,2)

                
    
    def on_draw(self)->None:
        self.clear()
        self.sprite_list.draw()
        

game = GameView()

window.show_view(game)

arcade.run()