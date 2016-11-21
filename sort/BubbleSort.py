import unittest

def bubbleSort(targetList):
    for i in range(len(targetList)-1):
        for j in range(len(targetList)-1):
            if targetList[j] > targetList[j+1]:
                targetList[j], targetList[j+1] = targetList[j+1], targetList[j]
    return targetList

class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], bubbleSort([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubbleSort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubbleSort([6, 5, 4, 3, 2, 1]))