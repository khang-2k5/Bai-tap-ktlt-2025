print("Nguyễn Nhân Khang")
print("MSSV:235752020710012")
class StringManipulator:
    def __init__(self):
        self.user_string = ""  

    def get_String(self):
        self.user_string = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.user_string.upper())
manipulator = StringManipulator()
manipulator.get_String()
manipulator.print_String()
