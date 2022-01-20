#ifndef __FIR_12_H__
#define __FIR_12_H__

#define LENGTH_FIR_12    80

static fract16 fir12coeff[LENGTH_FIR_12] =
{
     -1,    -21,    -33,    -29,     -3,     36,     69,     69,
     19,    -66,   -143,   -153,    -63,    101,    256,    293,
    152,   -124,   -395,   -485,   -296,    113,    534,    709,
    491,    -51,   -641,   -933,   -717,    -64,    688,   1114,
    940,    224,   -658,  -1216,  -1119,   -399,    555,   1218,
   1218,    555,   -399,  -1119,  -1216,   -658,    224,    940,
   1114,    688,    -64,   -717,   -933,   -641,    -51,    491,
    709,    534,    113,   -296,   -485,   -395,   -124,    152,
    293,    256,    101,    -63,   -153,   -143,    -66,     19,
     69,     69,     36,     -3,    -29,    -33,    -21,     -1
};

#endif