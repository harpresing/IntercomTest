"""A class that takes a list from command line and returns a flat list.

Written by: Harpreet Singh
"""


class FlattenArray:
    """Class implementing flatten of lists."""
    
    def flatten(self, arr):
        """flatten method flattens the list recursively."""
        flatList = []
        for a in arr:
            if isinstance(a, list):
                flatList += (self.flatten(a))
            else:
                flatList.append(a)
        return flatList 

if __name__ == '__main__':
	ob = FlattenArray()
	arr = [1, 3, 434, [[[234]]], 2, 4, [[2, 9]]]  # This is the list that gets flattened
	ans = ob.flatten(arr)
	print ans 


















	
