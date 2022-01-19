#ifndef __FIR_420_H__
#define __FIR_420_H__

#define LENGTH_FIR_420    1000

static fract16 fir420coeff[LENGTH_FIR_420] =
{
      0,     -1,     -2,     -3,     -3,     -3,     -2,     -2,
     -1,      0,      1,      2,      2,      3,      3,      3,
      2,      1,      0,      0,     -1,     -2,     -3,     -3,
     -3,     -3,     -2,     -1,      0,      1,      2,      3,
      3,      3,      3,      2,      1,      0,      0,     -1,
     -2,     -3,     -4,     -3,     -3,     -2,     -1,      0,
      1,      2,      3,      4,      4,      4,      3,      2,
      0,      0,     -1,     -3,     -4,     -4,     -4,     -3,
     -3,     -1,      0,      1,      2,      3,      4,      4,
      4,      3,      2,      1,      0,     -2,     -3,     -4,
     -4,     -4,     -4,     -3,     -1,      0,      1,      2,
      4,      4,      5,      4,      4,      2,      1,      0,
     -2,     -3,     -4,     -5,     -5,     -4,     -3,     -2,
      0,      1,      2,      3,      4,      5,      4,      3,
      2,      1,      0,     -1,     -3,     -4,     -4,     -4,
     -4,     -3,     -1,      0,      1,      2,      3,      4,
      4,      4,      3,      2,      1,      0,     -1,     -2,
     -3,     -3,     -3,     -3,     -2,     -1,      0,      0,
      1,      2,      2,      2,      2,      2,      1,      0,
      0,      0,     -1,     -1,     -1,     -1,     -1,      0,
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      1,      1,
      1,      2,      1,      1,      0,      0,     -1,     -2,
     -3,     -4,     -4,     -3,     -3,     -1,      0,      1,
      3,      5,      6,      7,      6,      5,      3,      1,
     -1,     -4,     -6,     -8,    -10,    -10,     -9,     -6,
     -3,      0,      3,      7,     10,     13,     13,     13,
     10,      7,      2,     -2,     -7,    -12,    -15,    -17,
    -17,    -15,    -12,     -6,      0,      6,     12,     17,
     21,     22,     21,     17,     12,      4,     -3,    -11,
    -18,    -24,    -27,    -27,    -24,    -18,    -10,     -1,
      8,     18,     26,     31,     33,     31,     26,     18,
      7,     -4,    -16,    -26,    -34,    -38,    -38,    -34,
    -26,    -15,     -2,     11,     24,     35,     43,     45,
     43,     36,     25,     10,     -5,    -20,    -35,    -45,
    -51,    -52,    -46,    -36,    -21,     -3,     14,     32,
     46,     56,     59,     57,     48,     33,     15,     -5,
    -26,    -44,    -58,    -66,    -67,    -60,    -47,    -28,
     -6,     17,     39,     57,     70,     75,     72,     61,
     43,     20,     -5,    -31,    -54,    -71,    -81,    -83,
    -75,    -59,    -36,     -8,     19,     47,     69,     85,
     92,     88,     75,     53,     25,     -5,    -36,    -64,
    -85,    -98,   -100,    -91,    -72,    -44,    -12,     22,
     54,     82,    100,    108,    105,     90,     64,     32,
     -4,    -41,    -74,    -99,   -114,   -117,   -107,    -85,
    -53,    -16,     23,     61,     93,    115,    125,    122,
    105,     76,     39,     -3,    -45,    -83,   -112,   -130,
   -133,   -123,    -98,    -63,    -20,     24,     68,    104,
    130,    141,    138,    119,     87,     46,     -1,    -48,
    -91,   -125,   -145,   -149,   -138,   -111,    -72,    -25,
     25,     73,    114,    143,    156,    153,    133,     98,
     53,      1,    -51,    -98,   -135,   -158,   -164,   -152,
   -123,    -81,    -30,     24,     77,    122,    154,    169,
    166,    145,    108,     59,      4,    -52,   -103,   -144,
   -169,   -176,   -164,   -134,    -89,    -34,     23,     80,
    128,    163,    180,    177,    156,    117,     66,      7,
    -52,   -107,   -150,   -178,   -186,   -174,   -143,    -96,
    -39,     22,     81,    132,    169,    188,    186,    164,
    125,     71,     10,    -52,   -109,   -154,   -183,   -192,
   -181,   -149,   -102,    -43,     19,     81,    134,    172,
    192,    191,    170,    130,     76,     13,    -50,   -108,
   -155,   -186,   -196,   -185,   -154,   -106,    -47,     16,
     79,    133,    173,    193,    193,    173,    133,     79,
     16,    -47,   -106,   -154,   -185,   -196,   -186,   -155,
   -108,    -50,     13,     76,    130,    170,    191,    192,
    172,    134,     81,     19,    -43,   -102,   -149,   -181,
   -192,   -183,   -154,   -109,    -52,     10,     71,    125,
    164,    186,    188,    169,    132,     81,     22,    -39,
    -96,   -143,   -174,   -186,   -178,   -150,   -107,    -52,
      7,     66,    117,    156,    177,    180,    163,    128,
     80,     23,    -34,    -89,   -134,   -164,   -176,   -169,
   -144,   -103,    -52,      4,     59,    108,    145,    166,
    169,    154,    122,     77,     24,    -30,    -81,   -123,
   -152,   -164,   -158,   -135,    -98,    -51,      1,     53,
     98,    133,    153,    156,    143,    114,     73,     25,
    -25,    -72,   -111,   -138,   -149,   -145,   -125,    -91,
    -48,     -1,     46,     87,    119,    138,    141,    130,
    104,     68,     24,    -20,    -63,    -98,   -123,   -133,
   -130,   -112,    -83,    -45,     -3,     39,     76,    105,
    122,    125,    115,     93,     61,     23,    -16,    -53,
    -85,   -107,   -117,   -114,    -99,    -74,    -41,     -4,
     32,     64,     90,    105,    108,    100,     82,     54,
     22,    -12,    -44,    -72,    -91,   -100,    -98,    -85,
    -64,    -36,     -5,     25,     53,     75,     88,     92,
     85,     69,     47,     19,     -8,    -36,    -59,    -75,
    -83,    -81,    -71,    -54,    -31,     -5,     20,     43,
     61,     72,     75,     70,     57,     39,     17,     -6,
    -28,    -47,    -60,    -67,    -66,    -58,    -44,    -26,
     -5,     15,     33,     48,     57,     59,     56,     46,
     32,     14,     -3,    -21,    -36,    -46,    -52,    -51,
    -45,    -35,    -20,     -5,     10,     25,     36,     43,
     45,     43,     35,     24,     11,     -2,    -15,    -26,
    -34,    -38,    -38,    -34,    -26,    -16,     -4,      7,
     18,     26,     31,     33,     31,     26,     18,      8,
     -1,    -10,    -18,    -24,    -27,    -27,    -24,    -18,
    -11,     -3,      4,     12,     17,     21,     22,     21,
     17,     12,      6,      0,     -6,    -12,    -15,    -17,
    -17,    -15,    -12,     -7,     -2,      2,      7,     10,
     13,     13,     13,     10,      7,      3,      0,     -3,
     -6,     -9,    -10,    -10,     -8,     -6,     -4,     -1,
      1,      3,      5,      6,      7,      6,      5,      3,
      1,      0,     -1,     -3,     -3,     -4,     -4,     -3,
     -2,     -1,      0,      0,      1,      1,      2,      1,
      1,      1,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      0,      0,
      0,     -1,     -1,     -1,     -1,     -1,      0,      0,
      0,      1,      2,      2,      2,      2,      2,      1,
      0,      0,     -1,     -2,     -3,     -3,     -3,     -3,
     -2,     -1,      0,      1,      2,      3,      4,      4,
      4,      3,      2,      1,      0,     -1,     -3,     -4,
     -4,     -4,     -4,     -3,     -1,      0,      1,      2,
      3,      4,      5,      4,      3,      2,      1,      0,
     -2,     -3,     -4,     -5,     -5,     -4,     -3,     -2,
      0,      1,      2,      4,      4,      5,      4,      4,
      2,      1,      0,     -1,     -3,     -4,     -4,     -4,
     -4,     -3,     -2,      0,      1,      2,      3,      4,
      4,      4,      3,      2,      1,      0,     -1,     -3,
     -3,     -4,     -4,     -4,     -3,     -1,      0,      0,
      2,      3,      4,      4,      4,      3,      2,      1,
      0,     -1,     -2,     -3,     -3,     -4,     -3,     -2,
     -1,      0,      0,      1,      2,      3,      3,      3,
      3,      2,      1,      0,     -1,     -2,     -3,     -3,
     -3,     -3,     -2,     -1,      0,      0,      1,      2,
      3,      3,      3,      2,      2,      1,      0,     -1,
     -2,     -2,     -3,     -3,     -3,     -2,     -1,      0
};

#endif
