#ifndef __FIR_720_H__
#define __FIR_720_H__

#define LENGTH_FIR_720    500

static fract16 fir720coeff[LENGTH_FIR_720] =
{
     -5,      0,      6,      4,     -2,     -6,     -3,      4,
      6,      1,     -5,     -6,      0,      6,      5,     -1,
     -7,     -4,      3,      7,      2,     -5,     -7,     -1,
      7,      7,     -1,     -8,     -5,      3,      8,      4,
     -5,     -9,     -2,      7,      8,      0,     -8,     -7,
      2,      9,      5,     -4,    -10,     -3,      6,      9,
      1,     -8,     -8,      1,      9,      6,     -3,     -9,
     -4,      5,      9,      2,     -7,     -8,      0,      8,
      6,     -2,     -8,     -4,      3,      7,      2,     -4,
     -5,      0,      4,      4,      0,     -3,     -2,      0,
      1,      0,      0,      0,      0,     -1,     -2,      0,
      3,      3,     -1,     -6,     -4,      4,     10,      4,
     -8,    -13,     -1,     13,     14,     -2,    -19,    -15,
      8,     24,     12,    -16,    -29,     -7,     25,     31,
      0,    -35,    -31,     10,     43,     27,    -23,    -50,
    -19,     37,     54,      7,    -52,    -54,      8,     66,
     49,    -27,    -77,    -38,     48,     83,     21,    -70,
    -84,      0,     89,     78,    -26,   -106,    -65,     55,
    117,     44,    -84,   -120,    -16,    112,    115,    -17,
   -136,   -100,     55,    153,     75,    -94,   -160,    -41,
    131,    157,      0,   -164,   -142,     46,    188,    114,
    -95,   -202,    -75,    143,    203,     27,   -186,   -189,
     28,    220,    160,    -87,   -241,   -118,    146,    248,
     63,   -200,   -238,      0,    244,    210,    -68,   -275,
   -166,    138,    289,    108,   -203,   -285,    -37,    258,
    261,    -39,   -299,   -217,    118,    323,    157,   -193,
   -326,    -83,    260,    308,      0,   -312,   -268,     87,
    346,    208,   -172,   -358,   -133,    248,    347,     46,
   -311,   -313,     46,    356,    257,   -139,   -378,   -183,
    224,    376,     95,   -296,   -349,      0,    351,    299,
    -96,   -383,   -229,    188,    391,    144,   -268,   -373,
    -49,    331,    331,    -49,   -373,   -268,    144,    391,
    188,   -229,   -383,    -96,    299,    351,      0,   -349,
   -296,     95,    376,    224,   -183,   -378,   -139,    257,
    356,     46,   -313,   -311,     46,    347,    248,   -133,
   -358,   -172,    208,    346,     87,   -268,   -312,      0,
    308,    260,    -83,   -326,   -193,    157,    323,    118,
   -217,   -299,    -39,    261,    258,    -37,   -285,   -203,
    108,    289,    138,   -166,   -275,    -68,    210,    244,
      0,   -238,   -200,     63,    248,    146,   -118,   -241,
    -87,    160,    220,     28,   -189,   -186,     27,    203,
    143,    -75,   -202,    -95,    114,    188,     46,   -142,
   -164,      0,    157,    131,    -41,   -160,    -94,     75,
    153,     55,   -100,   -136,    -17,    115,    112,    -16,
   -120,    -84,     44,    117,     55,    -65,   -106,    -26,
     78,     89,      0,    -84,    -70,     21,     83,     48,
    -38,    -77,    -27,     49,     66,      8,    -54,    -52,
      7,     54,     37,    -19,    -50,    -23,     27,     43,
     10,    -31,    -35,      0,     31,     25,     -7,    -29,
    -16,     12,     24,      8,    -15,    -19,     -2,     14,
     13,     -1,    -13,     -8,      4,     10,      4,     -4,
     -6,     -1,      3,      3,      0,     -2,     -1,      0,
      0,      0,      0,      1,      0,     -2,     -3,      0,
      4,      4,      0,     -5,     -4,      2,      7,      3,
     -4,     -8,     -2,      6,      8,      0,     -8,     -7,
      2,      9,      5,     -4,     -9,     -3,      6,      9,
      1,     -8,     -8,      1,      9,      6,     -3,    -10,
     -4,      5,      9,      2,     -7,     -8,      0,      8,
      7,     -2,     -9,     -5,      4,      8,      3,     -5,
     -8,     -1,      7,      7,     -1,     -7,     -5,      2,
      7,      3,     -4,     -7,     -1,      5,      6,      0,
     -6,     -5,      1,      6,      4,     -3,     -6,     -2,
      4,      6,      0,     -5
};

#endif
