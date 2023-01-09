from uuid import uuid4

from django.db import models


class APIManagement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    auto_schedule = models.BooleanField(default=False)
    active_time = models.DecimalField(max_digits=3, decimal_places=2, null=True)

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    daily_quotas = models.OneToOneField(
        "daily_quotas.DailyQuota", on_delete=models.CASCADE
    )
    health_infos = models.OneToOneField(
        "health_infos.Heath_Info", on_delete=models.CASCADE
    )
    schedule = models.ForeignKey(
        "schedules.Schedule", on_delete=models.CASCADE, related_name="management"
    )
    academics = models.ForeignKey(
        "academics.Academic", on_delete=models.CASCADE, related_name="management"
    )
    finance = models.OneToOneField("finance_infos.Finance", on_delete=models.CASCADE)
