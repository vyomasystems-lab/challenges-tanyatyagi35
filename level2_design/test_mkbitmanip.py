# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test1(dut):
    # clock
    cocotb.fork(clock_gen(dut.CLK))
    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1
    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    #case1: for zero values of both mav_putvalue_src1 & mav_putvalue_src2 and non-zero value of mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x0
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x00100000

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 
    # obtaining the output
    dut_output = dut.mav_putvalue.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test2(dut):
    # clock
    cocotb.fork(clock_gen(dut.CLK))
    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1
    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    #case2: for non-zero values of both mav_putvalue_src1 & mav_putvalue_src3 and zero value for mav_outvalue_src3, the test will fail
    #applicable for all possible insrtructions 
    mav_putvalue_src1 = 0x1F
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x10100100

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 
    # obtaining the output
    dut_output = dut.mav_putvalue.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def run_test3(dut):
    # clock
    cocotb.fork(clock_gen(dut.CLK))
    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1
    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    #case3: for non-zero values of both mav_putvalue_src1 & mav_putvalue_src2 and zero value of mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x1F
    mav_putvalue_src2 = 0xFF2
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x10100010

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 
    # obtaining the output
    dut_output = dut.mav_putvalue.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message


@cocotb.test()
def run_test4(dut):
    # clock
    cocotb.fork(clock_gen(dut.CLK))
    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1
    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    #case4: for non-zero values of all three inputs i.e., mav_putvalue_src1, mav_putvalue_src2 and mav_outvalue_src3, the test will fail
    #applicable for all possible instructions
    mav_putvalue_src1 = 0x1
    mav_putvalue_src2 = 0x7F
    mav_putvalue_src3 = 0xFFFF1111
    mav_putvalue_instr = 0x11100B20

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 
    # obtaining the output
    dut_output = dut.mav_putvalue.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')

    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
