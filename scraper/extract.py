import requests
import json
from datetime import datetime

def get_steam_deals():
    """Obtém promoções da Steam e retorna dados formatados"""
    url = "https://store.steampowered.com/api/featuredcategories"
    params = {'cc': 'br', 'l': 'portuguese'}
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        # Processa os dados das promoções
        deals = []
        for item in data.get('specials', {}).get('items', []):
            deal = {
                'nome': item.get('name'),
                'preco_original': item.get('original_price', 0) / 100,
                'preco_com_desconto': item.get('final_price', 0) / 100,
                'desconto': item.get('discount_percent', 0),
                'validade_desconto': datetime.fromtimestamp(item.get('discount_expiration', 0)).strftime('%d/%m/%Y'),
                'link': f"https://store.steampowered.com/app/{item.get('id')}"
            }
            deals.append(deal)
        
        return deals
    
    except:
        return None

def save_to_json(deals, filename='promocoes_steam.json'):
    """Salva os dados em um arquivo JSON"""
    if deals:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(deals, f, ensure_ascii=False, indent=2)
        print(f"Dados salvos em {filename}")
    else:
        print("Nenhum dado para salvar")

# Execução principal
if __name__ == "__main__":
    print("Buscando promoções da Steam...")
    promocoes = get_steam_deals()
    
    if promocoes:
        print(f"Encontradas {len(promocoes)} promoções!")
        save_to_json(promocoes)
        
        # Mostra as 3 primeiras promoções no console
        print("\nExemplo de promoções encontradas:")
        for promo in promocoes[:3]:
            print(f"\n{promo['nome']}")
            print(f"De R${promo['preco_original']:.2f} por R${promo['preco_com_desconto']:.2f}")
            print(f"Desconto: {promo['desconto']}% (Válido até {promo['validade_desconto']})")
    else:
        print("Não foi possível obter as promoções")