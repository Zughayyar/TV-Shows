from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=20)
    released_date = models.DateField()
    desc = models.TextField()

def get_all_shows():
    return Show.objects.all()

def get_show_by_id(id):
    return Show.objects.get(id=id)

def create_new_show(data):
    title = data['title']
    network = data['network']
    released_date = data['released_date']
    desc = data['desc']
    Show.objects.create(title=title, network=network, released_date=released_date, desc=desc)

def delete_show(id):
    c = Show.objects.get(id=id)
    c.delete()

def update_show(data, id):
    this_show = Show.objects.get(id=id)
    this_show.title = data['title']
    this_show.network = data['network']
    this_show.released_date = data['released_date']
    this_show.desc = data['desc']
    this_show.save()
    print(id)
    print(data['title'])
    print(data['network'])
