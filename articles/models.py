from django.db import models

a = "HELLO"
class Article(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    brief = models.TextField()
    date = models.DateField(auto_now=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    number_of_visit = models.IntegerField()
    picture_list = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    picture_detail = models.ImageField(upload_to='pictures/%Y/%m/%d/')

    def __str__(self):
        return self.title

class Visitor(models.Model):
    ip = models.CharField(max_length=25)

    def __str__(self):
        return self.ip

class Bridge(models.Model):
    stars = models.IntegerField()
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.stars)
