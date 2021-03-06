from django.views.generic import CreateView
from django.conf import settings
from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.core.mail import send_mail

import json

from feedback.forms import FeedbackForm



class FeedbackView(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'

    def get_form_kwargs(self):
        kwargs = super(FeedbackView, self).get_form_kwargs()
        post = kwargs['data'].copy()
        post['url'] = self.kwargs['url']
        post['site'] = Site.objects.get_current().pk
        kwargs['data'] = post
        return kwargs

    def get_success_url(self):
        return self.kwargs['url']

    def form_valid(self, form):
        response = super(FeedbackView, self).form_valid(form)
        if hasattr(settings, 'FEEDBACK_EMAIL_LIST'):
            d = form.cleaned_data
            try:
                from_email = settings.DEFAULT_FROM_EMAIL
            except NameError:
                from_email = settings.SERVER_EMAIL
            try:
                send_mail(
                        'Feedback received: {}'.format(d['subject']),
                        'email: {} \n\n {}'.format(d['email'], d['text']),
                        from_email,
                        settings.FEEDBACK_EMAIL_LIST,
                        fail_silently=False,
                        )
            except Exception as e:
                return HttpResponse(json.dumps({'error': 'Failed to send email (%s)' % e.strerror}), status=503)
        return HttpResponse(json.dumps({}), status=201)

    def form_invalid(self, form):
        return HttpResponse(json.dumps({'errors': form.errors}))
