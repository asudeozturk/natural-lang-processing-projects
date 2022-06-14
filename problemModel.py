import pandas
from collections import deque

class ProblemModel:
    def __init__(self, initial, minParkNum, drivingData, zonesData, parksData):
        self.Initial = initial
        self.MinParkNum = minParkNum
        self.ParksVisited = 0

        self.LastZone = 0
        self.Stack = deque();

        self.DrivingDistances = self.loadDrivingData(drivingData)
        self.Zones = self.loadZonesData(zonesData)
        self.Parks = self.loadParksData(parksData)

        self.InitZone = self.getZoneNum(self.Initial)

    def getInitial(self):
        return self.Initial
    def getMinParkNum(self):
        return self.MinParkNum
    def getParksVisited(self):
        return self.ParksVisited
    def getInitZone(self):
        return self.InitZone
    def getLastZone(self):
        return self.LastZone
    def getStack(self):
        return self.Stack

    def getDrivingDistance(self, fromState, toState):        #find the cost of driving from one state to another
        return self.DrivingDistances[(fromState, toState)]
    def getZoneNum(self, state):                             #find the zone number of a given state
        return self.Zones[state]
    def getParkNum(self, state):                             #find the number of parks in a given state
        return self.Parks[state]



    def loadDrivingData(self, drivingData):                 #drivingData dictionary: (fromState, toState) -> cost
        drivingDistances = dict()
        for fromState, row in drivingData.iterrows():
            for toState, cost in row.items():
                if cost != -1:
                    drivingDistances[(fromState, toState)] = cost
        return drivingDistances

    def loadZonesData(self, zonesData):                     #zonesData dictionary: state -> zone number
        zones = dict()
        maxZone = 0
        for zone, row in zonesData.iterrows():
            for state, zoneNum in row.items():
                zones[state] = zoneNum
                if zoneNum > maxZone :                      #find the last zone in graph (avoids hardcoding zone 12)
                    maxZone = zoneNum
        self.LastZone = maxZone
        return zones

    def loadParksData(self, parksData):                     #parksData dictionary: state -> number of parks
        parks = dict()
        for park, row in parksData.iterrows():
            for state, parkNum in row.items():
                parks[state] = parkNum
        return parks

    def validState(self, state):                             #check if a state is in the graph
        for (fromState, toState) in self.DrivingDistances:
            if(state == fromState):
                return True
        return False

    def getStatesInZone(self, zone):                        #return all states in a given zone number
        states = []
        for state in self.Zones:
            if( self.getZoneNum(state) == zone):
                states.append(state)
        return states

    def isNeighbor(self, currentState, toState):             #check if two states are neighbors (only westward direction)
        if ((currentState, toState) in self.DrivingDistances):
            return True
        return False

    def addParksVisited(self, newParks):                    #update the number of parks visited
        self.ParksVisited = self.ParksVisited + newParks

    def subtractParksVisited(self, newParks):               #update the number of parks visited
        self.ParksVisited = self.ParksVisited - newParks
