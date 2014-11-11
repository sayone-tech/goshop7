from oscar.apps.basket.abstract_models import (
    AbstractBasket, AbstractLine, AbstractLineAttribute)


class InvalidBasketLineError(Exception):
    pass


class Basket(AbstractBasket):
    pass


class Line(AbstractLine):
    pass

    @property
    def description(self):
        product = (self.product)
        if not product.is_variant:
            return product.get_title()
        return ('%s (%s ,%s)' % (product.get_title(),
                product.get_my_size(),
                product.get_my_color())).strip()


class LineAttribute(AbstractLineAttribute):
    pass
