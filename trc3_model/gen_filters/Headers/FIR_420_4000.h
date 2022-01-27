#ifndef __FIR_420_H__
#define __FIR_420_H__

#define LENGTH_FIR_420    1000

static fract16 fir420coeff[LENGTH_FIR_420] =
{
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      0,     -1,     -1,      0,      0,      0,      1,
      1,      0,      0,     -1,     -1,     -1,      0,      0,
      1,      2,      1,      0,     -1,     -2,     -2,     -1,
      0,      1,      3,      2,      1,      0,     -2,     -3,
     -3,     -1,      1,      3,      4,      3,      0,     -2,
     -4,     -4,     -2,      0,      2,      4,      4,      2,
      0,     -3,     -5,     -4,     -1,      1,      4,      5,
      4,      1,     -2,     -5,     -6,     -4,      0,      3,
      6,      6,      3,      0,     -4,     -7,     -6,     -2,
      1,      6,      7,      6,      1,     -3,     -7,     -7,
     -5,      0,      4,      7,      7,      4,      0,     -5,
     -8,     -7,     -3,      2,      6,      8,      6,      2,
     -3,     -7,     -8,     -6,      0,      4,      8,      8,
      4,      0,     -5,     -8,     -7,     -3,      1,      6,
      8,      6,      2,     -2,     -6,     -7,     -5,     -1,
      3,      6,      6,      4,      0,     -4,     -6,     -5,
     -2,      1,      4,      5,      4,      1,     -1,     -3,
     -4,     -3,      0,      1,      2,      2,      1,      0,
     -1,     -1,     -1,      0,      0,      0,      0,      0,
      0,      0,      1,      1,      1,      0,     -1,     -3,
     -3,     -2,      0,      3,      5,      5,      3,      0,
     -5,     -8,     -7,     -3,      2,      8,     10,      8,
      2,     -5,    -11,    -13,     -9,     -1,      8,     15,
     15,      9,     -1,    -12,    -18,    -17,     -8,      4,
     16,     21,     18,      6,     -9,    -21,    -24,    -17,
     -2,     14,     25,     26,     16,     -1,    -19,    -30,
    -28,    -14,      6,     25,     33,     28,     10,    -12,
    -30,    -36,    -26,     -5,     18,     35,     38,     23,
      0,    -25,    -40,    -38,    -19,      7,     32,     43,
     37,     14,    -14,    -38,    -45,    -34,     -8,     22,
     43,     46,     30,      0,    -29,    -47,    -45,    -24,
      6,     35,     49,     42,     17,    -14,    -41,    -50,
    -38,    -10,     22,     45,     49,     32,      2,    -28,
    -47,    -46,    -25,      5,     34,     48,     42,     18,
    -12,    -38,    -47,    -36,    -10,     18,     39,     43,
     29,      3,    -23,    -39,    -39,    -22,      3,     26,
     37,     33,     15,     -8,    -27,    -33,    -26,     -8,
     11,     25,     27,     18,      2,    -12,    -21,    -20,
    -11,      0,     11,     15,     13,      5,     -2,     -7,
     -8,     -5,     -1,      1,      1,      0,     -1,      0,
      2,      7,      9,      7,      0,     -9,    -17,    -18,
    -10,      4,     19,     28,     26,     10,    -11,    -32,
    -40,    -31,     -7,     22,     46,     51,     34,      0,
    -36,    -61,    -61,    -34,     10,     53,     77,     68,
     29,    -25,    -72,    -91,    -71,    -19,     44,     93,
    104,     71,      5,    -66,   -113,   -113,    -65,     14,
     91,    132,    119,     53,    -37,   -117,   -150,   -119,
    -36,     65,    144,    163,    114,     13,    -96,   -169,
   -172,   -102,     14,    129,    192,    175,     83,    -47,
   -162,   -211,   -171,    -57,     84,    195,    225,    160,
     25,   -124,   -225,   -233,   -142,     11,    164,    250,
    232,    115,    -53,   -204,   -271,   -224,    -81,     99,
    241,    284,    207,     41,   -146,   -274,   -289,   -181,
      4,    192,    302,    285,    148,    -54,   -237,   -322,
   -272,   -106,    107,    278,    334,    250,     58,   -160,
   -314,   -337,   -218,     -5,    211,    342,    329,    177,
    -50,   -260,   -361,   -311,   -129,    108,    302,    371,
    283,     75,   -165,   -338,   -370,   -246,    -17,    219,
    366,    359,    201,    -42,   -269,   -383,   -337,   -148,
    102,    312,    390,    305,     91,   -161,   -346,   -386,
   -264,    -30,    215,    372,    372,    215,    -30,   -264,
   -386,   -346,   -161,     91,    305,    390,    312,    102,
   -148,   -337,   -383,   -269,    -42,    201,    359,    366,
    219,    -17,   -246,   -370,   -338,   -165,     75,    283,
    371,    302,    108,   -129,   -311,   -361,   -260,    -50,
    177,    329,    342,    211,     -5,   -218,   -337,   -314,
   -160,     58,    250,    334,    278,    107,   -106,   -272,
   -322,   -237,    -54,    148,    285,    302,    192,      4,
   -181,   -289,   -274,   -146,     41,    207,    284,    241,
     99,    -81,   -224,   -271,   -204,    -53,    115,    232,
    250,    164,     11,   -142,   -233,   -225,   -124,     25,
    160,    225,    195,     84,    -57,   -171,   -211,   -162,
    -47,     83,    175,    192,    129,     14,   -102,   -172,
   -169,    -96,     13,    114,    163,    144,     65,    -36,
   -119,   -150,   -117,    -37,     53,    119,    132,     91,
     14,    -65,   -113,   -113,    -66,      5,     71,    104,
     93,     44,    -19,    -71,    -91,    -72,    -25,     29,
     68,     77,     53,     10,    -34,    -61,    -61,    -36,
      0,     34,     51,     46,     22,     -7,    -31,    -40,
    -32,    -11,     10,     26,     28,     19,      4,    -10,
    -18,    -17,     -9,      0,      7,      9,      7,      2,
      0,     -1,      0,      1,      1,     -1,     -5,     -8,
     -7,     -2,      5,     13,     15,     11,      0,    -11,
    -20,    -21,    -12,      2,     18,     27,     25,     11,
     -8,    -26,    -33,    -27,     -8,     15,     33,     37,
     26,      3,    -22,    -39,    -39,    -23,      3,     29,
     43,     39,     18,    -10,    -36,    -47,    -38,    -12,
     18,     42,     48,     34,      5,    -25,    -46,    -47,
    -28,      2,     32,     49,     45,     22,    -10,    -38,
    -50,    -41,    -14,     17,     42,     49,     35,      6,
    -24,    -45,    -47,    -29,      0,     30,     46,     43,
     22,     -8,    -34,    -45,    -38,    -14,     14,     37,
     43,     32,      7,    -19,    -38,    -40,    -25,      0,
     23,     38,     35,     18,     -5,    -26,    -36,    -30,
    -12,     10,     28,     33,     25,      6,    -14,    -28,
    -30,    -19,     -1,     16,     26,     25,     14,     -2,
    -17,    -24,    -21,     -9,      6,     18,     21,     16,
      4,     -8,    -17,    -18,    -12,     -1,      9,     15,
     15,      8,     -1,     -9,    -13,    -11,     -5,      2,
      8,     10,      8,      2,     -3,     -7,     -8,     -5,
      0,      3,      5,      5,      3,      0,     -2,     -3,
     -3,     -1,      0,      1,      1,      1,      0,      0,
      0,      0,      0,      0,      0,     -1,     -1,     -1,
      0,      1,      2,      2,      1,      0,     -3,     -4,
     -3,     -1,      1,      4,      5,      4,      1,     -2,
     -5,     -6,     -4,      0,      4,      6,      6,      3,
     -1,     -5,     -7,     -6,     -2,      2,      6,      8,
      6,      1,     -3,     -7,     -8,     -5,      0,      4,
      8,      8,      4,      0,     -6,     -8,     -7,     -3,
      2,      6,      8,      6,      2,     -3,     -7,     -8,
     -5,      0,      4,      7,      7,      4,      0,     -5,
     -7,     -7,     -3,      1,      6,      7,      6,      1,
     -2,     -6,     -7,     -4,      0,      3,      6,      6,
      3,      0,     -4,     -6,     -5,     -2,      1,      4,
      5,      4,      1,     -1,     -4,     -5,     -3,      0,
      2,      4,      4,      2,      0,     -2,     -4,     -4,
     -2,      0,      3,      4,      3,      1,     -1,     -3,
     -3,     -2,      0,      1,      2,      3,      1,      0,
     -1,     -2,     -2,     -1,      0,      1,      2,      1,
      0,      0,     -1,     -1,     -1,      0,      0,      1,
      1,      0,      0,      0,     -1,     -1,      0,      0,
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      0,      0
};

#endif
