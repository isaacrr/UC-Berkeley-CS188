# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def DFS(states, problem, closeList):
	for s in states[::-1]:
		if s[0] in closeList or s is None:
			continue
		if problem.isGoalState(s[0]):
			return [s[1]]
		closeList.add(s[0])
		a = DFS(problem.getSuccessors(s[0]), problem, closeList)
		if a:
			return [s[1]] + a

def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:

	print "Start:", problem.getStartState()
	print "Is the start a goal?", problem.isGoalState(problem.getStartState())
	print "Start's successors:", problem.getSuccessors(problem.getStartState())

	"""
	'''
	Quan fiques, es posa a sobre.
	Quan consultes, treu el primer.

	Exemple: A|B|C
	Mentre stack No Buit:
	Pop A
	Analitzar A -> en cas de ja haber-lo vist Seguent iteracio
	Si A Es Final:
	BackTrack -> Com es pot lincar en el pare?
	Altrament:
	Push de tots els fill d'A -> D|E|F B|C
	Posar A Vist
	'''

	'''
	stack = utils.Stack()
	start = (problem.getStartState(), None, None)	# ((x, y), direccio, cost)
	stack.push(start)

	while not stack.isEmpy():


	util.raiseNotDefined()
	'''

	"*** YOUR CODE HERE ***"

	closeList = set()				# Un Set normal
	start = problem.getStartState()
	closeList.add(start)

	return DFS(problem.getSuccessors(start), problem, closeList)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    '''
	Quan fiques, es posa a sota.
	Quan consultes, treu el primer.

	Exemple: A|B|C
	Mentre queu No Buit:
	Pop A
	Analitzar A -> en cas de ja haber-lo vist Seguent iteracio
	Si A Es Final:
	BackTrack -> Com es pot lincar en el pare?
	Altrament:
	Push de tots els fill d'A -> B|C D|E|F
	Posar A Vist
	'''
    start = (problem.getStartState(), None, None)

    closeList = set()
    output =  []
    queue = util.Queue()

    queue.push(start)

    while not queue.isEmpty():
        state = queue.pop()
        if state in closeList or state[0] is None:
            continue
        if problem.isGoalState(state[0]):
            while state[1]:
                output.append(state[1])
                for parent in closeList:
                    if parent[0][0] == state[2][0] and parent[0][1] == state[2][1]:
                        state = parent
                        break
            break
        for child in problem.getSuccessors(state[0]):
            queue.push((child[0], child[1], state[0]))
        closeList.add(state)

    return output[::-1]

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    '''
    start = problem.getStartState()
	closeList.add(start)

	queu = utils.Queue

	for s in queu.pop:
		if s[0] in closeList or s is None:
			continue
		if p.isGoalState(s[0]):
			output.append(s[1])
			return
		closeList.add(s[0])
		DFS(p.getSuccessors(s[0]), p)
		if output:
			output.append(s[1])
			return
    '''
    return output[::-1]

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
