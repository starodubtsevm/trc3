#ifndef __FIR_480I_H__
#define __FIR_480I_H__

#define LENGTH_FIR_480I    400

static fract16 fir480coeffI[LENGTH_FIR_480I] =
{
     -4,     -2,      1,      3,      4,      2,      0,     -3,
     -4,     -2,      0,      2,      3,      2,      0,     -2,
     -3,     -2,      0,      1,      2,      2,      0,     -1,
     -2,     -1,      0,      0,      1,      1,      0,      0,
      0,      0,      0,      0,      0,     -1,     -1,      0,
      1,      3,      3,      0,     -2,     -5,     -5,     -2,
      3,      8,      8,      4,     -3,    -10,    -12,     -7,
      2,     13,     17,     11,     -1,    -15,    -22,    -17,
     -1,     16,     27,     23,      5,    -17,    -33,    -31,
    -11,     16,     38,     40,     19,    -14,    -43,    -50,
    -28,     10,     47,     60,     40,     -4,    -49,    -70,
    -53,     -4,     50,     80,     68,     16,    -48,    -90,
    -84,    -30,     43,     97,    100,     47,    -35,   -103,
   -117,    -66,     24,    106,    134,     88,     -8,   -106,
   -149,   -111,     -9,    102,    162,    135,     32,    -93,
   -173,   -160,    -57,     81,    180,    184,     86,    -63,
   -183,   -207,   -116,     41,    182,    227,    148,    -14,
   -175,   -245,   -181,    -15,    163,    258,    213,     50,
   -145,   -266,   -244,    -87,    121,    269,    273,    126,
    -92,   -266,   -297,   -166,     58,    256,    318,    206,
    -20,   -240,   -333,   -245,    -21,    217,    341,    280,
     65,   -188,   -343,   -313,   -111,    154,    338,    340,
    156,   -114,   -326,   -362,   -201,     70,    306,    377,
    243,    -24,   -280,   -386,   -282,    -24,    248,    386,
    316,     73,   -209,   -379,   -344,   -121,    167,    365,
    365,    167,   -121,   -344,   -379,   -209,     73,    316,
    386,    248,    -24,   -282,   -386,   -280,    -24,    243,
    377,    306,     70,   -201,   -362,   -326,   -114,    156,
    340,    338,    154,   -111,   -313,   -343,   -188,     65,
    280,    341,    217,    -21,   -245,   -333,   -240,    -20,
    206,    318,    256,     58,   -166,   -297,   -266,    -92,
    126,    273,    269,    121,    -87,   -244,   -266,   -145,
     50,    213,    258,    163,    -15,   -181,   -245,   -175,
    -14,    148,    227,    182,     41,   -116,   -207,   -183,
    -63,     86,    184,    180,     81,    -57,   -160,   -173,
    -93,     32,    135,    162,    102,     -9,   -111,   -149,
   -106,     -8,     88,    134,    106,     24,    -66,   -117,
   -103,    -35,     47,    100,     97,     43,    -30,    -84,
    -90,    -48,     16,     68,     80,     50,     -4,    -53,
    -70,    -49,     -4,     40,     60,     47,     10,    -28,
    -50,    -43,    -14,     19,     40,     38,     16,    -11,
    -31,    -33,    -17,      5,     23,     27,     16,     -1,
    -17,    -22,    -15,     -1,     11,     17,     13,      2,
     -7,    -12,    -10,     -3,      4,      8,      8,      3,
     -2,     -5,     -5,     -2,      0,      3,      3,      1,
      0,     -1,     -1,      0,      0,      0,      0,      0,
      0,      0,      1,      1,      0,      0,     -1,     -2,
     -1,      0,      2,      2,      1,      0,     -2,     -3,
     -2,      0,      2,      3,      2,      0,     -2,     -4,
     -3,      0,      2,      4,      3,      1,     -2,     -4
};

#endif
