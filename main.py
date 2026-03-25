import time

closingMessage = "\nFinished writing! Closing now..."

x = 1
fi = open("outputfile.txt" , "a")
for i in range(15):
    fi.write(f"{str(x)}\n")
    x += 1

for i in range(10, 0, -1):
    fi.write(f"Deleting in {i} seconds.\n")

fi.write(closingMessage)
fi.close()