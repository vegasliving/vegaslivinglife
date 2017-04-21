from django.shortcuts import render

def GoogleWebVR(request):
	return render(request, 'GoogleWebVR.html')

def Unity3DVR(request):
	return render(request, 'index.html')

def AFrameVR(request):
	return render(request, 'a-frame.html')



