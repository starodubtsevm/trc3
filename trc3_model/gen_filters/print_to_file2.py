import os
from const import *


def prn_to_file2(y, len_y, n_taps, delay_ms, delay_tick):
    res = []
    head_count = 0
    directory_path = "./CPPs"
    file_path = os.path.join(directory_path, "const_params" + ".cpp")
    out_file = open(file_path, "wt")

    global_head = '''//
//  const_params.cpp
//
//  Code generation for model "CRLdecoder".
//
//  Model version              : 1.192
//  Simulink Coder version : 9.0 (R2018b) 24-May-2018
//  C++ source code generated on : Wed Apr 15 14:42:52 2020

#include "rtwtypes.h"
'''
    head_1 = '''
extern const uint8_T rtCP_pooled_2VbQ4fwuIrYI;
const uint8_T rtCP_pooled_2VbQ4fwuIrYI = 84U;
extern const uint8_T rtCP_pooled_7RDcWxPAsoZj[8];
const uint8_T rtCP_pooled_7RDcWxPAsoZj[8] = { 171U, 87U, 174U, 93U, 186U, 117U,
   234U, 213U } ;

extern const uint8_T rtCP_pooled_7SO3KLzA3oiw;
const uint8_T rtCP_pooled_7SO3KLzA3oiw = 181U;
'''
    str1 = "extern const int16_T rtCP_pooled_8yBDKlhJRBwC[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_8yBDKlhJRBwC[" + str(
        n_taps) + "] = {" + '\n'

    head_1 = head_1 + str1 + str2

    head_2 = '''
extern const uint8_T rtCP_pooled_9FnEYJadcCNv[8];
const uint8_T rtCP_pooled_9FnEYJadcCNv[8] = { 134U, 13U, 26U, 52U, 104U, 208U,
  161U, 67U } ;

extern const uint8_T rtCP_pooled_Cb5pPY6UVSBf;
const uint8_T rtCP_pooled_Cb5pPY6UVSBf = 74U;
extern const uint8_T rtCP_pooled_CfX2Fv7a5Szf;
const uint8_T rtCP_pooled_CfX2Fv7a5Szf = 121U;
'''
    str1 = "extern const int16_T rtCP_pooled_Edk1mcyMo0OS[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_Edk1mcyMo0OS[" + str(
        n_taps) + "] = {" + '\n'

    head_2 = head_2 + str1 + str2

    head_3 = '''
extern const uint8_T rtCP_pooled_HZCEvVJK6aRK[8];
const uint8_T rtCP_pooled_HZCEvVJK6aRK[8] = { 211U, 167U, 79U, 158U, 61U, 122U,
  244U, 233U } ;
'''
    str1 = "extern const int16_T rtCP_pooled_KNqaX0SAN7Zx[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_KNqaX0SAN7Zx[" + str(
        n_taps) + "] = {" + '\n'

    head_3 = head_3 + str1 + str2

    head_4 = '''
extern const uint8_T rtCP_pooled_LuULhQSLkhhC[8];
const uint8_T rtCP_pooled_LuULhQSLkhhC[8] = { 74U, 148U, 41U, 82U, 164U, 73U,
  146U, 37U } ;

extern const uint8_T rtCP_pooled_N7sBK2Mw9Epj[8];
const uint8_T rtCP_pooled_N7sBK2Mw9Epj[8] = { 205U, 155U, 55U, 110U, 220U, 185U,
  115U, 230U } ;
'''

    #head_5
    str1 = "extern const int16_T rtCP_pooled_OgkIRmPmpSMM[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_OgkIRmPmpSMM[" + str(
        n_taps) + "] = {" + '\n'

    head_5 = str1 + str2

    head_6 = '''
extern const uint8_T rtCP_pooled_PDi6MRGkSSA3;
const uint8_T rtCP_pooled_PDi6MRGkSSA3 = 171U;
'''
    str1 = "extern const int16_T rtCP_pooled_PlaOfBkhFuCr[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_PlaOfBkhFuCr[" + str(
        n_taps) + "] = {" + '\n'
    head_6 = head_6 + str1 + str2

    #head_7 =
    str1 = "extern const int16_T rtCP_pooled_Wpx20rOZVq0F[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_Wpx20rOZVq0F[" + str(
        n_taps) + "] = {" + '\n'

    head_7 = str1 + str2

    #head_8 =
    str1 = "extern const int16_T rtCP_pooled_XM0RBTJG4YQ8[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_XM0RBTJG4YQ8[" + str(
        n_taps) + "] = {" + '\n'

    head_8 = str1 + str2

    head_9 = '''
extern const uint8_T rtCP_pooled_ZDi27VJOtg5z[8];
const uint8_T rtCP_pooled_ZDi27VJOtg5z[8] = { 50U, 100U, 200U, 145U, 35U, 70U,
  140U, 25U } ;

extern const uint8_T rtCP_pooled_ZLAO6JieMuq9;
const uint8_T rtCP_pooled_ZLAO6JieMuq9 = 50U;
'''
    str1 = "extern const int16_T rtCP_pooled_ajOyiEKWABkv[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_ajOyiEKWABkv[" + str(
        n_taps) + "] = {" + '\n'

    head_9 = head_9 + str1 + str2

    head_10 = '''
extern const uint8_T rtCP_pooled_c2uBisso22Ig[8];
const uint8_T rtCP_pooled_c2uBisso22Ig[8] = { 84U, 168U, 81U, 162U, 69U, 138U,
  21U, 42U } ;

extern const uint8_T rtCP_pooled_ckcLlbJeGFkU;
const uint8_T rtCP_pooled_ckcLlbJeGFkU = 103U;
extern const uint8_T rtCP_pooled_dEnNnIsPPoTY[8];
const uint8_T rtCP_pooled_dEnNnIsPPoTY[8] = { 103U, 206U, 157U, 59U, 118U, 236U,
  217U, 179U } ;
'''
    str1 = "extern const int16_T rtCP_pooled_e4pcgdD1TyBV[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_e4pcgdD1TyBV[" + str(
        n_taps) + "] = {" + '\n'

    head_10 = head_10 + str1 + str2

    head_11 = '''
extern const uint8_T rtCP_pooled_gsAVIpHav1fv;
const uint8_T rtCP_pooled_gsAVIpHav1fv = 152U;
extern const uint8_T rtCP_pooled_h2OnYFqtQmAB;
const uint8_T rtCP_pooled_h2OnYFqtQmAB = 134U;
extern const uint8_T rtCP_pooled_hHFTkZzEKbKD;
const uint8_T rtCP_pooled_hHFTkZzEKbKD = 44U;
extern const uint8_T rtCP_pooled_i8fHHn2eLyuv[8];
const uint8_T rtCP_pooled_i8fHHn2eLyuv[8] = { 181U, 107U, 214U, 173U, 91U, 182U,
  109U, 218U } ;

extern const uint8_T rtCP_pooled_iew4g4hR5Emc;
const uint8_T rtCP_pooled_iew4g4hR5Emc = 205U;
extern const uint8_T rtCP_pooled_kImaMppgcEjN;
const uint8_T rtCP_pooled_kImaMppgcEjN = 211U;
'''
    str1 = "extern const int16_T rtCP_pooled_mJnUGzDBmqYT[" + str(
        n_taps) + "];" + '\n'
    str2 = "const int16_T rtCP_pooled_mJnUGzDBmqYT[" + str(
        n_taps) + "] = {" + '\n'

    head_11 = head_11 + str1 + str2

    head_12 = '''
extern const uint8_T rtCP_pooled_mPYnLtgiiItT[8];
const uint8_T rtCP_pooled_mPYnLtgiiItT[8] = { 152U, 49U, 98U, 196U, 137U, 19U,
  38U, 76U } ;

extern const uint8_T rtCP_pooled_saAltC75HJby[8];
const uint8_T rtCP_pooled_saAltC75HJby[8] = { 121U, 242U, 229U, 203U, 151U, 47U,
  94U, 188U } ;

extern const uint8_T rtCP_pooled_ubizTtDyKTxE[8];
const uint8_T rtCP_pooled_ubizTtDyKTxE[8] = { 44U, 88U, 176U, 97U, 194U, 133U,
  11U, 22U } ;
'''

    head_13 = '''
extern const int16_T rtCP_pooled_O3hVsjLmxGGI[644];
const int16_T rtCP_pooled_O3hVsjLmxGGI[644] = { -80, -3, -3, -3, -3, -3, -3, -3,
  -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4,
  -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,
  -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,
  -4, -4, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -2, -2, -2,
  -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0,
  0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5,
  5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 12,
  12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 17, 18,
  18, 18, 19, 19, 20, 20, 20, 21, 21, 21, 22, 22, 22, 23, 23, 23, 24, 24, 24, 25,
  25, 25, 26, 26, 26, 27, 27, 28, 28, 28, 29, 29, 29, 30, 30, 30, 31, 31, 31, 32,
  32, 32, 33, 33, 33, 34, 34, 35, 35, 35, 36, 36, 36, 37, 37, 37, 38, 38, 38, 39,
  39, 39, 39, 40, 40, 40, 41, 41, 41, 42, 42, 42, 43, 43, 43, 43, 44, 44, 44, 45,
  45, 45, 45, 46, 46, 46, 46, 47, 47, 47, 47, 48, 48, 48, 48, 48, 49, 49, 49, 49,
  50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 52, 52, 52,
  53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 54, 54, 54, 54,
  54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 53, 53, 53, 53, 53,
  53, 53, 53, 53, 53, 53, 52, 52, 52, 52, 52, 52, 52, 52, 51, 51, 51, 51, 51, 51,
  50, 50, 50, 50, 50, 50, 49, 49, 49, 49, 48, 48, 48, 48, 48, 47, 47, 47, 47, 46,
  46, 46, 46, 45, 45, 45, 45, 44, 44, 44, 43, 43, 43, 43, 42, 42, 42, 41, 41, 41,
  40, 40, 40, 39, 39, 39, 39, 38, 38, 38, 37, 37, 37, 36, 36, 36, 35, 35, 35, 34,
  34, 33, 33, 33, 32, 32, 32, 31, 31, 31, 30, 30, 30, 29, 29, 29, 28, 28, 28, 27,
  27, 26, 26, 26, 25, 25, 25, 24, 24, 24, 23, 23, 23, 22, 22, 22, 21, 21, 21, 20,
  20, 20, 19, 19, 18, 18, 18, 17, 17, 17, 17, 16, 16, 16, 15, 15, 15, 14, 14, 14,
  13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 10, 10, 10, 10, 9, 9, 9, 8, 8, 8, 8, 7,
  7, 7, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2,
  2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -2,
  -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
  -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,
  -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,
  -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3,
  -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -80 } ;
'''
    data_h = [
        head_1, head_2, head_3, head_5, head_6, head_7, head_8, head_9,
        head_10, head_11
    ]

    out_file.write(global_head)

    for j in range(len_y):
        out_file.write(data_h[j])
        for i in range(0, len(y[j]), 8):
            if (len(y[j]) - i) > 8:
                string = "{:6d},{:6d},{:6d},{:6d},{:6d},{:6d},{:6d},{:6d},".format(y[j][i],\
                y[j][i+1],y[j][i+2],y[j][i+3],y[j][i+4],y[j][i+5],y[j][i+6],y[j][i+7])
            elif (len(y[j]) - i) == 8:
                string = "{:6d},{:6d},{:6d},{:6d},{:6d},{:6d},{:6d},{:6d}".format(y[j][i],\
                y[j][i+1],y[j][i+2],y[j][i+3],y[j][i+4],y[j][i+5],y[j][i+6],y[j][i+7])
            elif (len(y[j]) - i) == 7:
                string = "{:6d},{:6d},{:6d},{:6d},{:6d},{:6d},{:6d}".format(y[j][i],\
                y[j][i+1],y[j][i+2],y[j][i+3],y[j][i+4],y[j][i+5],y[j][i+6])
            elif (len(y[j]) - i) == 6:
                string = "{:6d},{:6d},{:6d},{:6d},{:6d},{:6d}".format(y[j][i],\
                y[j][i+1],y[j][i+2],y[j][i+3],y[j][i+4],y[j][i+5])
            elif (len(y[j]) - i) == 5:
                string = "{:6d},{:6d},{:6d},{:6d},{:6d}".format(y[j][i],y[j][i+1],y[j][i+2],\
                y[j][i+3],y[j][i+4])
            elif (len(y[j]) - i) == 4:
                string = "{:6d},{:6d},{:6d},{:6d}".format(
                    y[j][i], y[j][i + 1], y[j][i + 2], y[j][i + 3])
            elif (len(y[j]) - i) == 3:
                string = "{:6d},{:6d},{:6d}".format(y[j][i], y[j][i + 1],
                                                    y[j][i + 2])
            elif (len(y[j]) - i) == 2:
                string = "{:6d},{:6d}".format(y[j][i], y[j][i + 1])
            elif (len(y[j]) - i) == 1:
                string = "{:6d}".format(y[j][i])
            out_file.write(string + '\n')
            string = ""
        out_file.write(" };")
        if j == 2:
            out_file.write(head_4)
    out_file.write(head_12)
    out_file.write(head_13)

    out_file.close
