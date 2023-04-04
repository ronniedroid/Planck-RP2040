import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.stringy_keymaps import StringyKeymaps
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.capsword import CapsWord

PlanckHW = KMKKeyboard()

PlanckHW.modules.append(Layers())
PlanckHW.modules.append(CapsWord())
PlanckHW.extensions.append(StringyKeymaps())
PlanckHW.extensions.append(MediaKeys())

LOWER = KC.MO(1)
RAISE = KC.MO(2)
xx = "NO"
__ = "TRNS"
cut = KC.LCTL(KC.X)
copy = KC.LCTL(KC.C)
paste = KC.LCTL(KC.V)
close = KC.LALT(KC.Z)

# fmt: off
PlanckHW.keymap = [
    # layer 0, Qwerty
    [
        'ESC',     'Q',    'W',    'E',   'R',   'T',   'Y',    'U',     'I',     'O',     'P',  'BSPC',
        'TAB',     'A',    'S',    'D',   'F',   'G',   'H',    'J',     'K',     'L',  'SCLN',  'QUOT',
        'LSFT',    'Z',    'X',    'C',   'V',   'B',   'N',    'M',  'COMM',   'DOT',  'SLSH',   'ENT',
        'GRAVE', 'LCTL', 'LALT', 'LGUI', LOWER,    'SPC',    RAISE,    'LEFT',  'DOWN',    'UP', 'RIGHT',
    ],
        # layer 1, LOWER
    [
             __,    '1',    '2',     '3',      '4',      '5',      '6',     '7',       '8',       '9',      '0',      __,
           'CW', 'EXLM',   'AT',  'HASH',    'DLR',   'PERC',   'CIRC',  'AMPR',    'ASTR',    'LPRN',   'RPRN',      __,
         'LSFT', 'TILD',  'EQL',  'PLUS',   'MINS',   'UNDS',   'LBRC',  'RBRC',    'LCBR',    'RCBR',  'BSLSH',  'PIPE',
             xx,     __,     __,      __,       __,         'SPC',           xx,        __,        __,       __,      __,
    ],
        # layer 2, RAISE
    [
            'F12',   'F1',    'F2',    'F3',    'F4',    'F5',     'F6',    'F7',      'F8',    'F9',    'F10',  'F11',
          'RESET', 'MUTE',  'VOLD',  'VOLU',  'BRID',  'BRIU',   'PSCR',  'LEFT',    'DOWN',    'UP',  'RIGHT',     xx,
         'RELOAD',  close,     cut,    copy,   paste,      xx,    'INS',  'HOME',    'PGDN',  'PGUP',    'END',     xx,
          'DEBUG',     __,      __,      __,      xx,         'SPC',          __,        __,      __,       __,     __,
    ],
]



if __name__ == "__main__":
    PlanckHW.go()
