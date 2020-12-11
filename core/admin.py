from django.contrib import admin
from .models import Worker, Genre, Ticket, Performance, OrchestraMember, \
    Orchestra, Role, Author, Position, Play, Hall, Customer

admin.site.register(Genre)
admin.site.register(Performance)
admin.site.register(Orchestra)
admin.site.register(OrchestraMember)
admin.site.register(Author)
admin.site.register(Play)
admin.site.register(Worker)
admin.site.register(Position)
admin.site.register(Hall)
admin.site.register(Role)
admin.site.register(Ticket)
admin.site.register(Customer)

