from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .form import RegisterForm, ReportForm
from .models import Report


def home(request):
    reports = Report.objects.filter(status="Active")
    return render(request, "home.html", {"reports": reports})


def report_list(request):
    reports = Report.objects.all()

    search = request.GET.get("search", "")
    category = request.GET.get("category", "")
    report_type = request.GET.get("type", "")
    status = request.GET.get("status", "")

    if search:
        reports = reports.filter(
            Q(item_name__icontains=search) |
            Q(description__icontains=search) |
            Q(location__icontains=search)
        )

    if category:
        reports = reports.filter(category=category)

    if report_type:
        reports = reports.filter(report_type=report_type)

    if status:
        reports = reports.filter(status=status)

    return render(
        request,
        "report.html",
        {"reports": reports}
    )


def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)

    return render(
        request,
        "report_detail.html",
        {"report": report}
    )


@login_required
def report_create(request):

    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            report = form.save(commit=False)
            report.owner = request.user
            report.save()

            messages.success(
                request,
                "Report created successfully!"
            )

            return redirect("report_detail", pk=report.pk)

    else:
        form = ReportForm()

    return render(
        request,
        "report_form.html",
        {"form": form}
    )


@login_required
def report_update(request, pk):

    report = get_object_or_404(
        Report,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":

        form = ReportForm(
            request.POST,
            request.FILES,
            instance=report
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Report updated successfully!"
            )

            return redirect(
                "report_detail",
                pk=report.pk
            )

    else:
        form = ReportForm(instance=report)

    return render(
        request,
        "report_form.html",
        {"form": form}
    )


@login_required
def report_delete(request, pk):

    report = get_object_or_404(
        Report,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        report.delete()

        messages.success(
            request,
            "Report deleted successfully!"
        )

        return redirect("my_reports")

    return render(
        request,
        "report confirm_delete.html",
        {"report": report}
    )


@login_required
def report_resolve(request, pk):

    report = get_object_or_404(
        Report,
        pk=pk,
        owner=request.user
    )

    report.status = "Resolved"
    report.save()

    messages.success(
        request,
        "Report marked as resolved!"
    )

    return redirect(
        "report_detail",
        pk=report.pk
    )


@login_required
def my_reports(request):

    reports = Report.objects.filter(
        owner=request.user
    )

    return render(
        request,
        "my_report.html",
        {"reports": reports}
    )


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Registration successful!"
            )

            return redirect("home")

    else:
        form = RegisterForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )


class UserLoginView(LoginView):
    template_name = "login.html"


class UserLogoutView(LogoutView):
    next_page = "/"

# Create your views here.
