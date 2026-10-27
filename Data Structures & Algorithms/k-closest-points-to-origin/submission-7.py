class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # BRUTE FORCE: 

        # # Loop through the points and calculate distance of each from 0,0 and store them in a distance  arrary with the original index o(n)
        # distances = []
        # for i in range(len(points)):
        #     d = points[i][0]**2 + points[i][1]**2
        #     distances.append((d, i))

        # #  sort the distance arrary and find k min element s o(n log n)
        # distances.sort()
        # answer = []
        # for i in range(k):
        #     index = distances[i][1]
        #     answer.append(points[index])

        # # return the k min element index of the orignal points  
        # return answer


        # REAL APPROACH?
        minHeap = []
        for x, y in points: 
            dis = (x*x) + (y*y)
            minHeap.append([dis, x, y])
        heapq.heapify(minHeap)
        answer = []
        
        while k > 0:
            dis, x, y = heapq.heappop(minHeap)
            answer.append([x,y])
            k -= 1

        return answer


        