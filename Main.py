import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2
from sklearn.tree import DecisionTreeClassifier as DTC
import os

np.random.seed(1)

X = [np.random.rand(1000)*3]

Moyenne = np.mean(X)

EcartType = np.std(X)

Median = np.median(X)

print(Moyenne,EcartType,Median)

"""Y = round(X)"""
np.random.seed(1)

X_bis = [np.random.rand(1000)*3]

Moyenne_bis = np.mean(X_bis)

EcartType_bis = np.std(X_bis)

Median_bis = np.median(X_bis)

print(Moyenne_bis,EcartType_bis,Median_bis)

noise = np.random.randn(1000)

Y = np.sin(X)+noise*0.1

plt.figure(figsize=(8,6))
plt.scatter(X, Y)
plt.show()


plt.hist(X)

plt.show()

"""ex 2"""

# Specify the path to the directory you want to count files in
directory_path = r'C:\Users\PCPG\Desktop\Cours\Vision par ordinateur\data1\computer_vision_tp1\data1\car'  # Replace this with your directory path
File_path = r'C:\Users\PCPG\Desktop\Cours\Vision par ordinateur\data1\computer_vision_tp1\data1\car\car(1).jpeg'  # Replace this with your directory path
# Check if the specified path is a directory
if os.path.isdir(directory_path):
    # Get the list of files in the directory
    files = os.listdir(directory_path)

    # Count the number of files
    num_files = len(files)

    print(f'The number of files in the directory {directory_path} is {num_files}.')
else:
    print(f'The specified path {directory_path} is not a directory.')

# Check if the specified path is a directory
if os.path.isdir(directory_path):
    # Get the list of files in the directory
    files = os.listdir(directory_path)

    print(f'{"File Name": <30} {"File Size (in bytes)": <20} {"File Format": <20}')
    for file in files:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            file_format = os.path.splitext(file)[-1]
            print(f'{file: <30} {str(file_size): <20} {file_format: <20}')
else:
    print(f'The specified path {directory_path} is not a directory.')

image = img.imread( file_path )


"""ex 3"""
clf = DTC(random_state=0)
