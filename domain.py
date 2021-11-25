import sys

class Domain:
    _words = []
    _stop_words = []
    _minimum_count = 0

    def __init__(self, *args) -> None:
        arg_len = len(args)
        if arg_len <= 1:
            print(
                "Please include neccessary parameter: file_name [stop_words_file_name] [minimum_count].")
        elif arg_len > 4:
            print("Too many parameters.")
        else:
            self._words = self.read_and_parse(args[1])
            try:
                self._minimum_count = int(args[2])
            except ValueError:
                self._stop_words = self.read_and_parse(args[2])
            if arg_len == 4:
                try:
                    self._minimum_count = int(args[3])
                except:
                    print("Require to input whole number")
                    sys.exit(1)


    def read_and_parse(self, file_name):
        try:
            with open(file_name, 'r') as my_file:
                return my_file.read().split()
        except FileNotFoundError:
            print(f'{file_name} not found.')
            sys.exit(1)

    def s(self):
        return 21
        # return file_name


if __name__ == '__main__':
    Domain(*sys.argv)
