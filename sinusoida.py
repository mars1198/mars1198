import pylab as pyl

dt = 0.05
p = -5.0
sp = 5.0

acc = [p*sp]
vel = [0.0]
s = [sp]
t = [0.0]

for i in range (1, 100):
   acc.append(s[-1]*p)
   vel.append(vel[-1] + acc[-1]*dt)
   s.append(s[-1]+vel[-1]*dt)
   t.append(dt*i)

dp = pyl.plot(t, s)
pyl.show()
