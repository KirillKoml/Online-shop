from django.db import models

from login.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Категория",
        help_text="Введите название категорий",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категорий",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Mete:
        verbose_name = "Товар"
        verbose_description = "Товара"


class Product(models.Model):
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Название",
        help_text="Введите название товара",
    )
    image = models.ImageField(
        upload_to="products/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию товара",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена",
        help_text="Укажите цену"
    )
    data_bd = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата создания",
        help_text="укажите дату создания",
    )
    data_refresh = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата изменения",
        help_text="укажите дату изменения",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="укажите количество просмотров товара",
        default=0,
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True,
                               related_name='login', )
    sign_publication_product = models.BooleanField(default=False, verbose_name='Признак публикации продукта', )

    def __str__(self):
        return self.name

    class Mete:
        verbose_name = "Товар"
        verbose_description = "Товара"
        ordering = ["name", "description"]
        permissions = [
            ('may_cancel_publication_product', 'may cancel publication product'),
            ('can_change_description_product', 'can change description product'),
            ('can_change_category_product', 'can change category product')
        ]


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    message = models.TextField(verbose_name="Сообщение")
    data_send = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return self.name
