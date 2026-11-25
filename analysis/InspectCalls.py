from ghidra.app.decompiler import DecompInterface
d=DecompInterface()
d.openProgram(currentProgram)
seen=set()
for s in ["016da3f0","016da4f0","016da5b8","016da610"]:
 print("IAT",s)
 for r in getReferencesTo(toAddr(s)):
  f=getFunctionContaining(r.getFromAddress())
  print("REF",r.getFromAddress(),f.getEntryPoint() if f else "unknown")
  if f and str(f.getEntryPoint()) not in seen:
   seen.add(str(f.getEntryPoint()))
   z=d.decompileFunction(f,30,monitor)
   if z.decompileCompleted(): print("CODE",z.getDecompiledFunction().getC())
d.dispose()
