from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    brief = models.TextField()
    date = models.DateField(auto_now=True)
    rate = models.DecimalField(max_digits=1, decimal_places=1)
    number_of_visit = models.IntegerField()
    picture_list = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    picture_detail = models.ImageField(upload_to='pictures/%Y/%m/%d/')

    def __str__(self):
        return self.title
