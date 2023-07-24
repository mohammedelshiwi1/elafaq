from django.db import models
from exams.models import Quiz


month_choices=(("jan", "jan"),
    ("feb", "feb"),
    ("mar", "mar"),
    ("apr", "apr"),
    ("may", "may"),
    ("jun", "jun"),
    ("jul", "jul"),
    ("aug", "aug"),
    ("sep","sep"),
    ("oct","oct"),
    ("nov","nov"),
    ("dec","dec"))
class lecture(models.Model):
    title=models.CharField(max_length=50)
    des=models.CharField(max_length=100)
    image=models.ImageField( )
    slug=models.SlugField(blank=True)
    pdf= models.URLField(blank=True)
    videourl=models.URLField(blank=True)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True)
    lecture_month=models.CharField(null=True,choices=month_choices,max_length=20)
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.slug=self.id
        super().save(*args,**kwargs)
# Create your models here.
class notfication(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    number=models.IntegerField()
    des=models.TextField()
class questions(models.Model):
    user=models.CharField(max_length=40)
    ques=models.CharField(max_length=200)
    lecture=models.ForeignKey(lecture,null=True,on_delete=models.CASCADE)
    