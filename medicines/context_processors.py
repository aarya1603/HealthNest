from medicines.models import Medicine
from django.db.models import F

def low_stock_medicines(request):
    low_stock = Medicine.objects.filter(
        stock__lte=F('low_stock_alert')
    )

    return {
        'low_stock_medicines': low_stock,
        'has_low_stock': low_stock.exists()
    }
