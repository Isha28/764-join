import matplotlib
matplotlib.use('Agg')

# importing package
import matplotlib.pyplot as plt
import numpy as np
  
# create data
x = ['A', 'B', 'C', 'D']
y1 = np.array([10, 20, 10, 30])
y2 = np.array([20, 25, 15, 25])
y3 = np.array([12, 15, 19, 6])
    
# plot bars in stack manner
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='y')
plt.xlabel("Teams")
plt.ylabel("Score")
plt.legend(["Round 1", "Round 2", "Round 3", "Round 4"])
plt.title("Scores by Teams in 4 Rounds")
#plt.show()

out_png = '/proj/cs764spring2021-PG0/exp/sugu267-QV95772/Isha/Selectivity/graphs/sel1.png'
plt.savefig(out_png, dpi=150)
