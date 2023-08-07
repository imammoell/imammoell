import time

# Initialize variables
base_volume = 5
current_volume = 12
cumulative_total_volume = base_volume
cumulative_num_readings = 1  # Start with 1 to include the base volume

# Start the loop
while True:
    # Calculate the average volume per second
    average_volume_per_second = (cumulative_total_volume + current_volume) / (cumulative_num_readings + 1)

    # Display the current volume, base volume, and the average volume per second
    print("Base volume: ", base_volume)
    print("Current volume from sensor: ", current_volume)
    print("Average volume per second: ", average_volume_per_second)

    # Update the cumulative total volume and cumulative number of readings
    cumulative_total_volume = (average_volume_per_second * cumulative_num_readings) + current_volume
    cumulative_num_readings += 1

    # Get the next volume reading from the sensor (replace this with the actual function)
    current_volume = 18# Replace this with the actual function to get the volume reading from the sensor

    # Wait for 1 second before the next reading
    time.sleep(1)