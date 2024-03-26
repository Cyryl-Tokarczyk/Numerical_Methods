import gpxpy
import matplotlib.pyplot as plt

import os
import matplotlib.pyplot as plt

def read_file(file_path):
    elevations = []

    # Read the file
    with open(file_path, 'r') as f:
        for line in f:
            try:
                if ',' in line:
                    delimiter = ','
                else:
                    delimiter = ' '
                distance, elevation = map(float, line.strip().split(delimiter))
                elevations.append((distance, elevation))
            except ValueError:
                pass
            
    # Separate distance and elevation values
    distances, elev_vals = zip(*elevations)

    return distances, elev_vals

    

def plot_elevations(folder_path):
    # Collect all files in the folder
    files = [file for file in os.listdir(folder_path) if file.endswith(".csv") or file.endswith(".txt")]
    
    # Iterate over each file
    for file in files:
        file_path = os.path.join(folder_path, file)
        
        distances, elev_vals = read_file(file_path)
        # # Read the file
        # with open(file_path, 'r') as f:
        #     if file.endswith(".csv"):
        #         reader = csv.reader(f)
        #     elif file.endswith(".txt"):
        #         reader = csv.reader(f, delimiter='\t')
            
        #     # Extract elevation information
        #     for row in reader:
        #         if len(row) == 2:
        #             try:
        #                 distance = float(row[0])
        #                 elevation = float(row[1])
        #                 elevations.append((distance, elevation))
        #             except ValueError:
        #                 pass

        plot_elevation(distances, elev_vals, file)
        
def plot_elevation(distances, elev_vals, label):
        # Plot the elevations
        plt.plot(distances, elev_vals, label=label)
        
        # Add labels and legend
        plt.title(len(distances))
        plt.xlabel('Distance')
        plt.ylabel('Elevation')
        plt.legend()
        
        # Display the plot
        plt.show()

def extract_elevation(gpx_file_path):
    gpx_file = open(gpx_file_path, 'r')
    gpx = gpxpy.parse(gpx_file)

    elevations = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                elevations.append(point.elevation)

    return elevations

if __name__ == '__main__':
    # gpx_file_path = 'route.gpx'
    # elevations = extract_elevation(gpx_file_path)
    # print(elevations)
    # plt.plot(elevations)
    # plt.show();

    # tczew_starogard, MountEverest, astale, WielkiKanionKolorado
    
    # Provide the path to the folder containing the files
    folder_path = 'data'
    plot_elevations(folder_path)

