from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    due_date = models.DateField(db_index=True)
    paid_out = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    category = models.ForeignKey(
        'core.Category',
        related_name='expenses',
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        'core.Tag',
        related_name='tags',
        blank=True,
    )

    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_changed = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.title

    # repeat