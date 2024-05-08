from django.db import models


class Actor(models.Model):
    image = models.ImageField("Изображение", upload_to="actors/")
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    age = models.SmallIntegerField("Возраст", default=0)
    discription = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Актёры и Режиссёры"
        verbose_name_plural = "Актёры и Режиссёры"


class Film(models.Model):
    image = models.ImageField("Постер", upload_to="poster/")
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='acted_in')
    director = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='directed_films')
    name = models.CharField("Название", max_length=100)
    discription = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    date = models.DateTimeField("Дата выхода:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"