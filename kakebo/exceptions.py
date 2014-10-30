#!/usr/bin/env python3

# For Json Formatter


class IllegalFormatException(ValueError):

    """ This exception means un-correct json format """


class FirstMoneyNotFoundException(ValueError):

    """ This exception means first money of Kakebo instance is not found. """


class IllegalItemException(ValueError):

    """ This exception means item in Kakebo instance is un-correct.
    """


class IllegalDateException(ValueError):

    """ This exception means date in kakebo instance is un-correct """
