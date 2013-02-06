from django.db import models
from django.contrib import admin

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    models
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Author(models.Model):
    salutation = models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField()
    headsot = models.ImageField(upload_to='tmp/', blank=True,null=True)
    
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

   
class AuthorAdmin(admin.ModelAdmin):
    pass
    #exclude=('headsot',)


class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publisher','publication_date')
    search_fields = ('title',)
    ordering = ('-publication_date',)
    #date_hierarchy = 'publication_date'
    

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

admin.autodiscover()

