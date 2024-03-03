import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file into a pandas DataFrame
csv_file_path = 'csv files/Theft.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Assuming your CSV file has columns 'area', 'crime', and 'count'


# Save the bar graph as an image


areas = df['area']
counts = df['count']
plt.figure(figsize=(15, 8))
plt.pie(counts, labels=areas, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Crime Counts Distribution by Area')
plt.tight_layout()

# Save the pie chart as an image
plt.savefig('crime_counts_pie_chart.png')
plt.show()


 
