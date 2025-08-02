def calculator(x, y, op):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "unknown value"

    # Ardından, "op" değişkeninin geçerli bir işlem sembolü olup olmadığını kontrol et.
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        # Bölme işleminde sıfıra bölme durumunu da kontrol etmek önemlidir.
        if y == 0:
            return "unknown value" # Ya da bir hata mesajı döndürülebilir.
        return x / y
    else:
        # Eğer işlem sembolü geçerli değilse, "unknown value" döndür.
        return "unknown value"