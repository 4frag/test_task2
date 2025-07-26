from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.title

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) ->  str:
        return self.title

    def get_url(self) -> str:
        if self.parent is not None:
            return f'{self.parent.get_url()}/{self.slug}'
        return self.slug

    class Meta:
        indexes = (
            models.Index(fields=('parent', 'slug')),
        )
