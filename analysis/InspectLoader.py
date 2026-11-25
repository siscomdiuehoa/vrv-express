from ghidra.app.decompiler import DecompInterface
d=DecompInterface()
d.openProgram(currentProgram)
for s in ["004bb810","00858f80","00859660"]:
 f=getFunctionAt(toAddr(s))
 print("TARGET",s)
 if f:
  z=d.decompileFunction(f,45,monitor)
  if z.decompileCompleted(): print(z.getDecompiledFunction().getC())
d.dispose()

