# SPI_Master Design Verification
The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![image](https://user-images.githubusercontent.com/30209235/182022570-64dd2114-e07a-482c-81a4-d44f27ef530d.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (SPI_Master module here) which includes inputs like i_TX_Byte (8 bit input), i_TX_DV (1 bit input), i_SPI_MISO (1 bit input).
```
i_TX_Byte= 209
i_TX_DV= 0
i_SPI_MISO= 1
```

The values are assigned to the input port using
```
dut.i_TX_Byte.value = i_TX_Byte
dut.i_TX_DV.value = i_TX_DV
dut.i_SPI_MISO.value = i_SPI_MISO
```
The assert statement is used for comparing the SPI_Master's output to the expected value.
```
error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL =
{hex(expected_output)}'
assert dut_output == expected_output, error_message
```


## Test Scenario **(Important)**
- Test Inputs:
```
#for 6th bit transmission
i_TX_Byte= 209   i.e., 11010001 in binary and this will be transmitted through MOSI line bit by bit.
i_TX_DV= 1
i_SPI_MISO= 1
```
- Expected Output: i_TX_Byte[6] i.e., '1' in above given input
- Observed Output in the DUT dut.o_SPI_MOSI= i_TX_Byte[5] i.e., '0' in above given input.

Output mismatches for the above inputs proving that there is a design bug in the the design code.


## Design Bug
Based on the above test input and analysing the design, we see the following
Based on the above test input and analysing the design, we see the following:
```
 else
    begin
      // If ready is high, reset bit counts to default
      if (o_TX_Ready)
      begin
        r_TX_Bit_Count <= 3'b111;
      end
      // Catch the case where we start transaction and CPHA = 0
      else if (r_TX_DV & ~w_CPHA)
      begin
        o_SPI_MOSI <= r_TX_Byte[3'b111];
        r_TX_Bit_Count <= 3'b110;
      end
      else if ((r_Leading_Edge & w_CPHA) | (r_Trailing_Edge & ~w_CPHA))
      begin
        r_TX_Bit_Count <= r_TX_Bit_Count - 1'b1;
        o_SPI_MOSI <= r_TX_Byte[r_TX_Bit_Count];      //--->bug in this line
      end
    end
```
for initial count 7, we will transmit bit 7 i.e., r_TX_Byte[7] then count is made 6  
but when last “else if” block is executed then it again decremented the count to 5 and now the transmitted bit on MOSI line will be r_TX_Byte[5] rather than r_TX_Byte[6].  


## Design Fix
Updating the design and re-running the test makes the test pass.
We need to replace “o_SPI_MOSI <= r_TX_Byte[r_TX_Bit_Count];” line by “o_SPI_MOSI <= r_TX_Byte[r_TX_Bit_Count+1];”.
The updated design is checked in as SPI_Master_fix.v

## Verification Strategy
Here for verification we will check whether all the bits of i_TX_Byte are transmitted onto the MOSI line or not. There should not be any case in which any of the bit transmission is missed. If any other bit is transmitted in place of the desired bit then we can judge that there is a bug in the code.

## Is the verification complete ?
yes, the entire verification is completed.
