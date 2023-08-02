class Identifier:
    def __init__(self, id_string):
        self.id_string = id_string

    def get_id(self):
        return self.id_string

    def set_id(self, new_id):
        self.id_string = new_id

    def __str__(self):
        return self.id_string

    def __eq__(self, other):
        if isinstance(other, Identifier):
            return self.id_string == other.id_string
        return False

    def __hash__(self):
        return hash(self.id_string)