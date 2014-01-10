# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import (Agenda, Deliberation, Vote)

admin.site.register(Agenda)
admin.site.register(Deliberation)
admin.site.register(Vote)
