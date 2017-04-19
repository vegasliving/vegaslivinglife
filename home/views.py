from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def login(request):
	return render(request, 'home/home_page.html')

def logout(request):
	return render(request, 'home/home_page.html')


