class Automaton(object):
    """
    Belirli bir dildeki komutları okuyan bir Sonlu Durum Makinesi (Otomaton)
    uygulaması.
    """

    def __init__(self):
        """
        Otomaton'un durumlarını, başlangıç durumunu ve geçiş kurallarını
        ayarlar.
        """
        # Durumlar ve geçiş kurallarını temsil eden bir sözlük (dictionary).
        # Anahtarlar (mevcut durum, komut) ikilisi, değerler ise
        # bir sonraki durumdur.
        self.transitions = {
            ('q1', '0'): 'q1',
            ('q1', '1'): 'q2',
            ('q2', '0'): 'q3',
            ('q2', '1'): 'q2',
            ('q3', '0'): 'q2',
            ('q3', '1'): 'q2',
        }
        
        # Başlangıç durumu, 'q1'.
        self.start_state = 'q1'
        # Kabul durumu, 'q2'.
        self.accept_state = 'q2'

    def read_commands(self, commands):
        """
        Bir komut dizisini okur ve son durumun kabul durumu olup
        olmadığını döndürür.

        Parametreler:
        commands (list): Okunacak komutları içeren bir dizi.
        
        Dönüş değeri:
        (bool): Son durum kabul durumu ise True, aksi takdirde False.
        """
        # Mevcut durumu başlangıç durumu olarak ayarla.
        current_state = self.start_state
        
        # Komut dizisindeki her bir komutu sırayla oku.
        for command in commands:
            # Geçiş kurallarını kullanarak bir sonraki duruma geç.
            # (current_state, command) ikilisi ile sözlükten yeni durumu al.
            current_state = self.transitions.get((current_state, command), current_state)

        # Tüm komutlar okunduktan sonra, son durumun kabul durumu olup
        # olmadığını kontrol et ve sonucu döndür.
        return current_state == self.accept_state

# Otomaton nesnesini oluştur. Bu nesne testler tarafından çağrılacaktır.
my_automaton = Automaton()

# Durumların, geçişlerin ve kabul durumunun __init__ metodunda tanımlanması
# sayesinde, burada ekstra bir kurulum yapmaya gerek yoktur.