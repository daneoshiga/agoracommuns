# -*- coding: utf-8 -*-
from django.test import TestCase

from model_mommy import mommy

from core.models import Agenda


class CoreModelsTests(TestCase):

    def test_agenda_create(self):
        agenda = mommy.make(Agenda)
        self.assertTrue(isinstance(agenda, Agenda))
        self.assertEqual(agenda.__unicode__(), agenda.title)
