class Item:
    name = None
    slot = None
    itemtype = None

    # Assigns values to the object upon instantiation
    def __init__(self, n, s, t):
        self.name = n
        self.slot = s
        self.itemtype = t

    # Returns a string containing the weapon or armor attributes
    def __str__(self):
        return (f"{self.name}"
                f"{self.slot} {self.itemtype}")

    # Returns the name of the object
    def get_name(self):
        return self.name

    # Returns the slot of the object
    def get_slot(self):
        return self.slot

    # Returns the type of the object
    def get_itemtype(self):
        return self.itemtype
