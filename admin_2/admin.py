from django.contrib import admin
from .models import donorInfo, NoticeBoard, Requester, triagePatient, DonorRequesterRelation, MotivatedDonorTable
# Register your models here.


class donorModify(admin.ModelAdmin):
    # readonly_fields = ['last_donation_date']

    class Meta:
        model = donorInfo


admin.site.register(donorInfo, donorModify)

admin.site.register(MotivatedDonorTable)

admin.site.register(Requester)

admin.site.register(triagePatient)

admin.site.register(DonorRequesterRelation)

admin.site.register(NoticeBoard)
