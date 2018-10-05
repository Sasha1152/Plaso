from django.db import models
import datetime


class CommonData(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='planets/images/')
    symbol = models.ImageField(blank=True, null=True, upload_to='planets/images/')
    escape_velocity = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Escape velocity, km/s')
    surface_gravity = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2, verbose_name='Surface gravity, g')
    orbital_period = models.TextField(blank=True)
    mean_radius_to_earth = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Planet radius relative to an Earth')
    surface_pressure = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Surface pressure, bar')
    discovery_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    wiki = models.URLField(blank=True)

    class Meta:
        abstract = True


class Planet(CommonData):
    number = models.PositiveSmallIntegerField(primary_key=True)
    planet_mass_to_earth = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, verbose_name='Planet mass relative to an Earth')
    orbital_speed = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Average orbital speed, km/s')
    moons_quantity = models.PositiveSmallIntegerField(blank=True, default=0)
    rotation_period = models.TextField(blank=True)
    semi_major_axis = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Semi major axis, AU')

    class Meta:
        ordering = ['number']
        verbose_name = 'planet'
        verbose_name_plural = 'planets'

    def __str__(self):
        return self.name


class Moon(CommonData):
    name = models.CharField(max_length=30, primary_key=True)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name='moons')
    number_m = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['planet']
        verbose_name = 'moon'
        verbose_name_plural = 'moons'

    def __str__(self):
        return str(self.planet) + '--' + str(self.name)
