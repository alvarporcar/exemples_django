from aplica1.models import Usuaris, Organismes, Projectes, Carrecs, Tipus_Organismes
from django.contrib import admin


class UsuarisAdmin(admin.ModelAdmin):
    list_display= ('cognoms','nom', 'email1','email2','tel1','carrec','organisme','notes')
    
    list_filter= ('organisme','projectes','carrec')
    search_fields = ['cognoms']

class OrganismesAdmin(admin.ModelAdmin):
    list_display= ('nom', 'email1','tel1','fax1','web','notes')
    search_fields = ['nom']

class ProjectesAdmin(admin.ModelAdmin):
    list_display = ('nom','abrev','web', 'responsable','notes')
    search_fields = ['nom']

admin.site.register(Usuaris, UsuarisAdmin)
admin.site.register(Organismes,OrganismesAdmin)
admin.site.register(Projectes,ProjectesAdmin)
admin.site.register(Carrecs)
admin.site.register(Tipus_Organismes)


