from django.db import models
from django.urls import reverse



class News(models.Model):
    title = models.CharField(max_length=300, verbose_name='Имя и Фамилия')
    content = models.CharField(max_length=300, blank=True, verbose_name='Должность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Edited')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', verbose_name='Фотография, 120x120, круглая', blank='True')
    is_published = models.BooleanField(default = True, verbose_name='Published?')
    category = models.ForeignKey('category', on_delete=models.PROTECT, verbose_name='Отдел')
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Создатель')
    views = models.IntegerField(default=0)
    facebook = models.URLField(max_length=300, verbose_name='Ссылка на фейсбук', default='https://www.facebook.com/reputation.moscow')
    telegram = models.CharField(max_length=300, verbose_name='Ссылка на Телеграм', default='https://t.me/reputation_moscow')
    twitter = models.URLField(max_length=300, verbose_name='Ссылка на Твиттер', default='https://twitter.com/reputation_msk')
    youtube = models.URLField(max_length=300, verbose_name='Ссылка на Ютуб', default='https://www.youtube.com/channel/UCO5ByGg4jQZbIjvxvTrGHXA')
    email = models.EmailField(verbose_name='Email', blank=True)
    brand = models.ForeignKey('brand', on_delete=models.PROTECT, verbose_name='Бренд')
    photoUrl = models.URLField(max_length=300, verbose_name='Ссылка на круглую фотографию размером 120x120', default='https://reputation.moscow/wp-content/uploads/2021/10/tpt4wah34-ur3adchsq-0842468d74a9-512-3.png')

    def get_absolute_url(self):
        return reverse("view_news", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подпись'
        verbose_name_plural = 'Подписи'
        ordering = ['-created_at', 'title']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Отдел')

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ['title']

class Brand(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Бренд')

    def get_absolute_url(self):
        return reverse("brand", kwargs={"brand_id": self.pk})

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['title']

class Author(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Author") 

    def __str__(self):
            return self.title

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['title']



