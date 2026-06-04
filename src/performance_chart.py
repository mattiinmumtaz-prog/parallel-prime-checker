import matplotlib.pyplot as plt

methods = ['Sequential', 'Parallel']
times = [1.5537, 0.9973]

plt.figure(figsize=(6,4))

plt.bar(methods, times)

plt.title('Prime Number Search Performance')
plt.ylabel('Execution Time (seconds)')

plt.savefig('../images/performance.png', bbox_inches='tight')

plt.show()