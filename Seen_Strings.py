import csv
import json
from typing import Dict

class Seen_Strings:
    def __init__(self, csv_path: str = None):
        if csv_path == None:
            self.strings: Dict[str, int] = {}
        else:
            self.strings: Dict[str, int] = {}
            with open(csv_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    self.strings[row[0]] = int(row[1])

    def add(self, s: str) -> None:
        if s in self.strings:
            self.strings[s] += 1
        else:
            self.strings[s] = 1
    
    def stats(self) -> Dict[str, str]:
        if len(self.strings) == 0:
            return {'NOT AVAILABLE': 'No strings added, stats are not available'}
        
        all_strings = json.dumps(self.strings)
        most_popular: str = max(self.strings, key=self.strings.get)
        longest: str = max(self.strings, key=len)

        return {
            "all strings": all_strings,
            "most popular string": most_popular,
            "longest string": longest
        }
    
    def to_csv(self, csv_path: str) -> None:
        with open(csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for s in self.strings:
                csv_writer.writerow([s, self.strings[s]])

    def from_csv(self, csv_path: str) -> None:
        self.strings.clear()
        with open(csv_path) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    self.strings[row[0]] = int(row[1])