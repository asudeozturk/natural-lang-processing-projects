import pandas
import sys
from problemModel import ProblemModel as Problem
from state import State


def main():
    if(len(sys.argv) != 3):
        sys.exit("ERROR: Not enough or too many input arguments.")

    initial = sys.argv[1]
    minParkNum = int(sys.argv[2])
    drivingData = pandas.read_csv('driving2.csv',index_col=0)           #load driving distances data
    zonesData = pandas.read_csv('zones.csv',index_col=0)                #load zones data
    parksData = pandas.read_csv('parks.csv', index_col=0)               #load parks data

    solution = "FAILURE: NO PATH FOUND"
    pCost = pCount = parkNum = 0

    problem = Problem(initial, minParkNum, drivingData, zonesData,parksData)    #constraint satisfaction problem

    if not problem.validState(initial):                                         #the state is not in graph
        printResults(initial, minParkNum, solution, pCount, pCost, parkNum)
        sys.exit("ERROR: Invalid state.")

    results = backtrackingSearch(problem)                                       #execute the Backtracking Search
    if(results == False or results == None):
        printResults(initial, minParkNum, solution, pCount, pCost, parkNum)
        sys.exit("ERROR: path not found")


    pCost = results[problem.getLastZone()].getPathCost()                        #get the results if the search finds a solution
    parkNum = results[problem.getLastZone()].getParksVisited()
    solution = ""
    for zone in results:
        solution = solution + results[zone].getState() + ", "
        pCount += 1
    solution = solution[0:-2] #remove last ,
    printResults(initial, minParkNum, solution, pCount, pCost, parkNum)

def printResults(initial, minParkNum, solution, pCount, pCost, parkNum):
    print("Initial state: ", initial)
    print("Minimum number of parks: ", minParkNum)
    print()
    print("Solution path: ", solution)
    print("Number of states on a path: ", pCount)
    print("Path cost: ", pCost)
    print("Number of national parks visited: ", parkNum)


def backtrackingSearch(problem):
    state = State(problem.getInitial(),
                 problem.getInitZone(),
                 problem.getParkNum(problem.getInitial()),
                 0,
                 problem.getParkNum(problem.getInitial()))
    assignment = { state.getZone() : state}                                       #add the initial state to assignments
    problem.addParksVisited(state.getParkNum())

    return backtrack(problem, assignment, state)                                 #start backtrack search

def backtrack(problem, assignment, state):
    if checkAssignComplete(problem, assignment):
        return assignment
    zone = selectUnassignedVariable(problem, assignment, state)
    if (zone == 0):                                                             #if invalid zone, return False
      return False

    for s in orderDomainValues(problem,zone,state):
        #problem.getStack().append(state)
        if zone not in assignment:
            #assignment[zone] = problem.getStack().pop()
            assignment[zone] == s
            problem.addParksVisited(problem.getParkNum(assignment[zone].getState()))
            assignment[zone].updateParksVisited(problem.getParksVisited())

            result = backtrack(problem,assignment, s)
            if (result == False): #assignment is incomplete, or minimum number of parks is not satisfied -> backtrack
                problem.subtractParksVisited(problem.getParkNum(assignment[zone].getState()))
                assignment[zone].updateParksVisited(problem.getParksVisited())
                assignment.pop(zone, None)
            else:
                if checkAssignComplete(problem, assignment):
                    return assignment
    return False


#returns True: if all assignments from initial zone to the last zone are complete
#              AND the number of visited parks is >= minimum number of parks
def checkAssignComplete(problem, assignment):
    initialZone = problem.getInitZone()
    for zone in range(initialZone, problem.getLastZone()+1): #starts from initial state's zone number
        if zone not in assignment:
            return False
    if problem.getParksVisited() >= problem.getMinParkNum():
        return True
    return False

#returns the next zone number based on current zone
#returns 0 if current zone is the last zone on graph
def selectUnassignedVariable(problem, assignment, state):
    currentZone = state.getZone()
    if(currentZone>=problem.getLastZone()):
        return 0
    return currentZone + 1

#sets up ordered(alphabetically) list of next possible states
def orderDomainValues(problem, zone, state):
    domainStates = []
    currentState = state.getState()
    for toState in problem.getStatesInZone(zone):                                        #get all states in the zone
        if problem.isNeighbor(currentState, toState):                                    #only add states that are neighbor to current state
            cost = state.getPathCost() + problem.getDrivingDistance(currentState,toState) #calculate path cost
            totalParkNum = state.getParkNum() + problem.getParksVisited()                 #calculate total number of visited parks
            domainStates.append(State(toState,
                                    zone,
                                    problem.getParkNum(toState),
                                    cost,
                                    totalParkNum))
    domainStates.sort(key = lambda n: n.getState())
    return domainStates


if __name__=="__main__":
    main()
