import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.stringy_keymaps import StringyKeymaps

PlanckHW = KMKKeyboard()

PlanckHW.modules.append(Layers())
PlanckHW.extensions.append(StringyKeymaps())

LOWER = KC.MO(1)
RAISE = KC.MO(2)
xx = "NO"
__ = "TRNS"

# fmt: off
PlanckHW.keymap = [
    # layer 0, Qwerty
    [
        'ESC',     'Q',    'W',    'E',   'R',   'T',   'Y',    'U',     'I',     'O',     'P',  'BSPC',
        'TAB',     'A',    'S',    'D',   'F',   'G',   'H',    'J',     'K',     'L',  'SCLN',  'QUOT',
        'LSFT',    'Z',    'X',    'C',   'V',   'B',   'N',    'M',  'COMM',   'DOT',  'SLSH',   'ENT',
        'BSPC', 'LCTL', 'LALT', 'LGUI', LOWER,    'SPC',    RAISE,    'LEFT',  'DOWN',    'UP', 'RIGHT',
    ],
        # layer 1, LOWER
    [
             __,    '1',    '2',     '3',      '4',      '5',   '6',        '7',       '8',       '9',      '0',      __,
         ' TAB', 'EXLM',   'AT',  'HASH',    'DLR',   'PERC',   'CIRC',  'AMPR',    'ASTR',    'LPRN',   'RPRN',      __,
         'LSFT', 'TILD',  'EQL',  'PLUS',   'MINS',   'UNDS',   'LBRC',  'RBRC',    'LCBR',    'RCBR',  'BSLSH',  'PIPE',
        'GRAVE',     __,     __,      __,    LOWER,         'SPC',           xx,        __,        __,       __,      __,
    ],

]



if __name__ == "__main__":
    PlanckHW.go()
