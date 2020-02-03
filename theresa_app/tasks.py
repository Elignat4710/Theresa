from theresa_proj.celery_app import app
from .models import Product


@app.task
def save_product(items):
    Product.objects.bulk_create(
        [Product(**item) for item in items]
    )