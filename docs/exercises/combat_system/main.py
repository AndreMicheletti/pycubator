"""
Sprite Collect Coins with Background

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins_background
"""

import arcade
import pytweening
from arcade import gl

from tween import TweenManager

from game_data import GameData

# Forces all future SpriteLists to use Nearest Neighbor pixel filtering
arcade.SpriteList.DEFAULT_TEXTURE_FILTER = gl.NEAREST, gl.NEAREST

arcade.resources.load_kenney_fonts()

PLAYER_SCALING = 3

WINDOW_WIDTH = 1280 / 2
WINDOW_HEIGHT = 720 / 2
WINDOW_TITLE = "Sistema de Combate"


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """Initializer"""

        # Call the parent class initializer
        super().__init__()

        # Background image will be stored in this variable
        self.background = arcade.load_texture("assets/bg.png")
        
        self.game_data = GameData()
        self.running_turn = False

        # Variables that will hold sprite lists
        arcade.load_texture("assets/players/rogues-0.png")
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("assets/players/rogues-0.png")
        self.player_list.append(self.player_sprite)

        self.enemy_sprite = arcade.Sprite("assets/monsters/monsters-0.png")
        self.player_list.append(self.enemy_sprite)

        # Set the background color
        self.background_color = arcade.color.AMAZON

    def reset(self):
        """Restart the game."""
        # Set up the player
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 75
        self.player_sprite.scale = PLAYER_SCALING
        self.player_sprite.scale_x = -PLAYER_SCALING

        self.enemy_sprite.center_x = WINDOW_WIDTH - 200
        self.enemy_sprite.center_y = 75
        self.enemy_sprite.scale = PLAYER_SCALING

    def on_update(self, delta_time: float):
        TweenManager.update(delta_time)

        if self.running_turn:
            return
        
        rodada = self.game_data.executar_rodada()
        print("TEVE RODADA? ", rodada)
        if rodada is None:
            return
        if rodada == {}:
            return

        self.running_turn = True
        dano = rodada.get("dano", 10)
        alvo = rodada.get("alvo", "")
        if str(alvo).lower() == "jogador":
            if dano > 0: self.animate_hit(self.player_sprite)
            self.animate_attack(self.enemy_sprite, movement=-50, callback=self.reseta_running)
        else:
            if dano > 0: self.animate_hit(self.enemy_sprite)
            self.animate_attack(self.player_sprite, callback=self.reseta_running)

    def reseta_running(self):
        self.running_turn = False

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the background texture
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT),
        )

        # Draw all the sprites.
        self.player_list.draw()

    def animate_hit(self, sprite, callback=None):
        """Animate a sprite being hit."""
        TweenManager.to(
            sprite=sprite,
            property_name="alpha",
            target_val=0,
            duration=0.1,
            easing_func=pytweening.easeInOutSine,
            callback=lambda: TweenManager.to(
                sprite=sprite,
                property_name="alpha",
                target_val=255,
                duration=0.3,
                easing_func=pytweening.easeInOutSine,
                callback=callback,
            ),
        )

    def animate_attack(self, sprite, movement=50, callback=None):
        """Animate a sprite attacking."""
        original_x = sprite.center_x
        TweenManager.to(
            sprite=sprite,
            property_name="center_x",
            target_val=original_x + movement,
            duration=0.2,
            easing_func=pytweening.easeInOutSine,
            callback=lambda: TweenManager.to(
                sprite=sprite,
                property_name="center_x",
                target_val=original_x,
                duration=0.8,
                easing_func=pytweening.easeInOutSine,
                callback=callback,
            ),
        )


def main():
    """Main function"""
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()
    game.reset()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
