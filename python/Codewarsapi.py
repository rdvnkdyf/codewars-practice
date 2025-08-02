""" Bu kod düzeltilecek."""
import requests
from bs4 import BeautifulSoup
import re

def get_code_challenges(n: int) -> list[int]:
    """
    Codewars liderlik tablosundan n'inci sıradaki kullanıcının 'totalAuthored' ve
    'totalCompleted' değerlerini çeker.

    Args:
        n (int): Liderlik tablosundaki sıralama numarası (1 <= n <= 500).

    Returns:
        list[int]: [totalAuthored, totalCompleted] değerlerini içeren bir liste.
                   Veri bulunamazsa boş bir liste döndürür.
    """
    # Codewars liderlik tablosunun URL'si
    url = "https://www.codewars.com/users/leaderboard"

    # Liderlik tablosu 8 sayfa (her sayfada 75 kullanıcı) ve 500. sıraya kadar
    # veri almak için her sayfayı gezmemiz gerekiyor.
    # Her sayfada 75 kullanıcı olduğu için, n'inci kullanıcı hangi sayfada
    # olduğunu hesaplıyoruz.
    page_number = (n - 1) // 75
    leaderboard_url = f"{url}?page={page_number}"

    try:
        # HTTP isteği göndererek sayfa içeriğini al
        response = requests.get(leaderboard_url)
        response.raise_for_status()  # HTTP hatası durumunda istisna fırlatır

        # BeautifulSoup ile HTML içeriğini ayrıştır
        soup = BeautifulSoup(response.text, 'html.parser')

        # Liderlik tablosu bir tablo (`<table>`) içinde yer alır.
        # Bu tabloyu bulmak için `table` etiketini arayabiliriz.
        # Tablonun body kısmındaki satırları (`<tr>`) alıyoruz.
        table_rows = soup.find('tbody').find_all('tr')
        
        # n'inci sıradaki kullanıcıya ait satırı bul.
        # Listeler 0'dan başladığı için n-1. indeksi kullanırız.
        # Ancak, her sayfada 75 kullanıcı olduğu için doğru satırı bulmak için
        # n'nin o sayfadaki indeksini hesaplamamız gerekiyor.
        # Sayfa 0 için n-1, sayfa 1 için n-1-75, vs.
        row_index_on_page = (n - 1) % 75

        if row_index_on_page < len(table_rows):
            target_row = table_rows[row_index_on_page]
            
            # Bu satırdaki sütunları (`<td>`) bul
            columns = target_row.find_all('td')

            # `totalAuthored` ve `totalCompleted` değerlerini içeren
            # sütunları bulmak için HTML yapısına bakmamız gerekiyor.
            # Kodwears'deki sıralama:
            # 1. sıra (boş)
            # 2. kullanıcı adı
            # 3. toplam yetkinlik
            # 4. total authored (kendi yazdığı kodlar)
            # 5. total completed (çözdüğü kodlar)
            
            # Genellikle 4. ve 5. sütunlar ilgilendiğimiz verileri içerir.
            if len(columns) > 4:
                # `totalAuthored` değerini al ve temizle
                authored_str = columns[3].get_text(strip=True)
                authored_value = int(re.sub(r'[^\d]', '', authored_str))

                # `totalCompleted` değerini al ve temizle
                completed_str = columns[4].get_text(strip=True)
                completed_value = int(re.sub(r'[^\d]', '', completed_str))
                
                return [authored_value, completed_value]

    except requests.exceptions.RequestException as e:
        print(f"Hata: Sayfaya erişilemiyor. {e}")
    except (AttributeError, IndexError) as e:
        print(f"Hata: HTML yapısı beklenenden farklı. Veri bulunamadı. {e}")
    
    return []
