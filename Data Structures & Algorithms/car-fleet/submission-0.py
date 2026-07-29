class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = list(zip(position, speed))
        cars = sorted(cars, reverse=True)

        for index, car in enumerate(cars):
            arrival = (target - car[0]) / car[1]
            
            if stack and stack[-1] >= arrival:
                continue

            stack.append(arrival)
        
        return len(stack)

        # target: 10
        # position: [1, 4]
        # speed: [3, 2]

        # target:   0 1 2 3 4 5 6 7 8 9 10
        # car 1:    _ 0 _ _ 1 _ _ 2 _ _ 3 --> 3 iterations
        # car 2:    _ _ _ _ 0 _ 1 _ 2 _ 3 --> 3 iterations
        # 
        # target:   0 1 2 3 4 5 6 7 8 9 10
        # car1:     _ _ _ _ 0 _ 1 _ 2 _ 3   -->  iterations
        # car2:     _ 0 _ 1 _ 2 _ 3 _ 4 _ 5 --> 5 iterations
        # car3:     0 1 2 3 4 5 6 7 8 9 10  --> 10 iterations
        # car4:     _ _ _ _ _ _ _ 0 1 2 3 --> 3 iterations

        # ALGORITHM
        # sort by position (descending)
        # iteration = (target - position) / step
        # return len(set) iterations
