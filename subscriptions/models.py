from django.db import models
from django.contrib.auth import get_user_model

from djmoney.models.fields import MoneyField

from accounts.models import TelegramAccount


class Subscription(models.Model):
    title = models.CharField('Название', max_length=256)
    price = MoneyField('Стоимость', max_digits=14, decimal_places=2,
                       default_currency='RUB')
    is_active = models.BooleanField(default=True)
    duration = models.DurationField()

    def __str__(self):
        return self.title


# TODO: эта модель не нужна, удалить.
class UserSubscription(models.Model):
    """Связывает подписку с пользователем.

    Срок окончания вычисляется через `start_date` и период из модели подписки.
    """
    start_date = models.DateField('Начало')
    subscription = models.ForeignKey(Subscription, related_name='used_by',
                                     on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='subscriptions',
                             on_delete=models.CASCADE)

    @property
    def end_date(self):
        return self.start_date + self.subscription.duration

    def __str__(self):
        return f'{self.subscription}, {self.user}, {self.start_date}—{self.end_date}'


class Payment(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    tg_account = models.ForeignKey(TelegramAccount, related_name='payments',
                                   on_delete=models.CASCADE)
    amount = MoneyField('Сумма', max_digits=14, decimal_places=2,
                        default_currency='RUB')

    def __str__(self):
        return f'{self.tg_account}, {self.created_at}, {self.amount}'
