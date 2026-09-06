from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine, MedicineLog, MedicineDose

def delete_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    if request.method == "POST":
        medicine.delete()
        return redirect('medicine_list')

    return render(request, 'medicines/confirm_delete.html', {
        'medicine': medicine
    })

def add_medicine(request):
    if request.method == 'POST':

        medicine = Medicine.objects.create(
            name=request.POST['name'],
            dosage=request.POST['dosage'],
            stock=request.POST['stock'],
            low_stock_alert=request.POST['low_stock_alert'],
        )

        times = request.POST.getlist('times')  # checkbox values

        for time in times:
            MedicineDose.objects.create(
                medicine=medicine,
                time_of_day=time,
                frequency='daily'
            )

        return redirect('medicine_list')

    return render(request, 'medicines/add_medicine.html')

def medicine_list(request):
    morning_doses = MedicineDose.objects.filter(time_of_day='morning')
    afternoon_doses = MedicineDose.objects.filter(time_of_day='afternoon')
    night_doses = MedicineDose.objects.filter(time_of_day='night')

    context = {
        'morning_doses': morning_doses,
        'afternoon_doses': afternoon_doses,
        'night_doses': night_doses,
    }

    return render(request, 'medicines/medicine_list.html', context)
def mark_taken(request, dose_id):
    dose = get_object_or_404(MedicineDose, id=dose_id)
    today = timezone.now().date()

    # 🔒 SAFETY: prevent double dose on same day
    already_taken = MedicineLog.objects.filter(
        medicine_dose=dose,
        date=today
    ).exists()

    if not already_taken:
        MedicineLog.objects.create(
            medicine_dose=dose,
            status='taken'
        )

        # reduce stock
        medicine = dose.medicine
        if medicine.stock > 0:
            medicine.stock -= 1
            medicine.save()

    return redirect('medicine_list')

def mark_skipped(request, dose_id):
    dose = get_object_or_404(MedicineDose, id=dose_id)
    today = timezone.now().date()

    # Prevent duplicate skip/taken logs for same dose & day
    already_logged = MedicineLog.objects.filter(
        medicine_dose=dose,
        date=today
    ).exists()

    if not already_logged:
        MedicineLog.objects.create(
            medicine_dose=dose,
            status='skipped'
        )

    return redirect('medicine_list')