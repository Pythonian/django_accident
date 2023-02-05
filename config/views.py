from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from reports.models import Report
from reports.forms import ReportForm


def home(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.save()
            messages.success(
                request, "Your witness report has been recorded.")
            return redirect(report)
    else:
        form = ReportForm()
    return render(request, 'home.html', {'form': form})


def report(request, id):
    report = get_object_or_404(Report, id=id)
    return render(request, 'report.html', {'report': report})
