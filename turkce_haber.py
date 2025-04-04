# Haber verilerinde türkçe harici çok fazla dil olduğundan dolayı türkçe haberleri önüme çıkarması için bu kodu ekledim.

import json

# Dosyanın yolu
file_path = 'C:/Users/Cansu/OneDrive/Masaüstü/2020717022/data/news.json'

# Dosyayı yükle ve JSON verilerini oku
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Türkçe haberleri filtrele
turkce_haberler = [haber for haber in data if haber.get('Language') == 'tr']

# Türkçe haberleri kaydet
filtered_file_path = 'C:/Users/Cansu/OneDrive/Masaüstü/2020717022/data/news.json'
with open(filtered_file_path, 'w', encoding='utf-8') as file:
    json.dump(turkce_haberler, file, ensure_ascii=False, indent=4)

filtered_file_path