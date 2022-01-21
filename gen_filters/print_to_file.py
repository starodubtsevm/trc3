import os
from const import*

def prn_headers(y, freqs, len_tabs, fs, text):

    str1 = "#ifndef __FIR_"+ str(freqs)+str(text)+"_H__"
    str2 = "#define __FIR_"+ str(freqs)+str(text)+"_H__"
    str3 = ""
    str4 = "#define LENGTH_FIR_"+str(freqs)+str(text)+"    "+str(len_tabs)
    str5 = ""
    str6 = "static fract16 fir"+ str(freqs)+"coeff"+str(text)+"[LENGTH_FIR_"+str(freqs)+str(text)+"] ="
    str7 = "{"
    str8 = "};"
    str9 = ""
    str10 = "#endif"

    head = (str1, str2, str3, str4, str5, str6, str7)

    directory_path = "./Headers"
    file_path = os.path.join(directory_path, "FIR_" + str(freqs)+ "_" + str(fs) + str(text) + ".h")

    out_file = open(file_path,"wt")
    for i in range (len(head)):
        out_file.write(head[i] +'\n')

    string = ""

    for i in range (0,len_tabs,8):
        if (len_tabs - i) > 8:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},".format(y[i],\
            y[i+1],y[i+2],y[i+3],y[i+4],y[i+5],y[i+6],y[i+7])
        elif (len_tabs - i) == 8:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d}".format(y[i],\
            y[i+1],y[i+2],y[i+3],y[i+4],y[i+5],y[i+6],y[i+7])
        elif (len_tabs - i) == 7:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d}".format(y[i],\
            y[i+1],y[i+2],y[i+3],y[i+4],y[i+5],y[i+6])
        elif (len_tabs - i) == 6:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d},{:7d}".format(y[i],\
            y[i+1],y[i+2],y[i+3],y[i+4],y[i+5])
        elif (len_tabs - i) == 5:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d}".format(y[i],y[i+1],y[i+2],\
            y[i+3],y[i+4])
        elif (len_tabs - i) == 4:
            string = "{:7d},{:7d},{:7d},{:7d}".format(y[i],y[i+1],y[i+2],y[i+3])
        elif (len_tabs - i) == 3:
            string = "{:7d},{:7d},{:7d}".format(y[i],y[i+1],y[i+2])
        elif (len_tabs - i) == 2:
            string = "{:7d},{:7d}".format(y[i],y[i+1])
        elif (len_tabs - i) == 1:
            string = "{:7d} ".format(y[i])

        out_file.write(string + '\n')
        string = ""

    finish = (str8, str9)
    for i in range (len(finish)):
        out_file.write(finish[i] +'\n')

    out_file.write(str10 +'\n')
    out_file.close


def prn_model_files(y, freqs, len_tabs,fs,text):

    str4 = "#LENGTH_FIR_"+str(freqs)+" Hz "+str(len_tabs)+ " taps"
    str5 = "#fs = " + " " + str(fs) + " Hz"
    str7 = "["
    str8 = "]"
    str9 = "f_" + str(freqs) + " = ["

    head = (str4, str5, str9)

    directory_path = "../trc3_model/FIR_models/"
    file_path = os.path.join(directory_path, "FIR_" + str(freqs)+ str(text) +".py")

    out_file = open(file_path,"wt")
    for i in range (len(head)):
        out_file.write(head[i] +'\n')

    string = ""

    for i in range (0,len_tabs,8):
        if (len_tabs - i) > 8:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},".format(y[i],\
            y[i+1],y[i+2],y[i+3],y[i+4],y[i+5],y[i+6],y[i+7])
        elif (len_tabs - i) == 8:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d}".format(y[i],\
            y[i+1],y[i+2],y[i+3],y[i+4],y[i+5],y[i+6],y[i+7])
        elif (len_tabs - i) == 7:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d},{:7d},{:7d}".format(y[i],\
            y[i+1],y[i+2],y[i+3],y[i+4],y[i+5],y[i+6])
        elif (len_tabs - i) == 6:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d},{:7d}".format(y[i],\
            y[i+1],y[i+2],y[i+3],y[i+4],y[i+5])
        elif (len_tabs - i) == 5:
            string = "{:7d},{:7d},{:7d},{:7d},{:7d}".format(y[i],y[i+1],y[i+2],\
            y[i+3],y[i+4])
        elif (len_tabs - i) == 4:
            string = "{:7d},{:7d},{:7d},{:7d}".format(y[i],y[i+1],y[i+2],y[i+3])
        elif (len_tabs - i) == 3:
            string = "{:7d},{:7d},{:7d}".format(y[i],y[i+1],y[i+2])
        elif (len_tabs - i) == 2:
            string = "{:7d},{:7d}".format(y[i],y[i+1])
        elif (len_tabs - i) == 1:
            string = "{:7d} ".format(y[i])

        out_file.write(string + '\n')
        string = ""

    finish = (str8)
    for i in range (len(finish)):
        out_file.write(finish[i] +'\n')

    out_file.close

