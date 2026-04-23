from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Player, Match, PlayerStat

@login_required
def dashboard(request):
    total_players = Player.objects.filter(is_active=True).count()
    total_wages = sum(p.wage for p in Player.objects.filter(is_active=True))
    total_matches = Match.objects.count()
    recent_matches = Match.objects.order_by('-match_date')[:5]
    return render(request, 'core/dashboard.html', {
        'total_players': total_players,
        'total_wages': total_wages,
        'total_matches': total_matches,
        'recent_matches': recent_matches,
    })

@login_required
def squad(request):
    search = request.GET.get('search', '')
    players = Player.objects.filter(is_active=True)
    if search:
        players = players.filter(name__icontains=search)
    players = players.order_by('shirt_number')
    return render(request, 'core/squad.html', {
        'players': players,
        'search': search,
    })

@login_required
def matches(request):
    all_matches = Match.objects.order_by('-match_date')
    return render(request, 'core/matches.html', {'matches': all_matches})

@login_required
def stats(request):
    all_stats = PlayerStat.objects.select_related('player', 'match').order_by('-match__match_date')
    return render(request, 'core/stats.html', {'stats': all_stats})
