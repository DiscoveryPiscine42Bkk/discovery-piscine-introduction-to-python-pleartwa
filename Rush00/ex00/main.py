from checkmate import checkmate
import sys

def load_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except:
        return None  # Error ระหว่างเปิดไฟล์ → จะ print("Error") ภายหลัง

def main():
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            content = load_file(path)
            if content:
                checkmate(content)
            else:
                print("Error")
    else:
        # กระดาน default หากไม่ระบุ argument
        board = """\
R...
.K..
..P.
...."""
        checkmate(board)

if __name__ == "__main__":
    main()
