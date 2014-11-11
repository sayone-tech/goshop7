#-- coding:utf-8 --
import sys
reload(sys).setdefaultencoding('utf8')
import json
from forms import NewsLetterSubscriptionForm
from apps.newsletter.models import *
from django.contrib.sites.models import Site
from django.forms.util import ErrorList
from django.http import Http404,HttpResponse
from django.core.mail import EmailMessage
from django.template import Context
from django.template import RequestContext
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives


class Newsletter(TemplateView):
    template_name='newsletter/newsletter.html'

    def get_context_data(self, ** kwargs):
        context = super(Newsletter, self).get_context_data(** kwargs)
        context['page_title'] = 'Newsletter'
        return context
    
def newsletter_subscription(request):
     try:
        current_site = Site.objects.get_current()
        result={}
        if request.method == 'POST':
            email = request.POST['email']
            submit = request.POST['submit']
            form = NewsLetterSubscriptionForm(data=request.POST.copy(),auto_id=False)
            news_sub = NewsletterSubscription.objects.filter(email=request.POST['email'])
            if news_sub:
                if submit == '':
                    form = NewsLetterSubscriptionForm(instance=news_sub[0])
                    result['status']="success"
                    result['message']="User Already Subscribed"
                    return HttpResponse(json.dumps(result),mimetype='application/json')
                if submit == 'Unsubscribe':
                    subscription = get_object_or_404(NewsletterSubscription, email=email)
                    subscription.hash_key = subscription.random_key()
                    subscription.confirm=False
                    subscription.save()
#                    t = loader.get_template('newsletters/newsletter_unsubscription_confirm_email.txt')
#                    c = Context({'key': subscription.hash_key, 'site':current_site,'host': request.get_host() })
#                    email_obj = EmailMessage('[%s] %s' % (current_site.name, 'Newsletter subscription confirmation'), t.render(c), settings.DEFAULT_FROM_EMAIL,
#                    [email], [],
#                    headers = {})
#                    email_obj.send()
                    result['status']='unsubsribe'
                    return HttpResponse(json.dumps(result),mimetype='application/json')

            else:
                if submit == '':
                    if form.is_valid():
                        subscription = form.save(commit=False)
                        subscription.email = email
                        subscription.confirm=True
                        subscription.save()
                        t = loader.get_template('newsletter/newsletter_confirm_email.html')
                        c = Context({'key': subscription.hash_key, 'site':current_site,'host': request.get_host() })
#                        title=Site.objects.get_current(pk=1)
                        rendered=t.render(c)
                        text_content = strip_tags(rendered)
                        html_content = rendered
                        email_obj = EmailMultiAlternatives(' Thank you for subscribing!', text_content, settings.DEFAULT_FROM_EMAIL,[email])
                        email_obj.attach_alternative(html_content, "text/html")
                        email_obj.send()
                        result['status']="subscribed"
                        result['message']="Successfully Subscribed"
                        return HttpResponse(json.dumps(result),mimetype='application/json')
                    else:
                        errors = form.errors
                        result['status']="validation_errors"
                        result['message']="Enter a Valid Email"
                        return HttpResponse(json.dumps(result),mimetype='application/json')
                else:
                    errors = form.errors
                    result['status']="validation_errors"
                    result['message']="Enter a Valid Email"
                    return HttpResponse(json.dumps(result),mimetype='application/json')
#        return HttpResponse(json.dumps(result),mimetype='application/json')
     except Exception as inst:
         print type(inst)     # the exception instance
         print inst.args      # arguments stored in .args
         print inst
     return HttpResponse(json.dumps(result),mimetype='application/json')
def newsletter_subscription_confirm(request, key):
    subscription = get_object_or_404(NewsletterSubscription, hash_key=key)
    error = ''
    if subscription.confirm:
        error = ErrorList(['This subscription has already been confirmed.'])
    else:
        subscription.confirm = True
        subscription.hash_key = ''
        subscription.save()
    return render_to_response('newsletter/newsletter_confirm.html',
                              {'subscription': subscription, 'error': error},
                              context_instance=RequestContext(request))

def newsletter_unsubscription_confirm(request,key):
     subscription = get_object_or_404(NewsletterSubscription, hash_key=key)
     if subscription.confirm:
        subscription.confirm=False
        subscription.hash_key = ''
        subscription.save()
     return render_to_response('newsletter/newsletter_unsubscribed.html',
                              context_instance=RequestContext(request))


from django.views.generic import TemplateView
class NewsletterUnsubscription(TemplateView):
   
    template_name = 'newsletter/newsletter_unsub_form.html'
    def get_context_data(self, *args, **kwargs):
        context = super(NewsletterUnsubscription, self).get_context_data(**kwargs)
        context['page_title'] = 'Newsletter'
        return context

    def post(self, request, *args, **kwargs):
        if request.POST['email']:
            email = request.POST['email']
            try:
                obj = NewsletterSubscription.objects.get(email=email)
                obj.delete()
                messages.success(self.request, _('Successfully unsubscribed.'))
            except Exception as e:
                print e,"kkkkkkkkkkkk"
                messages.success(self.request, _('Entered email is not subscribed our new letter'))
                return redirect('newsletter_unsubscription')
        return redirect('newsletter')