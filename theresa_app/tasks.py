from theresa_proj.celery_app import app
from .models import Product


@app.task
def save_product(items):
    for item in items:
        Product.objects.create(
            url=item['url'],
            title=item['title'],
            price=item['price'],
            images=item['images'],
            description=item['description'],
            sizes=item['sizes'],
            category=item['category'],
        )
