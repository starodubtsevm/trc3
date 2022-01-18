#ifndef __FIR_780_H__
#define __FIR_780_H__

#define LENGTH_FIR_780    1000

static fract16 fir780coeff[LENGTH_FIR_780] =
{
      1,      2,      3,      2,      1,      0,     -2,     -3,
     -3,     -1,      0,      2,      3,      3,      1,      0,
     -2,     -3,     -3,     -2,      0,      2,      3,      3,
      2,      0,     -1,     -3,     -3,     -2,      0,      1,
      3,      3,      2,      0,     -1,     -3,     -3,     -3,
     -1,      1,      3,      4,      3,      1,      0,     -3,
     -4,     -3,     -1,      0,      2,      4,      3,      2,
      0,     -2,     -4,     -4,     -2,      0,      2,      4,
      4,      3,      0,     -2,     -4,     -4,     -3,      0,
      2,      4,      4,      3,      1,     -1,     -4,     -4,
     -4,     -1,      1,      3,      4,      4,      2,      0,
     -3,     -5,     -4,     -2,      0,      3,      4,      4,
      2,      0,     -3,     -4,     -4,     -3,      0,      2,
      4,      4,      3,      0,     -2,     -4,     -4,     -3,
      0,      2,      4,      4,      3,      1,     -1,     -3,
     -4,     -3,     -1,      1,      3,      4,      3,      1,
      0,     -3,     -4,     -3,     -2,      0,      2,      3,
      3,      2,      0,     -2,     -3,     -3,     -2,      0,
      1,      2,      2,      1,      0,     -1,     -2,     -2,
     -1,      0,      0,      1,      1,      1,      0,      0,
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      0,      0,      1,      0,      0,     -1,
     -1,     -2,     -1,      0,      1,      2,      3,      2,
      0,     -2,     -4,     -4,     -3,      0,      2,      5,
      6,      4,      1,     -2,     -6,     -7,     -6,     -2,
      2,      7,      9,      8,      3,     -2,     -8,    -11,
    -10,     -5,      1,      8,     12,     12,      7,     -1,
     -9,    -14,    -14,     -9,      0,      9,     16,     17,
     11,      1,     -9,    -17,    -19,    -14,     -3,      9,
     19,     22,     17,      5,     -8,    -20,    -25,    -20,
     -8,      7,     21,     28,     24,     11,     -6,    -22,
    -30,    -27,    -14,      4,     22,     33,     31,     18,
     -1,    -22,    -35,    -35,    -22,      0,     22,     37,
     39,     27,      4,    -21,    -39,    -43,    -32,     -8,
     19,     40,     47,     37,     12,    -17,    -41,    -51,
    -42,    -17,     14,     42,     55,     48,     23,    -11,
    -42,    -58,    -53,    -28,      7,     41,     61,     59,
     35,     -2,    -40,    -64,    -64,    -41,     -2,     38,
     66,     70,     48,      8,    -35,    -67,    -75,    -55,
    -15,     31,     68,     80,     63,     22,    -27,    -68,
    -84,    -70,    -30,     22,     67,     89,     78,     38,
    -16,    -66,    -92,    -85,    -46,      9,     63,     95,
     92,     55,     -2,    -60,    -97,    -99,    -64,     -5,
     56,     98,    105,     74,     14,    -51,    -99,   -111,
    -83,    -24,     44,     98,    116,     92,     34,    -37,
    -97,   -121,   -101,    -44,     29,     94,    125,    110,
     55,    -21,    -90,   -128,   -119,    -66,     11,     86,
    130,    127,     77,     -1,    -80,   -131,   -134,    -88,
     -9,     73,    130,    141,     99,     21,    -65,   -129,
   -146,   -110,    -33,     56,    127,    151,    121,     46,
    -46,   -123,   -155,   -131,    -59,     35,    118,    158,
    141,     71,    -24,   -112,   -160,   -149,    -84,     11,
    104,    160,    157,     97,      1,    -96,   -159,   -164,
   -110,    -14,     86,    157,    170,    122,     28,    -75,
   -153,   -175,   -133,    -42,     64,    148,    179,    144,
     57,    -51,   -142,   -181,   -154,    -71,     38,    135,
    182,    164,     85,    -24,   -126,   -182,   -172,    -99,
     10,    116,    180,    179,    112,      4,   -105,   -177,
   -185,   -125,    -19,     93,    173,    189,    137,     34,
    -80,   -167,   -192,   -148,    -49,     67,    159,    194,
    158,     64,    -52,   -151,   -194,   -167,    -79,     38,
    141,    193,    175,     93,    -23,   -131,   -191,   -182,
   -106,      7,    119,    187,    187,    119,      7,   -106,
   -182,   -191,   -131,    -23,     93,    175,    193,    141,
     38,    -79,   -167,   -194,   -151,    -52,     64,    158,
    194,    159,     67,    -49,   -148,   -192,   -167,    -80,
     34,    137,    189,    173,     93,    -19,   -125,   -185,
   -177,   -105,      4,    112,    179,    180,    116,     10,
    -99,   -172,   -182,   -126,    -24,     85,    164,    182,
    135,     38,    -71,   -154,   -181,   -142,    -51,     57,
    144,    179,    148,     64,    -42,   -133,   -175,   -153,
    -75,     28,    122,    170,    157,     86,    -14,   -110,
   -164,   -159,    -96,      1,     97,    157,    160,    104,
     11,    -84,   -149,   -160,   -112,    -24,     71,    141,
    158,    118,     35,    -59,   -131,   -155,   -123,    -46,
     46,    121,    151,    127,     56,    -33,   -110,   -146,
   -129,    -65,     21,     99,    141,    130,     73,     -9,
    -88,   -134,   -131,    -80,     -1,     77,    127,    130,
     86,     11,    -66,   -119,   -128,    -90,    -21,     55,
    110,    125,     94,     29,    -44,   -101,   -121,    -97,
    -37,     34,     92,    116,     98,     44,    -24,    -83,
   -111,    -99,    -51,     14,     74,    105,     98,     56,
     -5,    -64,    -99,    -97,    -60,     -2,     55,     92,
     95,     63,      9,    -46,    -85,    -92,    -66,    -16,
     38,     78,     89,     67,     22,    -30,    -70,    -84,
    -68,    -27,     22,     63,     80,     68,     31,    -15,
    -55,    -75,    -67,    -35,      8,     48,     70,     66,
     38,     -2,    -41,    -64,    -64,    -40,     -2,     35,
     59,     61,     41,      7,    -28,    -53,    -58,    -42,
    -11,     23,     48,     55,     42,     14,    -17,    -42,
    -51,    -41,    -17,     12,     37,     47,     40,     19,
     -8,    -32,    -43,    -39,    -21,      4,     27,     39,
     37,     22,      0,    -22,    -35,    -35,    -22,     -1,
     18,     31,     33,     22,      4,    -14,    -27,    -30,
    -22,     -6,     11,     24,     28,     21,      7,     -8,
    -20,    -25,    -20,     -8,      5,     17,     22,     19,
      9,     -3,    -14,    -19,    -17,     -9,      1,     11,
     17,     16,      9,      0,     -9,    -14,    -14,     -9,
     -1,      7,     12,     12,      8,      1,     -5,    -10,
    -11,     -8,     -2,      3,      8,      9,      7,      2,
     -2,     -6,     -7,     -6,     -2,      1,      4,      6,
      5,      2,      0,     -3,     -4,     -4,     -2,      0,
      2,      3,      2,      1,      0,     -1,     -2,     -1,
     -1,      0,      0,      1,      0,      0,      0,      0,
      0,      0,      0,      0,      0,      0,      0,      0,
      0,      0,      1,      1,      1,      0,      0,     -1,
     -2,     -2,     -1,      0,      1,      2,      2,      1,
      0,     -2,     -3,     -3,     -2,      0,      2,      3,
      3,      2,      0,     -2,     -3,     -4,     -3,      0,
      1,      3,      4,      3,      1,     -1,     -3,     -4,
     -3,     -1,      1,      3,      4,      4,      2,      0,
     -3,     -4,     -4,     -2,      0,      3,      4,      4,
      2,      0,     -3,     -4,     -4,     -3,      0,      2,
      4,      4,      3,      0,     -2,     -4,     -5,     -3,
      0,      2,      4,      4,      3,      1,     -1,     -4,
     -4,     -4,     -1,      1,      3,      4,      4,      2,
      0,     -3,     -4,     -4,     -2,      0,      3,      4,
      4,      2,      0,     -2,     -4,     -4,     -2,      0,
      2,      3,      4,      2,      0,     -1,     -3,     -4,
     -3,      0,      1,      3,      4,      3,      1,     -1,
     -3,     -3,     -3,     -1,      0,      2,      3,      3,
      1,      0,     -2,     -3,     -3,     -1,      0,      2,
      3,      3,      2,      0,     -2,     -3,     -3,     -2,
      0,      1,      3,      3,      2,      0,     -1,     -3,
     -3,     -2,      0,      1,      2,      3,      2,      1
};

#endif
