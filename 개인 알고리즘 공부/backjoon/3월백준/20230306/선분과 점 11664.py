import sys
sys.stdin = open('input', 'r')

def  calculate(x1,y1,z1,x2,y2,z2):
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** 0.5

ax, ay, az, bx, by, bz, cx, cy, cz = list(map(int,input().split()))

minlen = 1000000000000
lenac = calculate(ax,ay,az,cx,cy,cz)
lenbc = calculate(bx,by,bz,cx,cy,cz)

while True:
    mx = (ax+bx)/2
    my = (ay+by)/2
    mz = (az+bz)/2
    lenmc = calculate(mx,my,mz,cx,cy,cz)
    if abs(minlen - lenmc) <= 1e-6:
        print(f'{lenmc:.10f}')
        break
    minlen = min(lenmc,minlen)
    if lenac<lenbc:
        bx,by,bz = mx,my,mz
        lenbc = lenmc
    else:
        ax,ay,az = mx,my,mz
        lenac = lenmc

