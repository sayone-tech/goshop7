from oscar.core.loading import get_class, get_model
from oscar.apps.dashboard.catalogue.forms import ProductForm as CoreProductForm

Product = get_model('catalogue', 'Product')
ProductClass = get_model('catalogue', 'ProductClass')
Category = get_model('catalogue', 'Category')
StockRecord = get_model('partner', 'StockRecord')
Partner = get_model('partner', 'Partner')
ProductClass = get_model('catalogue', 'ProductClass')
ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
ProductCategory = get_model('catalogue', 'ProductCategory')
ProductImage = get_model('catalogue', 'ProductImage')
ProductRecommendation = get_model('catalogue', 'ProductRecommendation')
ProductSelect = get_class('dashboard.catalogue.widgets', 'ProductSelect')
ProductSelectMultiple = get_class('dashboard.catalogue.widgets',
                                  'ProductSelectMultiple')


class ProductForm(CoreProductForm):

    # We need a special field to distinguish between group and standalone
    # products.  It's impossible to tell when the product is first created.
    # This is quite clunky but will be replaced when #693 is complete.

    class Meta:
        model = Product
        exclude = ('slug', 'score', 'product_class',
                   'recommended_products', 'product_options',
                   'attributes', 'categories')
        widgets = {
            'related_products': ProductSelectMultiple,
        }
