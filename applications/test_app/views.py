from django.shortcuts import render
import requests

from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.template import Template

from io import BytesIO

from applications.document.views import render_pdt
from django.http import HttpResponse

def test_index(request):
    template = 'test_app/index.html'
    context_dict = {'test':'vagina'}

    html = '<h1>pipka</h1>'
    css = 'h1 {color: #f00;}'
    filename = 'pipka'

    #html_t = Template(html).render(Context())
    #print(html_t)

    pdf = render_pdt(html, css)

    if pdf:
         response = HttpResponse(pdf, content_type='application/pdf')
         filename = "%s.pdf" % (filename)
         content = "inline; filename='%s'" % (filename)
         download = request.GET.get("download")
         if download:
             content = "attachment; filename='%s'" % (filename)
         response['Content-Disposition'] = content
         return response
    return HttpResponse("Not found")


    test = 'template_test'
    context = {'test' : test}
    return render(request, template, context)
