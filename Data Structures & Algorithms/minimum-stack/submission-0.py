class MinStack:
    def __init__(self):
        self.stack = []
        self.orderToIndex = {}
        self.minOrder = 1

    def push(self, val: int) -> None:
        # always store the min at index 0
        if self.stack and val < self.stack[0]:
            # swap the old min with the new min in the stack
            self.stack.append(self.stack[0])
            self.stack[0] = val

            # the new min will be at index 0 with the highest order
            # the old min will be at index len(stack) - 1 with its old order
            self.orderToIndex[len(self.stack)] = 0
            self.orderToIndex[self.minOrder] = len(self.stack) - 1
            self.minOrder = len(self.stack)
        else:
            # if no new min detected, append as normal
            # update the index to order appropriately
            self.stack.append(val)
            self.orderToIndex[len(self.stack)] = len(self.stack) - 1
            
        print("push")
        print("stack:", self.stack)
        print("orderToIndex", self.orderToIndex)
        print("minOrder:", self.minOrder)
        print()
        return

    def pop(self) -> None:
        # we must pop the index at the highest order
        self.stack.pop(self.orderToIndex[len(self.stack)])
        
        return

    def top(self) -> int:
        return self.stack[self.orderToIndex[len(self.stack)]]

    def getMin(self) -> int:
        return self.stack[0]

