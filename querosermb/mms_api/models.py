from django.db import models
from .choices import TYPE_CRIPTO

class CriptoValores(models.Model):
    pair = models.PositiveSmallIntegerField("Pair",choices=TYPE_CRIPTO, db_index=True, null=False, blank=False)
    mms_timestamp = models.BigIntegerField("Timestamp",db_index=True, null=False, blank=False)
    close = models.DecimalField("Valor do fechamento diario", max_digits=16, decimal_places=5, null=False, blank=False)
    mms_20 = models.DecimalField("Mms 20 dias", max_digits=16, decimal_places=5, default=0)
    mms_50 = models.DecimalField("Mms 50 dias", max_digits=16, decimal_places=5, default=0)
    mms_200 = models.DecimalField("Mms 200 dias", max_digits=16, decimal_places=5, default=0)

    def __str__(self):
        return '{}'.format(self.mms_timestamp)