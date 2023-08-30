class Note(object):
    def __init__(self, contents = None):    #초기값 : None
        self.contents = contents

    def write_content(self, contents):
        self.contents = contents

    def remove_all(self):
        self.contents = ""

    def __str__(self):
        return self.contents            



class Notebook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}     #딕셔너리형 (key : page_number, value : Note의 인스턴스)

    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page:note}
                self.page_number += 1
        else:
            print("페이지가 모두 채워짐")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않음")

    def get_number_of_pages(self):
        return len(self.notes.keys())     
        