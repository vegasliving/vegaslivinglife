from django.shortcuts import render

def GoogleWebVR(request):
	return render(request, 'GoogleWebVR.html')

def Unity3DVR(request):
	return render(request, 'Unity3D.html')

def AFrameVR(request):
	return render(request, 'a-frame.html')



