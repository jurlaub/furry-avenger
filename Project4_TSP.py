from math import sqrt
import sys
import getopt
import os.path
import random
import operator


#            intdex [0][n],        index[1]    ,    index[2]
#  city_entry = [(tuple), distance to prev city, distance running total]
class Cluster():

    def __init__(self, n, x, y, ident):
        self.ident = ident
        self.n = int(n)
        self.x = int(x)
        self.y = int(y)
        self.nearestNeighbors = {}
        self.cityList = []
        self.length = 0
        self.distanceToNeighbor = 0
        self.distanceRunningTotal = 0
    

    #def addCityList(self, entry, m, x1, y1):
    def addCityList(self, val):
        self.cityList.append(val)
    
    def replaceCityList(self, val):
        self.cityList = val 

    def getClusterIdent(self):
        return self.ident

    def setNearestNeighbor(self, val):
        self.nearestNeighbors = val


    def addToNearestNeighbor(self, key, val):
        self.nearestNeighbors[key] = val

    def updateNearestNeighbor(self, val):
        self.nearestNeighbors.update(val)

    def getNearestNeighbor(self):
        return self.nearestNeighbors.viewitems()

    def existsNearestNeighbor(self, key):
        return key in self.nearestNeighbors


    def getParent(self):
        return self.cityList[0][0]

    def getParentDistanceStats(self):
        return self.distanceToNeighbor, self.distanceRunningTotal

    def getDistanceRunningTotal(self):
        return self.distanceRunningTotal

    def setParentDistanceStats(self, toNeighbor, runTotal):
        self.distanceToNeighbor = toNeighbor
        self.distanceRunningTotal = runTotal

    def getCoord(self):
        return self.x, self.y

    def getCityList(self):
        return self.cityList

    def getLastCityList(self):
        return int(self.cityList[-1][0][1]), int(self.cityList[-1][0][2]), int(self.cityList[-1][2])

    def getLastCityDistance(self):
        return int(self.cityList[-1][2])

    def getN(self):
        return self.n




# input:  filename, ordered list with length
# output: filename.tour ; 1st line "tour length: #" ; list of city ids
#
def print_to_file(filename, length, list):

    pass



def neighbor_list_bruteforce(ClusterList):
    """
    input: ClusterList - a list of cluster objects
    output: - sorted list of objects using parent nodes for distance
        - update cluster's neighbor list, 
        - if current cluster not in neighbor list - add

    """


    
    Cluster_Sorted = []

    #Set up the Cluster_Sort: obtain starter Cluster
    if ClusterList:

        tmp = ClusterList.pop()
        tmp_d, tourtotal = tmp.getParentDistanceStats()
         

        #   Closest Neighbors to Cluster:  NeighborList 
        #   - Actively enter up to N_TEST neighbors
        neighbors = {}
        list_size = len(ClusterList)        
        N_TEST = int(list_size * .15)
        max_neighbor = tourtotal 
        n_count = 0                  

        # set starter cluster values to 0
        tmp.setParentDistanceStats( 0, 0)

        Cluster_Sorted.append(tmp)


    #   Compare every item in Cluster_Sorted to the Cluster list
    #   - appends the closest to index 
    #   - advances index
    for index in Cluster_Sorted:

        # coordinates for the index in Cluster_Sorted
        x1, y1 = index.getCoord()

        # d_n is not needed, t1 is running total
        d_n, t1 = index.getParentDistanceStats()

        minDistance = tourtotal
        minIndex = 0
        counter = 0                 # used for index to extract cluster from ClusterList

        for runner in ClusterList:

            x2, y2 = runner.getCoord()
            m2 = distance(x1, y1, x2, y2) 
            if(m2 <= minDistance):
                minIndex = counter
                minDistance = m2


            #   Neighborhood list
            #       testing to see if the values remaining in ClusterList are close
            #       optimization decreases as ClusterList becomes smaller
            #       only adds n_count values to list. 
            #       then replaces max with smaller values
            if m2 < max_neighbor:

                r = runner.getParent()
                
                if n_count < N_TEST:     
                    neighbors[r] = m2           # add to dictionary
                    n_count+=1
                    
                    #print str(m2) + " >> max neighbors " + str(max_neighbor) 
                else:
                    #print "this is the neighbors list"
                    key, val = max(neighbors.iteritems(), key=lambda x:x[1])

                    if key:
                        del neighbors[key]
                    neighbors[r] = m2

                max_neighbor = max(neighbors.itervalues(), key=lambda x:x)
                

            counter+=1         



        if Cluster_Sorted:
            Cluster_Sorted[-1].updateNearestNeighbor(neighbors)
            #print ">>> " + str(neighbors)
 
            
        if ClusterList:

            tmp = ClusterList.pop(minIndex)
            tmp.setParentDistanceStats( minDistance, t1 + minDistance)
            Cluster_Sorted.append(tmp)


        
        neighbors = {}
        max_neighbor = tourtotal
        n_count = 0 




    return Cluster_Sorted


def cluster_neighbor_update(Cluster_Sorted):
    """
    input: Cluster list
    output: Cluster list with updated nearestNeighbor list

    Checks each clusters neighbor list. If a neighbor does not have itself in the list adds 
    the first cluster

    O(n*C*n)) where n are clusters

    might be better to have a dictionary of {ParentClusters: neighborlist} and update neighborlist

    """

    if Cluster_Sorted:

        for each in Cluster_Sorted:

            t = each.getParent()
            neighbors = each.getNearestNeighbor()


            for item in neighbors:
                
                for entry in Cluster_Sorted:
                    z = entry.getParent()
                    
                    if not z == t and item[0] == z:
                        # item neighbor list
                        nlist = entry.getNearestNeighbor()
                        if not entry.existsNearestNeighbor(t):
                            entry.addToNearestNeighbor(t, item[1])






#calculates the nearest 3 neighbors
def cluster_neighbor(ClusterList):
    pass

def cluster_citysort(cluster):

    a = cluster.getCityList()
    a.sort(key = lambda c: c[0][1] )



def cluster_city_bruteforce(cluster, startPoint):
    """ 
    Sorts within city using a greedy algorithm

    input:  cluster, 
            startPoing = [tuple, distance, running total]
            (starting point = last citylist entry in prior cluster)
            last city from current cluster used if starting point is None
    output: sorted cluster

    

    """

    cities = cluster.getCityList()
    citiesSorted = []
    subtotal = []
    tourtotal = cluster.getLastCityDistance()
    print cluster.getCityList()

    # obtain the last item from current cities (i.e. not parent item)
    #   place into new list in order to do the search sequence
    if startPoint is not None:
        print startPoint
        print cities
        startTuple = startPoint[0]

        v = [x[0] for x in cities].index(startTuple)
        print " At brute force starting point " + str(v) + " " + str(startPoint[1]) + " " + str(startPoint[2])
        print cities[v]
        tmp = cities.pop(v)

        tmp[1] = startPoint[1]
        tmp[2] = startPoint[2]
        citiesSorted.append(tmp)

    elif cities:
        tmp = cities.pop(-1)
        tmp[1] = 0
        tmp[2] = 0
        citiesSorted.append(tmp)

    

    # Iterate through copied list, comparing the distances to items 
    #   in the original list, append the closest to the copied list
    for index in citiesSorted:
        #            intdex [0][n],        index[1]    ,    index[2]
        #  city_entry = [(tuple), distance to prev city, distance running total]
        x1, y1, t1 = int(index[0][1]), int(index[0][2]), int(index[2])

        minDistance = tourtotal
        minIndex = 0
        counter = 0

        for runner in cities:

            x2, y2 = int(runner[0][1]), int(runner[0][2])
            m2 = distance(x1, y1, x2, y2) 
            if(m2 <= minDistance):
                minIndex = counter
                minDistance = m2

            counter+=1

        if cities:
            tmp = cities.pop(minIndex)
            tmp[1] = minDistance
            tmp[2] = t1 + minDistance
            citiesSorted.append(tmp)
    return citiesSorted

def cluster_sequencer_find_NextNeighbor(cluster, Cluster_Sorted):
    """
    input: index cluster, remaining Cluster_Sorted list
    output: next cluster: Cluster_Sorted.index of closest cluster

        returns closest neighbor from nearestNeighborsList 
        or finds new one if values in neighborlist are not present in Cluster_Sorted


    """

    nlist = cluster.getNearestNeighbor()

    for item in nlist:
        print item

    # not finished.



def cluster_sequencer_printNextNeighbor(cluster, Cluster_Sorted):
    nlist = cluster.getNearestNeighbor()

    for item in nlist:
        print item


  
def cluster_sequencer(Cluster_Sorted):
    """
    input: Cluster_Sorted + updated Neighborhood list
    output: Externally and Internally sorted list of Clusters

    >>> print out == iterating through each SortedClusterSequence.cityList
    >>> total is SortedClusterSequence[-1].cityList[-1] running total distance

    """

    SortedClusterSequence = []

    #   obtain the first element 
    if Cluster_Sorted:
        tmp = Cluster_Sorted.pop()
        tmp.replaceCityList(cluster_city_bruteforce(tmp, None))

        # call findNextNeighbor

        
    # Add starter cluster to SortedClusterSequence
    #   sort internally

    # obtain next cluster Cluster_Sorted index
    # obtain closest city within cluster

    # itera




    return SortedClusterSequence


def cluster_sequencer_simple(Cluster_Sorted):
    """
    input: Cluster_Sorted + updated Neighborhood list
    output: Externally and Internally sorted list of Clusters

    using clusters in Cluster_Sorted indexed order, 
    connect all cities.

    """ 

    SortedClusterSequence = []

    #   obtain the first element 
    if Cluster_Sorted:
        if Cluster_Sorted[1]:
            cityTuple, distance = get_closest_city(Cluster_Sorted[0], Cluster_Sorted[1].getParent())
            

            tmp = cluster_city_bruteforce(Cluster_Sorted[0], [cityTuple, 0, 55])
            print " this sequencer simple" + str(cityTuple) + " " + str(distance)
            print tmp
            Cluster_Sorted[0].replaceCityList(tmp[::-1])  #insert list in reverse order  http://stackoverflow.com/questions/3705670/best-way-to-create-a-reversed-list-in-python

            SortedClusterSequence.append(Cluster_Sorted.pop(0))

        for cluster in Cluster_Sorted:

            

            

        # call findNextNeighbor

        
    # Add starter cluster to SortedClusterSequence
    #   sort internally

    # obtain next cluster Cluster_Sorted index
    # obtain closest city within cluster

    # itera




    #return SortedClusterSequence


def get_closest_city(clusterA, entry):
    """
    input: cluster to search, entry tuple
    output: the city in clusterA closest to tuple, distance from tuple to city
    """

    cities = clusterA.getCityList()
    x1, y1 = int(entry[1]), int(entry[2])

    minDistance = clusterA.getN()
    minIndex = 0
    counter = 0

    for city in cities:
        
        x2, y2 = int(city[0][1]), int(city[0][2])
        m2 = distance(x1, y1, x2, y2) 

        if(m2 <= minDistance):
            minIndex = counter
            minDistance = m2

        counter+=1

    val = cities[minIndex]

    return val[0], minDistance





def cluster_sort(cluster):
    pass

def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return int(sqrt(dx*dx + dy*dy))   


def make_Cluster(entry, ClusterList, n):
    # if not ClusterList:
    #     #create new cluster
    #     # find n from x or y      
    #n = max(entry[1], entry[2])

    x1, y1 = int(entry[1]), int(entry[2])
    ident = int(entry[0])

    s = Cluster(n, x1, y1, ident)
    s.addCityList([entry, 0, 0])

    if ClusterList:
        p_d, p_rt = ClusterList[-1].getParentDistanceStats()
        x2, y2 = ClusterList[-1].getCoord()
        # get distance
        m2 = distance(x1, y1, x2, y2)
        s.setParentDistanceStats(m2, m2+p_rt)


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
            x2, y2, m2 = item.getLastCityList()
            m = distance(x1, y1, x2, y2)
            #item.cityList.append([entry, m])
            #item.addCityList(entry, m, x1, y1)
            item.addCityList([entry, m, m+m2])
            return True
        # else:
        #     print "sorry not included " + str(entry) + "       distance: " + str(m)

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
    NeighborList = []

    #call input_coords ()
    input_coords(filename, ClusterList)


    ClusterList = neighbor_list_bruteforce(ClusterList)
    cluster_neighbor_update(ClusterList)

    m = 0
    for item in ClusterList:
        m+=1
        print str(m) + " " + str(item.getParent())
        #item.replaceCityList(cluster_city_bruteforce(item, None))
        print item.getCityList()
        #item.replaceCityList(cluster_city_bruteforce(item))
        #cluster_sequencer_find_NextNeighbor(item, ClusterList)

    # ClusterList = neighbor_list_bruteforce(ClusterList)
    # cluster_neighbor_update(ClusterList)


    cluster_sequencer_simple(ClusterList)

    # m = 0
    # for item in ClusterList:
    #     m+=1
    # #     #print str(m) + " " + str(item.x) + " " + str(item.y)
    # #     print str(item.getParent()) + " "  + str(m)
    #     print item.getNearestNeighbor()
    #     print " "


    # call sort: neighbor and cluster
    # seperate list of neighbor clusters

    #sort within clusters
    #find closest point from cluster to neighbor clusters

    # Refine (OPT)
    #   neighbor cluster list
    #       newCLusterList 

    #print out
    #   follow neighbor cluster list
    #   print into list each point in cluster, iteratively

    # write to file




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
        
                                   
                
        
    

    

        

        

        
        

