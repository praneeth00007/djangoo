from django.shortcuts import render

def video_conferencing(request, class_name):
    # Your view logic, for example:
    return render(request, 'video_conference.html', {'class_name': class_name})
