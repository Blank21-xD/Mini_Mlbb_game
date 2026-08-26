class CombatEngine:
    """
    Production Service Layer for game mechanics.
    Decoupled from HTTP requests and Django view logic.
    """

    @staticmethod
    def calculate_scaled_stats(hero, level=1):
        # Base stat growth multipliers
        hp_growth = 140
        attack_growth = 12

        current_hp = hero.base_hp + (hp_growth * (level - 1))
        current_attack = hero.base_attack + (attack_growth * (level - 1))

        # Role-specific passive pass-throughs
        crit_rate = 0.05  # 5% base
        role = hero.role.lower()

        if role == 'marksman':
            crit_rate = 0.25
        elif role == 'assassin':
            crit_rate = 0.35

        return {
            'level': level,
            'hp': current_hp,
            'attack': current_attack,
            'crit_rate_pct': int(crit_rate * 100),
        }
