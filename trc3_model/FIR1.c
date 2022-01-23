int main()
{

    float X[1000] = {0};
    X[0] = 1;

    float Y[1000] = {0};


    float yn = 0;
    const int N = 3;
    float h[N] = {0.32590173795979338000,
                  0.34819652408041324000,
                  0.32590173795979338000};
    float x[N] = {0,0,0};


    for(int i=0; i<1000; i++)
    {
                                                 //  Alternative implementation
        for(int k=0; k < N-1; k++)               //  for(int k=N-1; k>0; k--)
        {                                        //  {                      
          x[N-k-1] = x[N-k-2];//shift the data   //    x[k] = x[k-1];
        }                                        //  }              

        x[0] = X[i]; // move input sample to buffer
        yn = 0; // clear output sample

        for(int k=0; k < N; k++)
        {
            yn += h[k]*x[k]; // multiply data on coefficients with accumulation
        }

        Y[i] = yn;
    }

     HANDLE hFile = CreateFile("Y.dat", GENERIC_READ | GENERIC_WRITE, 0, NULL, 
                               CREATE_ALWAYS, 0, NULL);

    DWORD dwCount;
    WriteFile(hFile,Y,sizeof(Y),&dwCount,NULL);
    CloseHandle(hFile);

    return 0;
}
