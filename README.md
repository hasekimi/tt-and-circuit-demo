![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# TinyTapeout AND Gate Circuit Project

A simple combinational logic project demonstrating multiple AND gate implementations for learning ASIC design.

- [📋 Read the detailed project documentation](docs/info.md)
- [🔧 View the project source code](src/project.v)

## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## Project Overview

This project implements **5 independent AND gates**:
- **4 × 2-input AND gates**: Process pairs of input pins
- **1 × 8-input AND gate**: Combines all input pins

### Quick Architecture Summary

```
Inputs:  ui_in[7:0] (8 pins)
Outputs: uo_out[4:0] (5 pins used)

ui_in[1:0] → AND Gate 1 → uo_out[0]
ui_in[3:2] → AND Gate 2 → uo_out[1]  
ui_in[5:4] → AND Gate 3 → uo_out[2]
ui_in[7:6] → AND Gate 4 → uo_out[3]
ui_in[7:0] → 8-AND Gate → uo_out[4]
```

## How to Test This Project

### Method 1: Local Testing (Recommended)

**Prerequisites:**
```bash
# Ubuntu/Debian
sudo apt install iverilog gtkwave python3 python3-pip

# macOS  
brew install icarus-verilog gtkwave python3
```

**Run Tests:**
```bash
cd test/
pip install -r requirements.txt  # Install cocotb, pytest
make clean && make               # Run all tests

# Expected output:
# TESTS=2 PASS=2 FAIL=0 SKIP=0
```

**View Waveforms:**
```bash
gtkwave tb.gtkw  # Opens with preset signals
```

### Method 2: Manual Test Patterns

Test these input patterns to verify AND gate behavior:

| Test Case | Input (`ui_in`) | Expected Output (`uo_out[4:0]`) |
|-----------|-----------------|--------------------------------|
| All zeros | `0b00000000` | `0b00000` |
| Gate 1 active | `0b00000011` | `0b00001` |  
| Gates 2&4 active | `0b11001100` | `0b01010` |
| All ones | `0b11111111` | `0b11111` |

### Method 3: GitHub Actions

Push your changes and check the **Actions** tab:
- ✅ **GDS Generation**: ASIC layout creation
- ✅ **Test**: Automated cocotb testing  
- ✅ **Documentation**: Auto-generated docs
- ✅ **FPGA**: FPGA implementation (if enabled)

## Project Structure

```
├── src/
│   ├── project.v       # Main Verilog implementation
│   └── config.json     # ASIC synthesis configuration
├── test/
│   ├── tb.v           # Verilog testbench
│   ├── test.py        # Python cocotb tests
│   ├── Makefile       # Test automation
│   └── requirements.txt # Python dependencies
├── docs/
│   └── info.md        # Detailed technical documentation
└── info.yaml          # TinyTapeout project metadata
```

## Development Workflow

1. **Design**: Edit `src/project.v`
2. **Test Locally**: `cd test/ && make`
3. **Update Docs**: Edit `docs/info.md` and `info.yaml`
4. **Commit & Push**: GitHub Actions auto-builds
5. **Submit**: Use [TinyTapeout submission portal](https://app.tinytapeout.com/)

The GitHub action will automatically build the ASIC files using [OpenLane](https://www.zerotoasiccourse.com/terminology/openlane/).

## Enable GitHub actions to build the results page

- [Enabling GitHub Pages](https://tinytapeout.com/faq/#my-github-action-is-failing-on-the-pages-part)

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://tinytapeout.com/discord)
- [Build your design locally](https://www.tinytapeout.com/guides/local-hardening/)

## What next?

- [Submit your design to the next shuttle](https://app.tinytapeout.com/).
- Edit [this README](README.md) and explain your design, how it works, and how to test it.
- Share your project on your social network of choice:
  - LinkedIn [#tinytapeout](https://www.linkedin.com/search/results/content/?keywords=%23tinytapeout) [@TinyTapeout](https://www.linkedin.com/company/100708654/)
  - Mastodon [#tinytapeout](https://chaos.social/tags/tinytapeout) [@matthewvenn](https://chaos.social/@matthewvenn)
  - X (formerly Twitter) [#tinytapeout](https://twitter.com/hashtag/tinytapeout) [@tinytapeout](https://twitter.com/tinytapeout)
