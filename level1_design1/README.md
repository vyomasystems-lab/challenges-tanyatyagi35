# multiplexer Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/30209235/182022570-64dd2114-e07a-482c-81a4-d44f27ef530d.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which includes inputs like select line i.e.,sel (5 bit input) and values are assigned to all the inputs inp0 to inp30 (2 bit inputs).
s=30 
i30=2

The values are assigned to the input port using 
```
dut.sel.value = s
dut.inp30.value = i30
```

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.out.value==i30, f"mux result is incorrect:(dut.out.value)!=inp30"
```

## Test Scenario **(Important)**
- Test Inputs: sel=30, inp30=2
- Expected Output: out=inp30 i.e., out=2
- Observed Output in the DUT dut.out=0 

Output mismatches for the above inputs proving that there is a design bug
![image](https://user-images.githubusercontent.com/30209235/182032923-9d2895fa-4ca6-426d-b1a6-7d1aceb96c0e.png)

## Design Bug
Based on the above test input and analysing the design, we see the following

case condition  "5'b11110: out = inp30;" is missing after line 57 in mux.v file
so when select line is 5'b11110 then it will take default case output (which is zero) rather than giving inp30 at output so to remove this bug then insert line "5'b11110: out = inp30;" after line 57

## Design Fix
Updating the design and re-running the test makes the test pass.
The updated design is checked in as mux_fix.v
![image](https://user-images.githubusercontent.com/30209235/182033461-8fca941b-c9e8-4d9b-ab21-1635c4462769.png)
![image](https://user-images.githubusercontent.com/30209235/182033446-41b5f67b-9fa3-48b6-9d15-8305a1cb9447.png)

## Verification Strategy
in case of multiplexer, we will try to figure out how many inputs (that are going to be multiplexed to the output) are available in the code and check whether all those inputs are being transmitted to the output line in any of the possible cases formed by select line inputs.if there is any possibility that a paricular case is not written in the code for which the particular input will go to the output line then there is a bug in creating possible cases in the code.

## Is the verification complete ?
yes, the entire verification is completed.
