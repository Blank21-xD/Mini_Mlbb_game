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


def api_roster(request):
    heroes = Hero.objects.all()
    api_data = []

    for hero in heroes:
        stats = CombatEngine.calculate_scaled_stats(hero, level=15)

        # Build a clean dictionary for each hero
        api_data.append({
            'name': hero.name,
            'role': hero.role,
            'stats': stats
        })

    # 3. Return the data. safe=False is required when returning a List instead of a Dict.
    return JsonResponse(api_data, safe=False)


def api_assasins(request):
    heroes = Hero.objects.filter(role__iexact="Assasin")
    api_data = []

    for hero in heroes:
        stats = CombatEngine.calculate_scaled_stats(hero, level=15)
        api_data.append({
            'name': hero.name,
            'role': hero.role,
            'stats': stats
        })

    # The return statement is now OUTSIDE the loop.
    # It will return the list even if it is empty [].
    return JsonResponse(api_data, safe=False)
