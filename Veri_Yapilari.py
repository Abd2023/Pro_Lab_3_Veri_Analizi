class MyDict:
    def __init__(self):
        self.keys = []
        self.values = []

    def insert(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def get(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        else:
            return None

    def __setitem__(self, key, value):
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.insert(key, value)

    def __getitem__(self, key):
        return self.get(key)







class MyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items += [item]

    def get(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            return None





class MySet:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def contains(self, item):
        return item in self.items
