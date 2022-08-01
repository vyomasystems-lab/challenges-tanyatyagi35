# sequence detector Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/30209235/182022570-64dd2114-e07a-482c-81a4-d44f27ef530d.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test which takes in the sequence of input bits into inp_bit input signal one by one as inp_bit is 1 bit signal.

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
![image](https://user-images.githubusercontent.com/30209235/182044562-2af47f50-76c7-4951-9623-0880d107c4f0.png)
The updated design is checked in as seq_detect_1011_fix.v

## Verification Strategy
In order to create overlapping sequence detector, following cases should be considered (explained using examples):
1. for sequence 11011:
when first bit comes (which is '1') then the sequence detector moves from IDLE state to SEQ_1 state. Now when second bit comes (which is again '1') then detector should remain at achieved SEQ_1 state so that this '1' can be used for creating further sequence(1011) rather than going to IDLE state and then again waiting for new '1' to start the required sequence detection.
2. for sequence 101011:
when first bit comes (which is '1') then the sequence detector moves from IDLE state to SEQ_1 state. Now when second bit comes (which is '0') then the sequence detector moves from the SEQ_1 state to SEQ_10 state. Now when third bit I.e., '1' comes now it will go to SEQ_101 state. Now when '0' comes then the desired sequence is broken but we can use previous two bits i.e., '10' for starting point of creation of our desired sequence.
3. for sequence 1011011:
when first 4 bits comes i.e., '1011' then we are able to detect our desired sequence and seq_seen becomes '1' and the further coming new input bits in order to make the entire '1011' sequence again, we can use previous one bit i.e., '1'. so when '011' comes in next incoming bits then we can detect '1011' again using '1' from previous detected sequence and again seq_seen will become '1'.


## Is the verification complete ?
yes, entire verification is completed.
