import pyghidra
base=r"C:\Users\namph\Documents\Codex\2026-11-23\https-github-com-storytold-craft-anything\work"
pyghidra.start()
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import TaskMonitor
with pyghidra.open_program(None,project_location=base+r"\ghidra-project",project_name="XpressDIL",program_name="VRV_Xpress.exe",nested_project_location=False,analyze=False) as api:
 program=api.getCurrentProgram()
 d=DecompInterface()
 d.openProgram(program)
 for s in ["008533b0","01045680","0085a120"]:
  f=program.getFunctionManager().getFunctionAt(api.toAddr(s))
  print("TARGET",s,flush=True)
  if f:
   z=d.decompileFunction(f,90,TaskMonitor.DUMMY)
   if z.decompileCompleted(): print(z.getDecompiledFunction().getC(),flush=True)
 d.dispose()


