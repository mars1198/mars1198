import matplotlib.pyplot as plt

r = 1
c = 1
tau = r*c
dt = 0.05
t = 0
v = 0
threshold = 5
i = []
tdata = []
vdata = []

#this will be our current pulse
for z in range (0, 40):
        num = 10
        i.append(num)

#Now return input current to zero
for z in range (40, 75):
        num = 0
        i.append(num)

#this loop calculalate our voltage
for j in range (0, 75):
	dvdt = (1/tau) * (r*i[j] - v)
	v = v + dvdt*dt
	if v > threshold:
		v = 0
	t = t + dt
	tdata.append(t)
	vdata.append(v)
plt.plot(tdata, vdata)
plt.axis([0, t, -1, 7])
plt.xlabel('Time')
plt.ylabel('Voltage (arbitrary units)')
plt.show()
