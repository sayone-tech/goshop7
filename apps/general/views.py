import json

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from oscar.apps.catalogue.models import Product
from oscar.apps.wishlists.models import Line, WishList


class BasketRemoveView(View):
    """
    Handles the delete-to-basket operation,
    """
    preview = False

    def get(self, request, *args, **kwargs):
        current = request.get_full_path()
        ctx = {}
        try:
            line_id = self.request.GET['prod']
            self.remove_line(request.basket, line_id)
        except:
            pass
        if self.preview == False and request.is_ajax():
            status = 'success'
            ctx['html'] = render_to_string(
                'oscar/basket/partials/basket_delete.html', {'request': request, })
            ctx.update({'status': status})
            results = simplejson.dumps(ctx)
            return HttpResponse(results, mimetype='application/json')
        else:
            return HttpResponseRedirect(reverse('checkout:review_order'))

    def remove_line(self, basket, line_id):
        """Remove one lines from basket."""
        if basket.status == basket.FROZEN:
            raise PermissionDenied("A frozen basket cannot be flushed")
        basket.lines.all().filter(id=line_id).delete()
        if not basket.lines.all():
            basket._lines = None


def custom_404(request, template='404.html'):
    """
    Customized view for 404 page
    """
    response =  render(request, template,{'code':'404','message':_("")})
    response.status_code = 404
    return response

def custom_500(request, template='500.html'):
    """
    Customized view for 500 page.
    """
    response = render(request, template,{'code':'500','message':_("")})
    response.status_code = 500
    return response


class AutoCompSearchView(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(AutoCompSearchView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        ctx = []
        myDic = {}
        query = request.POST.get('query')
        products = Product.objects.filter(title__icontains=query)
        for product in products:
            categories = product.categories.all()
            myDic[product.title] = [cat.name for cat in categories]
        print myDic
        results = simplejson.dumps(myDic)
        return HttpResponse(results, mimetype='application/json')


class WishlistLineDeleteView(View):
    """
    Customized template view to manage content of News event page.
    """
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(WishlistLineDeleteView, self).dispatch(*args, **kwargs)

    def post(self, args, **kwargs):
        prod_id = self.request.POST.get('prod_id')
        line_ids = []
        user = self.request.user
        wishlist = WishList.objects.get(owner=user)
        lines = Line.objects.filter(wishlist=wishlist)
        for line in lines:
            line_ids.append(int(line.id))
            if int(line.id) == int(prod_id):
                line.delete()
        lines = Line.objects.filter(wishlist=wishlist)
        context = {}
        if lines:
            context['status'] = 'wish'
            context['html'] = render_to_string(
                'basket/partials/wishlist_line_delete_popup.html',
                {'wishs': lines, 'request': self.request})
        else:
            context['status'] = 'no_wish'
            context['html'] = render_to_string(
                'basket/partials/empty_wishlist.html', {'request': self.request})

        return HttpResponse(json.dumps({'context': context, }), mimetype='application/json')
