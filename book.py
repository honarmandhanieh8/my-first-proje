class Ketab:
    def __init__(self, name, writer, price):
        self.name = name
        self.writer = writer
        self.price = price

    def namayesh(self):
        print("Name:", self.name)
        print("Writer:", self.writer)
        print("Price:", self.price)

    def takhfif(self, percent):
        self.price = self.price * (1 - percent / 100)


k = Ketab("Python", "Ali", 50)
k.namayesh()       
k.takhfif(10) 
k.namayesh()       
