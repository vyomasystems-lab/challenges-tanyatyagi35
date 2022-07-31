# sequence detector Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/30209235/182022570-64dd2114-e07a-482c-81a4-d44f27ef530d.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in the sequence of input bits into inp_bit input signal one by one as inp_bit is 1 bit signal.

FOR BUG1:
The values are assigned to the input port using 
```
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    #now input sequence is given as: 11011 
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
```

FOR BUG2:
The values are assigned to the input port using 
```
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    #now input sequence is given as: 101011
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
```

FOR BUG3:
The values are assigned to the input port using 
```
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    #now input sequence is given as: 1011011
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
```

The assert statement is used for comparing the sequence detector's outut to the expected value:
assert dut.seq_seen.value==1,f"sequencer result is incorrect:(dut.seq_seen)!=1"

## Test Scenario **(Important)**
- Test Inputs for detecting bug1:
```
  input sequence is given as: 11011 to the inp_bit (1 bit) one by one
  Expected Output: seq_seen=1
  Observed Output in the DUT dut.seq_seen=0
```
  
- Test Inputs for detecting bug2:
```
  input sequence is given as: 101011 to the inp_bit (1 bit) one by one
  Expected Output: seq_seen=1
  Observed Output in the DUT dut.seq_seen=0
```  
- Test Inputs for detecting bug3:
```
  input sequence is given as:1011011 to the inp_bit (1 bit) one by one
  Expected Output: seq_seen=1
  Observed Output in the DUT dut.seq_seen=0
```

Output mismatches for the above inputs proving that there is a design bug
![image](https://user-images.githubusercontent.com/30209235/182042000-f860d193-4090-4385-af80-1eeb6a75d8cf.png)


## Design Bug
Based on the above test input and analysing the design, we see the following
- bug1  in line 49 of seq_detect_1011.v file so for correction of this bug: put "next_state=SEQ_1;" in line 49
- bug2 in line 65 of seq_detect_1011.v file so for correction of this bug: put "next_state=SEQ_10;" in line 65
- bug3 in line 69 of seq_detect_1011.v file so for correction of this bug: put "next_state=SEQ_1;" in line 69

## Design Fix
Updating the design and re-running the test makes the test pass.

The updated design is checked in as seq_detect_1011_fix.v

## Verification Strategy


## Is the verification complete ?
yes, entire verification is completed.
