# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    s=30
    i0=0
    i1=1
    i2=2
    i3=3
    i4=0
    i5=1
    i6=2
    i7=3
    i8=0
    i9=1
    i10=2
    i11=3
    i12=0
    i13=1
    i14=2
    i15=3
    i16=0
    i17=1
    i18=2
    i19=3
    i20=0
    i21=1
    i22=2
    i23=3
    i24=0
    i25=1
    i26=2
    i27=3
    i28=0
    i29=1
    i30=2

    #input driving
    dut.sel.value=s
    dut.inp0.value=i0
    dut.inp1.value=i1
    dut.inp2.value=i2
    dut.inp3.value=i3
    dut.inp4.value=i4
    dut.inp5.value=i5
    dut.inp6.value=i6
    dut.inp7.value=i7
    dut.inp8.value=i8
    dut.inp9.value=i9
    dut.inp10.value=i10
    dut.inp11.value=i11
    dut.inp12.value=i12
    dut.inp13.value=i13
    dut.inp14.value=i14
    dut.inp15.value=i15
    dut.inp16.value=i16
    dut.inp17.value=i17
    dut.inp18.value=i18
    dut.inp19.value=i19
    dut.inp20.value=i20
    dut.inp21.value=i21
    dut.inp22.value=i22
    dut.inp23.value=i23
    dut.inp24.value=i24
    dut.inp25.value=i25
    dut.inp26.value=i26
    dut.inp27.value=i27
    dut.inp28.value=i28
    dut.inp29.value=i29
    dut.inp30.value=i30

    await Timer(2,units='ns')
    

    #cocotb.log.info('##### CTB: Develop your test here ########')
    assert dut.out.value==i30, f"mux result is incorrect:(dut.out.value)!=inp30"
