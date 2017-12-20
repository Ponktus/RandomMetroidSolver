#!/usr/bin/env python

import sys

from parameters import *
from helpers import *
from solver import ParamsLoader

def stuff(base, nEtanks, nMissiles, nSupers, nPowerBombs):
    ret = base
    ret.extend(['ETank'] * nEtanks)
    ret.extend(['Missile'] * nMissiles)
    ret.extend(['Super'] * nSupers)
    ret.extend(['PowerBomb'] * nPowerBombs)
    return ret

itemSets = {
    'Kraid' : {
        'Standard' : stuff(['Spazer', 'Charge'], 1, 4, 1, 0),
        'ChargeLess' : stuff([], 1, 4, 1, 0)
    },
    'Phantoon' : {
        'Standard' : stuff(['Spazer', 'Charge', 'Wave', 'Varia'], 5, 6, 1, 1),
        'ChargeLess' : stuff(['Varia'], 5, 6, 3, 1),
        'Tough' : stuff(['Charge', 'Wave'], 5, 3, 1, 1)
    },
    'Draygon' : {
        'Standard' : stuff(['Spazer', 'Charge', 'Wave', 'Ice', 'Varia', 'Gravity'], 7, 10, 4, 3),
        'ChargeLess' : stuff(['Varia', 'Gravity'], 7, 10, 6, 3),
        'Tough' : stuff(['Charge', 'Wave', 'Ice', 'Varia', 'Gravity'], 5, 8, 2, 3),
    },
    'Ridley' : {
        'Standard' : stuff(['Plasma', 'Charge', 'Wave', 'Ice', 'Varia', 'Gravity'], 9, 10, 6, 3),
        'ChargeLess' : stuff(['Varia', 'Gravity'], 9, 10, 9, 3),
        'Tough' : stuff(['Spazer', 'Charge', 'Wave', 'Ice', 'Varia', 'Gravity'], 5, 10, 3, 3)
    },
    'MotherBrain' : {
        'Standard' : stuff(['Plasma', 'Charge', 'Wave', 'Ice', 'Varia', 'Gravity'], 9, 10, 6, 3),
        'ChargeLess' : stuff(['Varia', 'Gravity'], 9, 10, 14, 3),
        'Tough' : stuff(['Spazer', 'Charge', 'Wave', 'Ice', 'Varia', 'Gravity'], 5, 10, 5, 3)
    }
}

def boss(name, diffFunction):
    print("*** " + name + " ***")
    for setName, itemSet in itemSets[name].items():
        print('* ' + setName)
#        print(str(itemSet))
        d = diffFunction(itemSet)
        print('---> ' + str(d))

if __name__ == "__main__":
    params=None
    if len(sys.argv) >= 2:
        params = sys.argv[1]
    ParamsLoader.factory(params).load()
    print(str(Settings.bossesDifficulty))

    boss('Kraid', enoughStuffsKraid)
    boss('Phantoon', enoughStuffsPhantoon)
    boss('Draygon', enoughStuffsDraygon)
    boss('Ridley', enoughStuffsRidley)
    boss('MotherBrain', enoughStuffsMotherbrain)
