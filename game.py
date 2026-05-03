import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAP_X = 30
MAP_Y = 30

window = arcade.Window(SCREEN_WIDTH,SCREEN_HEIGHT,"Facebook Cooking Game")
window.center_window()
window.background_color = arcade.color.AMAZON

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.sprite_list = arcade.SpriteList()
        self.camera = arcade.camera.Camera2D()
        self.gui_cam = arcade.camera.Camera2D()
        self.dragging = False
        self.last_mouse_pos = (0,0)

        start_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT // 2
        TILE_WIDTH = 64
        TILE_HEIGHT = 32
        map_base = [[0 for _ in range(MAP_X)] for _ in range(MAP_Y)]
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
}

        for row in range(len(map_base)):
            for col in range(len(map_base[0])):
                center_col = (MAP_X - 1)/2
                center_row = (MAP_Y - 1)/2

                cx = start_x + (col - center_col - (row - center_row)) * TILE_WIDTH // 2
                cy = start_y + (col - center_col + (row - center_row)) * TILE_HEIGHT // 2

                sprite = arcade.Sprite(tiles[map_base[row][col]])
                sprite.center_x = cx
                sprite.center_y = cy
                sprite.width = TILE_WIDTH
                sprite.height = TILE_HEIGHT

                self.sprite_list.append(sprite)

        for row in range(len(mapa)):
            for col in range(len(mapa[0])):
                center_col = (MAP_X - 1) //6
                center_row = (MAP_Y - 1) //6
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
        self.camera.use()
        self.sprite_list.draw()

        self.gui_cam.use()
        arcade.draw_text(
            "Dinheiro: 100€",
            10,SCREEN_HEIGHT - 30,
            arcade.color.WHITE,
            20
        )
        

    def on_mouse_drag(self, x, y, dx, dy, _buttons, _modifiers):
        if _buttons & arcade.MOUSE_BUTTON_LEFT:
            self.camera.position = (
                self.camera.position[0] - dx,
                self.camera.position[1] - dy
            )
            
        

game = GameView()

window.show_view(game)

arcade.run()