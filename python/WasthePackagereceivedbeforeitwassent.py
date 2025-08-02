def was_package_received_yesterday(tz_from, tz_to, start, duration):
    # Paketin gönderildiği saat UTC cinsinden
    # Örnek: tz_from=3, start=13 -> UTC saat: 13 - 3 = 10 (10:00 UTC)
    gonderim_utc = start - tz_from

    # Paketin teslim edildiği saat UTC cinsinden
    # Örnek: gonderim_utc=10, duration=1 -> Teslimat UTC: 10 + 1 = 11 (11:00 UTC)
    teslimat_utc = gonderim_utc + duration

    # Paketin hedef zaman dilimindeki yerel teslimat saati
    # Örnek: teslimat_utc=11, tz_to=0 -> Teslimat Yerel: 11 + 0 = 11 (0. zaman diliminde 11:00)
    teslimat_yerel = teslimat_utc + tz_to

    # Teslimatın gün farkını kontrol et
    # Eğer teslimat_yerel 0'dan küçükse, bu paketin bir önceki gün teslim edildiği anlamına gelir.
    # Örneğin, teslimat_yerel = -2 ise, bu bir önceki günün saat 22:00'idir.
    return teslimat_yerel < 0