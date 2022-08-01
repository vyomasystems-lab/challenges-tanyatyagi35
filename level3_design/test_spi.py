
# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
import sys
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1)

@cocotb.test()
def test_spi(dut):
    # clock
    cocotb.fork(clock_gen(dut.i_Clk))

    # reset
    dut.i_Rst_L.value <= 0
    yield Timer(4)
    dut.i_Rst_L.value <= 1


    """Test for SPI_Master"""
    #input driving
    i_TX_Byte= 209
    i_TX_DV= 0
    i_SPI_MISO= 1

    # driving the input transaction
    dut.i_TX_Byte.value = i_TX_Byte
    dut.i_TX_DV.value = i_TX_DV
    dut.i_SPI_MISO.value = i_SPI_MISO
    yield Timer(2)


    # for bit 7 transmission
    dut.i_TX_Byte.value=209
    dut.i_TX_DV.value= 1
    dut.i_SPI_MISO.value= 1
   
    expected_output=i_TX_Byte[5]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL ={hex(expected_output)}'
    assert dut_output == expected_output, error_message


    # for bit 6 transmission
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 0
    yield Timer(2)
    expected_output=i_TX_Byte[6]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')
    yield Timer(2)

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL ={hex(expected_output)}'
    assert dut_output == expected_output, error_message


    # for bit 5 transmission
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 1
    yield Timer(2)
    expected_output=i_TX_Byte[5]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL ={hex(expected_output)}'
    assert dut_output == expected_output, error_message


    # for bit 4 transmission
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 1
    yield Timer(2)
    expected_output=i_TX_Byte[4]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL ={hex(expected_output)}'
    assert dut_output == expected_output, error_message


    # for bit 3 transmission
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 0
    yield Timer(2)
    expected_output=i_TX_Byte[3]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL ={hex(expected_output)}'
    assert dut_output == expected_output, error_message


    # for bit 2 transmission
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 0
    yield Timer(2)
    expected_output=i_TX_Byte[2]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL ={hex(expected_output)}'
    assert dut_output == expected_output, error_message


    # for bit 1 transmission
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 1
    yield Timer(2)
    expected_output=i_TX_Byte[1]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL ={hex(expected_output)}'
    assert dut_output == expected_output, error_message


    # for bit 0 transmission
    i_TX_Byte= 209
    i_TX_DV= 1
    i_SPI_MISO= 1
    yield Timer(2)
    expected_output=i_TX_Byte[0]
    # obtaining the output
    dut_output = dut.o_SPI_MOSI.value
    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_output)}')

    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL ={hex(expected_output)}'
    assert dut_output == expected_output, error_message
