import time

# Initialize variables
max_volume = 1000
volume_readings = []

# Start the loop
while True:
    # Get the current water volume reading from the sensor (replace this with the actual function)
    volume =  # Replace this with the actual function to get the volume reading from the sensor

    # Ensure the volume is within the specified range
    volume = min(max_volume, max(0, volume))

    # Add the current volume reading to the list
    volume_readings.append(volume)

    # Sort the list of volume readings
    volume_readings.sort()

    # Calculate the median volume
    num_readings = len(volume_readings)
    median_volume = (volume_readings[num_readings // 2] + volume_readings[
        (num_readings - 1) // 2]) / 2 if num_readings % 2 == 0 else volume_readings[num_readings // 2]

    # Display the median volume
    print("Median water volume: ", median_volume)

    # Wait for 1 second before the next reading
    time.sleep(1)
