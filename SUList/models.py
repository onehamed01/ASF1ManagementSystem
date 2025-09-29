from django.db import models

class ApplicationBase(models.Model):
    name = models.DateTimeField(auto_now=True)
    total_app = models.PositiveSmallIntegerField()
    submitted = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
    
class MonthApplication(ApplicationBase):
    pass

class DayApplication(ApplicationBase):
    monthapplication = models.ForeignKey(MonthApplication, on_delete=models.CASCADE)

class ServiceUser(models.Model):
    serviceuser_name = models.CharField(max_length = 100)
    references = models.CharField(max_length = 30)
    status = models.BooleanField(default=False)
    po_num = models.CharField(max_length = 10)
    dayapplication = models.ForeignKey(DayApplication, on_delete=models.CASCADE)

    def __str__(self):
        return self.references