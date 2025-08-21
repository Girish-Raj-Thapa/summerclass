from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from . models import Product, Category
from utils.media_cleanup import delete_file_on_delete, delete_old_file_on_update

@receiver(pre_save, sender=Product)
def product_image_update_cleanup(sender, instance, **kwargs):
    delete_old_file_on_update(instance, Product, 'product_image')


@receiver(post_delete, sender=Product)
def product_image_delete_cleanup(sender, instance, **kwargs):
    delete_file_on_delete(instance, 'product_image')


@receiver(pre_save, sender=Category)
def category_image_update_cleanup(sender, instance, **kwargs):
    delete_old_file_on_update(instance, Category, 'category_image')

@receiver(post_delete, sender=Category)
def category_image_delete_cleanup(sender, instance, **kwargs):
    delete_file_on_delete(instance, 'category_image')