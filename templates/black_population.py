import csv

from matplotlib import pyplot as plt

total = 0

data = []

with open('census_county_demographics_2015.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['YEAR'] == 8 and row['AGEGRP'] == 0:
			info = {'state': row['STNAME'], 
					'county': row['CTYNAME'],
					'totpop': row['TOT_POP'],
					'blkmale': row['BA_MALE']
					'blkfemale': row['BA_FEMALE']}
			data.append(info)
print(data)

"""sorted_data = sorted(data, key = lambda k: k['pct'], reverse=True)

counties = []
pcts = []

for row in sorted_data[0:10]:
	counties.append(row['county'])
	pcts.append(float(row['pct']))

plt.bar(range(0,10), pcts)

ax = plt.gca() # gca = get current axis

plt.xticks(range(0,10))
ax.set_xticklabels(counties, rotation=45)
plt.title("Clinton's Top 10 California Counties in 2016 Primary")
plt.ylabel("Pct of Vote")

plt.show()"""