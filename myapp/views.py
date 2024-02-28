from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import ClassRoom # we can also write .models as they are in same level location

# Create your views here.
def home(request):
    return HttpResponse("""
                        <html>
                            <head>
                                <title>My App</title>
                            </head>
                            <body>
                                <h1>Hello World.</h1> <h3>I am learning Django.</h3>
                            </body>
                        </html>
                        """)

def root_page(request):
        return render(request, template_name="myapp/root_page.html")

def temp_inherit_home(request):
      return render(request, template_name="myapp/temp_inherit_home.html")

def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")

def classroom(request):
    classrooms = [
         {"name": "One", "address": "KTM"},
         {"name": "Two", "address": "PKR"},
         {"name": "Three", "address": "BKT"},
         {"name": "Four", "address": "LTP"},
    ]
    return render(request, template_name="myapp/classroom.html",
                  context={"classroom_name": "One", "location": "KTM", "classrooms": classrooms})


def classroom_queryset(request):
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="myapp/classroom_queryset.html", context={"classrooms": classrooms})