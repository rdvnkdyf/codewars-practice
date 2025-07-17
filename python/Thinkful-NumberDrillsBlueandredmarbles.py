def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    remaining_blue = blue_start - blue_pulled
    total_remaining = (blue_start - blue_pulled) + ( red_start - red_pulled)

    # Torba boşsa 0.0 döndür, aksi takdirde olasılığı hesapla.
    return float(remaining_blue) / total_remaining if total_remaining else 0.0