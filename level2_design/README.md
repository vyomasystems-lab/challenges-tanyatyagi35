# bitmanipulation Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/30209235/182022570-64dd2114-e07a-482c-81a4-d44f27ef530d.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (bitmanip module here) which takes in four inputs as:

FOR CASE1:
The values are assigned to the input port using 
```

```

FOR CASE2:
The values are assigned to the input port using 
```

```

FOR CASE3:
The values are assigned to the input port using 
```

```

FOR CASE4:
The values are assigned to the input port using 
```

```

The assert statement is used for comparing the bitmanip's outut to the expected value.
```

```

## Test Scenario **(Important)**
FOR CASE1:
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

FOR CASE2:
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

FOR CASE3
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

FOR CASE4
- Test Inputs: a=7 b=5
- Expected Output: sum=12
- Observed Output in the DUT dut.sum=2

Output mismatches for the above inputs proving that there is a design bug
![image](https://user-images.githubusercontent.com/30209235/182044081-968e135e-c5b5-4733-b181-41d646c5887a.png)

## Verification Strategy

## Is the verification complete ?
yes, every possible test cases are taken for which test will fail.
