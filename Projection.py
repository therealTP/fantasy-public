class Projection:
    'Common base class for all projection entries'
    projCount = 0

    def __init__(self, pts, reb, ast, stl, blk, tpt, tov, mins):
        self.pts = pts
        self.reb = reb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.tpt = tpt
        self.tov = tov
        self.mins = mins
        Projection.projCount += 1

    def addEntryToDict(self, playerId, projDict):
        projDict[playerId] = self.__dict__

    def displayProjCount(self):
        print (Projection.projCount)
