import random
class Ghost(object):
    """
    Rastgele bir renge sahip bir Ghost nesnesi oluşturur.
    """
    def __init__(self):
        """
        Ghost nesnesini başlatır ve rastgele bir renk atar.
        """
        # Muhtemel renklerin bir listesini tanımla
        colors = ["white", "yellow", "purple", "red"]
        
        # self.color özelliğine rastgele bir renk ata
        # random.choice() metodu, bir listeden rastgele bir eleman seçer.
        self.color = random.choice(colors)