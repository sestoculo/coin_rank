from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    return render(request, 'home.html')



#Templates are a very powerful feature of Django’s, and their main
#strength consists of substituting Python variables into HTML text.
#We use render and (later) render_to_ string rather
#than, say, manually reading the file from disk with the built-in
#open.

