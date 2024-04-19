from django.shortcuts import render, redirect

from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        type = request.POST['type']
        details = request.POST['details']
        attachment = request.FILES.get('attachment')

        ServiceRequest.objects.create(
            type=type,
            details=details,
            attachment=attachment
        )
        return redirect('request_tracking')
    return render(request, 'submit_request.html')

def request_tracking(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'request_tracking.html', {'requests': requests})

def home(request):
    return render(request, 'home.html')
