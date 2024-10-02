# Search

## Search Problems

Search problem examples:
- Maze
- Directions
- Tic Tac Toe
- Puzzles

## Terminology

Agent
: An entity that perceives its environment and acts upon that environment.

State
: A configuration of an agent in its environment

- Initial State
: The state from which the search algorithm starts.

Actions
: Choices that can be made in a state.  

- Actions can also be defined as a function
- Upon receiving state _s_ as input, `Action(s)` returns as output the set of actions that can be executed in state _s_
- Actions can take us from one state to another

Transition Model
: A description of what state results from performing any applicable action in any state

- Can also be described as a function
- Upon receiving state _s_ and action _a_ as input, `Results(s, a)` returns the state _S_ resulting from performing action _a_ in state _s_
- _Result_ function moves from one state to another

State Space
: The set of all states reachable (numerations) from the initial state by any sequence of actions. 

- Configurations of possibilities can be represented mathematically using factorials like _16!_ as representation of permutations of possibilities, combinations of possibilities, etc.
- So saying a puzzle state space of 15 filled boxes in a 16 total grid, the state space consists of all the 16!/2 configurations on the board that can be reached from any initial state
The state space can be visualised as a directed graph with states, represented as nodes, and actions, represented as arrows between the notes.

Goal Test
: The condition that determins whether a given state is the goal state.  

- Whether current location of the agent is at the destination
- Example: Driving instructions, reaching your destination 

Path Cost
: A numerical cost associated with a given path

- Minimise the path cost, finding fastest way possible to goal state
- Example: Driving instructions, fuel cost, directness, etc

Node
: a data structure that keeps track of
- a state
- a parent (node which generated this node)
- an action (applied to parent to get node)
- a path cost (from initial state to node)

Frontier
: mechanism that managed the nodes
- Starts by containing an initial state and an empty set of explored items, then repeats actions until a solution is reached

Solution
: a sequence of actions that leads from the initial state to the goal state

Optimal Solution
: a solution that has the lowest path cost among all the solutions

## Search Problem

1. Initial state
2. Actions
3. Transition model
4. Goal Test
5. Path cost function

## Search Approach

- Starting with a frontier that contains the initial state

- Repeat:

1. If the frontier is empty
    - There is no solution to the problem - stop.

2. Remove a node from the frontier
    - This is the node that will be considered

3. If the node contains the goal state
    - Return the solution - stop.

    Else 
    - Expand the node
        - find all the new nodes that could be reached from this node
        - Add the resulting nodes to the frontier

    - Add the current node to the explored set







