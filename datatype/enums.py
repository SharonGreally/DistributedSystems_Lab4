from enum import IntEnum


class DartMultiplier(IntEnum):
    MISS = 0
    SINGLE = 1
    DOUBLE = 2
    TREBLE = 3

class MatchStatus(IntEnum):
    INVALID = 0
    WAITING = 2
    IN_PROGRESS = 3
    FINISHED = 4
