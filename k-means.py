
import numpy as np
import matplotlib.pyplot as plt



def setCluster (data, centers, dims, first_cluster=False):
    for point in data:
        jarakTerdekat = 0
        nearest_center_dist = None
        for i in range(0, len(centers)):
            euclidean_dist = 0
            for d in range(0, dims):
                dist = abs(point[d] - centers[i][d])
                euclidean_dist += dist
            euclidean_dist = np.sqrt(euclidean_dist)
            if nearest_center_dist == None:
                nearest_center_dist = euclidean_dist
                jarakTerdekat = i
            elif nearest_center_dist > euclidean_dist:
                nearest_center_dist = euclidean_dist
                jarakTerdekat = i
        if first_cluster:
            point.append(jarakTerdekat)
        else:
            point[-1] = jarakTerdekat
    return data

def hitungRataCenters (data, centers, dims, epoch): 
    new_centers = []
    for i in range(len(centers)):
        new_center = []
        n_of_points = 0
        total_of_points = []
        for point in data:
            if point[-1] == i:
                n_of_points += 1
                for dim in range(0,dims):
                    if dim < len(total_of_points):
                        total_of_points[dim] += point[dim]
                    else:
                        total_of_points.append(point[dim])
        if len(total_of_points) != 0:
            for dim in range(0,dims):
                new_center.append(total_of_points[dim]/n_of_points)
            new_centers.append(new_center)
        else:
            new_centers.append(centers[i])
    return new_centers
   
cluster = []

# Gets data and k, returns a list of center points.
def k_means_clustering(data, k, epochs):
    dims = len(data[0])
    centers = [[2,10],[5,8],[1,2]]
    clustered_data = setCluster(data, centers, dims, first_cluster=True)   
    print(clustered_data)
    for i in range(epochs):
        centers = hitungRataCenters(clustered_data, centers, dims,i+1)
        print(str('Nilai Pusat Kluster Epoch ke-') + str(i+1) +str(' :'), centers)
        clustered_data = setCluster(data, centers, dims, first_cluster=False)
    for c in range(len(clustered_data)): 
        cluster.append(clustered_data[c][2])
    return centers

#def predict_k_means_clustering(point, centers):
#    dims = len(point)
#    center_dims = len(centers[0])
#    if dims != center_dims:
#        raise ValueError('Point given for prediction have', dims, 'dimensions but centers have', center_dims, 'dimensions')
#    nearest_center = None
#    nearest_dist = None
#    for i in range(len(centers)):
#        euclidean_dist = 0
#        for dim in range(1, dims):
#            dist = point[dim] - centers[i][dim]
#            euclidean_dist += dist**2
#        euclidean_dist = np.sqrt(euclidean_dist)
#        if nearest_dist == None:
#            nearest_dist = euclidean_dist
#            nearest_center = i
#        elif nearest_dist > euclidean_dist:
#            nearest_dist = euclidean_dist
#            nearest_center = i
#        print('center:',i, 'dist:',euclidean_dist)
#    return nearest_center

X = [[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]]

centers = k_means_clustering(X,3,1)
centers = np.array(centers)
print('\n' + str(centers))


plotx = []
ploty = []
for i in range(len(X)):
    plotx.append(X[i][0])
    ploty.append(X[i][1])
colors = ['tab:blue', 'tab:orange', 'y']
for i in range(8):
    col = colors[cluster[i]]
    plt.title('Hasil Clustering')
    plt.plot(plotx[i], ploty[i], '.', markerfacecolor=col,markeredgecolor='w', markersize=15)
    plt.plot(centers[:, 0], centers[:, 1],'.', c='red',  markeredgecolor='w', markersize=25)
plt.show()
