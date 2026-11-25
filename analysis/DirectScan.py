import pyghidra
base=r"C:\Users\namph\Documents\Codex\2026-11-23\https-github-com-storytold-craft-anything\work"
pyghidra.start()
with pyghidra.open_program(None,project_location=base+r"\ghidra-project",project_name="XpressDIL",program_name="VRV_Xpress.exe",nested_project_location=False,analyze=False) as api:
 program=api.getCurrentProgram()
 print("INSTRUCTIONS",program.getListing().getNumInstructions(),flush=True)
 for s in ["004bb580","004bb810","004ba6c0"]:
  a=api.toAddr(s)
  print("TARGET",s,flush=True)
  for r in program.getReferenceManager().getReferencesTo(a):
   f=program.getFunctionManager().getFunctionContaining(r.getFromAddress())
   print("REF",r.getFromAddress(),f.getEntryPoint() if f else "unknown",flush=True)
