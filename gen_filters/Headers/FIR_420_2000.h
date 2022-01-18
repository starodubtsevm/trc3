#ifndef __FIR_420_H__
#define __FIR_420_H__

#define LENGTH_FIR_420    1000

static fract16 fir420coeff[LENGTH_FIR_420] =
{
      0,      0,      0,      0,      0,      0,      0,      0,
      0,     -1,      0,      1,      1,      0,     -1,      0,
      2,      0,     -1,     -2,      0,      2,      0,     -2,
     -1,      1,      2,      0,     -3,     -1,      2,      2,
     -1,     -3,      0,      3,      2,     -2,     -3,      1,
      4,      0,     -3,     -2,      2,      4,      0,     -4,
     -1,      3,      3,     -1,     -4,      0,      4,      2,
     -2,     -3,      0,      4,      1,     -3,     -2,      1,
      3,      0,     -3,     -1,      2,      2,      0,     -2,
      0,      2,      1,     -1,     -1,      0,      1,      0,
      0,      0,      0,      0,      0,      0,      0,      0,
     -1,      0,      2,      0,     -2,     -1,      1,      3,
      0,     -4,     -1,      3,      4,     -2,     -5,      0,
      6,      3,     -4,     -6,      1,      8,      2,     -7,
     -6,      4,      9,      0,     -9,     -4,      7,      9,
     -3,    -11,     -1,     10,      7,     -7,    -11,      1,
     12,      4,    -10,     -9,      5,     12,      0,    -11,
     -6,      8,     10,     -3,    -11,     -2,     10,      7,
     -6,    -10,      0,     10,      3,     -7,     -7,      3,
      8,      0,     -7,     -3,      4,      5,     -1,     -4,
     -1,      3,      2,     -1,     -1,      0,      0,      0,
      1,      1,      0,     -3,      0,      4,      3,     -4,
     -7,      1,      9,      3,     -9,     -9,      5,     13,
      0,    -14,     -8,     12,     15,     -5,    -19,     -4,
     18,     14,    -12,    -21,      2,     24,     10,    -20,
    -20,     10,     27,      2,    -26,    -16,     19,     26,
     -6,    -30,     -8,     26,     21,    -15,    -29,      0,
     30,     14,    -23,    -25,     10,     29,      4,    -26,
    -17,     17,     25,     -4,    -26,     -8,     20,     18,
    -10,    -21,      0,     19,      9,    -12,    -14,      4,
     14,      2,    -10,     -6,      4,      6,      0,     -4,
      0,      0,      0,      1,      4,      0,     -7,     -5,
      7,     11,     -3,    -17,     -5,     18,     16,    -12,
    -25,      0,     29,     14,    -25,    -29,     12,     39,
      6,    -39,    -27,     28,     44,     -7,    -51,    -17,
     44,     41,    -25,    -56,     -1,     58,     31,    -44,
    -54,     17,     65,     14,    -59,    -44,     37,     63,
     -6,    -66,    -26,     53,     53,    -26,    -65,     -6,
     61,     36,    -42,    -56,     13,     60,     16,    -49,
    -39,     27,     50,     -1,    -47,    -21,     33,     34,
    -13,    -37,     -5,     29,     17,    -15,    -21,      3,
     16,      4,     -8,     -4,      1,      0,      0,      7,
      6,    -11,    -16,      6,     27,      6,    -31,    -26,
     24,     44,     -4,    -55,    -23,     50,     53,    -28,
    -75,     -7,     79,     49,    -60,    -85,     21,    102,
     29,    -94,    -80,     59,    114,     -3,   -122,    -58,
     98,    110,    -46,   -137,    -21,    130,     88,    -88,
   -134,     23,    147,     50,   -123,   -112,     68,    146,
      4,   -142,    -75,    103,    125,    -40,   -142,    -30,
    122,     89,    -74,   -121,     11,    120,     46,    -90,
    -86,     41,     98,      8,    -83,    -46,     50,     62,
    -13,    -57,    -13,     36,     24,    -13,    -17,      0,
      1,     -3,     12,     21,    -12,    -45,     -8,     60,
     46,    -53,    -89,     17,    119,     44,   -118,   -116,
     75,    174,      5,   -194,   -109,    161,    206,    -70,
   -265,    -60,    259,    201,   -178,   -310,     32,    351,
    146,   -301,   -311,    161,    414,     40,   -418,   -257,
    310,    429,   -107,   -506,   -144,    456,    383,   -281,
   -542,     18,    573,    271,   -456,   -511,    213,    636,
    101,   -603,   -408,    414,    627,   -108,   -697,   -239,
    591,    541,   -330,   -717,    -23,    716,    382,   -534,
   -655,    213,    768,    168,   -691,   -514,    438,    736,
    -73,   -775,   -312,    621,    621,   -312,   -775,    -73,
    736,    438,   -514,   -691,    168,    768,    213,   -655,
   -534,    382,    716,    -23,   -717,   -330,    541,    591,
   -239,   -697,   -108,    627,    414,   -408,   -603,    101,
    636,    213,   -511,   -456,    271,    573,     18,   -542,
   -281,    383,    456,   -144,   -506,   -107,    429,    310,
   -257,   -418,     40,    414,    161,   -311,   -301,    146,
    351,     32,   -310,   -178,    201,    259,    -60,   -265,
    -70,    206,    161,   -109,   -194,      5,    174,     75,
   -116,   -118,     44,    119,     17,    -89,    -53,     46,
     60,     -8,    -45,    -12,     21,     12,     -3,      1,
      0,    -17,    -13,     24,     36,    -13,    -57,    -13,
     62,     50,    -46,    -83,      8,     98,     41,    -86,
    -90,     46,    120,     11,   -121,    -74,     89,    122,
    -30,   -142,    -40,    125,    103,    -75,   -142,      4,
    146,     68,   -112,   -123,     50,    147,     23,   -134,
    -88,     88,    130,    -21,   -137,    -46,    110,     98,
    -58,   -122,     -3,    114,     59,    -80,    -94,     29,
    102,     21,    -85,    -60,     49,     79,     -7,    -75,
    -28,     53,     50,    -23,    -55,     -4,     44,     24,
    -26,    -31,      6,     27,      6,    -16,    -11,      6,
      7,      0,      0,      1,     -4,     -8,      4,     16,
      3,    -21,    -15,     17,     29,     -5,    -37,    -13,
     34,     33,    -21,    -47,     -1,     50,     27,    -39,
    -49,     16,     60,     13,    -56,    -42,     36,     61,
     -6,    -65,    -26,     53,     53,    -26,    -66,     -6,
     63,     37,    -44,    -59,     14,     65,     17,    -54,
    -44,     31,     58,     -1,    -56,    -25,     41,     44,
    -17,    -51,     -7,     44,     28,    -27,    -39,      6,
     39,     12,    -29,    -25,     14,     29,      0,    -25,
    -12,     16,     18,     -5,    -17,     -3,     11,      7,
     -5,     -7,      0,      4,      1,      0,      0,      0,
     -4,      0,      6,      4,     -6,    -10,      2,     14,
      4,    -14,    -12,      9,     19,      0,    -21,    -10,
     18,     20,     -8,    -26,     -4,     25,     17,    -17,
    -26,      4,     29,     10,    -25,    -23,     14,     30,
      0,    -29,    -15,     21,     26,     -8,    -30,     -6,
     26,     19,    -16,    -26,      2,     27,     10,    -20,
    -20,     10,     24,      2,    -21,    -12,     14,     18,
     -4,    -19,     -5,     15,     12,     -8,    -14,      0,
     13,      5,     -9,     -9,      3,      9,      1,     -7,
     -4,      3,      4,      0,     -3,      0,      1,      1,
      0,      0,      0,     -1,     -1,      2,      3,     -1,
     -4,     -1,      5,      4,     -3,     -7,      0,      8,
      3,     -7,     -7,      3,     10,      0,    -10,     -6,
      7,     10,     -2,    -11,     -3,     10,      8,     -6,
    -11,      0,     12,      5,     -9,    -10,      4,     12,
      1,    -11,     -7,      7,     10,     -1,    -11,     -3,
      9,      7,     -4,     -9,      0,      9,      4,     -6,
     -7,      2,      8,      1,     -6,     -4,      3,      6,
      0,     -5,     -2,      4,      3,     -1,     -4,      0,
      3,      1,     -1,     -2,      0,      2,      0,     -1,
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      1,      0,     -1,     -1,      1,      2,      0,
     -2,      0,      2,      2,     -1,     -3,      0,      3,
      1,     -2,     -3,      1,      4,      0,     -3,     -2,
      2,      4,      0,     -4,     -1,      3,      3,     -1,
     -4,      0,      4,      2,     -2,     -3,      0,      4,
      1,     -3,     -2,      2,      3,      0,     -3,     -1,
      2,      2,     -1,     -3,      0,      2,      1,     -1,
     -2,      0,      2,      0,     -2,     -1,      0,      2,
      0,     -1,      0,      1,      1,      0,     -1,      0,
      0,      0,      0,      0,      0,      0,      0,      0
};

#endif
