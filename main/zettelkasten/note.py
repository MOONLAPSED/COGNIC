class Note:
    def __init__(self, id, content):
        self.id = id
        self.content = content
        self.links = []

    def add_link(self, note):
        if note not in self.links:
            self.links.append(note)

    def remove_link(self, note):
        if note in self.links:
            self.links.remove(note)

    def get_links(self):
        return self.links

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def get_id(self):
        return self.id