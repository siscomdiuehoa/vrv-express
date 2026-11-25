import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.*;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.Reference;
public class TraceDIL extends GhidraScript {
 public void run() throws Exception {
  String[] targets={"008594d0","00858f80","01042730","01045cf0","014940e0"};
  DecompInterface d=new DecompInterface(); d.openProgram(currentProgram);
  for(String s:targets){Address a=toAddr(s);Function f=getFunctionAt(a);println("TARGET "+s);
   for(Reference r: getReferencesTo(a)){Function owner=getFunctionContaining(r.getFromAddress());println("CALLER "+r.getFromAddress()+" "+(owner==null?"unknown":owner.getEntryPoint()));}
   if(f!=null){DecompileResults z=d.decompileFunction(f,60,monitor);if(z.decompileCompleted())println("CODE "+z.getDecompiledFunction().getC());}
  }d.dispose();
 }
}
