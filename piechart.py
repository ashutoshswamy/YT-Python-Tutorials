import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [215, 130, 245, 210]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')

plt.show()
