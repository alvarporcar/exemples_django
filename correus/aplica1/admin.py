from aplica1.models import Usuaris, Organismes, Projectes, Carrecs, Tipus_Organismes, Usuaris_Projectes
from django.contrib import admin

admin.site.register(Usuaris)
admin.site.register(Organismes)
admin.site.register(Projectes)
admin.site.register(Carrecs)
admin.site.register(Tipus_Organismes)
admin.site.register(Usuaris_Projectes)

class UsuarisAdmin(admin.ModelAdmin):
    list_display= ('__unicode__','cognoms','organisme')

