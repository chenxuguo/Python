from settings import SAVED_SETTINGS, DEFAULT_COLORS
from simplified_pygame import SPRITES, Canvas, assets_path

# upload sprited
sprites = Canvas.load(assets_path('menu_sprites.png'), corner_alpha=True)
items = """ \
    _1 _8
    _2 _3 _4
    _5 _6 _7
    _wasd arrows controller
    """
for k, line in enumerate(items.split('\n')):
    for i, U in enumerate(line.split()):
        X, Y = 5 + i*176, 5 + k*106
        SPRITES[U] = sprites.crop(X, Y, 175, 105)


def make_game_mode_sprites():
    new_color = SAVED_SETTINGS['color_scheme']
    for i in range(1, 9):
        color_scheme = {tuple(col): tuple(new_color[k]) for k, col in DEFAULT_COLORS.items()}
        SPRITES[str(i)] = SPRITES['_' + str(i)].replace_colors(color_scheme)

def make_letters_sprite():
    SPRITES['wasd'] = s = SPRITES['_wasd'].copy()
    letters = {v: k.replace('comma', '<').replace('period', '>').upper() for k, v in SAVED_SETTINGS['letters'].items()}
    if 'up' in letters:
        s.write(62, 10, letters['up'], size=20, font='cambria', col=(0, 0, 0), pos='.')
    if 'down' in letters:
        s.write(62, 50, letters['down'], size=20, font='cambria', col=(0, 0, 0), pos='.')
    if 'left' in letters:
        s.write(22, 50, letters['left'], size=20, font='cambria', col=(0, 0, 0), pos='.')
    if 'right' in letters:
        s.write(102, 50, letters['right'], size=20, font='cambria', col=(0, 0, 0), pos='.')


make_game_mode_sprites()
make_letters_sprite()