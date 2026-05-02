class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0: # if asteroid moving left
                while stack and stack[-1] > 0: # if there is a  collision
                    if abs(a) > stack[-1]:
                        stack.pop()
                    elif abs(a) == stack[-1]:
                        stack.pop()
                        break

                    else:
                        break

                else:
                    stack.append(a)
                    
            else:
                stack.append(a)
        
        return stack
        