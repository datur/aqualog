from enum import Enum


class WaterType(Enum):
    FRESH = 1
    SALT = 2
    BRACKISH = 3

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class WaterUnitType(Enum):
    LITRES = 1
    GALLONS = 2

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class PlantSizeType(Enum):
    FOREGROUND = 1
    MIDGROUND = 2
    BACKGROUND = 3

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class DoseUnits(Enum):
    GRAMS: 1
    MILLILITRES: 2

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
