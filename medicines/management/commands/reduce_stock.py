# from django.core.management.base import BaseCommand
# from datetime import datetime
# from medicines.models import Medicine

# class Command(BaseCommand):
#     help = "Reduce medicine stock when reminder time matches"

#     def handle(self, *args, **kwargs):
#         current_time = datetime.now().time().replace(second=0, microsecond=0)

#         medicines = Medicine.objects.all()

#         for med in medicines:
#             if (
#                 med.reminder_time.hour == current_time.hour and
#                 med.reminder_time.minute == current_time.minute
#             ):
#                 if med.total_tablets > 0:
#                     med.total_tablets -= med.tablets_per_dose
#                     med.save()

#                     self.stdout.write(
#                         f"{med.name} stock reduced. Remaining: {med.total_tablets}"
#                     )
