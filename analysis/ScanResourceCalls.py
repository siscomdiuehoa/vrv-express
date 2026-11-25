targets=set([toAddr("004bb580"),toAddr("004bb810"),toAddr("004ba6c0")])
instructions=currentProgram.getListing().getInstructions(True)
count=0
while instructions.hasNext() and not monitor.isCancelled():
 ins=instructions.next()
 if ins.getFlowType().isCall():
  for dest in ins.getFlows():
   if dest in targets:
    f=getFunctionContaining(ins.getAddress())
    print("CALL",ins.getAddress(),"TO",dest,"FUNCTION",f.getEntryPoint() if f else "unknown")
 count+=1
print("INSTRUCTIONS",count)
