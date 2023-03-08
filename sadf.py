import os
def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


with open('webtoon.csv','w') as f:
    f.write("안녕")
    f.write("ㅂㅇ가")