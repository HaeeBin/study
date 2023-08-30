from lab9 import Note
from lab9 import Notebook

sentence = "Hello"
note_1 = Note(sentence)

sentence = "No pain no gain"
note_2 = Note(sentence)

sentence = """That some achieve great success, is proof to all that 
others can achieve it as well"""
note_3 = Note(sentence)

sentence = """To follow, without halt, one aim: that's the secret of success"""
note_4 = Note(sentence)

book_1 = Notebook("명언")
book_1.add_note(note_1)
book_1.add_note(note_2)
book_1.add_note(note_3)
book_1.add_note(note_4)

print(book_1.get_number_of_pages())     #결과 : 4

book_1.remove_note(3)
print(book_1.get_number_of_pages())     #결과 : 3

book_1.add_note(note_1, 100)
