for s in ["004bb580","004bb810","004ba6c0"]:
 print("TARGET",s)
 for r in getReferencesTo(toAddr(s)):
  f=getFunctionContaining(r.getFromAddress())
  print("REF",r.getFromAddress(),f.getEntryPoint() if f else "unknown",r.getReferenceType())
