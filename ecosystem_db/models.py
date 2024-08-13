from django.db import models

class Stakeholder(models.Model):
    name = models.CharField(max_length=255)
    entity = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    venture_studio_friendly_outreach = models.BooleanField(default=False)
    pdx_climate_friends = models.BooleanField(default=False)
    pdx_cf_711 = models.CharField(max_length=255, blank=True, null=True)
    ecosystem_group = models.CharField(max_length=255, blank=True, null=True)
    cw_primary_program = models.CharField(max_length=255, blank=True, null=True)
    cw_secondary_program = models.CharField(max_length=255, blank=True, null=True)
    contact_owner = models.CharField(max_length=255, blank=True, null=True)
    next_steps_notes = models.TextField(blank=True, null=True)

class CallNote(models.Model):
    stakeholder = models.ForeignKey(Stakeholder, on_delete=models.CASCADE)
    note_date = models.DateField()
    notes = models.TextField()