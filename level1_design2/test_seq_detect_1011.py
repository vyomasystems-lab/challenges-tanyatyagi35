# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    #now input sequence is given as: 11011 
    #bug in line 49 of seq_detect_1011.v file
    #for correction of this bug: put "next_state=SEQ_1;" in line 49
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

    assert dut.seq_seen.value==1,f"sequencer result is incorrect:(dut.seq_seen)!=1"
#    cocotb.log.info('#### CTB: Develop your test here! ######')




@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    #now input sequence is given as: 101011
    #bug in line 65 of seq_detect_1011.v file
    #for correction of this bug: put "next_state=SEQ_10;" in line 65
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

    assert dut.seq_seen.value==1,f"sequencer result is incorrect:(dut.seq_seen)!=1"
#    cocotb.log.info('#### CTB: Develop your test here! ######')


@cocotb.test()
async def test_seq_bug3(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    #now input sequence is given as: 1011011
    #bug in line 69 of seq_detect_1011.v file
    #for correction of this bug: put "next_state=SEQ_1;" in line 69
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    assert dut.seq_seen.value==1,f"sequencer result is incorrect:(dut.seq_seen)!=1"
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    assert dut.seq_seen.value==1,f"sequencer result is incorrect:(dut.seq_seen)!=1"
#    cocotb.log.info('#### CTB: Develop your test here! ######')
