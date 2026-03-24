import os
import hashlib

class MD5Manager:
    def __init__(self, file_path: str="md5.text"):
        self.file_path: str = file_path

    @staticmethod
    def get_md5(input: str) -> str:
        md5_generator = hashlib.md5()
        md5_generator.update(input.encode())
        md5_hex_str: str = md5_generator.hexdigest()
        return md5_hex_str

    def is_exist(self, md5_str: str) -> bool:
        if not os.path.exists(self.file_path):
            return False

        with open(self.file_path, "r", encoding="utf-8") as f:
            for l in f.readlines():
                md5_in_file: str = l.strip()
                if md5_in_file == md5_str:
                    return True
            
        return False

    def save_md5(self, md5_str: str, unique: bool=True) -> bool:
        if unique and self.is_exist(md5_str):
            return False
            
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(md5_str + "\n")
            return True
    

if __name__ == "__main__":
    mm = MD5Manager()
    hello_str = "hello"
    hello_str_md5 = mm.get_md5(hello_str)
    print(mm.get_md5("hello"))
    mm.save_md5(hello_str_md5)
    print(mm.is_exist(hello_str_md5))