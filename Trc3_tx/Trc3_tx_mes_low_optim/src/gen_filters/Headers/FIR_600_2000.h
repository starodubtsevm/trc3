#ifndef __FIR_600_H__
#define __FIR_600_H__

#define LENGTH_FIR_600    45

static fract16 fir600coeff[LENGTH_FIR_600] =
{
     11,    -13,     97,    -37,    -61,    -53,    -81,    400,
   -102,     16,   -456,   -315,   1021,   -104,    743,  -1789,
   -840,   1681,    371,   4459,  -8215,  -4243,  15073,  -4243,
  -8215,   4459,    371,   1681,   -840,  -1789,    743,   -104,
   1021,   -315,   -456,     16,   -102,    400,    -81,    -53,
    -61,    -37,     97,    -13,     11
};

#endif