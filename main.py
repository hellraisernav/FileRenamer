# TODO: import required libraries
import os,shutil,re
# TODO: define universal parameters
yearPattern=re.compile(r"""\d{4}""")
namePattern=re.compile(r"""
    (\d{4})
    .*
    ([\S\W]+)""",re.VERBOSE)
message="Please enter the address: \n"
prompt=input(message)

os.chdir(prompt)



# TODO: define the classes needed
# TODO: define the functions
for folderName,subfolders,filenames in os.walk('.'):
    for subfolder in subfolders:
      
        mo=namePattern.search(subfolder)

   
        # skip non available
        if mo==None:
            continue
    
        # get the different part of the subfoldername
        datePart=mo.group(1)
        movieName=mo.group(2)
        # print(movieName)
       
        # print(newDatePart)
# TODO: Rename
        
        newFolderName_temp=datePart+' - '+movieName
        absWorkingDir=os.path.abspath('.')
        print(absWorkingDir)
        oFolderName=os.path.join(absWorkingDir,folderName,subfolder)
        print(oFolderName)
        newFilename=os.path.join(absWorkingDir,folderName,newFolderName_temp)
        print('renaming {0} to {1}'.format(oFolderName,newFilename))
        shutil.move(oFolderName,newFilename)
    for filename in filenames:
        
        mo=namePattern.search(subfolder)


        # skip non available
        if mo==None:
            continue
    
        # get the different part of the subfoldername
        datePart=mo.group(1)
        movieName=mo.group(2)
        newFolderName_temp=datePart+' - '+movieName
        absWorkingDir=os.path.abspath('.')
        print(absWorkingDir)
        oFolderName=os.path.join(absWorkingDir,folderName,subfolder)
        print(oFolderName)
        newFilename=os.path.join(absWorkingDir,folderName,newFolderName_temp)
        print('renaming {0} to {1}'.format(oFolderName,newFilename))
        
        