# Create your views here.
from django.http import HttpResponse

def contact_form(request):
    return HttpResponse("Hello, world. You're at the contact form.")