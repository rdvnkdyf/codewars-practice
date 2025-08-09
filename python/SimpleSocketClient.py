import socket

def socket_client():
    """
    Connects to a server on port 1111, sends a packet, and determines 
    if the server is a regular echo server or a reversing server.

    Returns:
        True if the server is regular (sends back the same data).
        False if the server is a reversing server.
    """
    # Veriyi tanımlayalım. Tersine çevrildiğinde farklı olacak bir string seçmek önemlidir.
    # Örneğin, "hello" ters çevrildiğinde "olleh" olur.
    test_data = "hello"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 1111))
        
        # Veriyi sunucuya gönderelim. encode() ile byte dizisine çevirmeliyiz.
        s.sendall(test_data.encode())
        
        # Sunucudan gelen veriyi alalım.
        # recv(1024) ile en fazla 1024 byte veri okuruz.
        received_data = s.recv(1024).decode()
        
    # Gelen veri, gönderdiğimiz veriye eşitse, sunucu düzenli bir sunucudur.
    if received_data == test_data:
        return True
    else:
        # Aksi halde, gelen veri tersine çevrilmiş olmalıdır.
        return False