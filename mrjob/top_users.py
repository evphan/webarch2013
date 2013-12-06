""" Users > 20 visits """

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopUsers(MRJob):

    def mapper(self, line_no, line):
        """Extracts the Vroot that was visited"""
        cell = csv_readline(line)
        if len(cell) > 0 :
            if cell[0] == 'V':
                yield cell[2], 1
                  # What  Key, Value  do we want to output?

    def reducer(self, vroot, visit_counts):        
        """Sumarizes the visit counts by adding them together.  If total visits
        is more than 20, yield the results"""
        total = sum(visit_counts) 
                # How do we calculate the total visits from the visit_counts?
        if total > 20:
            yield vroot, total 
                  # What  Key, Value  do we want to output?
        
if __name__ == '__main__':
    TopUsers.run()
