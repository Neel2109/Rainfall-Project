import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('fall.csv')

# Ensure 'date' column exists for plotting purposes
data['date'] = pd.to_datetime(data[['year', 'month', 'day']])
data.set_index('date', inplace=True)

# Plot overall trends
fig, axs = plt.subplots(4, 1, figsize=(12, 20))

# Plot temperature trends
axs[0].plot(data.index, data['tempavg'], color='tab:red')
axs[0].set_title('Average Temperature Over Time')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Average Temperature (°C)')
fig.savefig('average_temperature_over_time.png')

# Plot humidity trends
axs[1].plot(data.index, data['humidity avg'], color='tab:blue')
axs[1].set_title('Average Humidity Over Time')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Average Humidity (%)')
fig.savefig('average_humidity_over_time.png')

# Plot wind speed trends
axs[2].plot(data.index, data['windavg'], color='tab:green')
axs[2].set_title('Average Wind Speed Over Time')
axs[2].set_xlabel('Date')
axs[2].set_ylabel('Average Wind Speed (km/h)')
fig.savefig('average_wind_speed_over_time.png')

# Plot rainfall trends
axs[3].plot(data.index, data['Rainfall'], color='tab:purple')
axs[3].set_title('Rainfall Over Time')
axs[3].set_xlabel('Date')
axs[3].set_ylabel('Rainfall (mm)')
fig.savefig('rainfall_over_time.png')

plt.tight_layout()
plt.show()

# Monthly patterns
monthly_data = data.resample('M').mean()

fig, axs = plt.subplots(4, 1, figsize=(12, 20))

# Plot monthly average temperature
axs[0].bar(monthly_data.index, monthly_data['tempavg'], color='tab:red')
axs[0].set_title('Monthly Average Temperature')
axs[0].set_xlabel('Month')
axs[0].set_ylabel('Average Temperature (°C)')
fig.savefig('monthly_average_temperature.png')

# Plot monthly average humidity
axs[1].bar(monthly_data.index, monthly_data['humidity avg'], color='tab:blue')
axs[1].set_title('Monthly Average Humidity')
axs[1].set_xlabel('Month')
axs[1].set_ylabel('Average Humidity (%)')
fig.savefig('monthly_average_humidity.png')

# Plot monthly average wind speed
axs[2].bar(monthly_data.index, monthly_data['windavg'], color='tab:green')
axs[2].set_title('Monthly Average Wind Speed')
axs[2].set_xlabel('Month')
axs[2].set_ylabel('Average Wind Speed (km/h)')
fig.savefig('monthly_average_wind_speed.png')

# Plot monthly total rainfall
axs[3].bar(monthly_data.index, monthly_data['Rainfall'], color='tab:purple')
axs[3].set_title('Monthly Total Rainfall')
axs[3].set_xlabel('Month')
axs[3].set_ylabel('Total Rainfall (mm)')
fig.savefig('monthly_total_rainfall.png')

plt.tight_layout()
plt.show()

# Correlation matrix
correlation_matrix = data[['tempavg', 'DPavg', 'humidity avg', 'SLPavg', 'visibilityavg', 'windavg', 'Rainfall']].corr()

plt.figure(figsize=(10, 8))
plt.matshow(correlation_matrix, fignum=1, cmap='coolwarm')
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Matrix of Weather Variables', pad=20)
plt.savefig('correlation_matrix.png')
plt.show()

# Scatter plots
fig, axs = plt.subplots(3, 2, figsize=(15, 15))

# Scatter plot between tempavg and humidity avg
axs[0, 0].scatter(data['tempavg'], data['humidity avg'], alpha=0.5, color='tab:blue')
axs[0, 0].set_title('Temperature vs Humidity')
axs[0, 0].set_xlabel('Average Temperature (°C)')
axs[0, 0].set_ylabel('Average Humidity (%)')

# Scatter plot between tempavg and windavg
axs[0, 1].scatter(data['tempavg'], data['windavg'], alpha=0.5, color='tab:green')
axs[0, 1].set_title('Temperature vs Wind Speed')
axs[0, 1].set_xlabel('Average Temperature (°C)')
axs[0, 1].set_ylabel('Average Wind Speed (km/h)')

# Scatter plot between humidity avg and rainfall
axs[1, 0].scatter(data['humidity avg'], data['Rainfall'], alpha=0.5, color='tab:purple')
axs[1, 0].set_title('Humidity vs Rainfall')
axs[1, 0].set_xlabel('Average Humidity (%)')
axs[1, 0].set_ylabel('Rainfall (mm)')

# Scatter plot between tempavg and visibilityavg
axs[1, 1].scatter(data['tempavg'], data['visibilityavg'], alpha=0.5, color='tab:orange')
axs[1, 1].set_title('Temperature vs Visibility')
axs[1, 1].set_xlabel('Average Temperature (°C)')
axs[1, 1].set_ylabel('Average Visibility (km)')

# Scatter plot between windavg and rainfall
axs[2, 0].scatter(data['windavg'], data['Rainfall'], alpha=0.5, color='tab:red')
axs[2, 0].set_title('Wind Speed vs Rainfall')
axs[2, 0].set_xlabel('Average Wind Speed (km/h)')
axs[2, 0].set_ylabel('Rainfall (mm)')

# Scatter plot between SLPavg and rainfall
axs[2, 1].scatter(data['SLPavg'], data['Rainfall'], alpha=0.5, color='tab:cyan')
axs[2, 1].set_title('Sea-Level Pressure vs Rainfall')
axs[2, 1].set_xlabel('Sea-Level Pressure (hPa)')
axs[2, 1].set_ylabel('Rainfall (mm)')

plt.tight_layout()
plt.savefig('scatter_plots.png')
plt.show()