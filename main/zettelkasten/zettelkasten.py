from note import Note
from identifier import Identifier
from graph import Graph

class Zettelkasten:
    def __init__(self):
        self.notes = {}
        self.graph = Graph()

    def create_note(self, content):
        note = Note(content)
        self.notes[note.id] = note
        return note.id

    def get_note(self, id):
        return self.notes.get(id)

    def link_notes(self, id1, id2):
        self.graph.add_edge(id1, id2)

    def get_linked_notes(self, id):
        linked_ids = self.graph.get_linked_nodes(id)
        return [self.notes[id] for id in linked_ids]

    def search_notes(self, query):
        return [note for note in self.notes.values() if query in note.content]