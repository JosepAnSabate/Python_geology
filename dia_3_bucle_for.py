import os 
import shutil 
import glob 


#for i in range(1,10):
    
  #  if i == 5:
  #      break
  #  else:
  #      pass #sutilitza sobretot per try i except
   # print(i)

dir = "C:/Users/34639/Desktop/imgsent2/"

dir_out = dir + "Fotots/"

if not os.path.exists(dir_out):
    os.mkdir(dir_out)

os.chdir(dir)

for i in glob.glob("*.JPG"):
    print(i)
    new_name= dir_out+ i[:-4]+"m"+".jpg"
    shutil.move(i,new_name)