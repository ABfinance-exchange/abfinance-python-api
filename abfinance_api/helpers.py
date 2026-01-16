import logging


def _opposite_side(side):
    if side == "Buy":
        return "Sell"
    else:
        return "Buy"


class Helpers:
    def __init__(self, session):
        self.logger = logging.getLogger(__name__)
        self.session = session

    def close_position(self, category, symbol) -> list:
        """Market close the positions on a certain symbol.

        Required args:
            category (string): Product type: linear,inverse
            symbol (string): Symbol name

        Returns:
            Request results as list.

