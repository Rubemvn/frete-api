from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Quote(models.Model):
    cep_origin = models.CharField(max_length=8, db_index=True)
    city_origin = models.CharField(max_length=50)
    uf_origin = models.CharField(max_length=2)
    cep_destination = models.CharField(max_length=8, db_index=True)
    city_destination = models.CharField(max_length=50)
    uf_destination = models.CharField(max_length=2)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cep_origin} - {self.city_origin}-{self.uf_origin} -> {self.cep_destination} - {self.city_destination}-{self.uf_destination}"
    
class QuoteOption(models.Model):
    quote = models.ForeignKey(
        Quote,
        on_delete=models.CASCADE,
        related_name="options"
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.PROTECT
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    delivery_days = models.PositiveIntegerField()
    raw_response = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.price} - {self.provider}"