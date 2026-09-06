from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import MedicalReport


@login_required
def report_list(request):

    if request.method == "POST":

        report_name = request.POST.get("report_name")
        report_date = request.POST.get("report_date")
        report_file = request.FILES.get("report_file")

        if report_name and report_file:

            MedicalReport.objects.create(
                user=request.user,
                report_name=report_name,
                report_date=report_date or None,
                report_file=report_file
            )

            return redirect("report_list")

    reports = MedicalReport.objects.filter(
        user=request.user
    ).order_by("-uploaded_at")

    return render(
        request,
        "reports/report_list.html",
        {
            "reports": reports
        }
    )
@login_required
def report_summary(request, report_id):

    report = MedicalReport.objects.get(
        id=report_id,
        user=request.user
    )

    # Dummy AI / rule-based demonstration
    report_name = report.report_name.lower()

    if "blood" in report_name:
        summary = {
            "overview": (
                "This report appears to be a blood test. "
                "It may contain routine parameters such as haemoglobin, "
                "blood glucose and cholesterol."
            ),
            "findings": [
                "Blood-related health parameters are available for review.",
                "Values can be compared with previous reports to identify changes.",
                "Any unusual or out-of-range values should be discussed with a healthcare professional."
            ],
            "advice": (
                "Consider keeping this report with your previous blood-test "
                "records for easier comparison during medical consultations."
            )
        }

    elif "scan" in report_name or "xray" in report_name:
        summary = {
            "overview": (
                "This appears to be a medical imaging report. "
                "The report may contain observations from an X-ray, scan or similar examination."
            ),
            "findings": [
                "Imaging observations should be reviewed in the context of your symptoms.",
                "Previous imaging reports may help identify changes over time.",
                "Discuss the findings with your healthcare professional."
            ],
            "advice": (
                "Keep the original imaging report available for your doctor or specialist."
            )
        }

    elif "urine" in report_name:
        summary = {
            "overview": (
                "This appears to be a urine examination report containing "
                "routine urine-test observations."
            ),
            "findings": [
                "The report may include routine urine parameters.",
                "Results should be interpreted together with your symptoms and medical history.",
                "Any abnormal findings should be discussed with a healthcare professional."
            ],
            "advice": (
                "Keep this report with your other medical records for future reference."
            )
        }

    else:
        summary = {
            "overview": (
                "This is a demonstration AI summary for your uploaded medical report. "
                "The system has identified the report as a general medical record."
            ),
            "findings": [
                "The uploaded report has been successfully stored in Care360.",
                "Important information should be reviewed carefully.",
                "Any abnormal or concerning information should be discussed with a healthcare professional."
            ],
            "advice": (
                "Keep your medical reports organized so they can be easily accessed "
                "during future healthcare visits."
            )
        }

    return render(
        request,
        "reports/report_summary.html",
        {
            "report": report,
            "summary": summary
        }
    )