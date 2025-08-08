<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a simple combinational logic circuit with multiple AND gates using the TinyTapeout framework. The design demonstrates basic digital logic operations and serves as a learning project for ASIC design flow.

### Circuit Architecture

The circuit contains **5 independent AND gates**:

1. **Four 2-input AND gates**: Each takes a pair of input pins and produces one output
2. **One 8-input AND gate**: Takes all input pins and produces a single output when all inputs are high

### Pin Configuration

**Input Pins (`ui_in[7:0]`)**:
- `ui_in[1:0]` → AND Gate 1 inputs (A, B)
- `ui_in[3:2]` → AND Gate 2 inputs (C, D)  
- `ui_in[5:4]` → AND Gate 3 inputs (E, F)
- `ui_in[7:6]` → AND Gate 4 inputs (G, H)

**Output Pins (`uo_out[7:0]`)**:
- `uo_out[0]` → AND Gate 1 output (A & B)
- `uo_out[1]` → AND Gate 2 output (C & D)
- `uo_out[2]` → AND Gate 3 output (E & F)
- `uo_out[3]` → AND Gate 4 output (G & H)
- `uo_out[4]` → 8-input AND gate output (ui_in[7] & ui_in[6] & ... & ui_in[0])
- `uo_out[7:5]` → Unused (tied to 0)

### Logic Implementation

The circuit is implemented as pure combinational logic in SystemVerilog:

```systemverilog
// Four 2-input AND gates
assign uo_out[0] = ui_in[0] & ui_in[1];  // Gate 1
assign uo_out[1] = ui_in[2] & ui_in[3];  // Gate 2
assign uo_out[2] = ui_in[4] & ui_in[5];  // Gate 3
assign uo_out[3] = ui_in[6] & ui_in[7];  // Gate 4

// One 8-input AND gate
assign uo_out[4] = &ui_in;  // Reduction AND operator

// Unused outputs
assign uo_out[7:5] = 3'b000;
```

### Truth Tables

**2-input AND gates** (applies to all 4 gates):
| Input A | Input B | Output |
|---------|---------|--------|
|    0    |    0    |   0    |
|    0    |    1    |   0    |
|    1    |    0    |   0    |
|    1    |    1    |   1    |

**8-input AND gate**:
- Output = 1 **only** when all 8 input bits are 1
- Output = 0 for any other input combination (255 out of 256 cases)

### Circuit Diagram

For a visual representation of the circuit architecture, see [circuit_diagram.md](circuit_diagram.md).

## How to test

### Local Testing (Recommended)

**Prerequisites**:
- Linux/macOS/WSL environment
- Python 3.7+ with pip
- Icarus Verilog (`iverilog`)
- Git

**Setup**:
```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt install iverilog gtkwave

# Clone and navigate to test directory
cd test/

# Install Python dependencies
pip install -r requirements.txt
```

**Run Tests**:
```bash
# Clean build and test execution
make clean
make

# Expected output:
# TESTS=2 PASS=2 FAIL=0 SKIP=0
```

**View Waveforms** (optional):
```bash
# Open GTKWave with preset configuration
gtkwave tb.gtkw

# Or open raw VCD file
gtkwave tb.vcd
```

### Manual Testing Patterns

You can verify the circuit behavior with these test patterns:

**Test 1: Single AND Gate**
- Set `ui_in = 0b00000011` (binary)
- Expect `uo_out[0] = 1` (first gate: 1 & 1 = 1)
- Expect `uo_out[4] = 0` (8-input gate: not all bits are 1)

**Test 2: Multiple Gates**
- Set `ui_in = 0b11001100`
- Expect `uo_out[0] = 0` (0 & 0 = 0)
- Expect `uo_out[1] = 1` (1 & 1 = 1) 
- Expect `uo_out[2] = 0` (0 & 0 = 0)
- Expect `uo_out[3] = 1` (1 & 1 = 1)
- Expect `uo_out[4] = 0` (not all inputs are 1)

**Test 3: 8-input AND Gate**
- Set `ui_in = 0b11111111` (all ones)
- Expect `uo_out[4] = 1` (8-input AND: all inputs high)
- Expect `uo_out[3:0]` to reflect individual gate results

### GitHub Actions Testing

The project includes automated testing via GitHub Actions that runs:
- RTL simulation tests
- Gate-level simulation (post-synthesis)
- Lint checks
- Documentation generation

## External hardware

**No external hardware is required** for this project.

This is a purely digital combinational logic design that operates on the input pins and produces outputs on the dedicated output pins. The circuit can be tested with:

- **Logic analyzer**: To monitor input/output pin states
- **Digital multimeter**: To verify voltage levels (0V/3.3V)
- **Oscilloscope**: To observe signal transitions (though not necessary for combinational logic)
- **LED indicators**: Connected to output pins to visualize gate states

### Recommended Test Setup

For educational purposes, you could connect:
- **DIP switches** to `ui_in[7:0]` for manual input control
- **LEDs** to `uo_out[4:0]` to visualize AND gate outputs
- **Logic analyzer** to capture and analyze signal patterns

This would create a hands-on digital logic trainer to demonstrate AND gate behavior and Boolean algebra principles.
