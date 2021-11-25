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
            if arg_len > 2:
                try:
                    self._minimum_count = int(args[2])
                except ValueError:
                    self._stop_words = self.read_and_parse(args[2])
                if arg_len == 4:
                    try:
                        self._minimum_count = int(args[3])
                    except:
                        print("Require to input whole number.")
                        sys.exit(1)

            self.frequency_outputter(self.frequency_sorter(self.stop_words_removed_remove_minimum_count))

    def frequency_outputter(self,frequency):        
        for word in frequency:
            print(word[0], word[1])

    def frequency_sorter(self, frequency):
        return sorted(frequency.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    @property
    def stop_words_removed_remove_minimum_count(self):
        return self.remove_minimum_count(self.stop_words_removed)

    def remove_minimum_count(self, frequency):
        if self._minimum_count > 0:
            return {key: value for key, value in frequency.items() if value > self._minimum_count}
        return frequency

    @property
    def stop_words_removed(self):
        if self._stop_words:
            new_frequency = self.frequency
            for word in self._stop_words:
                del new_frequency[word]
            return new_frequency
        return self.frequency

    @property
    def frequency(self):
        frequency = {}
        for word in self._words:
            if word[-1] == '.':
                word = word[0:len(word) - 1]

            word = word.lower()
            if word in frequency:
                frequency[word] += 1
            else:
                frequency.update({word: 1})
        return frequency

    def read_and_parse(self, file_name):
        try:
            with open(file_name, 'r') as my_file:
                return my_file.read().split()
        except FileNotFoundError:
            print(f'{file_name} not found.')
            sys.exit(1)


if __name__ == '__main__':
    Domain(*sys.argv)
