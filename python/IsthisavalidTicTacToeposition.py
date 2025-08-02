def is_valid_position(board: tuple[tuple[str, ...], ...]) -> bool:
    """
    Belirtilen Tic Tac Toe tahtasının normal oyunla ulaşılabilir bir pozisyonu temsil edip etmediğini kontrol eder.

    Args:
        board: 3x3 bir Tic Tac Toe tahtasını temsil eden bir tuple tuple'ı.

    Returns:
        Pozisyon geçerliyse True, aksi takdirde False.
    """

    def check_win(player: str) -> bool:
        """Belirli bir oyuncunun kazanıp kazanmadığını kontrol eden yardımcı fonksiyon."""
        # Kazanma koşulları: 3 satır, 3 sütun ve 2 çapraz
        win_conditions = [
            # Satırlar
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            # Sütunlar
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            # Çaprazlar
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]
        ]
        
        for condition in win_conditions:
            if all(cell == player for cell in condition):
                return True
        return False

    # 1. 'X' ve 'O' sembollerinin sayısını say
    count_x = sum(row.count('X') for row in board)
    count_o = sum(row.count('O') for row in board)

    # 2. X ve O sayılarının geçerli bir oyun durumu için doğru olup olmadığını kontrol et
    # X her zaman ilk oynar, bu nedenle X sayısı O sayısına eşit veya bir fazla olmalıdır.
    if not (count_x == count_o or count_x == count_o + 1):
        return False

    # 3. Oyuncuların kazanıp kazanmadığını kontrol et
    x_has_won = check_win('X')
    o_has_won = check_win('O')

    # 4. Kazanma durumlarına göre geçerliliği belirle
    if x_has_won and o_has_won:
        # İki oyuncunun aynı anda kazanması mümkün değildir.
        return False
    
    if x_has_won:
        # Eğer 'X' kazandıysa, bu X'in son hamlesi olmalıdır.
        # Bu durumda, X'in sayısı O'nun sayısından bir fazla olmalıdır.
        return count_x == count_o + 1
    
    if o_has_won:
        # Eğer 'O' kazandıysa, bu O'nun son hamlesi olmalıdır.
        # Bu durumda, X'in sayısı O'nun sayısına eşit olmalıdır.
        return count_x == count_o
    
    # 5. Kazanan yoksa, hamle sırası geçerli olmalıdır.
    # Bu zaten yukarıdaki 2. adımda kontrol edildi.
    return True