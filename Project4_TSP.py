import math

class TSP:

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
        coordinates = []
        with open(filename) as f:
            #add in something to skip first line, also first character of each line (the city number)
            for line in f.readlines():
                n,x,y = line.strip().split(' ')
                coordinates.append((float(x), float(y)))
        return coordinates


    def myTour(matrix, tour):
        total = 0
        cities = len(tour)
        for i in range(cities):
            j=(i+1)%cities #shifts index up by 1
            city_i = tour[i]
            city_j = tour[j]
            total += matrix[city_i, city_j]
        return total
            
        
    
if __name__ == "__main__":
    main()                                   
        
                                   
                
        
    

    

        

        

        
        

