from typing import List, Dict

class Seen_Strings:
    def __init__(self):
        self.strings: Dict[str, int]                = {}
        # todo running record longest and most popular? better performance
        # self.longest_str: str                       = ''
        # self.most_popular_str: Dict[str, int]       = {}
        # todo init from an existing dict?
    
    def add(self, s: str):
        if s in self.strings.keys:
            self.strings[s] += 1
        else:
            self.strings[s] = 1
            if len(s) > len(self.longest_str):
                self.longest_str = s
            
    
    def stats(self) -> List[str]:
        all_strings: str = '\n'.join([s, self.strings[s] for s in self.strings.keys])
        most_popular: str = max(self.strings, key=self.strings.get)
        longest: str = max(self.strings, key=len)

        return [all_strings, most_popular, longest]