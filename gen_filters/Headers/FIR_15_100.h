#ifndef __FIR_15_H__
#define __FIR_15_H__

#define LENGTH_FIR_15    100

static fract16 fir15coeff[LENGTH_FIR_15] =
{
      7,     17,     12,     -3,    -19,    -21,     -4,     21,
     34,     17,    -20,    -50,    -40,     10,     65,     73,
     14,    -73,   -113,    -58,     64,    155,    123,    -30,
   -188,   -207,    -39,    198,    303,    152,   -167,   -399,
   -313,     76,    476,    524,    101,   -508,   -789,   -406,
    457,   1131,    932,   -241,  -1641,  -2024,   -460,   2929,
   6846,   9458,   9458,   6846,   2929,   -460,  -2024,  -1641,
   -241,    932,   1131,    457,   -406,   -789,   -508,    101,
    524,    476,     76,   -313,   -399,   -167,    152,    303,
    198,    -39,   -207,   -188,    -30,    123,    155,     64,
    -58,   -113,    -73,     14,     73,     65,     10,    -40,
    -50,    -20,     17,     34,     21,     -4,    -21,    -19,
     -3,     12,     17,      7
};

#endif
