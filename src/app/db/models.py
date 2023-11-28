from tortoise import models, fields


class IdMixin(models.Model):
    id = fields.UUIDField(pk=True)

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created_at = fields.DatetimeField(auto_now=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseModel(IdMixin, TimeStampMixin):
    class Meta:
        abstract = True


class Product(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.TextField()
    description = fields.TextField()
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    image = fields.CharField(max_length=255)

    class Meta:
        table = 'product'


class Order(models.Model):
    id = fields.UUIDField(pk=True)
    products = fields.ManyToManyField('models.Product', related_name='orders', through='order_product')
    status = fields.CharField(max_length=20, choices=["in progress", "done"])
    total_amount = fields.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table = 'order'
