from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(
        unique=True,
        verbose_name="ID пользователя",
        help_text="Уникальный идентификатор пользователя в Telegram.",
    )
    username = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name="Имя пользователя",
        help_text="Имя пользователя в Telegram.",
    )
    first_name = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name="Имя",
        help_text="Имя пользователя в Telegram.",
    )
    last_name = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name="Фамилия",
        help_text="Фамилия пользователя в Telegram.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создан",
        help_text="Временная метка, указывающая, когда был создан пользователь.",
    )

    def get_name(self):
        if self.username:
            return self.username
        elif self.last_name:
            return self.last_name
        elif self.first_name:
            return self.first_name
        else:
            return "Пользователь"

    def __str__(self):
        return f"{self.user_id}: {self.get_name()}"

    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"
        ordering = ["-created_at"]


class Stage(models.Model):
    title = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class StageProgress(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    completed_volume = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def remaining_volume(self):
        return self.stage.volume - self.completed_volume

    def __str__(self):
        return f"Progress for {self.stage.title}"
