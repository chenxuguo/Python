import sys

import pygame
import simplified_pygame

import game_modes as game
import tetris
import settings
from settings import SAVED_SETTINGS, ACTIVE_SETTINGS



SCREEN = simplified_pygame.PyGameWindow(
    w=SAVED_SETTINGS['w'],
    h=SAVED_SETTINGS['h'],
    caption='Tetris for two',
    use_icon=True,
    bg_color=ACTIVE_SETTINGS['color_scheme']['background'],
    default_font='cambria',
    resizable=True)


import sprites


GAME_MODES = {
    # inner_index: row, name, text
    '1': (2, 'Single Player',  game.TetrisGame),
    '2': (4, 'Parallel Match', game.TetrisGame2Players),
    '3': (5, 'Mirror Match',   game.TetrisGameMirror),
    '4': (6, 'Speed-up',       game.TetrisGameSpeedUp),
    '5': (8, 'Control Swap',   game.TetrisGameSwap),
    '6': (9, 'Balanced Wells', game.TetrisGameBalance),
    '7': (10, 'Common Well',   game.TetrisGameCommonWell),
    '8': (11, 'Heart-shaped Well',    game.TetrisHeartMode)
    }


def startgame(mode):
    global GAME
    global GAME_STATE
    for k in 'wasd arrows controller shadow letters bleed'.split():
        ACTIVE_SETTINGS[k] = SAVED_SETTINGS[k]
    GAME = GAME_MODES[mode][2]()
    GAME_STATE = 'pause'

def window_resize(w=1200, h=800):
    scale = min(w/600, h/400)
    screen_w = int(600 * scale)
    screen_h = int(400 * scale)
    screen_x0 = (w - screen_w) // 2
    screen_y0 = (h - screen_h) // 2
    SCREEN.set_game_resolution(w, h)
    #SCREEN.x0 = w // 2
    SCREEN.y0 = screen_y0
    ACTIVE_SETTINGS['scale'] = scale
    ACTIVE_SETTINGS['size'] = int(10*scale)
    SAVED_SETTINGS['w'] = w
    SAVED_SETTINGS['h'] = h

def select_buttons():
    global GAME_STATE
    GAME_STATE = 'select_buttons'
    MenuLetterSelector.selector = [
        ['left', 'press [move left]'],
        ['right', 'press [move right]'],
        ['down', 'press [move down]'],
        ['up', 'press [rotate]']]
    SAVED_SETTINGS['letters'] = {}


class AppControlls(simplified_pygame.EventReaderAsClass):

    def on_key_escape():
        global GAME_STATE
        if GAME_STATE in ('pause', 'game', 'settings'):
            GAME_STATE = 'menu'
        elif GAME_STATE == 'select_buttons':
            GAME_STATE = 'settings'
        elif GAME_STATE == 'menu':
            SCREEN.exit()

    def on_key_space():
        global GAME_STATE
        GAME_STATE = {
            'game': 'pause',
            'pause': 'game',
            'menu': 'menu',
            'settings': 'menu',
            'select_buttons': 'settings'}[GAME_STATE]

    def on_key_joy_start(cls):
        AppControlls.on_key_space()

    def on_window_resize(w, h):
        window_resize(w, h)


class MenuGameSelector(simplified_pygame.EventReaderAsClass):
    def on_any_key(key):
        if key in GAME_MODES:
            startgame(key)

    def on_mouse_click(button):
        startgame(button)

    @classmethod
    def draw(cls, W):
        size = ACTIVE_SETTINGS['size']
        x0 = SCREEN.w // 2 - size*5
        for key, (i, name, *_) in GAME_MODES.items():
            if key == cls._mouse_pos:
                W.rect((x0-size, (i*3-1)*size, 13*size, 3.5*size), (255, 200, 100))
                cls.draw_help(W, key)
            W.write(x0, i*size*3, f'[{key}] {name}', col=(0, 0, 0), size=int(size*1))

        W.write(x0, 1*size*3, 'Single Player:', font='cambria-bold', size=size)
        W.write(x0, 3*size*3, 'Competition:', font='cambria-bold', size=size)
        W.write(x0, 7*size*3, 'Cooperation:', font='cambria-bold', size=size)

    def draw_help(W, key):
        size = ACTIVE_SETTINGS['size']
        scale = ACTIVE_SETTINGS['scale']
        x0 = SCREEN.w // 4 * 3 - size
        W.rect((x0, size*1, size*15, size*28), (255, 200, 100))
        W.sprite(x0+size*3, size*3, str(key), scale=scale/2)
        _, name, obj = GAME_MODES[key]
        W.write(x0, 10*size, "    "+name, font='cambria-bold', size=size)
        W.write(x0, 10*size, str(obj.__doc__), size=size)

    def mouse_map(x, y):
        size = ACTIVE_SETTINGS['size']
        if -5 < (x - SCREEN.w /2) / size < 5:
            y = int(((y-SCREEN.y0) / size + 1) / 3)
            for key, (i, *_) in GAME_MODES.items():
                if i == y:
                    return key


class MenuSwapButton(simplified_pygame.EventReaderAsClass):
    @classmethod
    def draw(cls, W):
        size = ACTIVE_SETTINGS['size']
        scale = ACTIVE_SETTINGS['scale']
        x = SCREEN.w // 4 * 3
        y = 33 * size
        w = 14 * size
        h = 4 * size

        title = {
            'menu': 'Settings',
            'settings': 'Back',
            'select_buttons': 'Back'}[GAME_STATE]
        if cls._mouse_pos:
            W.rect((x, y, w, h), (255, 200, 100))
        W.write(x+w/2, y+size, title, size=size, pos='.', font='cambria-bold')

    def mouse_map(x, y):
        size = ACTIVE_SETTINGS['size']
        x = (x - SCREEN.w/4*3) / size
        y = int((y-SCREEN.y0)/size + 1)
        if simplified_pygame.in_box(x, y, (0, 33, 14, 4)):
            return True

    def on_mouse_click(_):
        global GAME_STATE
        GAME_STATE = {
            'menu': 'settings',
            'settings': 'menu'}[GAME_STATE]
        simplified_pygame.mixer.play_sound('pop0')


BUTTONS = [
    ((0, 7, 14, 6), 'wasd', ''),
    ((0, 13, 14, 6), 'arrows', ''),
    ((0, 19, 14, 6), 'controller', ''),
]


class MenuControlls(simplified_pygame.EventReaderAsClass):
    @classmethod
    def draw(cls, W):
        size = ACTIVE_SETTINGS['size']
        scale = ACTIVE_SETTINGS['scale']
        x0 = SCREEN.w // 4 * 3

        for (x, y, w, h), sprite, title in BUTTONS:
            if sprite == cls._mouse_pos:
                W.rect((x0+x*size, y*size, w*size, h*size), (255, 200, 100))
            W.write(x0+(x+1)*size, (y+1)*size, title, size=size)

            if sprite in 'arrows wasd controller':
                if SAVED_SETTINGS[sprite]:
                    W.sprite(x0+6*size, (y+1)*size, sprite, scale=scale/2)
                    W.write(x0+2*size, (y+2)*size, '<', size=size*2)
                else:
                    W.sprite(x0+size, (y+1)*size, sprite, scale=scale/2)
                    W.write(x0+10*size, (y+2)*size, '>', size=size*2)

        W.write(x0, 3*size, 'Controlls:', font='cambria-bold', size=size)
        W.write(x0, 5*size, 'Left Player           Right Player', size=size)

    def mouse_map(x, y):
        size = ACTIVE_SETTINGS['size']
        x = (x - SCREEN.w/4*3) / size
        y = int((y-SCREEN.y0)/size + 1)
        for (x0, y0, w, h), action, _ in BUTTONS:
            if simplified_pygame.in_box(x, y, (x0, y0, w, h)):
                return action

    def on_mouse_click(button):
        if button in 'arrows wasd controller':
            SAVED_SETTINGS[button] = not SAVED_SETTINGS[button]
            # guaranty there at least some controlls for everyone
            if SAVED_SETTINGS['arrows'] == SAVED_SETTINGS['wasd'] == SAVED_SETTINGS['controller']:
                for i in 'arrows wasd controller'.split():
                    if i != button:
                        SAVED_SETTINGS[i] = not SAVED_SETTINGS[i]
        simplified_pygame.mixer.play_sound('pop0')


SETTIGS_BUTTONS = [
    ((0, 3, 0, 0), 'Color Scheme:', 'title'),
    ((0, 4, 10, 3), 'Default', ['set', 'color_scheme', settings.DEFAULT_COLORS]),
    ((0, 7, 10, 3), 'Piet Mondrian', ['set', 'color_scheme', settings.MONDRIAN_COLORS]),
    ((0, 10, 10, 3), 'Leonardo da Vinci', ['set', 'color_scheme', settings.LEONARDO_COLORS]),
    ((0, 13, 10, 3), 'John Everett Millais', ['set', 'color_scheme', settings.MILLAIS_COLORS]),
    ((0, 16, 10, 3), 'Vincent van Gogh', ['set', 'color_scheme', settings.VAN_GOGH_COLORS]),
    ((0, 19, 10, 3), 'Gustav Klimt', ['set', 'color_scheme', settings.KLIMT_COLORS]),

    ((0, 25, 0, 0), 'Color blending effect:', 'title'),
    ((0, 26, 4, 3), 'Off', ['set', 'bleed', False]),
    ((4, 26, 4, 3), 'On', ['set', 'bleed', True]),

    ((14, 3, 0, 0), 'Keyboard Layout:', 'title'),
    ((14, 4, 10, 3), 'QWERT', ['set', 'letters', simplified_pygame.WASD_AS_ARROWS]),
    ((14, 7, 10, 3), 'AZERT', ['set', 'letters', simplified_pygame.ZQSD_AS_ARROWS]),
    ((14, 10, 10, 3), 'Dvorak', ['set', 'letters', simplified_pygame.AOE_AS_ARROWS]),
    ((14, 13, 10, 3), 'Colemak', ['set', 'letters', simplified_pygame.WARS_AS_ARROWS]),
    ((15, 17, 0, 0), '', ['sprite', 'wasd']),
    ((14, 22, 10, 3), 'Select Buttons...', ['do', select_buttons]),

    ((28, 3, 0, 0), 'Figures cast shadows:', 'title'),
    ((28, 4, 3, 3), 'Yes', ['set', 'shadow', True]),
    ((33, 4, 3, 3), 'No', ['set', 'shadow', False]),

    ((28, 10, 0, 0), 'Sound:', 'title'),
    ((28, 11, 4, 3), 'Off', ['set', 'volume', 0]),
    ((32, 11, 4, 3), '1/2', ['set', 'volume', 0.5]),
    ((36, 11, 4, 3), 'On', ['set', 'volume', 1]),

    ((28, 17, 0, 0), 'Screen:', 'title'),
    ((28, 18, 10, 3), 'Reset Screen Size', ['do', window_resize]),
]


class MenuSettings(simplified_pygame.EventReaderAsClass):

    def draw( W):
        selected_col = [min(255, x+30) for x in ACTIVE_SETTINGS['color_scheme']['background']]
        size = ACTIVE_SETTINGS['size']
        scale = ACTIVE_SETTINGS['scale']
        x0 = SCREEN.w // 2 - size * 12

        for (x, y, w, h), text, action in SETTIGS_BUTTONS:
            box = (x0+x*size, (y+0.1)*size, w*size, h*size)

            col = (0, 0, 0)
            if action[0] == 'set':
                _, par, val = action
                if SAVED_SETTINGS[par] == val:
                    W.rect(box, selected_col)

            if action == MenuSettings._mouse_pos:
                W.rect(box, (255, 200, 100))

            if action == 'title':
                W.write(x0+x*size, y*size, text, size=size, font='cambria-bold')
            else:
                W.write(x0+(x+1)*size, (y+1)*size, text, size=size)
            if action[0] == 'sprite':
                W.sprite(x0+x*size, y*size, action[1], scale=scale/2)

    def mouse_map(x, y):
        size = ACTIVE_SETTINGS['size']
        x = (x - SCREEN.w/2) / size + 12
        y = int((y-SCREEN.y0)/size + 1)
        for (x0, y0, w, h), text, action in SETTIGS_BUTTONS:
            if simplified_pygame.in_box(x, y, (x0, y0, w, h)) and not (w == h == 0):
                return action

    def on_mouse_click(action):
        if action[0] == 'set':
            _, par, val = action
            SAVED_SETTINGS[par] = val
            if par == 'volume':
                simplified_pygame.mixer.volume = SAVED_SETTINGS['volume']
            elif par == 'color_scheme':
                ACTIVE_SETTINGS['color_scheme'].update(val)
                start_title.__init__()
                sprites.make_game_mode_sprites()
                SCREEN.bg_color=SAVED_SETTINGS[par]['background'],
            elif par == 'bleed':
                ACTIVE_SETTINGS['bleed'] = val
                start_title.__init__()
            elif par == 'letters':
                sprites.make_letters_sprite()

        if action[0] == 'do':
            action[1]()

        simplified_pygame.mixer.play_sound('pop0')


class MenuLetterSelector(simplified_pygame.EventReaderAsClass):
    def draw(W):
        size = ACTIVE_SETTINGS['size']
        x0 = SCREEN.w // 2
        y0 = size*26
        with W.part(x0, y0, size*14, size*10, (0, 0, 0, 200)) as C:
            C.write(size*7, size*4, MenuLetterSelector.selector[0][1], col=(255, 255, 255), pos='.')

    @classmethod
    def on_any_key(cls, key):
        (action, _), *cls.selector = cls.selector
        # activate saving
        letters = SAVED_SETTINGS['letters']
        letters[key] = action
        SAVED_SETTINGS['letters'] = letters

        sprites.make_letters_sprite()
        if not cls.selector:
            global GAME_STATE
            GAME_STATE = 'settings'


GAME = None
GAME_STATE = "menu"

window_resize(SCREEN.w, SCREEN.h)
simplified_pygame.mixer.volume = SAVED_SETTINGS['volume']
start_title = tetris.StartTitle()


for events, time_passed, pressed_keys in SCREEN.main_loop(framerate=600):
    AppControlls.read_events(events, time_passed, pressed_keys)
    if GAME_STATE == 'game':
        GAME.read_events(events, time_passed, pressed_keys)
    elif GAME_STATE == 'menu':
        MenuGameSelector.read_events(events, time_passed, pressed_keys)
        MenuControlls.read_events(events, time_passed, pressed_keys)
        MenuSwapButton.read_events(events, time_passed, pressed_keys)
        start_title.read_events(events, time_passed, pressed_keys)
    elif GAME_STATE == 'settings':
        MenuSettings.read_events(events, time_passed, pressed_keys)
        MenuSwapButton.read_events(events, time_passed, pressed_keys)
        start_title.read_events(events, time_passed, pressed_keys)
    elif GAME_STATE == 'select_buttons':
        MenuLetterSelector.read_events(events, time_passed, pressed_keys)

    if GAME_STATE == 'game':
        GAME.draw_game(SCREEN)
    elif GAME_STATE == "pause":
        GAME.draw_game(SCREEN)
        GAME.draw_pause(SCREEN)
    elif GAME_STATE == "menu":
        start_title.draw(SCREEN)
        MenuControlls.draw(SCREEN)
        MenuGameSelector.draw(SCREEN)
        MenuSwapButton.draw(SCREEN)
    elif GAME_STATE == "settings":
        start_title.draw(SCREEN)
        MenuSettings.draw(SCREEN)
        MenuSwapButton.draw(SCREEN)
    elif GAME_STATE == "select_buttons":
        start_title.draw(SCREEN)
        MenuSettings.draw(SCREEN)
        MenuSwapButton.draw(SCREEN)
        MenuLetterSelector.draw(SCREEN)

print ('GAME OVER')
