from django.db import models


# Create your models here.
class Blog(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите название заголовка",
    )
    description = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите описание заголовка",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="blog_images/",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        blank=True,
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
        default=0,
        verbose_name="Количество просмотров",
        help_text="укажите количество просмотров товара",
        blank=True,
        null=True,
    )

    class Mete:
        verbose_name = "Заметка"
        verbose_description = "Заметки"
        ordering = ["name", "description"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    message = models.TextField(verbose_name="Сообщение")
    data_send = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return self.name
