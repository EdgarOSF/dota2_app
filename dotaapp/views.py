import requests
from django.shortcuts import render

def player_matches(request):
    account_id = request.GET.get('account_id', '76561198043548173')  # Puedes cambiar este por un id real
    url = f'https://api.opendota.com/api/players/{account_id}/heroes'

    response = requests.get(url)
    matches = response.json()

    print(matches)

    context = {
        'matches': matches,
        'account_id': account_id
    }
    return render(request, 'dotaapp/matches.html', context)
