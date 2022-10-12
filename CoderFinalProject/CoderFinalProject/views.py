from django.http import HttpResponse

from django.template import Context, Template


def inicio_con_template(request):
    archivo = open("\Users/User/Documents/CoderFinalProject/CoderFinalProject/CoderFinalProject/templates/templates.html")
    template = Template(archivo.read())
    archivo.close()
    
    context = Context()
    
    result = template.render(context)
    
    return HttpResponse(result)
