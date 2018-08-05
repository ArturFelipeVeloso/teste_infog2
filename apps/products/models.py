from django.db import models


class Product(models.Model):
    name = models.CharField("Nome", null=False, blank=False, max_length=50)
    picture = models.ImageField(
        "Foto", upload_to='uploads/product/%Y/%m/', null=True, blank=True)
    price = models.DecimalField(
        "Preço", max_digits=6, decimal_places=2, default=0.0)
    amount = models.IntegerField(
        "Quantidade", null=False, blank=False, default=0)
    description = models.TextField("Descrição", null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Alterado em", auto_now=True)

    class Meta:
        # Latest by ascending order_date.
        get_latest_by = "-created_at"
        ordering = ['-created_at']
        verbose_name_plural = "Produtos"
        verbose_name_plural = "Produto"


    def get_absolute_url(self):
        return "/detail/%d/" % (self.id)
