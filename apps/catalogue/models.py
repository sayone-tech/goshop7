"""
Vanilla product models
"""
from oscar.apps.catalogue.abstract_models import *  # noqa

from apps.utils.constants import ProductConstants


class Product(AbstractProduct):
    pass

    def get_size_list(self):
        """
        get all variants size list
        """
        ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
        if self.is_variant:
            parent = self.parent
            _varients_ids = parent.variants.all().values_list('id', flat=True)
            varients_ids = []
            my_color = self.get_my_color()
            for id in _varients_ids:
                attr_val = ProductAttributeValue.objects.filter(
                    product__id=id,
                    attribute__name__iexact=ProductConstants.color)
                if attr_val:
                    if '%s' % attr_val[0].value == my_color:
                        varients_ids.append(id)
            if not varients_ids:
                varients_ids = _varients_ids
            values = ProductAttributeValue.objects.filter(
                attribute__name__iexact=ProductConstants.size,
                product__id__in=varients_ids)
            return [('%s' % val.value, '%s' % val.product.get_absolute_url())
                    for val in values]
        return []

    def get_color_list(self):
        """
        get all variants color list
        """
        ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
        if self.is_variant:
            parent = self.parent
            _varients_ids = parent.variants.all().values_list('id', flat=True)
            varients_ids = []
            my_size = self.get_my_size()
            for id in _varients_ids:
                attr_val = ProductAttributeValue.objects.filter(
                    product__id=id,
                    attribute__name__iexact=ProductConstants.size)
                if attr_val:
                    if '%s' % attr_val[0].value == my_size:
                        varients_ids.append(id)
            if not varients_ids:
                varients_ids = _varients_ids
            values = ProductAttributeValue.objects.filter(
                attribute__name__iexact=ProductConstants.color,
                product__id__in=varients_ids)
            return [('%s' % val.value, '%s' % val.product.get_absolute_url())
                    for val in values]
        return []

    def get_my_size(self):
        ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
        values = ProductAttributeValue.objects.filter(
            attribute__name__iexact=ProductConstants.size,
            product=self)
        if values.count() > 0:
            return '%s' % values[0].value
        return ""

    def get_my_color(self):
        ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
        values = ProductAttributeValue.objects.filter(
            attribute__name__iexact=ProductConstants.color,
            product=self)
        if values.count() > 0:
            return '%s' % values[0].value
        return ""

    @property
    def get_product(self):
        """
        Get the product if it is a varient else return
        return first varient of this product
        """
        return self.variants.all()[0] if self.is_group else self

from oscar.apps.catalogue.models import *
