from django.views.generic import TemplateView
from django.template.loader import render_to_string
from oscar.core.loading import get_model
from django.http import HttpResponsePermanentRedirect
from utils.views import JSONResponseMixin
from django.shortcuts import render_to_response, HttpResponse,\
    get_object_or_404, redirect
from oscar.apps.catalogue import views as catalogue_views
from oscar.core.loading import get_class
from endless_pagination.decorators import page_template
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.utils import simplejson
from endless_pagination.views import AjaxListView
from decimal import Decimal
from django.template import RequestContext
Product = get_model('catalogue', 'product')
ProductReview = get_model('reviews', 'ProductReview')
Category = get_model('catalogue', 'category')
ProductAlert = get_model('customer', 'ProductAlert')
ProductAlertForm = get_class('customer.forms', 'ProductAlertForm')
ProductCategory = get_model('catalogue', 'productcategory')


class OnapageView(TemplateView):
    template_name = 'catalogue/onepage_home.html'

onepage_view = OnapageView.as_view()


class ProductDetailView(catalogue_views.ProductDetailView):
    template_name_ajax = 'catalogue/partials/product_popup.html'

    def get(self, request, **kwargs):
        """
        Ensures that the correct URL is used before rendering a response
        """
        self.object = product = self.get_object()
        response = self.render_to_response(self.get_context_data(**kwargs))
        self.send_signal(request, response, product)
        return response

    def get_object(self, queryset=None):
        # Check if self.object is already set to prevent unnecessary DB calls
        if hasattr(self, 'object'):
            return self.object
        else:
            product = super(ProductDetailView, self).get_object(queryset)
            if product.is_group:
                return product.variants.all()[0]
            return product

    def get_template_names(self):
        return [self.template_name_ajax] if self.request.is_ajax()\
            else super(ProductDetailView, self).get_template_names()


class ProductCategoryView(
        catalogue_views.ProductCategoryView, AjaxListView, JSONResponseMixin):
    context_object_name = "products"
    template_name = 'catalogue/browse.html'
    page_template = 'catalogue/partials/product_list.html'
    extra_context = None
    paginate_by = None

    def get(self, request, *args, **kwargs):
        self.get_object()
        correct_path = self.category.get_absolute_url()
        ctx = {}

#        min_amount='0'
#        max_amount='500'
#        type=self.request.GET.get('sort')
#        print "typtttttttttttttt",type
#        sort=self.request.GET.get('type')
#        sort1=self.request.GET.get('type1')
#        price=self.request.GET.get('price')
#        if price:
#            amount=price.split('-')
#            amt1=amount[0].split('$')
#            amt2=amount[1].split('$')
#            min_amount=Decimal(float(amt1[1]))
#            max_amount=Decimal(float(amt2[1]))
#        if sort=='outofstock':
#            qs = Product.browsable.base_queryset().filter(stockrecords__num_in_stock__lte=0)
#        elif sort1=='stock':
#            qs = Product.browsable.base_queryset().filter(stockrecords__num_in_stock__gte=1)
#        else:
#            qs = Product.browsable.base_queryset().filter(
#                stockrecords__price_excl_tax__gte=min_amount,
#                 stockrecords__price_excl_tax__lte=max_amount)
        if self.category is not None:
            categories = self.get_categories()
#            if type=='p.price&order=ASC':
#                qs = qs.filter(categories__in=categories).order_by('stockrecords__price_excl_tax')
#            elif type=='p.price&order=DESC':
#                qs = qs.filter(categories__in=categories).order_by('-stockrecords__price_excl_tax')
#            elif type=='pd.name&order=ASC':
#                qs = qs.filter(categories__in=categories).order_by('title')
#                print "qssssssssssssssssssss",qs
#            elif type=='pd.name&order=DESC':
#                qs = qs.filter(categories__in=categories).order_by('-title')
#                print "jdfvcdjhbvcjhdnbv",qs
#            elif type=='rating&order=DESC':
#                qs = qs.filter(categories__in=categories).order_by('-rating')
#            elif type=='rating&order=ASC':
#                qs = qs.filter(categories__in=categories).order_by('rating')
#
#            else:
#        if type or sort or price:
#            status = 'success'
#            ctx['prod'] = render_to_string(
#               'catalogue/partials/product_list.html',{'products':qs,},)
#            ctx.update({'status':status})
#            results = simplejson.dumps(ctx)
#            return HttpResponse(results,mimetype='application/json')
        if correct_path != request.path:
            return HttpResponsePermanentRedirect(reverse(correct_path),)
        return super(ProductCategoryView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['outofstock'] = Product.browsable.base_queryset().filter(
            categories=self.category, stockrecords__num_in_stock__lte=0).count()
        context['stock'] = Product.browsable.base_queryset().filter(
            categories=self.category, stockrecords__num_in_stock__gte=1).count()
        return context

    def get_queryset(self):
        min_amount = '0'
        max_amount = '500000'
        type = self.request.GET.get('sort')
        order = self.request.GET.get('order')
        sort = self.request.GET.get('type')
        sort1 = self.request.GET.get('type1')
        price = self.request.GET.get('price')
        if price:
            amount = price.split('-')
            amt1 = amount[0].split('$')
            amt2 = amount[1].split('$')
            min_amount = Decimal(float(amt1[1]))
            max_amount = Decimal(float(amt2[1]))
        if sort == 'outofstock':
            qs = Product.browsable.base_queryset().filter(stockrecords__num_in_stock__lte=0)
        elif sort1 == 'stock':
            qs = Product.browsable.base_queryset().filter(stockrecords__num_in_stock__gte=1)
        else:
            qs = Product.browsable.base_queryset().filter(
                stockrecords__price_excl_tax__gte=min_amount,
                stockrecords__price_excl_tax__lte=max_amount)
        if self.category is not None:
            categories = self.get_categories()
            if type == 'p.priceASC':
                qs = qs.filter(categories__in=categories).order_by('stockrecords__price_excl_tax')
            elif type == 'p.priceDESC':
                qs = qs.filter(categories__in=categories).order_by('-stockrecords__price_excl_tax')
            elif type == 'pd.nameASC':
                qs = qs.filter(categories__in=categories).order_by('title')
            elif type == 'pd.nameDESC':
                qs = qs.filter(categories__in=categories).order_by('-title')
            elif type == 'ratingDESC':
                qs = qs.filter(categories__in=categories).order_by('-rating')
            elif type == 'ratingASC':
                qs = qs.filter(categories__in=categories).order_by('rating')
            else:
                qs = qs.filter(categories__in=categories).distinct()
        return qs
