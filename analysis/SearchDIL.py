fm=currentProgram.getFunctionManager()
symbols=currentProgram.getSymbolTable().getAllSymbols(True)
for sym in symbols:
 name=sym.getName()
 if any(t in name.lower() for t in ["findresource","loadresource","lockresource","sizeofresource"]):
  print("SYMBOL",name,sym.getAddress())
  for r in getReferencesTo(sym.getAddress()):
   f=getFunctionContaining(r.getFromAddress())
   print("REF",r.getFromAddress(),f.getEntryPoint() if f else "unknown")
