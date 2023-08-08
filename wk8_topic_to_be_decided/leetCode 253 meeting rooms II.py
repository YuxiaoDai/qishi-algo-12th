# first you will sort them (with O(N logN) and then when you look at first meeting starting time,
#  you will wonder if there is a meeting ends (that means a meeting room is released), 
# if yes, you will just take that one; otherwise, you will find a new room.
# how to find a meeting room quickly that’s available when a meeting (for example, A) starts? 
# Below I will sort ending times and check the first one(let’s name it B), 
# if A.startTime ≥ B.endTime, then actually A can re-use the same meeting room A uses and in the same time, t
# if not, since B is the first one (and the earliest one) that ends, 
# then I don’t need to check others end times and will just add room number by 1 since a new room will be needed.

class Solution(object):
    def minMeetingRooms(self, intervals):
        
        startTimes = [i[0] for i in intervals]
        endTimes = [i[1] for i in intervals]
        
        startTimes = sorted(startTimes)
        endTimes = sorted(endTimes)
        
        rooms = 0
        while(len(startTimes) > 0):
            startTime = startTimes.pop(0)
            #now a meeting is going to start, is there a meeting ends
            #(meaning a meeting room is released)?
            endTime = endTimes[0]
            if endTime <= startTime:
                endTimes.pop(0)
            else:
                #need to ask for a new room
                rooms += 1
        return rooms