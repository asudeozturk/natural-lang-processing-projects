class State:
    def __init__(self, state, zone, parkNum,  pathCost, parksVisited):
        self.State = state
        self.Zone = zone
        self.ParkNum = parkNum              #number of parks in the state
        self.PathCost = pathCost            #path cost from initial state to current state
        self.ParksVisited = parksVisited    #number of parks visite from initial to current state

    def getState(self):
        return self.State

    def getZone(self):
        return self.Zone

    def getParkNum(self):
        return self.ParkNum

    def getPathCost(self):
        return self.PathCost

    def getParksVisited(self):
        return self.ParksVisited

    def updateParksVisited(self, newParkNum):
        self.ParksVisited = newParkNum

    def __cmp__(self,other):
        return cmp(self.State,other.State)
