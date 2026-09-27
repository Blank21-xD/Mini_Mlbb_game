from django.shortcuts import render
from .models import Hero
from .services import CombatEngine  # Fixed spelling: CombatEngine


def roster_view(request):
    # Fixed typo: objects instead of ojects
    heroes = Hero.objects.all()

    # We are tracking 'level' instead of 'attack' multiplier for our stat scaling
    level = int(request.GET.get("level", 1))

    processed_heroes = []
    for hero in heroes:
        # Pass the hero object and level into our CombatEngine method
        scaled_data = CombatEngine.calculate_scaled_stats(hero, level)
        processed_heroes.append(scaled_data)

    # Package everything into a context dictionary before returning
    context = {
        "heroes": processed_heroes,
        "current_level": level,
    }

    # Only one return statement at the end of the function
    return render(request, "roster.html", context)
