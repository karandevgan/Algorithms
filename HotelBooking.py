from operator import itemgetter

def hotel(arrive, depart, K):
        arrive.sort()
        depart.sort()
        arrive_depart_map = zip(arrive, depart)
        #arrive_depart_map.sort(key=itemgetter(0,1))
        room_left = K - 1
        print arrive_depart_map
        for i in xrange(1, len(arrive_depart_map)):
            if (arrive_depart_map[i][0] < arrive_depart_map[i-1][1]):
                if room_left > 0:
                    room_left -= 1
                else:
                    room_freed = 0
                    for j in xrange(i):
                        if arrive_depart_map[j][1] <= arrive_depart_map[i][0]:
                            room_freed += 1
                    room_left = K - i + room_freed
                    if room_left <= 0:
                        return False
                    else:
                        room_left -= 1
        return True
		
A = [ 42, 21, 29, 20, 23, 21, 18, 49, 21, 24, 8, 21, 10, 1, 3, 1, 30, 24, 13, 25 ]
B = [ 91, 31, 62, 60, 23, 50, 64, 79, 47, 68, 54, 35, 58, 41, 4, 6, 48, 73, 33, 37 ]
C = 4

print hotel(A,B,C)