#LENGTH_FIR_565 Hz 1000 taps
#fs =  8000 Hz
f_565 = [
      0,      0,     -2,     -3,     -3,     -3,     -2,      0,
      0,      2,      3,      3,      3,      2,      0,      0,
     -2,     -3,     -3,     -3,     -2,      0,      0,      2,
      3,      3,      3,      2,      1,      0,     -2,     -3,
     -3,     -3,     -2,     -1,      0,      2,      3,      3,
      3,      2,      1,      0,     -1,     -3,     -4,     -4,
     -3,     -1,      0,      1,      3,      4,      4,      3,
      1,      0,     -1,     -3,     -4,     -4,     -3,     -2,
      0,      1,      3,      4,      4,      3,      2,      0,
     -1,     -3,     -4,     -4,     -4,     -2,      0,      1,
      3,      4,      4,      4,      2,      0,     -1,     -3,
     -4,     -5,     -4,     -3,      0,      1,      3,      4,
      5,      4,      3,      1,     -1,     -3,     -4,     -5,
     -4,     -3,     -1,      0,      2,      4,      5,      4,
      3,      1,      0,     -2,     -4,     -4,     -4,     -3,
     -1,      0,      2,      3,      4,      4,      3,      1,
      0,     -2,     -3,     -4,     -3,     -3,     -1,      0,
      1,      3,      3,      3,      2,      1,      0,     -1,
     -2,     -2,     -2,     -2,     -1,      0,      0,      1,
      2,      2,      1,      0,      0,      0,      0,     -1,
     -1,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      1,      1,      1,
      1,      0,      0,     -1,     -2,     -3,     -3,     -2,
      0,      1,      2,      4,      5,      4,      3,      1,
     -1,     -3,     -6,     -7,     -6,     -5,     -2,      1,
      5,      7,      9,      9,      6,      3,     -1,     -6,
     -9,    -11,    -11,     -9,     -4,      1,      7,     11,
     14,     14,     11,      5,     -1,     -8,    -14,    -17,
    -17,    -14,     -7,      0,      9,     16,     20,     21,
     17,      9,      0,    -10,    -18,    -24,    -24,    -20,
    -12,     -1,     10,     20,     27,     28,     24,     15,
      2,    -11,    -23,    -31,    -33,    -28,    -18,     -3,
     11,     25,     34,     37,     32,     21,      5,    -11,
    -27,    -38,    -42,    -37,    -25,     -8,     11,     29,
     42,     47,     42,     29,     10,    -11,    -31,    -46,
    -52,    -48,    -34,    -13,     10,     33,     50,     57,
     53,     39,     17,     -9,    -34,    -53,    -62,    -59,
    -44,    -20,      7,     35,     57,     68,     66,     50,
     25,     -6,    -36,    -60,    -73,    -72,    -56,    -29,
      3,     37,     64,     79,     78,     63,     34,     -1,
    -37,    -67,    -84,    -85,    -69,    -40,     -1,     37,
     70,     89,     92,     76,     45,      5,    -36,    -72,
    -94,    -98,    -83,    -52,     -9,     35,     74,     99,
    105,     91,     58,     13,    -34,    -76,   -104,   -112,
    -98,    -65,    -18,     32,     77,    108,    118,    105,
     72,     23,    -29,    -78,   -112,   -125,   -113,    -79,
    -29,     26,     78,    116,    131,    120,     86,     35,
    -23,    -78,   -119,   -136,   -128,    -94,    -41,     19,
     77,    121,    142,    135,    102,     48,    -15,    -76,
   -123,   -147,   -142,   -109,    -55,     10,     74,    125,
    152,    149,    117,     62,     -5,    -72,   -126,   -156,
   -155,   -125,    -69,      0,     69,    126,    159,    161,
    132,     77,      6,    -66,   -126,   -162,   -167,   -139,
    -84,    -12,     62,    125,    165,    172,    146,     92,
     18,    -58,   -124,   -167,   -177,   -153,    -99,    -25,
     53,    122,    168,    181,    159,    106,     32,    -48,
   -120,   -168,   -185,   -165,   -113,    -39,     42,    116,
    168,    188,    171,    120,     46,    -36,   -113,   -168,
   -190,   -176,   -127,    -53,     30,    109,    166,    192,
    180,    133,     60,    -23,   -104,   -164,   -193,   -184,
   -139,    -67,     17,     99,    161,    193,    187,    145,
     74,    -10,    -93,   -158,   -192,   -189,   -150,    -81,
      3,     87,    154,    191,    191,    154,     87,      3,
    -81,   -150,   -189,   -192,   -158,    -93,    -10,     74,
    145,    187,    193,    161,     99,     17,    -67,   -139,
   -184,   -193,   -164,   -104,    -23,     60,    133,    180,
    192,    166,    109,     30,    -53,   -127,   -176,   -190,
   -168,   -113,    -36,     46,    120,    171,    188,    168,
    116,     42,    -39,   -113,   -165,   -185,   -168,   -120,
    -48,     32,    106,    159,    181,    168,    122,     53,
    -25,    -99,   -153,   -177,   -167,   -124,    -58,     18,
     92,    146,    172,    165,    125,     62,    -12,    -84,
   -139,   -167,   -162,   -126,    -66,      6,     77,    132,
    161,    159,    126,     69,      0,    -69,   -125,   -155,
   -156,   -126,    -72,     -5,     62,    117,    149,    152,
    125,     74,     10,    -55,   -109,   -142,   -147,   -123,
    -76,    -15,     48,    102,    135,    142,    121,     77,
     19,    -41,    -94,   -128,   -136,   -119,    -78,    -23,
     35,     86,    120,    131,    116,     78,     26,    -29,
    -79,   -113,   -125,   -112,    -78,    -29,     23,     72,
    105,    118,    108,     77,     32,    -18,    -65,    -98,
   -112,   -104,    -76,    -34,     13,     58,     91,    105,
     99,     74,     35,     -9,    -52,    -83,    -98,    -94,
    -72,    -36,      5,     45,     76,     92,     89,     70,
     37,     -1,    -40,    -69,    -85,    -84,    -67,    -37,
     -1,     34,     63,     78,     79,     64,     37,      3,
    -29,    -56,    -72,    -73,    -60,    -36,     -6,     25,
     50,     66,     68,     57,     35,      7,    -20,    -44,
    -59,    -62,    -53,    -34,     -9,     17,     39,     53,
     57,     50,     33,     10,    -13,    -34,    -48,    -52,
    -46,    -31,    -11,     10,     29,     42,     47,     42,
     29,     11,     -8,    -25,    -37,    -42,    -38,    -27,
    -11,      5,     21,     32,     37,     34,     25,     11,
     -3,    -18,    -28,    -33,    -31,    -23,    -11,      2,
     15,     24,     28,     27,     20,     10,     -1,    -12,
    -20,    -24,    -24,    -18,    -10,      0,      9,     17,
     21,     20,     16,      9,      0,     -7,    -14,    -17,
    -17,    -14,     -8,     -1,      5,     11,     14,     14,
     11,      7,      1,     -4,     -9,    -11,    -11,     -9,
     -6,     -1,      3,      6,      9,      9,      7,      5,
      1,     -2,     -5,     -6,     -7,     -6,     -3,     -1,
      1,      3,      4,      5,      4,      2,      1,      0,
     -2,     -3,     -3,     -2,     -1,      0,      0,      1,
      1,      1,      1,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      0,     -1,
     -1,      0,      0,      0,      0,      1,      2,      2,
      1,      0,      0,     -1,     -2,     -2,     -2,     -2,
     -1,      0,      1,      2,      3,      3,      3,      1,
      0,     -1,     -3,     -3,     -4,     -3,     -2,      0,
      1,      3,      4,      4,      3,      2,      0,     -1,
     -3,     -4,     -4,     -4,     -2,      0,      1,      3,
      4,      5,      4,      2,      0,     -1,     -3,     -4,
     -5,     -4,     -3,     -1,      1,      3,      4,      5,
      4,      3,      1,      0,     -3,     -4,     -5,     -4,
     -3,     -1,      0,      2,      4,      4,      4,      3,
      1,      0,     -2,     -4,     -4,     -4,     -3,     -1,
      0,      2,      3,      4,      4,      3,      1,      0,
     -2,     -3,     -4,     -4,     -3,     -1,      0,      1,
      3,      4,      4,      3,      1,      0,     -1,     -3,
     -4,     -4,     -3,     -1,      0,      1,      2,      3,
      3,      3,      2,      0,     -1,     -2,     -3,     -3,
     -3,     -2,      0,      1,      2,      3,      3,      3,
      2,      0,      0,     -2,     -3,     -3,     -3,     -2,
      0,      0,      2,      3,      3,      3,      2,      0,
      0,     -2,     -3,     -3,     -3,     -2,      0,      0
]