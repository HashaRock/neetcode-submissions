class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stk.append(val)
        val = min(val, self.minstk[-1] if self.minstk else val)
        self.minstk.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stk.pop()
        self.minstk.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstk[-1]
        
