class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        z=zip(position,speed)
        sorted_z=sorted(z,reverse=True)
        for p,s in sorted_z:
            time=(target-p)/s
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)


