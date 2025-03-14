# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:22:24 2023

@author: etber
"""

import rasterio
import csv
import os

countries = ["argentina","bolivia","brazil","colombia","cote_dIvoire","drc","ghana","indonesia","malaysia","paraguay","peru"]
# Specify your folder containing the TIFF files
for country in countries:
    folder_path = r'...\clipped_rasters\{}'.format(country)
    
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.tif') or filename.endswith('.tiff'):  # Check for TIFF files
            file_path = os.path.join(folder_path, filename)
    
            # Open the TIFF file
            with rasterio.open(file_path) as dataset:
                
                # Read the entire array
                data = dataset.read()
    
                # Access the geographic transform
                transform = dataset.transform
    
                # Output CSV file name based on input file name
                output_file = os.path.splitext(filename)[0] + '_output.csv'
    
                # Open a CSV file to write the data
                with open(os.path.join(folder_path, output_file), mode='w', newline='') as file:
                    writer = csv.writer(file)
    
                    # Write headers
                    writer.writerow(['File Name', 'Longitude', 'Latitude', 'Data Value'])
    
                    # Calculate coordinates and write data
                    for row in range(data.shape[1]):  # assuming data.shape as (bands, rows, cols)
                        for col in range(data.shape[2]):
                            x, y = rasterio.transform.xy(transform, row, col)
                            # Write file name, longitude, latitude, and data value to CSV
                            writer.writerow([filename, x, y, data[0, row, col]])  # Assuming single-band data
    
