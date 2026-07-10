import matplotlib.pyplot as plt
import seaborn as sns

titanic=sns.load_dataset('titanic')

plt.figure(figsize=(8,6))

#verifico distribuição de idade
sns.histplot(data=titanic,x='age')

plt.show()