from gimpfu import *
import os
import locale
from time import strftime,localtime

def run(*args):
    template_file,list_file,output_folder=args
    output_folder=os.path.join(os.path.expanduser('~'),output_folder)
    locale.setlocale(locale.LC_ALL, "Portuguese")
    currDate = strftime("%d de %B de %Y", localtime())
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    i=0
    with open(list_file,'r') as list:
        for name in list:
            i+=1;
            bg_image=pdb.gimp_file_load(template_file,template_file)
            name_layers=filter(lambda x: x.name == '<name>',bg_image.layers)
            if(name_layers != None and len(name_layers) >= 0):
                name_layer=name_layers[0]
                #pdb.gimp_text_layer_set_font(name_layer,'Comic Sans MS')
        
                #pdb.gimp_text_layer_set_font_size(name_layer,116,0) #Change how name (from input) will appear. Eg. Size,Font etc
                pdb.gimp_text_layer_set_text(name_layer,name)
            else:
                print 'could not find a layer named <name>'

            date_layers=filter(lambda x: x.name == '<date>',bg_image.layers)
            if(date_layers != None and len(date_layers) >= 0):
                date_layer=date_layers[0]
                #pdb.gimp_text_layer_set_font(name_layer,'Comic Sans MS')
        
                #pdb.gimp_text_layer_set_font_size(name_layer,116,0) #Change how name (from input) will appear. Eg. Size,Font etc
                pdb.gimp_text_layer_set_text(date_layer,currDate)
            else:
                print 'could not find a layer named <date>'

            merged = pdb.gimp_image_merge_visible_layers(bg_image,0)
            filename=name+str(i)+'.png'
            output_filename=os.path.join(output_folder,filename).replace('\n', ' ').replace('\r', '')

            pdb.file_png_save_defaults(bg_image,merged,output_filename,filename)
		    #print "Finished"
    
register("certificate_generator","","","","","","<Toolbox>/Xtns/Languages/Python-Fu/_Certificate-Generator","",[(PF_FILE,"arg0","Certificate Template File",""),(PF_FILE,"arg1","Input Data File",""),(PF_STRING,"arg2","Output Folder","")],[],run)

main()
    
