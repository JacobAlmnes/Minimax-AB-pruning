# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util
from math import inf

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    # self.depth finner dybden man skal søke


    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

    # def minimax(self, gameState, depth, agentIndex):
    #     if depth == 0 or gameState.isWin() or gameState.isLose():
    #         return self.evaluationFunction(gameState)
    #     if agentIndex == 0:
    #         return self.maxValue(gameState, depth)
    #     else:
    #         return self.minValue(gameState, depth, agentIndex)
        
    # def maxValue(self, gameState, depth):
    #     v = -inf
    #     for action in gameState.getLegalActions(0):
    #         v = max(v, self.minimax(gameState.generateSuccessor(0, action), depth, 1))
    #     return v

    # def minValue(self, gameState, depth, agentIndex):
    #     v = inf
    #     for action in gameState.getLegalActions(agentIndex):
    #         if agentIndex == gameState.getNumAgents() - 1:
    #             v = min(v, self.minimax(gameState.generateSuccessor(agentIndex, action), depth - 1, 0))
    #         else:
    #             v = min(v, self.minimax(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1))
    #     return v

        return self.getMinimaxValue(gameState, self.index, self.depth)
        # util.raiseNotDefined()

    def getMinimaxValue(self, gameState, agentIndex, depth):
        # TODO: Do something if win or lose
        if gameState.isWin() or gameState.isLose() or self.depth == 0 or gameState.getLegalActions(agentIndex) == []:
            return self.evaluationFunction(gameState)

        if agentIndex == 0:
            value, move = self.getMaxValue(gameState, agentIndex, depth=0)
        else:
            value, move = self.getMinValue(gameState, agentIndex, depth=0)
        # value, move = self.getMaxValue(gameState, agentIndex, depth=0)
        return move

    def checkEndState(self, gameState, depth, agentIndex):
        return gameState.isWin() or gameState.isLose() or depth == self.depth or gameState.getLegalActions(agentIndex) == []
            
    def getMaxValue(self, gameState, agentIndex, depth):
        # if gameState.isWin():
        #     return self.evaluationFunction(gameState), None

        # if gameState.isLose():
        #     return self.evaluationFunction(gameState), None
        if self.checkEndState(gameState, depth, agentIndex):
            return self.evaluationFunction(gameState), None

        v = None
        move = None
        for action in gameState.getLegalActions(agentIndex):
            v2, a2 = self.getMinValue(gameState.generateSuccessor(agentIndex, action), agentIndex, depth)
            if v == None or v2 == None or v2 > v:
                v = v2
                move = action
        return v, move
            

    def getMinValue(self, gameState, agentIndex, depth):
        # if gameState.isWin():
        #     return self.evaluationFunction(gameState), None

        # if gameState.isLose():
        #     return self.evaluationFunction(gameState), None

        if self.checkEndState(gameState, depth, agentIndex):
            return self.evaluationFunction(gameState), None

        v = None
        move = None
        for action in gameState.getLegalActions(agentIndex):
            v2, a2 = self.getMaxValue(gameState.generateSuccessor(agentIndex, action), agentIndex, depth+1)
            if  v == None or v2 == None or v2 < v:
                v = v2
                move = action
        return v, move

    def getMinValue(self, gameState, agentIndex, depth):
        if gameState.isWin():
            return self.evaluationFunction(gameState), None

        if gameState.isLose():
            return self.evaluationFunction(gameState), None

        v = None
        move = None
        newAgentIndex = (agentIndex+1) % gameState.getNumAgents()
        for action in gameState.getLegalActions(agentIndex):
            if newAgentIndex == 0:
                v2, a2 = self.getMaxValue(gameState.generateSuccessor(agentIndex, action), newAgentIndex, depth)
            else:
                v2, a2 = self.getMinValue(gameState.generateSuccessor(agentIndex, action), newAgentIndex, depth)
            if  v == None or v2 > v:
                v = v2
                move = action
        return v, move

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self.alphaBeta(gameState, self.index, self.depth, -inf, inf)
        util.raiseNotDefined()

    def alphaBeta(self, gameState, depth, agentIndex, alpha, beta):
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        if agentIndex == 0:
            return self.maxValue(gameState, depth, alpha, beta)
        else:
            return self.minValue(gameState, depth, agentIndex, alpha, beta)

    def maxValue(self, gameState, depth, alpha, beta):
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        v = -inf
        for action in gameState.getLegalActions(0):
            v = max(v, self.minValue(gameState.generateSuccessor(0, action), depth, 1, alpha, beta))
            if v > beta:
                return v
            alpha = max(alpha, v)
        return v
    
    def minValue(self, gameState, depth, agentIndex, alpha, beta):
        if depth == 0 or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        v = inf
        for action in gameState.getLegalActions(agentIndex):
            if agentIndex == gameState.getNumAgents() - 1:
                v = min(v, self.maxValue(gameState.generateSuccessor(agentIndex, action), depth - 1, alpha, beta))
            else:
                v = min(v, self.minValue(gameState.generateSuccessor(agentIndex, action), depth, agentIndex + 1, alpha, beta))
            if v < alpha:
                return v
            beta = min(beta, v)
        return v
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
