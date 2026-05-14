import matplotlib.pyplot as plt

#pie - number vs category. o/p will be in the form of %

labels = ['Maths', "Science", "English"]
values = [30, 40, 30]

#autopct - how many decimal point ? 1.1 - 1 decimal, 1.2 - 2 decimal. % f%% -> syntax
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)

plt.title('Pie Chart example')

plt.show()