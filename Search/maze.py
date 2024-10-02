import sys

class Node() :

    def __init__(self, state, parent, action) :

        self.state = state
        self.parent = parent
        self.action = action

# Creates frontier using Stack data type - last-in, first-out

class StackFrontier() :

    def __init__(self) :

        self.frontier = []

    # Adds node to frontier

    def add(self, node) :

        self.frontier.append(node)

    # Checks if frontier contains particular state

    def contains_state(self, state) :

        return any(node.state == state for node in self.frontier)

    # Checks if frontier is empty

    def empty(self) :

        return len(self.frontier) == 0
    
    # Function to remove a node from frontier

    def remove(self) :

    # Terminates the search if the frontier is empty, as this is a no solution

        if self.empty() :

            raise Exception("Empty frontier - no solution")

        else :

            # Save the last item in the list *(which is the newest node added)

            node = self.frontier[-1]

            # Save all the items on the list besides the last node (removes last node)

            self.frontier = self.frontier[:-1]
            return node
        
# Creates new class for Queue data type, inheriting same class properties created above

class QueueFrontier(StackFrontier) :

    def remove(self) :

        # Terminate the search if the frontier is empty, so no solution

        if self.empty() :

            raise Exception("Empty frontier - no solution")

        else :

            # Save the oldest item on the list (which was first one to be added)

            node = self.frontier[0]

            # Save all the items on the list besides the first one (removes first node)

            self.frontier = self.frontier[1:]
            return node

# Reads in text file which can represent a maze, using # to represent a wall

class Maze() :

    def __init__(self, filename) :

        # Reads file and sets height and width of the maze

        with open(filename) as f :

            contents = f.read()

            # Validate start and end goal

            if contents.count("A") != 1 :

                raise Exception("Maze must have exactly one start point")
            
            if contents.count("B") != 1 :

                raise Exception("Maze must have exactly one goal point")
            
            # Determines height and width of maze

            contents = contents.splitlines()

            self.height = len(contents)
            self.width = max(len(line) for line in contents)

            # Keeps track of walls

            self.walls = []

            for i in range(self.height) :

                row = []

                for j in range(self.width) :

                    try :

                        if contents[i][j] == "A" :

                            self.start = (i, j)
                            row.append(False)

                        elif contents[i][j] == "B" :

                            self.goal = (i, j)
                            row.append(False)

                        elif contents[i][j] == " " :

                            row.append(False)

                        else :

                            row.append(True)

                    except IndexError :
                        
                        row.append(False)
                
                self.walls.append(row)
            
            self.solution = None

        def print(self) :

            solution =  self.solution[1] if self.solution is not None else None
            print()

            for i, row in enumerate(self.walls) :

                for j, col in enumerate(row) :

                    if col :

                        print(" ", end = "")  
                    
                    elif (i, j) == self.start :

                        print("A", end = "")

                    elif (i, j) == self.goal :

                        print("B", end = "")

                    elif solution is not None and (i, j) in solution :

                        print("*", end = "")

                    else :

                        print(" ", end = "")

                print()

            print()

        def neighbours(self, state) :

            row, col = state

            # All possible actions

            candidates = [

                ("up", (row - 1, col)),
                ("down", (row + 1, col)),
                ("left", (row, col - 1)),
                ("right", (row, col + 1))
            ]

            # Ensure actions are valid

            result = []

            for action, (r, c) in candidates :

                try :

                    if not self.walls[r][c] :

                        result.append((action, (r, c)))

                except IndexError :

                    continue
            return result
    
    def solve(self) :
        
        # Finds solution to maze if one exists

        # Keeps track of number of states explored

        self.num_explored = 0

        # Initialise frontier to just the starting positiion

        start = Node(state = self.start, parent = None, action = None)
        frontier = StackFrontier()
        frontier.add(start)

        # Initialise an empty explored set

        self.explored = set()

        # Keeps looping until solution is found

        while True :

            # if nothing left in frontier, then no path, no solution

            if frontier.empty() :

                raise Exception("No solution")
            
            # Choose a node from the frontier

            node = frontier.remove()
            self.num_explored += 1

            # Checks if node is the goal, aka solution

            if node.state == self.goal :

                actions = []
                cells = []

                # Follow parent nodes to find solution

                while node.parent is not None :
                    
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent

                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells) 
                return
            
            # Mark node as explored

            self.explored.add(node.state)

            # Add neighbours to frontier

            for action, state in self.neighbours(node.state) :

                if not frontier.contains_state(state) and state not in self.explored :

                    child = Node(state = state, parent = node, action = action)
                    frontier.add(child)
                    