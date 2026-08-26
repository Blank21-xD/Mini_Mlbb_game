from django.shortcuts import render
from .models import Hero
from .services import CombatEngine


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
