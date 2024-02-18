import os,re
message="enter the path: "
path=input(message)
os.chdir(path)
print(os.getcwd())
removeCriteria=re.compile(r"""(\.)""")
removeUnderScore=re.compile(r"""(_)""")    
renameCriteria=re.compile(r"""
(\d{4})     
.
([\s\w]+)""",re.VERBOSE)
for folder,subfolders,filenames in os.walk('.'):
   
    # for filename in filenames:
    #     print(os.getcwd())
    #     # nPath=os.path.join(os.getcwd(),subfolder,filename)
    #     # print(nPath)
    #     de=os.path.splitext(filename)
    #     print(de[0])
    #     mo=renameCriteria.search(de[0])
    #     if mo==None:
    #         continue
    #     print(mo.group(1))
    #     print(mo.group(2).lstrip())
        
    #     if mo!=None:
    #         newName=mo.group(1)+" "+mo.group(2).lstrip()+de[1]
    #         print(newName)
    #         print("renaming {0} to {1}".format(filename,newName))

    for filename in filenames:
        de=os.path.splitext(filename)
        removeC=removeCriteria.search(de[0])
        if removeC==None:
            continue
        else:
            newde=de[0].replace('.',' ')
            print(newde)        
            
        
        rus=removeUnderScore.search(de[0])
        if rus==None:
            continue
        else:
            newde=de[0].replace('_',' ')
            print(newde)
            