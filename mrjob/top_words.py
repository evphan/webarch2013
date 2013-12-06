""" Most Common Title Words - Note: 2 step process, based on the example from the tutorial (http://pythonhosted.org/mrjob/guides/quickstart.html#writing-your-second-job)"""

from mrjob.job import MRJob
from combine_user_visits import csv_readline
import re
WORD_RE = re.compile(r"[\w']+")

# WORD_RE.findall('the tree is green') will return this list: ['the', 'tree', 'is', 'green']

class TopWords(MRJob):

    def mapper_get_words(self, _, line):
        # yield each word in the line
        items = csv_readline(line)
        if items[0] == 'A':
            words = WORD_RE.findall(items[3].lower())
            for item in words:
                yield item, 1
            
            
    def reducer_count_words(self, word, counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        yield None, (sum(counts), word)

    # discard the key; it is just None
    def reducer_find_max_word(self, _, word_count_pairs):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        top_words = sorted(word_count_pairs, reverse=True)
        for i in range(10):
            yield top_words[i]
        
    def steps(self):
        return [
            self.mr(mapper=self.mapper_get_words,
                    reducer=self.reducer_count_words),
            self.mr(reducer=self.reducer_find_max_word)
        ]
        
if __name__ == '__main__':
    TopWords.run()
