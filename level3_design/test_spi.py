# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
import sys
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge


@cocotb.test()
async def test_spi(dut):

    clock = Clock(dut.i_Clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.i_Rst_L.value=0
    await RisingEdge(dut.i_Clk)  
    dut.i_Rst_L.value=1

    await RisingEdge(dut.i_Clk)  
    """Test for SPI_Master"""
    #input driving
    i_TX_Byte1= 209
    i_TX_DV1= 0
    i_SPI_MISO1= 1

    # driving the input transaction
    dut.i_TX_Byte.value = i_TX_Byte1
    dut.i_TX_DV.value = i_TX_DV1
    dut.i_SPI_MISO.value = i_SPI_MISO1
    
    # for bit 7 transmission
    await RisingEdge(dut.i_Clk)  
    dut.i_TX_Byte.value=209
    dut.i_TX_DV.value= 1
    dut.i_SPI_MISO.value= 1
   
    expected_output=1  #i.e., i_TX_Byte[7]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
    cocotb.log.info(f'EXPECTED OUTPUT={expected_output}')

    error_message = f'Value mismatch DUT = {dut_output} does not match MODEL ={expected_output}'
    assert dut_output == expected_output, error_message


    # for bit 6 transmission
    await RisingEdge(dut.i_Clk) 
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 0
    expected_output=1 #i.e., i_TX_Byte[6]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
    cocotb.log.info(f'EXPECTED OUTPUT={expected_output}')

    error_message = f'Value mismatch DUT = {dut_output} does not match MODEL ={expected_output}'
    assert dut_output == expected_output, error_message

    # for bit 5 transmission
    await RisingEdge(dut.i_Clk) 
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 1
    expected_output=0   #i.e., i_TX_Byte[5]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
    cocotb.log.info(f'EXPECTED OUTPUT={expected_output}')

    error_message = f'Value mismatch DUT = {dut_output} does not match MODEL ={expected_output}'
    assert dut_output == expected_output, error_message

    # for bit 4 transmission
    await RisingEdge(dut.i_Clk) 
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 1
    expected_output=1  #i.e., i_TX_Byte[4]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
    cocotb.log.info(f'EXPECTED OUTPUT={expected_output}')

    error_message = f'Value mismatch DUT = {dut_output} does not match MODEL ={expected_output}'
    assert dut_output == expected_output, error_message


    # for bit 3 transmission
    await RisingEdge(dut.i_Clk) 
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 0
    expected_output=0  #i.e., i_TX_Byte[3]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
    cocotb.log.info(f'EXPECTED OUTPUT={expected_output}')

    error_message = f'Value mismatch DUT = {dut_output} does not match MODEL ={expected_output}'
    assert dut_output == expected_output, error_message

    # for bit 2 transmission
    await RisingEdge(dut.i_Clk) 
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 0
    expected_output=0  #i.e., i_TX_Byte[2]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
    cocotb.log.info(f'EXPECTED OUTPUT={expected_output}')

    error_message = f'Value mismatch DUT = {dut_output} does not match MODEL ={expected_output}'
    assert dut_output == expected_output, error_message

    # for bit 1 transmission
    await RisingEdge(dut.i_Clk) 
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 1
    expected_output=0 #i.e., i_TX_Byte[1]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
    cocotb.log.info(f'EXPECTED OUTPUT={expected_output}')

    error_message = f'Value mismatch DUT = {dut_output} does not match MODEL ={expected_output}'
    assert dut_output == expected_output, error_message

    # for bit 0 transmission
    await RisingEdge(dut.i_Clk) 
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 1
    expected_output=1 #i.e., i_TX_Byte[0]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={dut_output}')
    cocotb.log.info(f'EXPECTED OUTPUT={expected_output}')

    error_message = f'Value mismatch DUT = {dut_output} does not match MODEL ={expected_output}'
    assert dut_output == expected_output, error_message
