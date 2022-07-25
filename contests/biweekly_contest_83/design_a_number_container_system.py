"""
Design a number container system that can do the following:
    - Insert or Replace a number at the given index in the system.
    - Return the smallest index for the given number in the system.

Implement the NumberContainers class:
    - NumberContainers() Initializes the number container system.
    - void change(int index, int number) Fills the container at index with the number.
      If there is already a number at that index, replace it.
    - int find(int number) Returns the smallest index for the given number,
      or -1 if there is no index that is filled by number in the system.
"""

"""
Example 1
    Input
    ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
    [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]
    Output
    [null, -1, null, null, null, null, 1, null, 2]

    Explanation
    NumberContainers nc = new NumberContainers();
    nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
    nc.change(2, 10); // Your container at index 2 will be filled with number 10.
    nc.change(1, 10); // Your container at index 1 will be filled with number 10.
    nc.change(3, 10); // Your container at index 3 will be filled with number 10.
    nc.change(5, 10); // Your container at index 5 will be filled with number 10.
    nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5.
		 // Since the smallest index that is filled with 10 is 1, we return 1.
    nc.change(1, 20); // Your container at index 1 will be filled with number 20.
		      // Note that index 1 was filled with 10 and then replaced with 20. 
    nc.find(10); // Number 10 is at the indices 2, 3, and 5.
		 // The smallest index that is filled with 10 is 2. Therefore, we return 2.
"""


class NumberContainers:

    def __init__(self):
        """
        There can be zero or multiple indices corresponding to a number
        The correspondance can be changed by the change method:
            indices are added or removed for some numbers
        """
        self.i2n = {}
        self.n2i = {}

    def change(self, index: int, number: int) -> None:
        """
        Update i2n: O(1)
        Update n2i: O(n) by using list to maintain sorted values
        """
        if index not in self.i2n:
            old_number = None
            self.i2n[index] = number
        else:
            old_number = self.i2n[index]
            self.i2n[index] = number
            if old_number == number:
                return

        if number not in self.n2i:
            self.n2i[number] = [index]
        else:
            indices = self.n2i[number]
            i = 0
            while i < len(indices) and indices[i] <= index:
                i += 1
            indices.insert(i, index)
            self.n2i[number] = indices

        if old_number is not None:
            indices = self.n2i[old_number]
            indices.remove(index)
            self.n2i[old_number] = indices

    def find(self, number: int) -> int:
        """
        O(1)
        """
        if number in self.n2i and self.n2i[number]:
            return self.n2i[number][0]
        return -1

        
if __name__ == '__main__':
    nc = NumberContainers()
    print(nc.find(10))
    nc.change(2, 10)
    nc.change(1, 10)
    nc.change(3, 10)
    nc.change(5, 10)
    print(nc.find(10))
    nc.change(1, 20)
    print(nc.find(10))




# 
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
