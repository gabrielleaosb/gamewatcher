from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def home(request):
    # Dados mock para jogos em destaque
    games = [
        {
            "name": "Elden Ring",
            "platforms": ["PC", "PS5", "Xbox Series X"],
            "image": "game-placeholder.jpg",
            "sites": [
                {"name": "Steam", "original_price": 299.90, "discount_price": 74.90, "discount": 75, "url": "#"},
                {"name": "Nuuvem", "original_price": 279.90, "discount_price": 69.90, "discount": 75, "url": "#"}
            ]
        },
        {
            "name": "The Witcher 3",
            "platforms": ["PC", "Nintendo Switch"],
            "image": "game-placeholder.jpg",
            "sites": [
                {"name": "GOG", "original_price": 99.90, "discount_price": 29.90, "discount": 70, "url": "#"}
            ]
        },
        {
            "name": "Cyberpunk 2077",
            "platforms": ["PC", "PS5"],
            "image": "game-placeholder.jpg",
            "sites": [
                {"name": "Epic Games", "original_price": 199.90, "discount_price": 99.90, "discount": 50, "url": "#"}
            ]
        },
        {
            "name": "Red Dead Redemption 2",
            "platforms": ["PC", "PS4", "Xbox One"],
            "image": "game-placeholder.jpg",
            "sites": [
                {"name": "Rockstar Store", "original_price": 249.90, "discount_price": 149.90, "discount": 40, "url": "#"}
            ]
        }
    ]
    
    # Dados mock para jogos monitorados (apenas para usuários logados)
    watched_games = []
    if request.user.is_authenticated:
        watched_games = [
            {"name": "The Witcher 3", "image": "game-placeholder.jpg", "current_price": 59.90, "lowest_price": 29.90, "discount": 50},
            {"name": "Stardew Valley", "image": "game-placeholder.jpg", "current_price": 24.90, "lowest_price": 14.90, "discount": 40}
        ]
    
    return render(request, 'core/home.html', {
        'games': games,
        'watched_games': watched_games,
        'user': request.user
    })

@login_required
def wishlist(request):
    return render(request, 'core/wishlist.html')
