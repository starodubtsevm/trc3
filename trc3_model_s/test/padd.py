import ctypes
import pathlib

if __name__ == "__main__":
	# load the lib
	libname = pathlib.Path().absolute() / "libcadd.so"
	c_lib = ctypes.CDLL(libname)

	x, y = 6, 2.3

	# define the return type
	c_lib.cadd.restype = ctypes.c_float
	# call the function with the correct argument types
	
	res = c_lib.cadd(x, ctypes.c_float(y))
	print(f"In Python: int: {x} float {y:.1f} return val {res:.1f}")
