#LENGTH_FIR_480 Hz 1000 taps
#fs =  8000 Hz
f_480 = [
     -3,     -2,     -1,      0,      0,      1,      2,      3,
      3,      3,      2,      1,      0,     -1,     -2,     -3,
     -3,     -3,     -2,     -1,      0,      0,      2,      3,
      3,      3,      3,      2,      0,      0,     -1,     -2,
     -3,     -3,     -3,     -2,     -1,      0,      1,      2,
      3,      3,      3,      3,      1,      0,     -1,     -2,
     -3,     -4,     -4,     -3,     -2,     -1,      0,      2,
      3,      4,      4,      4,      3,      1,      0,     -1,
     -3,     -4,     -4,     -4,     -3,     -2,      0,      1,
      2,      4,      4,      4,      4,      2,      1,      0,
     -2,     -3,     -4,     -4,     -4,     -3,     -1,      0,
      1,      3,      4,      5,      4,      3,      2,      0,
     -1,     -3,     -4,     -5,     -5,     -4,     -3,     -1,
      0,      2,      3,      4,      5,      4,      3,      1,
      0,     -1,     -3,     -4,     -4,     -4,     -3,     -2,
      0,      1,      2,      3,      4,      4,      3,      2,
      1,      0,     -2,     -3,     -3,     -4,     -3,     -2,
     -1,      0,      1,      2,      3,      3,      3,      2,
      1,      0,      0,     -1,     -2,     -2,     -2,     -1,
     -1,      0,      0,      0,      1,      1,      1,      1,
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,     -1,     -1,     -1,
     -1,     -1,      0,      0,      1,      2,      3,      3,
      3,      2,      1,      0,     -1,     -3,     -5,     -5,
     -5,     -4,     -3,      0,      1,      4,      6,      8,
      8,      7,      5,      2,     -1,     -5,     -8,    -10,
    -11,    -10,     -8,     -4,      0,      4,      9,     12,
     14,     14,     12,      7,      2,     -4,    -10,    -15,
    -17,    -18,    -16,    -11,     -5,      2,     10,     16,
     21,     22,     20,     16,      8,      0,     -9,    -17,
    -23,    -26,    -26,    -21,    -13,     -3,      7,     17,
     26,     30,     31,     27,     19,      8,     -4,    -16,
    -27,    -34,    -37,    -34,    -26,    -14,      0,     14,
     28,     37,     42,     40,     33,     21,      5,    -11,
    -27,    -39,    -47,    -47,    -41,    -29,    -12,      6,
     25,     40,     51,     54,     50,     38,     20,      0,
    -21,    -40,    -54,    -60,    -58,    -48,    -30,     -8,
     16,     38,     56,     66,     66,     58,     40,     17,
     -8,    -34,    -56,    -70,    -74,    -68,    -52,    -28,
      0,     29,     54,     72,     81,     78,     64,     40,
     10,    -21,    -50,    -73,    -86,    -87,    -76,    -53,
    -22,     11,     45,     72,     90,     96,     88,     67,
     36,      0,    -37,    -69,    -92,   -103,    -99,    -81,
    -51,    -13,     26,     64,     92,    108,    109,     95,
     66,     28,    -14,    -55,    -90,   -112,   -118,   -108,
    -82,    -44,      0,     45,     85,    113,    125,    120,
     98,     61,     16,    -32,    -77,   -111,   -130,   -131,
   -113,    -79,    -33,     17,     66,    107,    132,    140,
    127,     97,     52,      0,    -53,    -99,   -132,   -146,
   -140,   -114,    -72,    -18,     37,     89,    128,    150,
    151,    130,     91,     38,    -19,    -76,   -122,   -151,
   -159,   -145,   -110,    -59,      0,     60,    112,    149,
    165,    158,    128,     80,     21,    -42,    -99,   -144,
   -168,   -168,   -145,   -101,    -43,     21,     84,    135,
    167,    176,    160,    121,     65,      0,    -66,   -123,
   -163,   -180,   -172,   -140,    -87,    -22,     45,    108,
    155,    181,    182,    156,    109,     46,    -23,    -90,
   -144,   -179,   -188,   -171,   -129,    -69,      0,     70,
    130,    172,    191,    182,    147,     92,     24,    -47,
   -113,   -163,   -190,   -190,   -163,   -114,    -48,     24,
     93,    150,    185,    194,    176,    133,     72,      0,
    -72,   -134,   -177,   -195,   -186,   -151,    -94,    -24,
     48,    115,    165,    193,    193,    165,    115,     48,
    -24,    -94,   -151,   -186,   -195,   -177,   -134,    -72,
      0,     72,    133,    176,    194,    185,    150,     93,
     24,    -48,   -114,   -163,   -190,   -190,   -163,   -113,
    -47,     24,     92,    147,    182,    191,    172,    130,
     70,      0,    -69,   -129,   -171,   -188,   -179,   -144,
    -90,    -23,     46,    109,    156,    182,    181,    155,
    108,     45,    -22,    -87,   -140,   -172,   -180,   -163,
   -123,    -66,      0,     65,    121,    160,    176,    167,
    135,     84,     21,    -43,   -101,   -145,   -168,   -168,
   -144,    -99,    -42,     21,     80,    128,    158,    165,
    149,    112,     60,      0,    -59,   -110,   -145,   -159,
   -151,   -122,    -76,    -19,     38,     91,    130,    151,
    150,    128,     89,     37,    -18,    -72,   -114,   -140,
   -146,   -132,    -99,    -53,      0,     52,     97,    127,
    140,    132,    107,     66,     17,    -33,    -79,   -113,
   -131,   -130,   -111,    -77,    -32,     16,     61,     98,
    120,    125,    113,     85,     45,      0,    -44,    -82,
   -108,   -118,   -112,    -90,    -55,    -14,     28,     66,
     95,    109,    108,     92,     64,     26,    -13,    -51,
    -81,    -99,   -103,    -92,    -69,    -37,      0,     36,
     67,     88,     96,     90,     72,     45,     11,    -22,
    -53,    -76,    -87,    -86,    -73,    -50,    -21,     10,
     40,     64,     78,     81,     72,     54,     29,      0,
    -28,    -52,    -68,    -74,    -70,    -56,    -34,     -8,
     17,     40,     58,     66,     66,     56,     38,     16,
     -8,    -30,    -48,    -58,    -60,    -54,    -40,    -21,
      0,     20,     38,     50,     54,     51,     40,     25,
      6,    -12,    -29,    -41,    -47,    -47,    -39,    -27,
    -11,      5,     21,     33,     40,     42,     37,     28,
     14,      0,    -14,    -26,    -34,    -37,    -34,    -27,
    -16,     -4,      8,     19,     27,     31,     30,     26,
     17,      7,     -3,    -13,    -21,    -26,    -26,    -23,
    -17,     -9,      0,      8,     16,     20,     22,     21,
     16,     10,      2,     -5,    -11,    -16,    -18,    -17,
    -15,    -10,     -4,      2,      7,     12,     14,     14,
     12,      9,      4,      0,     -4,     -8,    -10,    -11,
    -10,     -8,     -5,     -1,      2,      5,      7,      8,
      8,      6,      4,      1,      0,     -3,     -4,     -5,
     -5,     -5,     -3,     -1,      0,      1,      2,      3,
      3,      3,      2,      1,      0,      0,     -1,     -1,
     -1,     -1,     -1,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      0,      0,
      1,      1,      1,      1,      0,      0,      0,     -1,
     -1,     -2,     -2,     -2,     -1,      0,      0,      1,
      2,      3,      3,      3,      2,      1,      0,     -1,
     -2,     -3,     -4,     -3,     -3,     -2,      0,      1,
      2,      3,      4,      4,      3,      2,      1,      0,
     -2,     -3,     -4,     -4,     -4,     -3,     -1,      0,
      1,      3,      4,      5,      4,      3,      2,      0,
     -1,     -3,     -4,     -5,     -5,     -4,     -3,     -1,
      0,      2,      3,      4,      5,      4,      3,      1,
      0,     -1,     -3,     -4,     -4,     -4,     -3,     -2,
      0,      1,      2,      4,      4,      4,      4,      2,
      1,      0,     -2,     -3,     -4,     -4,     -4,     -3,
     -1,      0,      1,      3,      4,      4,      4,      3,
      2,      0,     -1,     -2,     -3,     -4,     -4,     -3,
     -2,     -1,      0,      1,      3,      3,      3,      3,
      2,      1,      0,     -1,     -2,     -3,     -3,     -3,
     -2,     -1,      0,      0,      2,      3,      3,      3,
      3,      2,      0,      0,     -1,     -2,     -3,     -3,
     -3,     -2,     -1,      0,      1,      2,      3,      3,
      3,      2,      1,      0,      0,     -1,     -2,     -3
]