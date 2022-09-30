#directory/file reader
import os
import shutil
import time
directoryToSort=input("List the directory you want to sort:  ")

# Time checker
startTime= time.time_ns()

entries = os.listdir(directoryToSort)

#remove directories from the sort, only sort if the item is file
for entry in entries:
    if os.path.isfile(os.path.join(directoryToSort, entry)):

        # sort the file by type


        # creating arrays of extensions for checkings
        imagesExtensions=["rgb","gif","pbm","pgm","ppm","tiff","rast","xbm","jpeg","jpg","bmp","png","webp","exr","HEIC"]
        videoExtensions=["3g2",	"3gp","aaf","asf","avchd","avi","drc","flv","m2v","m3u8","m4p","m4v","mkv",	"mng","mov","mp2",	"mp4",	"mpe",	"mpeg",	"mpg",	"mpv",	"mxf",	"nsv",	"ogg",	"ogv",	"qt",	"rm",	"rmvb",	"roq",	"svi",	"vob",	"webm",	"wmv","yuv"]
        documentExtensions=["pdf","doc","docx","odt","xlsx","xls","ods","ppt","pptx","csv"]
        compressedExtensions=["7z",	"a","ace","apk","ar","arc","bz2","cab","chm","cpio","deb","dmg","ear","egg","epub","gz", "iso",	"jar","lz","lzma","lzo","mar","pea","pet","pkg",	"rar",	"rpm",	"s7z",	"sit",	"sitx",	"shar",	"tar",	"tbz2",	"tgz",	"tlz",	"txz",	"war",	"whl",	"xpi",	"xz",	"zip",	"zipx",	"zst"]

        # Create sorted directories if they do not exist
        if not os.path.exists(os.path.join(directoryToSort, "Images")):
            print("Images directory do not exist")
            print("creating Images directory .......")
            os.mkdir(os.path.join(directoryToSort, "Images"))
            print("Images directory created")
        if not os.path.exists(os.path.join(directoryToSort, "Videos")):
            print("Images directory do not exist")
            print("creating Images directory .......")
            os.mkdir(os.path.join(directoryToSort, "Videos"))
            print("Images directory created")
        if not os.path.exists(os.path.join(directoryToSort, "Documents")):
            print("Images directory do not exist")
            print("creating Images directory .......")
            os.mkdir(os.path.join(directoryToSort, "Documents"))
            print("Images directory created")
        if not os.path.exists(os.path.join(directoryToSort, "Compressed")):
            print("Images directory do not exist")
            print("creating Images directory .......")
            os.mkdir(os.path.join(directoryToSort, "Compressed"))
            print("Images directory created")
        if not os.path.exists(os.path.join(directoryToSort, "Others")):
            print("Images directory do not exist")
            print("creating Images directory .......")
            os.mkdir(os.path.join(directoryToSort, "Others"))
            print("Images directory created")


        # if file have extensions representing the extensions in variables then move it to respective directory
        if entry.split(".")[-1] in imagesExtensions:
            shutil.move(os.path.join(directoryToSort, entry),os.path.join(directoryToSort, "Images"))
        elif entry.split(".")[-1] in videoExtensions:
            shutil.move(os.path.join(directoryToSort, entry),os.path.join(directoryToSort, "Videos"))
        elif entry.split(".")[-1] in documentExtensions:
            shutil.move(os.path.join(directoryToSort, entry),os.path.join(directoryToSort, "Documents"))
        elif entry.split(".")[-1] in compressedExtensions:
            shutil.move(os.path.join(directoryToSort, entry), os.path.join(directoryToSort, "Compressed"))
        else:
            shutil.move(os.path.join(directoryToSort, entry), os.path.join(directoryToSort, "Others"))
# Time checker
endTime= time.time_ns()
print("Files are sorted, please check your folders")
print("Time Taken :" ,round((endTime-startTime)//1000000),"ms")