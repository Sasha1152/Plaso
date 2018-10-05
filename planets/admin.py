from django.contrib import admin
from . models import Planet, Moon


# class MoonInLine(admin.TabularInline):
#     model = Moon
#     extra = 1
#     list_display = (
#         'planet_mother',
#         'name',
#         'escape_velocity',
#     )


class PlanetAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'name',
        'planet_mass_to_earth',
        'mean_radius_to_earth',
        'semi_major_axis',
        'orbital_speed',
        'orbital_period',
        'rotation_period',
        'escape_velocity',
        'surface_gravity',
        'surface_pressure',
        'moons_quantity',
        'discovery_date',
        'image',
        'symbol',

    )
    # inlines = [MoonInLine]

class MoonAdmin(admin.ModelAdmin):
    list_display = (
        'planet',
        'number_m',
        'name',
        'escape_velocity',
        'mean_radius_to_earth',
        'surface_gravity',
        'orbital_period',
        'discovery_date',
        'image',
        'symbol',
    )

admin.site.register(Planet, PlanetAdmin)
admin.site.register(Moon, MoonAdmin)
