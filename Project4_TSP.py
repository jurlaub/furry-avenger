from math import sqrt
import sys
import getopt
import os.path
import random


class Cluster():
    # nearestNeighbers
    # Cluster Max-Length
    #  n
    # 
    #list of tuples, distances 
    # x = 0
    # y = 0
    # length = 0

    def __init__(self, n, x, y):
        self.n = int(n)
        self.x = int(x)
        self.y = int(y)
        self.nearestNeighbers = []
        self.cityList = []
        self.length = 0
    
        #self.cityList.append([node, distance])

    #def addCityList(self, entry, m, x1, y1):
    def addCityList(self, val):
        self.cityList.append(val)
      

    def getCoord(self):
        return self.x, self.y

    def getCityList(self):
        return self.cityList

    def getLastCityList(self):
        return int(self.cityList[-1][0][1]), int(self.cityList[-1][0][2]), int(self.cityList[-1][1])


#calculates the nearest 3 neighbors
def cluster_neighbor():
    pass

def cluster_citysort(cluster):

    a = cluster.getCityList()
    a.sort(key = lambda c: c[0][1] )
    

def cluster_sort(cluster):
    a = cluster.

def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return int(sqrt(dx*dx + dy*dy))   


def make_Cluster(entry, ClusterList, n):
    # if not ClusterList:
    #     #create new cluster
    #     # find n from x or y      
    #n = max(entry[1], entry[2])
    s = Cluster(n, entry[1], entry[2])
    s.addCityList([entry, 0])

    ClusterList.append(s)
    #     #v = ClusterList[0]
    #     #print v.cityList[0]
    #     #v.cityList[0] = ["hello world", 8]
    #print "this is a new cluster"
    #print ClusterList



def add_Cluster_Entry(entry, ClusterList):
    x1, y1 = int(entry[1]), int(entry[2])
    z = 0

    for item in ClusterList:
        z+=1
        # print str(z) + " we are at item"
        x2, y2 = item.getCoord() #item.x, item.y
        m = distance(x1, y1, x2, y2)

        if(m <= item.n):
            # print item
            # print str(m) + " this is the distance"
            # print str(item.n) + " this is n_max"
            #add to the existing cluster which is item
            #x2, y2, m2 = item.getLastCityList()
            #m = distance(x1, y1, x2, y2)
            #item.cityList.append([entry, m])
            #item.addCityList(entry, m, x1, y1)
            item.addCityList([entry, m])
            return True
        # else:
        #     print "sorry not included " + str(entry) + " distance: " + str(m)

    return False




def input_coords(filename, ClusterList):
    '''This function reads city coordinates from a text file'''
    
    fi = open(filename)   
    with fi as f:
        #add in something to skip first line, also first character of each line (the city number)
        first = f.readline()
        n,x,y = first.strip().split(' ')
        n_max = 2500 #(max(int(x),int(y)))
        entry = (n, x, y)
        make_Cluster(entry, ClusterList, n_max)

        for line in f.readlines():
            n,x,y = line.strip().split(' ')
            #coordinates.append((float(x), float(y)))
            #print str(n) + "   " + str(x) + "   " + str(y)
            entry = (n, x, y)
            if not add_Cluster_Entry(entry, ClusterList):
                #print "Make new Cluster"
                make_Cluster(entry, ClusterList, n_max)

            
            #call make_add_Cluster()
            # make_add_Cluster(entry, ClusterList)

            #ClusterList.append(entry)
    fi.close()
    return ClusterList


def myTour(matrix, tour):
    total = 0
    cities = len(tour)
    for i in range(cities):
        j=(i+1)%cities #shifts index up by 1
        city_i = tour[i]
        city_j = tour[j]
        total += matrix[city_i, city_j]
    return total
            
# place for cluster optimization
def command(filename):

    ClusterList = []

    #call input_coords ()
    input_coords(filename, ClusterList)
    m = 0
    for item in ClusterList:
        m+=1
        print str(m) + " " + str(item.x) + " " + str(item.y)
        print item.getCityList()
        cluster_citysort(item)
        print item.getCityList()
        # print " next round +++++++++++++++"
        # for entry in item.getCityList():
        #     print entry
        #print item.getLastCityList() 
    #print ClusterList






#_______________________________ main________________


def main():
    #parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    #process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print "Project4_TSP.py <filename>"
            sys.exit(0)
    # process args
    for arg in args:
        process(arg) # process() somewhere


def process(arg):
    try:
        if os.path.exists(arg):
            command(arg)

    except IOError as e:
        print("({})".format(e))

    if arg == "dd":
        print "still need to implement"

    
   
if __name__ == "__main__":
    main()                                   
        
                                   
                
        
    

    

        

        

        
        

