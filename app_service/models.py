from django.db import models
from multiselectfield import MultiSelectField


class FAQ(models.Model):
    question = models.CharField("Вопрос", max_length=255)
    answer = models.TextField("Ответ")

    class Meta:
        verbose_name = "Частый вопрос"
        verbose_name_plural = "Частые вопросы"

    def __str__(self):
        return self.question


class Program(models.Model):
    CATEGORY_CHOICES = [
        ('children_5_7', 'Для детей 5-7 классов'),
        ('school_8_11', 'Для школьников 8-11 классов'),
        ('adults', 'Для взрослых'),
        ('group', 'Групповой тренинг'),
    ]

    title = models.CharField(max_length=50, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    category = MultiSelectField(
        max_length=200,
        choices=CATEGORY_CHOICES,
        verbose_name='Категории',
        blank=False
    )
    benefits_list = models.TextField(verbose_name='Что дает программа?')
    image = models.FileField(upload_to='programs/', verbose_name='Баннер программы')
    start_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата проведения')

    def __str__(self):
        return f"{self.title} - {self.price}"


class Application(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Отправлено'),
        ('confirmed', 'Подтверждено'),
        ('paid', 'Оплачено'),
        ('canceled', 'Отменено'),
    ]

    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='sent',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    def __str__(self):
        return f"Заявка #{self.id} - {self.program.title}"


class Gallery(models.Model):
    image = models.FileField("Изображение", upload_to='gallery/')
    uploaded_at = models.DateTimeField("Дата загрузки", auto_now_add=True)

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Галерея изображений"
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"Изображение {self.id}"
