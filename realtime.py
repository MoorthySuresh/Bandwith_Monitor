import psutil
from matplotlib import pyplot as plt
from datetime import datetime
import time
from urllib.request import urlopen

def isIavaialbel():
    try:
        urlopen("https://www.google.com/", timeout=1)
        return True
    except:
        return False
        print("Internet Connection unavailable at:", datetime.now())  
        
print(isIavaialbel ())  

fig=plt.figure()
ax=fig.add_subplot(111)
fig.show()

i=0
time1=datetime.now()
print("Start_Time: ", time1)
x,y, y1=[],[],[]
upload=psutil.net_io_counters().bytes_sent
download=psutil.net_io_counters().bytes_recv
while i<10:
    #print(datetime.now())
    #upload=(psutil.net_io_counters().bytes_sent)
    #download= (psutil.net_io_counters().bytes_recv)
    
    x.append(i)
    y.append((psutil.net_io_counters().bytes_sent))
    y1.append((psutil.net_io_counters().bytes_recv))
   
    
    ax.plot(x,y, color="b")
    ax.plot(x,y1, color="g")
    
    fig.canvas.draw()
    time.sleep(1)
     
    i+=1
print("UPLOADED_MB :",(((psutil.net_io_counters().bytes_sent-upload))/10**6), "& TIME_DURATION :", datetime.now()-time1)
print("DOWNLOADED_MB :",((( psutil.net_io_counters().bytes_recv-download))/10**6),"& TIME_DURATION :", datetime.now()-time1)
#print(download, datetime.now())
#print(upload, datetime.now())
    
   
 