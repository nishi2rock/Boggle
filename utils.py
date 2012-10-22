#!/usr/bin/python

def adjacentCells(coords, adjy="VHC", filterNeg=True):
    """ Given a tuple, ``coords`` containing row number and a column number,
    return co-ordinates of all the possible adjacent cells. """

    rNum, cNum = coords

    relPos = []
    if "V" in adjy:
        relPos += [(0, 1), (0, -1)]

    if "H" in adjy:
        relPos += [(1, 0), (-1, 0)]

    if "C" in adjy:
        relPos += [(-1, -1), (1, -1),
                   (-1, 1), (1, 1)]

    adjCells = [(rNum + p[0], cNum + p[1]) for p in relPos]

    onlyPositive = lambda cell: cell[0] >= 0 and cell[1] >= 0
    if filterNeg:
        adjCells = filter(onlyPositive, adjCells)

    return adjCells
