from django.shortcuts import render
from django.http import HttpResponse

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
