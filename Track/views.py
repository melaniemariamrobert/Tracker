from django.shortcuts import render_to_response

def home(request):
    # return HttpResponse("Hello")
    return render_to_response('base.html')