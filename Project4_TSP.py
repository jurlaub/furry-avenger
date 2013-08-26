import math
import sys
import getopt
import os.path


class Cluster():
    # nearestNeighbers
    # Cluster Max-Length
    #  n
    # 
    #list of tuples, distances 
    x = 0
    y = 0
    nearNeighbor = []
    cityList = []
    length = 0

    def __init__(self, n, node, distance):
        self.n = n
        self.x = node[1]
        self.y = node[2]
        self.cityList.append([node, distance])

    def addCityList(val):
        self.cityList.append(val)





# pass in distance (n from parentnode), 
# list of clusters
# 
def make_add_Cluster(entry, ClusterList):

    # look at list of clusters
    # current node: find distance from each cluster parent node, 
    # if within n, add 
    # if not make new cluster

    if not ClusterList:
        #create new cluster
        # find n from x or y      
        n = max(entry[1], entry[2])
        print n
        ClusterList.append(Cluster(n, entry, 0))
        #v = ClusterList[0]
        #print v.cityList[0]
        #v.cityList[0] = ["hello world", 8]
        return

    x1, y1 = entry[1], entry[2]

    for item in ClusterList:
        # x2, y2 = item.x, item.y
        # print x2
        # print y2
        print item.cityList[0]


    ClusterList.append(entry)



def distance_matrix(coordinates):
    '''This function generates a matrix of distances from the two city coordinates
      These are euclidean distances. Distances are rounded to the nearest
      integer. Returns the distance between the two cities'''
    matrix = {}
    for i, (x1, y1) in enumerate(coordinates):          #first city's coordinates 
        for j, (x2, y2) in enumerate(coordinates):      #second city's coordinates
            dx = x1-x2
            dy = y1-y2
            distance = int(sqrt(dx*dx + dy*dy))         #calculate distance using pythagorean theorem
            matrix[i, j] = distance 
    return distance


def input_coords(filename, ClusterList):
    '''This function reads city coordinates from a text file'''
    
    fi = open(filename)   
    with fi as f:
        #add in something to skip first line, also first character of each line (the city number)
    
        for line in f.readlines():
            n,x,y = line.strip().split(' ')
            #coordinates.append((float(x), float(y)))
            #print str(n) + "   " + str(x) + "   " + str(y)
            entry = (n, x, y)

            #call make_add_Cluster()
            make_add_Cluster(entry, ClusterList)

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
    ClusterList = input_coords(filename, ClusterList)

    #print ClusterList


 

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
        
                                   
                
        
    

    

        

        

        
        

