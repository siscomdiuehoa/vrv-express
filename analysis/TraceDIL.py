from ghidra.app.decompiler import DecompInterface
d=DecompInterface()
d.openProgram(currentProgram)
for s in ["008594d0","00858f80","01042730","01045cf0","014940e0"]:
 a=toAddr(s)
 print("TARGET "+s)
 for r in getReferencesTo(a):
  f=getFunctionContaining(r.getFromAddress())
  print("CALLER "+str(r.getFromAddress())+" "+str(f.getEntryPoint() if f else "unknown"))
 f=getFunctionAt(a)
 if f:
  x=d.decompileFunction(f,60,monitor)
  if x.decompileCompleted():
   print("CODE "+x.getDecompiledFunction().getC())
d.dispose()
