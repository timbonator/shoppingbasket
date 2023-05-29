from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BasketItem:
    """An item in a shopping basket."""

    name: str
    unit_price: float
    barcode: Optional[int] = None
    units: Optional[str] = None
    quantity: float = 1.0

    @property
    def description(self):
        """A description of the item, to appear on the invoice."""
        desc = self.name
        if self.units:
            amount = f"{self.quantity}{self.units}"
            rate = f"£{self.unit_price}/{self.units}"
            desc += f"\n{amount} @ {rate}"
        return desc

    @property
    def line_price(self) -> float:
        """The price of the item."""
        return round(self.unit_price * self.quantity, 2)


@dataclass(frozen=True)
class Discount(BasketItem):
    """A discount on an item in a shopping basket.

    This is the same as a regular BasketItem, but with a negative line price.
    """

    @property
    def line_price(self) -> float:
        """The price of the discount."""
        return super().line_price * -1