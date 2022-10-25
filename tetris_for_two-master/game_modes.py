import simplified_pygame

from settings import ACTIVE_SETTINGS

import tetris


class TetrisGame():
    """
    Regular Tetris game.
    """
    def __init__(self, w=10, h=25):
        self.well = tetris.TetrisWell(self, w, h)
        self.player = tetris.FallingFigure(self, self.well, controlls=0)
        self.do_next_turn(self.player)

    @property
    def play(self): return self.well1.play

    def read_events(self, events, dt, key_pressed):
        self.player.read_events(events, dt, key_pressed)
        self.well.read_events(events, dt, key_pressed)

    def check_collision(self, well, player, figure):
        for i, j in figure:
            if well[i, j] == '#':
                return 'blocked'
        return False

    def do_check_lines(self, well, player):
        full = well.get_full_line()
        cleared = 0
        while full:
            well.remove_line(full)
            player.score_up()
            player.speed_up()
            full = well.get_full_line()
            cleared += 1
        simplified_pygame.mixer.play_sound(f'pop{min(4, cleared)}')

    def do_game_over(self, player):
        player.play = False

    def do_next_turn(self, player):
        player.drop()

    def draw_game(self, W):
        size = ACTIVE_SETTINGS['size']
        offset = W.with_offset(W.w//2 - self.well.w//2*size, size*10)
        self.well.draw(offset)
        self.player.draw(offset)
        self.player.draw_interface(offset)

    def draw_pause(self, W):
        size = ACTIVE_SETTINGS['size']
        with W.part(0, W.h//2 - size*5, W.w, size*10, (0, 0, 50, 200)) as C:
            C.write(W.w//2, size*2, 'PAUSE', size=int(2.5*size), col=[255]*3, pos='.')
            C.write(W.w//2, size*7, 'press -space- to continue', size=int(0.7*size), col=[255]*3, pos='.')


class TetrisGame2Players(TetrisGame):
    """
    Two regular independent tetris
    games happening side by side.
    """
    def __init__(self, w=10, h=25):
        self.well1 = tetris.TetrisWell(self, w, h)
        self.well2 = tetris.TetrisWell(self, w, h)
        self.player1 = tetris.FallingFigure(self, self.well1, controlls=1)
        self.player2 = tetris.FallingFigure(self, self.well2, controlls=2)

        self.ready = [False, False]
        self.do_next_turn(self.player1)
        self.do_next_turn(self.player2)

    def read_events(self, events, dt, key_pressed):
        self.player1.read_events(events, dt, key_pressed)
        self.player2.read_events(events, dt, key_pressed)
        self.well1.read_events(events, dt, key_pressed)
        self.well2.read_events(events, dt, key_pressed)

    @property
    def play(self):
        return self.well1.play | self.well2.play

    def draw_game(self, W):
        size = ACTIVE_SETTINGS['size']

        offset = W.with_offset(W.w//4 - self.well2.w//2*size, size*10)
        self.well2.draw(offset)
        self.player2.draw(offset)
        self.player2.draw_interface(offset)

        offset = W.with_offset(W.w//4*3 - self.well1.w//2*size, size*10)
        self.well1.draw(offset)
        self.player1.draw(offset)
        self.player1.draw_interface(offset)

    def do_next_turn(self, player):
        if player is self.player1:
            self.ready[0] = True
        elif player is self.player2:
            self.ready[1] = True

        if self.ready == [True, True]:
            self.ready = [not self.player1.play, not self.player2.play]
            self.do_drop()

    def do_drop(self):
        self.player1.drop()
        self.player2.drop()


class TetrisGameSpeedUp(TetrisGame2Players):
    """
    When a line is completed,
    opponent's game speed is
    doubled until they complete
    their own line.
    """
    def do_check_lines(self, well, player):
        if player is self.player1:
            other = self.player2
        elif player is self.player2:
            other = self.player1

        full = well.get_full_line()
        cleared = 0
        while full:
            well.remove_line(full)
            player.score_up()
            full = well.get_full_line()
            player.step_duration = player.appropriate_speed()
            other.step_duration = other.appropriate_speed() // 2
            player.message = ''
            other.message = '+ speed +'
            cleared += 1
        simplified_pygame.mixer.play_sound(f'pop{min(4, cleared)}')


class TetrisGameMirror(TetrisGame2Players):
    """
    Two players are receiving
    identical figures.
    """
    def __init__(self, w=10, h=25):
        self.well1 = tetris.TetrisWell(self, w, h)
        self.well2 = tetris.TetrisWell(self, w, h)
        self.player1 = tetris.FallingFigure(self, self.well1, controlls=1)
        self.player2 = tetris.FallingFigure(self, self.well2, controlls=2)

        self.ready = [False, False]
        self.player2.nextfig = self.player1.nextfig
        self.do_next_turn(self.player1)
        self.do_next_turn(self.player2)

    def do_drop(self):
        # assume nextfigs are the same
        self.player1.drop()
        self.player2.drop()
        self.player2.nextfig = self.player1.nextfig


class TetrisGameCoop(TetrisGame2Players):

    def do_game_over(self, _):
        self.player1.play = False
        self.player2.play = False

    @property
    def play(self):
        return self.well1.play & self.well2.play


class TetrisGameBalance(TetrisGameCoop):
    """
    Heights of both wells are
    balanced, so that each player
    gets about the same amount of
    empty space.
    """
    def __init__(self):
        super().__init__(10, 20)
        self.well1.possible_h = 30
        self.well2.possible_h = 30

    def do_drop(self):
        h1 = self.well1.space_left()
        h2 = self.well2.space_left()

        if h1 > h2+1:
            self.well2.borrow_line(self.well1)

        if h2 > h1+1:
            self.well1.borrow_line(self.well2)

        self.player1.drop()
        self.player2.drop()

    def draw_game(self, W):
        size = ACTIVE_SETTINGS['size']
        super().draw_game(W.with_offset(0, -size*2))

        sub = W.crop(W.w//4 - 5*size, size*8, size*10, size*self.well2.h).flip(False, True).set_alpha(50)
        W.sprite(W.w//4*3 - 5*size, size*(9+self.well1.h), sub)

        sub = W.crop(W.w//4*3 - 5*size, size*8, size*10, size*self.well1.h).flip(False, True).set_alpha(50)
        W.sprite(W.w//4 - 5*size, size*(9+self.well2.h), sub)


class TetrisGameSwap(TetrisGameCoop):
    """
    Each turn players swap
    their controls.
    """
    def do_drop(self):
        self.player1, self.player2 =  self.player2, self.player1
        self.player1.well, self.player2.well =  self.player2.well, self.player1.well
        self.player1.nextfig, self.player2.nextfig =  self.player2.nextfig, self.player1.nextfig
        self.player1.drop()
        self.player2.drop()


class TetrisGameCommonWell(TetrisGameCoop):
    """
    Play together in the same
    big well.
    """
    def __init__(self):
        self.well = tetris.TetrisWell(self, 20, 25)
        self.player1 = tetris.FallingFigure(self, self.well, controlls=1)
        self.player2 = tetris.FallingFigure(self, self.well, controlls=2)

        self.player2.start_x = 5
        self.player1.start_x = 15
        self.ready = [False, False]
        self.do_next_turn(self.player1)
        self.do_next_turn(self.player2)

    def read_events(self, events, dt, key_pressed):
        self.player1.read_events(events, dt, key_pressed)
        self.player2.read_events(events, dt, key_pressed)
        self.well.read_events(events, dt, key_pressed)

    def check_collision(self, well, player, figure):
        for i, j in figure:
            if well[i, j] == '#':
                return 'blocked'

        # in addition, we need to check collisions between figures
        if player is self.player1:
            other = self.player2
        elif player is self.player2:
            other = self.player1
        if set(other.figure) & set(figure):
            return 'friend'

        return False

    def draw_game(self, W):
        size = ACTIVE_SETTINGS['size']
        offset = W.with_offset(W.w//2 - self.well.w//2*size, size*10)
        self.well.draw(offset)
        self.player2.draw(offset)
        self.player1.draw(offset)
        self.player2.draw_interface(offset)

    def do_check_lines(self, well, player):
        pass

    def do_drop(self):
        """ check lines and drop """
        full = self.well.get_full_line()
        cleared = 0
        while full:
            self.well.remove_line(full)
            self.player1.score_up()
            self.player1.speed_up()
            self.player2.score_up()
            self.player2.speed_up()
            full = self.well.get_full_line()
            cleared += 1

        simplified_pygame.mixer.play_sound(f'pop{min(4, cleared)}')
        self.player1.drop()
        self.player2.drop()


class TetrisSeqentialDrop(TetrisGameCoop):

    def __init__(self, w=10, h=25):
        self.well1 = tetris.TetrisWell(self, w, h)
        self.well2 = tetris.TetrisWell(self, w, h)
        self.player1 = tetris.FallingFigure(self, self.well1, controlls=1)
        self.player2 = tetris.FallingFigure(self, self.well2, controlls=2)

        self.now_playing_1 = False
        self.player2.drop()

    def read_events(self, events, dt, key_pressed):
        if self.now_playing_1:
            self.player1.read_events(events, dt, key_pressed)
        else:
            self.player2.read_events(events, dt, key_pressed)

        self.well1.read_events(events, dt, key_pressed)
        self.well2.read_events(events, dt, key_pressed)

    def do_next_turn(self, player):
        self.now_playing_1 = not self.now_playing_1
        self.do_drop()

    def do_drop(self):
        if self.now_playing_1:
            self.player1.drop()
        else:
            self.player2.drop()


class TetrisHeartMode(TetrisSeqentialDrop):
    """
    Wells with the shared bottom.
    """
    def do_next_turn(self, player):
        if self.now_playing_1:
            self.well2.flip_copy_well(self.well1, reverse=True)
            self.now_playing_1 = False
        else:
            self.well1.flip_copy_well(self.well2)
            self.now_playing_1 = True
        self.do_drop()

    def draw_game(self, W):
        size = ACTIVE_SETTINGS['size']
        P1 = simplified_pygame.Canvas(10 * size, 20 * size, dy=5 * size)
        P2 = simplified_pygame.Canvas(10 * size-1, 30 * size, dy=5 * size)
        P3 = simplified_pygame.Canvas(10 * size, 30 * size, dy=5 * size)

        self.well2.draw(P2)
        self.player2.draw(P2)
        self.player2.draw_interface(W.with_offset(W.w//4 - self.well2.w//2*size, size*10))

        self.well1.draw(P1)
        self.player1.draw(P3)
        self.player1.draw_interface(W.with_offset(W.w//4*3 - self.well1.w//2*size, size*10))

        P3 = P3.rotate(-45)
        P2 = P2.rotate(45)
        P1 = P1.rotate(-45)
        dx = P2.w / 4
        x2 = W.w//2 - int(dx*3)
        x1 = W.w//2 - int(dx)
        x3 = W.w//2

        W.sprite(x3, size*5, P1)
        W.sprite(x2, size*5, P2)
        W.sprite(x1, size*5, P3)
