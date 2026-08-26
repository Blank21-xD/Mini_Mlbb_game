from django.shortcuts import render
from .models import Hero
from .services import CombatEngine
from django.http import JsonResponse


def roster_view(request):
    heroes = Hero.objects.all()
    processed_roster = []

    # Delegate math to the Service Layer for a Level 15 maxed hero
    for hero in heroes:
        stats = CombatEngine.calculate_scaled_stats(hero, level=15)
        processed_roster.append({
            'instance': hero,
            'calculated_stats': stats
        })

    context = {
        'roster': processed_roster
    }
    return render(request, 'heroes/roster.html', context)


def dynamic_role_view(request, role_name):
    # 1. Plug the URL variable directly into the filter!
    heroes = Hero.objects.filter(role__iexact=role_name)

    processed_roster = []

    for hero in heroes:
        processed_roster.append({
            'instance': hero,
            'calculated_stats': CombatEngine.calculate_scaled_stats(hero, level=15)
        })

    context = {
        'roster': processed_roster,
        # Optional: sending the name to the HTML
        'current_role': role_name.capitalize()
    }

    # We can safely reuse our existing roster template
    return render(request, 'heroes/roster.html', context)


def dynamic_api_view(request, role_name):
    # 1. Use the URL variable to filter the database (case-insensitive)
    heroes = Hero.objects.filter(role__iexact=role_name)
    api_data = []

    for hero in heroes:
        stats = CombatEngine.calculate_scaled_stats(hero, level=15)
        api_data.append({
            'name': hero.name,
            'role': hero.role,
            'stats': stats
        })

    # 2. Return the data as JSON instead of rendering a template
    return JsonResponse(api_data, safe=False)
