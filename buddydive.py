class AdvancedDiver:
    def __init__(self, target):
        self.target = target
        self.m = len(target)
        self.state_table = self._build_transition_table()

    def _build_transition_table(self):
        """
        Creates a map of all possible 'current depths'.
        This is the 'Advanced' logic: pre-calculating the dive path.
        """
        table = []
        for state in range(self.m + 1):
            row = {}
            # Check every possible character (simplified to unique chars in target)
            for char in set(self.target):
                # Find the longest prefix of target that is also a suffix of (state + char)
                next_state = state + 1
                while next_state > 0:
                    if self.target[:next_state] == (self.target[:state] + char)[-(next_state):]:
                        break
                    next_state -= 1
                row[char] = next_state
            table.append(row)
        return table

    def search(self, text):
        print(f"--- Initiating Advanced Dive for '{self.target}' ---")
        current_depth = 0 # Starting at the surface (State 0)
        
        for i, char in enumerate(text):
            # Move to the next depth based on the current character
            current_depth = self.state_table[current_depth].get(char, 0)
            
            # If current_depth matches target length, we've reached the bottom!
            if current_depth == self.m:
                print(f"Target found! Surface reached at index {i - self.m + 1}")
                return "up"
        
        print("Dived to the bottom... nothing found.")
        return "down"

# Execute the Dive
diver = AdvancedDiver("ocean")
result = diver.search("the deep blue ocean is vast")
print(f"Final Status: {result}")
