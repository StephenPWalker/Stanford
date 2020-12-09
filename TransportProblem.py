import sys
sys.setrecursionlimit(10000)
############################################################################
### (search)
############################################################################
class TransportationProblem(object):
    def __init__(self, N, weights):
        self.N = N
        self.weights = weights
    def startState(self):
        return 1
    def isEnd(self, state):
        return state == self.N
    def succAndCost(self, state):
        # Return list of (actions, newstates, costs) tuples
        result = []
        if state+1 <=self.N:
            result.append(('Walk',state+1,self.weights['Walk']))
        if state*2<=self.N:
            result.append(('Tram',state*2,self.weights['Tram']))
        return result

def printSolution(solution):
    totalCost, history = solution
    print('totalCost: {}'.format(totalCost))
    for item in history:
        print(item)
############################################################################
###Algorithms
############################################################################
def backtrackingSearch(problem):
    # Best solution so far (dictionary because python scoping technicality)
    best = {
        'cost': float('+inf'),
        'history': None
        }
    def recurse(state,history,totalCost):
        # At state, having undergone history, accumulated
        # TotalCost.
        # Explore the rest of the subtree under state.
        if problem.isEnd(state):
            #Update best solution so far
            if totalCost<best['cost']:
                best['cost'] = totalCost
                best['history'] = history
            return
        #Return on children
        for action, newState, cost in problem.succAndCost(state):
            recurse(newState, history+[(action, newState, cost)], totalCost+cost)
    recurse(problem.startState(),history=[],totalCost=0)
    return(best['cost'],best['history'])

def dynamicProgramming(problem):
    cache = {} #state -> futureCost(state)
    def futureCost(state):
        # Base case
        if problem.isEnd(state):
            return 0
        if state in cache:
            return cache[state][0]
        result = min((cost+futureCost(newState),action,newState,cost) \
            for action, newState, cost in problem.succAndCost(state))
        cache[state] = result
        return result[0]
    state = problem.startState()
    totalCost = futureCost(state)
    #recovery history
    history = []
    while not problem.isEnd(state):
        _,action,newState,cost = cache[state]
        history.append((action,newState,cost))
        state = newState
        
    return(futureCost(problem.startState()), history)

def predict(N, weights):
    problem = TransportationProblem(N,weights)
    totalCost, history = dynamicProgramming(problem)
    return [action for action, newState, cost in history]

def generateExamples():
    trueWeights = {'Walk':1,'Tram':5}
    return [(N,predict(N,trueWeights)) for N in range(1,30)]

def structuredPerceptron(examples):
    weights = {'Walk': 0, 'Tram':0}
    for t in range(100):
        numMistakes = 0
        for N, trueActions in examples:
            #Make prediction
            predActions = predict(N,weights)
            if predActions != trueActions:
                numMistakes += 1
            #Update weights
            for action in trueActions:
                weights[action] -= 1
            for action in predActions:
                weights[action] += 1
        print('Iteration {}, numMistakes = {}, weights = {}'.format(t,numMistakes,weights))
        if numMistakes == 0:
            break
                

examples = generateExamples()
print('Training dataset:')
for example in examples:
    print(' ', example )
structuredPerceptron(examples)
