"""
Determine if there is any overlap
"""
def meetingRooms(arr):
    arr.sort()

    for i in range(len(arr)-1):
        firstMeetEnd = arr[i][1]
        secondMeetStart = arr[i+1][0]
        if firstMeetEnd > secondMeetStart:
            return False
        return True
