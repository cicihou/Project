class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2)
        b = int(b,2)
        return bin(a+b)[2:]

a = "11"
b = "1"
s = Solution()
print(s.addBinary(a, b))
print(s.addBinary("1010", "1011"))