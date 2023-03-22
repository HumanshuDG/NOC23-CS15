def dist(A,B):

	m = abs(dragons[A][0] - dragons[B][0])
	n = abs(dragons[A][1] - dragons[B][1])
	return(m + n)

(rs,cs,ks,ds) = input().strip().split()

(r,c,k,d) = (int(rs),int(cs),int(ks),int(ds))

dragons = [(0,0)]


for i in range(d):
	(xs,ys) = input().strip().split() 
	(a,b) = (int(xs),int(ys))
	dragons.append((a,b))

dragons.sort()

kd = [[0 for cmn in range(k+1)] for row in range(d+1)]


for row in range(d+1):
	for cmn in range(k+1):
		if cmn != row:
			kd[row][cmn] = r*c+1

for dragon in range(1,d+1):
	for victim in range(1,min(dragon+1,k+1)):

		kd[dragon][victim] = min([ kd[i][victim-1] + dist(i,dragon) for i in range(victim-1,dragon) ])

res = min( [ kd[i][k] for i in range(dragon+1) ])
print(res,end="")
