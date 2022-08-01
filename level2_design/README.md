# bitmanipulation Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/30209235/182022570-64dd2114-e07a-482c-81a4-d44f27ef530d.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (bitmanip module here) which takes in four inputs as:

FOR CASE1:
The values are assigned to the input port using 
```
    #case1: for zero values of both mav_putvalue_src1 & mav_putvalue_src2 and non-zero value of mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x00100000
```

FOR CASE2:
The values are assigned to the input port using 
```
    #case2: for non-zero values of both mav_putvalue_src1 & mav_putvalue_src3 and zero value for mav_outvalue_src3, the test will fail
    #applicable for all possible insrtructions 
    mav_putvalue_src1 = 0x1F
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x10100100
```

FOR CASE3:
The values are assigned to the input port using 
```
    #case3: for non-zero values of both mav_putvalue_src1 & mav_putvalue_src2 and zero value of mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x1F
    mav_putvalue_src2 = 0xFF2
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x10100010
```

FOR CASE4:
The values are assigned to the input port using 
```
    #case4: for non-zero values of all three inputs i.e., mav_putvalue_src1, mav_putvalue_src2 and mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x1
    mav_putvalue_src2 = 0x7F
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x11100B20
```
    # driving the input transaction
```
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
```
    
The assert statement is used for comparing the bitmanip's outut to the expected value.
```
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
```

## Test Scenario **(Important)**
FOR CASE1:
```
- Test Inputs:
    #case1: for zero values of both mav_putvalue_src1 & mav_putvalue_src2 and non-zero value of mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x00100000
- Expected Output: expected_mav_putvalue=0x0
- Observed Output in the DUT dut.output=0x1fffe2222
```

FOR CASE2:
```
- Test Inputs:
    #case2: for non-zero values of both mav_putvalue_src1 & mav_putvalue_src3 and zero value for mav_outvalue_src3, the test will fail
    #applicable for all possible insrtructions 
    mav_putvalue_src1 = 0x1F
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x10100100
- Expected Output: expected_mav_putvalue=0x0
- Observed Output in the DUT dut.output=0x1fffe2222
```

FOR CASE3
```
- Test Inputs:
    #case3: for non-zero values of both mav_putvalue_src1 & mav_putvalue_src2 and zero value of mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x1F
    mav_putvalue_src2 = 0xFF2
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x10100010
- Expected Output: expected_mav_putvalue=0x0
- Observed Output in the DUT dut.output=0x3e
```

FOR CASE4
```
- Test Inputs:
    #case4: for non-zero values of all three inputs i.e., mav_putvalue_src1, mav_putvalue_src2 and mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x1
    mav_putvalue_src2 = 0x7F
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x11100B20
- Expected Output: expected_mav_putvalue=0x0
- Observed Output in the DUT dut.output=0x2
```

Output mismatches for the above inputs proving that there is a design bug
![image](https://user-images.githubusercontent.com/30209235/182044081-968e135e-c5b5-4733-b181-41d646c5887a.png)

## Verification Strategy
in order to find the bug, we have used possible cases for the input then we will check the whether expected output is equal to dut output or not:
```
case1:
mav_putvalue_src1: zero
mav_putvalue_src2: zero
mav_putvalue_src3: zero
here the expected output is equal to dut output. Therefore, the test will have status:pass

case2:
mav_putvalue_src1: zero
mav_putvalue_src2: zero
mav_putvalue_src3: non-zero
here the expected output is not equal to dut output. Therefore, the test will have status:fail

case3:
mav_putvalue_src1: zero
mav_putvalue_src2: non-zero
mav_putvalue_src3: zero
here the expected output is equal to dut output. Therefore, the test will have status:pass

case4:
mav_putvalue_src1: zero
mav_putvalue_src2: non-zero
mav_putvalue_src3: non-zero
here the expected output is equal to dut output. Therefore, the test will have status:pass

case5:
mav_putvalue_src1: non-zero
mav_putvalue_src2: zero
mav_putvalue_src3: zero
here the expected output is equal to dut output. Therefore, the test will have status:pass

case6:
mav_putvalue_src1: non-zero
mav_putvalue_src2: zero
mav_putvalue_src3: non-zero
here the expected output is not equal to dut output. Therefore, the test will have status:fail

case7:
mav_putvalue_src1: non-zero
mav_putvalue_src2: non-zero
mav_putvalue_src3: zero
here the expected output is not equal to dut output. Therefore, the test will have status:fail

case8:
mav_putvalue_src1: non-zero
mav_putvalue_src2: non-zero
mav_putvalue_src3: non-zero
here the expected output is not equal to dut output. Therefore, the test will have status:fail
```

## Is the verification complete ?
yes, every possible test cases are taken for which test will fail.
