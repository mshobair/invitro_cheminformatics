import os, sys
import pandas as pd
from PIL import Image
from colorama import init, Fore
# initilize colorama colored CLI text
init(autoreset=True)
# import CT_image_3

def imagemaker(mysigtxp, myfilename, mypath=''):
    # # # CREATE SIG TOXPRINTS IMAGE # # #
    # MYSIGTXP MUST BE pandas dataframe column header == 'Chemotype ID'

    # path to CT_image folder
    # path = '/share/home/rlougee/Desktop/CT_image_3/'
    path = os.path.realpath(__file__).split('\\')[:-1]
    if len(path) == 0:
        path = os.path.realpath(__file__).split('/')[:-1]
        path = '/'.join(path) + '/CT_image_3/'
    else:
        path = '\\'.join(path) + '\\CT_image_3\\'
    # print(path)
    if len(mysigtxp) == 0:
        return None

    # open image files for each enriched Toxprint
    myimages = list(map(Image.open, [path + str(i) + '.png' for i in mysigtxp.iloc[:,0]]))
    myimages = [x.resize((500, 500)) for x in myimages]

    # get the total width
    widths, heights = zip(*(i.size for i in myimages))
    total_width = sum(widths)
    max_height = max(heights)

    # set max width
    if total_width > 5000:
        total_width = 5000

    # create a blank new image
    new_im = Image.new('RGB', (total_width, max_height))

    # make and export the image(s)
    x_offset = 0
    count = 0
    count2 = 0

    for im in myimages:
        count += 1
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
        if count == 10:
            try:
                new_im.save('{}Enrichment_Image_{}_{}.jpg'.format(mypath, myfilename, count2))
            except:
                print(Fore.RED + 'ERROR: Image export failure')
            new_im = Image.new('RGB', (total_width, max_height))
            x_offset = 0
            count2 += 1
            count = 0
    try:
        new_im.save('{}Enrichment_Image_{}_{}.jpg'.format(mypath, myfilename, count2))
    except:
        print(Fore.RED + 'ERROR: Image export failure')

# #TEST
# if __name__ == "__main__":
#     imagemaker(pd.DataFrame(['Txp-1', 'Txp-2']), 'testtxp', '/home/rlougee/Desktop/')