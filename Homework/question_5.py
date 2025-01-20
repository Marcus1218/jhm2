import pandas as pd
import matplotlib.pyplot as plt
# create a sample csv file if dont have one
def create_csv(file_path):
    # Sample data
    data = {
        'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Sales': [10, 12, 15, 13, 17, 19, 21, 18, 20, 12, 10, 10]
    }
    # Create a DataFrame
    df = pd.DataFrame(data)
    # Write DataFrame to CSV
    df.to_csv(file_path, index=False)
    print(f"CSV file created at {file_path}")

# Example/file path
file_path = 'sales.csv'
csv_sample = input("Do you want to create a sample CSV file? (yes/no): ")
if csv_sample == 'yes':
    create_csv(file_path)

# Read data from CSV file
data = pd.read_csv(file_path)

# Plot the data as a bar chart
plt.bar(data['Month'], data['Sales'], color='green', width=0.5)

# Set the title and labels
plt.title('Bar Chart of Ice-cream Sales')
plt.xlabel('Month')
plt.ylabel('Sales (in thousand dollars)')

# Show the plot
plt.show()