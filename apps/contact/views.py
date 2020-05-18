import json

from apps.contact.forms import ContactForm, ContactForm2
from django.views.generic import View
#from django.contrib.gis.geoip import GeoIP

from django.http import Http404, HttpResponse, HttpResponseRedirect


class ContactView(View):    

    def post(self, request, *args, **kwargs):
        if request.method=='POST':
            ctx = {}
            contct_form = ContactForm(request.POST)
            if contct_form.is_valid():
                data = contct_form.cleaned_data
                contct_form.send_email(data)
                contct_form.save()
#                user_ip = request.META.get('REMOTE_ADDR', None)
#                user_agent = request.META.get('HTTP_USER_AGENT', None)
#                extra_info = {'user_ip': user_ip, 'user_agent': user_agent}
#                if user_ip:
#                    g = GeoIP()
#                try:
#                    country = g.country(user_ip)['country_name']
#                    extra_info.update({'country': country})
#                except:
#                    country = None
#                try:
#                    city = g.city(user_ip)['city']
#                    extra_info.update({'city': city})
#                except:
#                    city = None
#                data.update(extra_info)
#                contct_form.send_email(data)
#                contact_form.user_ip = user_ip
#                contact_form.country = country
#                contact_form.city = city
#                contact_form.browser_information = user_agent
                ctx['status']='success'
                ctx['message']="Contacts details successfully submitted."
            else:
                print "errors",contct_form.errors.as_text()
                ctx['errors']=contct_form.errors
                return HttpResponse(json.dumps(ctx),mimetype='application/json')
        return HttpResponse(json.dumps(ctx),mimetype='application/json')

class ContactView2(View):

    def post(self, request, *args, **kwargs):
        results = {'success': True, 'data': None, 'message': ''}
        if request.method=='POST':
            ctx = {}
            contct_form = ContactForm2(request.POST)
            if contct_form.is_valid():
                data = contct_form.cleaned_data
                contct_form.send_email(data)
                contct_form.save()
                # phone_no = data['subject']
                # print("&&&&&&&&&",phone_no)
            else:
                print "errors",contct_form.errors.as_text()
                ctx['errors']=contct_form.errors
                results['data'] = {
                    'errors': contct_form.errors,
                }
                return HttpResponse(json.dumps(results),mimetype='application/json')
        return HttpResponse(json.dumps(results))