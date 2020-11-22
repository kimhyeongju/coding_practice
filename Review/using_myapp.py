from myapp import Application, MenuItem
import sys

class NotepadApp(Application):
    def __init__(self):
        super().__init__()

    def create_menu(self, menu):
        menu.add(MenuItem("열기", self.open))
        menu.add(MenuItem("저장", self.save))
        menu.add(MenuItem("목록 보기", self.print_list))
        menu.add(MenuItem("종료", self.exit))

    def open(self):
        print("열기를 실행합니다.")

    def save(self):
        print("저장을 실행합니다.")

    def print_list(self):
        print("목록 보기를 실행합니다.")

    def exit(self):
        sys.exit(0)