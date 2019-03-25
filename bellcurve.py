import matplotlib.pyplot as plt
import random

# looks pretty with the following values
TOTAL_BALLS = 50000
TOTAL_LINES = 16

def galton(balls, lines) -> list:
	dist = [0] * ((lines * 2) + 1)

	for ball in range(0, balls):
		total = 0
		
		for line in range(1, lines+1):	
			outcome = random.uniform(0, 1)
			if(outcome >= 0.5):
				total += 1
			else:
				total -= 1	
		dist[total + lines] += 1 

	for i in range(0, lines + 1):
		dist[i] = dist[i*2]	

	return dist[0:lines+1]

def plot_galton(dist, lines):
	plt.bar([str(i) for i in range(0, lines + 1)], dist[0:lines+1])
	plt.xticks([])
	plt.show()

dist = galton(TOTAL_BALLS, TOTAL_LINES)
plot_galton(dist, TOTAL_LINES)
