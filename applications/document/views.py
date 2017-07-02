from django.shortcuts import render
import requests
import json
from django.contrib.auth.models import User
from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context, Template

from io import BytesIO

from src.settings.local import LOGIN_REGISTER_URLS


@csrf_exempt
def projects_list(request):
    # Get 'post' with  user-token, return all user projects
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)

        token = content['token']

        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization' : 'Token ' + token
        }

        post_data = {'headers': headers}
        # send user-token, get user data
        url = LOGIN_REGISTER_URLS['loginByToken']

        response = requests.get(url, headers=headers)

        responseData = {
            'data' : '',
            'detail' : ''
        }
        if response.status_code == 200:

            content = json.loads(response.text)

            if content['pk']:
                user = User.objects.get(pk=content['pk'])
                projects = Project.objects.filter(user=user)
                serializer = ProjectListSerializer(projects, many=True)
                responseData['data'] = serializer.data
                responseData['detail'] = 'OK'
                return JsonResponse(responseData, safe=False)
            else:
                responseData['detail'] = content['detail']
                return JsonResponse(responseData)
        else:
            responseData['detail'] = response.status_code
            return JsonResponse(responseData)

@csrf_exempt
def project_detail(request):
    # Get 'post' with user-token and project-pk, return project details
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)

        token = content['token']
        project_id = content['pk']

        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization' : 'Token ' + token
        }

        post_data = {'headers': headers}
        url = LOGIN_REGISTER_URLS['loginByToken']

        response = requests.get(url, headers=headers)

        responseData = {
            'data' : '',
            'detail' : ''
        }
        if response.status_code == 200:

            content = json.loads(response.text)

            if content['pk']:
                user = User.objects.get(pk=content['pk'])
                project = Project.objects.get(user=user,pk=project_id)
                serializer = ProjectDetailSerializer(project)
                responseData['data'] = serializer.data
                responseData['detail'] = 'OK'
                return JsonResponse(responseData, safe=False)
            else:
                responseData['detail'] = content['detail']
                return JsonResponse(responseData)
        else:
            responseData['detail'] = response.status_code
            return JsonResponse(responseData)

@csrf_exempt
def project_create(request,*args,**kwargs):
    # Get 'post' with user-token
    # and project-name for ctreating new project
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)

        token = content['token']
        project_name = content['name']

        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization' : 'Token ' + token
        }

        post_data = {'headers': headers}
        url = LOGIN_REGISTER_URLS['loginByToken']

        response = requests.get(url, headers=headers)

        responseData = {
            'data' : '',
            'detail' : ''
        }
        if response.status_code == 200:

            content = json.loads(response.text)

            if content['pk']:
                user = User.objects.get(pk=content['pk'])

                new_project = Project.objects.create(
                    name = project_name,
                    html = '',
                    css = '',
                    user = user
                )
                check_pk = new_project.pk
                check_project = Project.objects.get(pk=check_pk)
                if new_project == check_project:
                    responseData['detail'] = 'OK'
                else:
                    responseData['detail'] = 'Not created'
                return JsonResponse(responseData, safe=False)
            else:
                responseData['detail'] = content['detail']
                return JsonResponse(responseData)
        else:
            responseData['detail'] = response.status_code
            return JsonResponse(responseData)

@csrf_exempt
def project_update(request):
    # Get 'post' with project-data for updating
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)

        token = content['token']
        project_name = content['name']
        project_pk = content['pk']
        project_html = content['html']
        project_css = content['css']

        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization' : 'Token ' + token
        }

        post_data = {'headers': headers}
        url = LOGIN_REGISTER_URLS['loginByToken']

        response = requests.get(url, headers=headers)

        responseData = {
            'data' : '',
            'detail' : ''
        }
        if response.status_code == 200:

            content = json.loads(response.text)

            if content['pk']:
                user = User.objects.get(pk=content['pk'])
                project = Project.objects.get(user=user,pk=project_pk)
                project.html = project_html
                project.css = project_css
                project.save()

                check_pk = project.pk
                check_project = Project.objects.get(pk=check_pk)
                if project == check_project:
                    responseData['detail'] = 'OK'
                else:
                    responseData['detail'] = 'Not updated'
                return JsonResponse(responseData, safe=False)
            else:
                responseData['detail'] = content['detail']
                return JsonResponse(responseData)
        else:
            responseData['detail'] = response.status_code
            return JsonResponse(responseData)


def render_pdt(html, css):
    #Get html and css strings, return pdf object
    html_t = Template(html).render(Context())
    css_t = Template(css).render(Context())
    template = get_template('document/pdf_template.html')
    context = {'html':html_t,'css':css_t}
    final_html  = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(final_html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

@csrf_exempt
def template_2_pdf(request):
    #Get 'post' with projetc data, return pdf for downloading
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        content = json.loads(body_unicode)

        token = content['token']
        filename = content['name']
        html = content['html']
        css = content['css']

        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization' : 'Token ' + token
        }

        post_data = {'headers': headers}
        url = LOGIN_REGISTER_URLS['loginByToken']

        response = requests.get(url, headers=headers)

        if response.status_code == 200:

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
        else:
            return HttpResponse("Code:",response.status_code)
