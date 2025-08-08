# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_and_gates(dut):
    """Test the AND gate circuit implementation"""
    
    dut._log.info("Starting AND gate test")
    
    # Set the clock period to 10 ns (100 MHz)
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Test cases for 2-input AND gates
    test_cases = [
        # (ui_in value, expected uo_out[0] for inputs [1:0])
        (0b00000000, 0),  # A=0, B=0 → 0
        (0b00000001, 0),  # A=1, B=0 → 0  
        (0b00000010, 0),  # A=0, B=1 → 0
        (0b00000011, 1),  # A=1, B=1 → 1
    ]
    
    dut._log.info("Testing 2-input AND gate (ui_in[1:0] → uo_out[0])")
    for ui_in_val, expected in test_cases:
        dut.ui_in.value = ui_in_val
        await ClockCycles(dut.clk, 1)
        
        # Check first AND gate output
        actual = dut.uo_out.value & 0x01  # Get bit 0
        dut._log.info(f"ui_in={ui_in_val:08b}, uo_out[0]={actual}, expected={expected}")
        assert actual == expected, f"AND gate failed: got {actual}, expected {expected}"

    # Test all 4 AND gates systematically
    and_gates_config = [
        (1, [3, 2], "ui_in[3:2] → uo_out[1]"),    # 2nd AND gate
        (2, [5, 4], "ui_in[5:4] → uo_out[2]"),    # 3rd AND gate  
        (3, [7, 6], "ui_in[7:6] → uo_out[3]"),    # 4th AND gate
    ]
    
    for output_bit, input_bits, description in and_gates_config:
        dut._log.info(f"Testing {description}")
        
        # Test all combinations for this AND gate
        for a in range(2):
            for b in range(2):
                # Clear all inputs first
                dut.ui_in.value = 0
                # Set specific bits for this gate
                input_val = (a << input_bits[1]) | (b << input_bits[0])
                expected = a & b
                
                dut.ui_in.value = input_val
                await ClockCycles(dut.clk, 1)
                
                actual = (dut.uo_out.value >> output_bit) & 0x01
                dut._log.info(f"Gate {output_bit}: A={a}, B={b}, ui_in={input_val:08b}, uo_out[{output_bit}]={actual}, expected={expected}")
                assert actual == expected, f"AND gate {output_bit} failed: got {actual}, expected {expected}"

    # Test 8-input AND gate (all ui_in → uo_out[4])
    dut._log.info("Testing 8-input AND gate (all ui_in → uo_out[4])")
    
    # All zeros → output should be 0
    dut.ui_in.value = 0b00000000
    await ClockCycles(dut.clk, 1)
    actual = (dut.uo_out.value >> 4) & 0x01
    assert actual == 0, f"8-input AND failed for all zeros: got {actual}"
    
    # All ones → output should be 1
    dut.ui_in.value = 0b11111111
    await ClockCycles(dut.clk, 1)
    actual = (dut.uo_out.value >> 4) & 0x01
    assert actual == 1, f"8-input AND failed for all ones: got {actual}"
    
    # One bit missing → output should be 0
    dut.ui_in.value = 0b11111110
    await ClockCycles(dut.clk, 1)
    actual = (dut.uo_out.value >> 4) & 0x01
    assert actual == 0, f"8-input AND failed for missing bit: got {actual}"

    # Test that unused outputs are 0
    dut._log.info("Testing unused outputs")
    dut.ui_in.value = 0b11111111
    await ClockCycles(dut.clk, 1)
    
    unused_bits = (dut.uo_out.value >> 5) & 0x07  # bits [7:5]
    assert unused_bits == 0, f"Unused outputs should be 0: got {unused_bits:03b}"
    
    # Test bidirectional IOs are set correctly
    assert dut.uio_oe.value == 0, f"uio_oe should be 0: got {dut.uio_oe.value}"
    assert dut.uio_out.value == 0, f"uio_out should be 0: got {dut.uio_out.value}"

    dut._log.info("All tests passed!")


@cocotb.test()
async def test_comprehensive_and_combinations(dut):
    """Test various input combinations comprehensively"""
    
    dut._log.info("Starting comprehensive AND gate combination test")
    
    # Set the clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    # Test all combinations for first two bits
    dut._log.info("Testing all 4 combinations for ui_in[1:0]")
    for a in range(2):
        for b in range(2):
            input_val = (b << 1) | a
            expected = a & b
            
            dut.ui_in.value = input_val
            await ClockCycles(dut.clk, 1)
            
            actual = dut.uo_out.value & 0x01
            dut._log.info(f"A={a}, B={b}, input={input_val:08b}, output={actual}, expected={expected}")
            assert actual == expected, f"Failed for A={a}, B={b}: got {actual}, expected {expected}"

    dut._log.info("Comprehensive test completed successfully!")
