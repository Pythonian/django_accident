from django.shortcuts import render, redirect
from django.contrib import messages

from reports.models import Report
from reports.forms import ReportForm


def home(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your witness report was successfully sent.")
            return redirect('home')
    else:
        form = ReportForm()
    return render(request, 'home.html', {'form': form})
