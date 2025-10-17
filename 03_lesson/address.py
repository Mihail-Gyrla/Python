class Address:
    def __init__(self, index, gorod, ulitca, dom, kvartira):
        self.index = index
        self.gorod = gorod
        self.ulitca = ulitca
        self.dom = dom
        self.kvartira = kvartira

    def __str__(self):
        return f"{self.index}, {self.gorod}, {self.ulitca}, \
{self.dom} - {self.kvartira}"
