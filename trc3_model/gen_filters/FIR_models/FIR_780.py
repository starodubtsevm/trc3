#LENGTH_FIR_780 Hz 1000 taps
#fs =  4000 Hz
f_780 = [
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      0,     -1,
      0,      0,      0,      0,     -1,      0,      1,      1,
      0,     -1,      0,      1,      1,      0,     -2,     -1,
      1,      2,      0,     -2,     -1,      1,      2,      0,
     -2,     -2,      0,      3,      1,     -2,     -3,      0,
      3,      2,     -2,     -3,      0,      3,      2,     -1,
     -4,     -1,      3,      3,     -1,     -4,     -1,      3,
      4,      0,     -5,     -2,      3,      5,      0,     -5,
     -3,      3,      6,      1,     -5,     -4,      2,      6,
      2,     -5,     -5,      1,      7,      3,     -4,     -6,
      0,      7,      4,     -4,     -7,      0,      7,      5,
     -3,     -8,     -2,      6,      6,     -2,     -8,     -3,
      6,      7,      0,     -8,     -4,      5,      8,      0,
     -8,     -5,      4,      8,      1,     -7,     -6,      2,
      8,      3,     -6,     -7,      1,      8,      4,     -5,
     -7,      0,      7,      4,     -4,     -7,     -1,      6,
      5,     -2,     -7,     -2,      5,      5,     -1,     -6,
     -2,      4,      5,      0,     -5,     -2,      2,      4,
      0,     -3,     -2,      1,      3,      0,     -2,     -1,
      0,      1,      0,      0,      0,      0,      0,      0,
      0,      1,      0,     -1,     -1,      1,      3,      0,
     -3,     -3,      1,      5,      1,     -4,     -5,      1,
      7,      3,     -5,     -8,      0,      9,      6,     -6,
    -11,     -1,     11,      9,     -5,    -14,     -4,     13,
     13,     -4,    -17,     -7,     13,     17,     -2,    -20,
    -11,     13,     21,      1,    -22,    -16,     11,     25,
      5,    -22,    -21,      9,     28,     10,    -22,    -26,
      5,     31,     16,    -21,    -31,      0,     33,     22,
    -18,    -35,     -5,     33,     28,    -14,    -39,    -11,
     32,     34,     -9,    -41,    -18,     29,     39,     -3,
    -42,    -25,     25,     43,      3,    -42,    -32,     20,
     47,     11,    -40,    -38,     14,     48,     18,    -36,
    -43,      7,     48,     26,    -31,    -47,      0,     47,
     32,    -25,    -49,     -8,     43,     38,    -17,    -50,
    -16,     38,     42,    -10,    -48,    -22,     32,     44,
     -2,    -45,    -28,     25,     44,      5,    -40,    -32,
     18,     43,     11,    -34,    -33,     10,     39,     16,
    -27,    -33,      4,     34,     19,    -20,    -31,     -1,
     28,     19,    -13,    -26,     -5,     20,     18,     -7,
    -20,     -6,     13,     14,     -2,    -12,     -5,      6,
      7,      0,     -4,     -2,      0,      0,      0,      3,
      4,     -3,     -9,     -3,     11,     13,     -4,    -20,
     -9,     17,     24,     -2,    -30,    -19,     20,     37,
      3,    -39,    -31,     21,     50,     12,    -46,    -46,
     17,     63,     25,    -51,    -63,     10,     75,     41,
    -51,    -81,     -1,     85,     61,    -48,    -99,    -17,
     92,     83,    -39,   -115,    -38,     95,    106,    -25,
   -129,    -62,     92,    129,     -6,   -140,    -90,     84,
    152,     17,   -146,   -119,     69,    172,     46,   -146,
   -149,     49,    188,     79,   -140,   -178,     22,    199,
    114,   -127,   -205,    -10,    204,    151,   -106,   -228,
    -47,    202,    187,    -78,   -246,    -88,    192,    222,
    -44,   -258,   -131,    174,    253,     -4,   -262,   -175,
    148,    280,     40,   -258,   -218,    113,    299,     89,
   -244,   -257,     72,    311,    139,   -221,   -292,     25,
    314,    189,   -190,   -321,    -26,    308,    236,   -150,
   -342,    -80,    291,    280,   -103,   -354,   -136,    265,
    318,    -51,   -356,   -190,    229,    348,      5,   -347,
   -242,    185,    370,     64,   -328,   -288,    134,    381,
    124,   -299,   -328,     78,    382,    181,   -261,   -359,
     18,    373,    234,   -214,   -380,    -43,    352,    281,
   -161,   -391,   -103,    321,    321,   -103,   -391,   -161,
    281,    352,    -43,   -380,   -214,    234,    373,     18,
   -359,   -261,    181,    382,     78,   -328,   -299,    124,
    381,    134,   -288,   -328,     64,    370,    185,   -242,
   -347,      5,    348,    229,   -190,   -356,    -51,    318,
    265,   -136,   -354,   -103,    280,    291,    -80,   -342,
   -150,    236,    308,    -26,   -321,   -190,    189,    314,
     25,   -292,   -221,    139,    311,     72,   -257,   -244,
     89,    299,    113,   -218,   -258,     40,    280,    148,
   -175,   -262,     -4,    253,    174,   -131,   -258,    -44,
    222,    192,    -88,   -246,    -78,    187,    202,    -47,
   -228,   -106,    151,    204,    -10,   -205,   -127,    114,
    199,     22,   -178,   -140,     79,    188,     49,   -149,
   -146,     46,    172,     69,   -119,   -146,     17,    152,
     84,    -90,   -140,     -6,    129,     92,    -62,   -129,
    -25,    106,     95,    -38,   -115,    -39,     83,     92,
    -17,    -99,    -48,     61,     85,     -1,    -81,    -51,
     41,     75,     10,    -63,    -51,     25,     63,     17,
    -46,    -46,     12,     50,     21,    -31,    -39,      3,
     37,     20,    -19,    -30,     -2,     24,     17,     -9,
    -20,     -4,     13,     11,     -3,     -9,     -3,      4,
      3,      0,      0,      0,     -2,     -4,      0,      7,
      6,     -5,    -12,     -2,     14,     13,     -6,    -20,
     -7,     18,     20,     -5,    -26,    -13,     19,     28,
     -1,    -31,    -20,     19,     34,      4,    -33,    -27,
     16,     39,     10,    -33,    -34,     11,     43,     18,
    -32,    -40,      5,     44,     25,    -28,    -45,     -2,
     44,     32,    -22,    -48,    -10,     42,     38,    -16,
    -50,    -17,     38,     43,     -8,    -49,    -25,     32,
     47,      0,    -47,    -31,     26,     48,      7,    -43,
    -36,     18,     48,     14,    -38,    -40,     11,     47,
     20,    -32,    -42,      3,     43,     25,    -25,    -42,
     -3,     39,     29,    -18,    -41,     -9,     34,     32,
    -11,    -39,    -14,     28,     33,     -5,    -35,    -18,
     22,     33,      0,    -31,    -21,     16,     31,      5,
    -26,    -22,     10,     28,      9,    -21,    -22,      5,
     25,     11,    -16,    -22,      1,     21,     13,    -11,
    -20,     -2,     17,     13,     -7,    -17,     -4,     13,
     13,     -4,    -14,     -5,      9,     11,     -1,    -11,
     -6,      6,      9,      0,     -8,     -5,      3,      7,
      1,     -5,     -4,      1,      5,      1,     -3,     -3,
      0,      3,      1,     -1,     -1,      0,      1,      0,
      0,      0,      0,      0,      0,      0,      1,      0,
     -1,     -2,      0,      3,      1,     -2,     -3,      0,
      4,      2,     -2,     -5,      0,      5,      4,     -2,
     -6,     -1,      5,      5,     -2,     -7,     -2,      5,
      6,     -1,     -7,     -4,      4,      7,      0,     -7,
     -5,      4,      8,      1,     -7,     -6,      3,      8,
      2,     -6,     -7,      1,      8,      4,     -5,     -8,
      0,      8,      5,     -4,     -8,      0,      7,      6,
     -3,     -8,     -2,      6,      6,     -2,     -8,     -3,
      5,      7,      0,     -7,     -4,      4,      7,      0,
     -6,     -4,      3,      7,      1,     -5,     -5,      2,
      6,      2,     -4,     -5,      1,      6,      3,     -3,
     -5,      0,      5,      3,     -2,     -5,      0,      4,
      3,     -1,     -4,     -1,      3,      3,     -1,     -4,
     -1,      2,      3,      0,     -3,     -2,      2,      3,
      0,     -3,     -2,      1,      3,      0,     -2,     -2,
      0,      2,      1,     -1,     -2,      0,      2,      1,
     -1,     -2,      0,      1,      1,      0,     -1,      0,
      1,      1,      0,     -1,      0,      0,      0,      0,
     -1,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      0,      0
]