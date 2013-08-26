import math
import sys
import getopt
import os.path




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


def input_coords(filename):
    '''This function reads city coordinates from a text file'''
    runningList = []
    fi = open(filename)
    with fi as f:
        #add in something to skip first line, also first character of each line (the city number)
        for line in f.readlines():
            n,x,y = line.strip().split(' ')
            #coordinates.append((float(x), float(y)))
            print str(n) + "   " + str(x) + "   " + str(y)
            entry = (n, x, y)

            #call distance function

            runningList.append(entry)
    fi.close()
    return runningList


def myTour(matrix, tour):
    total = 0
    cities = len(tour)
    for i in range(cities):
        j=(i+1)%cities #shifts index up by 1
        city_i = tour[i]
        city_j = tour[j]
        total += matrix[city_i, city_j]
    return total
            





 

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
            print input_coords(arg)

    except IOError as e:
        print("({})".format(e))

    if arg == "dd":
        print "still need to implement"

    
   
if __name__ == "__main__":
    main()                                   
        
                                   
                
        
    

    

        

        

        
        

