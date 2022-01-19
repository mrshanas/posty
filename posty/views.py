from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    """Home page of the application"""

    return render(request,'posty/base.html')