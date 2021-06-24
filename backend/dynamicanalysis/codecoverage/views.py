from django.shortcuts import render

# Create your views here.
def codecoverage_view(request):
      
    # render function takes argument  - request
    # and return HTML as response
    htmlPage = request.GET["fileName"]
    return render(request, htmlPage)
