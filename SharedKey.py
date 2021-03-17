CLs = []
CL_XOR_Value = 0
def CLfunc(CL):
  CLs.append(CL)
  if CL_XOR_Value == 0:
      CL_XOR_Value = CL
  else:
      CL_XOR_Value = CL_XOR_Value ^ CL 
  return CL_XOR_Value