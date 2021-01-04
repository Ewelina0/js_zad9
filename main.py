try:
    with open("file1.txt", 'r') as f1:
        with open("file22.txt",'w') as f2:
            for line in f1:
                f2.write(line)
except:
    print('Exception during opening file1!')