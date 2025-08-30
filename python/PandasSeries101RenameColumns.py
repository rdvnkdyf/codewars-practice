import pandas as pd

def rename_columns(df, names):
    # Orijinal DataFrame'in bir kopyasını oluşturarak
    # orijinal veriyi değiştirmemeyi garanti altına alıyoruz.
    new_df = df.copy()

    # Sütunları yeni adlarla güncelliyoruz.
    new_df.columns = names

    # Yeni DataFrame'i döndürüyoruz.
    return new_df