import csv
from typing import Dict

class Seen_Strings:
    def __init__(self, csv_path=None):
        if csv_path == None:
            self.strings: Dict[str, int] = {}
        else:
            self.strings: Dict[str, int] = {}
            with open(csv_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    self.strings[row[0]] = int(row[1]) # check this

        # todo running record longest and most popular? better performance
        # self.longest_str: str                       = ''
        # self.most_popular_str: Dict[str, int]       = {}

    def add(self, s: str) -> None:
        if s in self.strings:
            self.strings[s] += 1
        else:
            self.strings[s] = 1
            # if len(s) > len(self.longest_str):
            #     self.longest_str = s
    
    def stats(self) -> Dict[str, str]:
        if len(self.strings) == 0:
            return {'NOT AVAILABLE': 'No strings added, stats are not available'}
        
        all_strings: str = ''
        for s in self.strings:
            all_strings += ('"' + s + '": ' + str(self.strings[s]) + ', ')

        most_popular: str = max(self.strings, key=self.strings.get)
        longest: str = max(self.strings, key=len)

        return {
            "all strings": all_strings,
            "most popular string": most_popular,
            "longest string": longest
        }