from django.db import models

# Create your models here.
class Detection(models.Model):

    dont_report= 'dont_report'
    report_by_text = 'text'
    report_by_call = 'call'

    POLICE_REPORT_CHOICES = (
        (dont_report,'Do not Report'),
        (report_by_text, 'Report by Text'),
        (report_by_call, 'Report by Call'),
    )

    device_id=models.CharField(max_length=100, blank=True)
    lng=models.CharField(max_length=20, blank=True)
    lat=models.CharField(max_length=20, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    police_report=models.CharField(
        max_length=10,
        choices=POLICE_REPORT_CHOICES,
        default=dont_report,
    )

    def is_report(self):
        return self.police_report!=self.dont_report

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        print(self.lng,self.lat)
        super(Detection, self).save(*args, **kwargs)


