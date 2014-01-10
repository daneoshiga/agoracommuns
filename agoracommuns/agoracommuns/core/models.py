from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.models import TimeStampedModel


class Agenda(TimeStampedModel):
    STATUS_CHOICES = Choices(
        (0, 'proposal', _(u"Proposal")),
        (1, 'deliberation', _(u"Deliberation")),
        (2, 'voting', _(u"Voting")),
        (2, 'closed', _(u"Closed")),
    )

    user = models.ForeignKey(User)
    validation_date = models.DateField(_("Validation Date"))
    deliberation_date = models.DateField(_("Data Deliberacao"))
    voting_date = models.DateField(_("Data Votacao"))
    promotion_votes = models.IntegerField(_("Promoting Votes"))
    title = models.CharField(_("Title"), max_length=70)
    agenda = models.TextField(_("Agenda"))
    status = models.IntegerField(
        _("Status"), max_length=1,
        choices=STATUS_CHOICES)

    def __unicode__(self):
        return self.title


class Deliberation(TimeStampedModel):
    agenda = models.ForeignKey(Agenda)
    user = models.ForeignKey(User)
    proposal = models.TextField(_("Proposal"))

    def __unicode__(self):
        return self.proposal


class Vote(TimeStampedModel):
    VOTE_CHOICES = Choices(
        (0, 'favor', _("Favor")),
        (1, 'against', _("Against")),
    )

    agenda = models.ForeignKey(Agenda)
    user = models.ForeignKey(User)
    deliberation = models.ForeignKey(Deliberation)
    type = models.IntegerField(
        choices=VOTE_CHOICES
    )
