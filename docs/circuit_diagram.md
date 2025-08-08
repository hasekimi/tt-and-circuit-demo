# AND Gate Circuit Diagram

## Overall Architecture

```
                    TinyTapeout AND Gate Circuit
                    ============================

   Input Pins                                    Output Pins
   ui_in[7:0]                                   uo_out[7:0]
        │                                            │
        ▼                                            ▼
   ┌─────────┐                                 ┌─────────┐
   │ ui_in[0]├──┐                              │uo_out[0]│◄─── AND Gate 1
   │ ui_in[1]├──┼──► [AND 1] ──────────────────┤uo_out[1]│◄─── AND Gate 2  
   │ ui_in[2]├──┼──► [AND 2] ──────────────────┤uo_out[2]│◄─── AND Gate 3
   │ ui_in[3]├──┼──► [AND 3] ──────────────────┤uo_out[3]│◄─── AND Gate 4
   │ ui_in[4]├──┼──► [AND 4] ──────────────────┤uo_out[4]│◄─── 8-input AND
   │ ui_in[5]├──┼──► [8-AND] ─────────────────►│uo_out[5]│◄─── 0 (unused)
   │ ui_in[6]├──┼──────────────────────────────┤uo_out[6]│◄─── 0 (unused)
   │ ui_in[7]├──┘──────────────────────────────┤uo_out[7]│◄─── 0 (unused)
   └─────────┘                                 └─────────┘
```

## Individual AND Gates Detail

### 2-Input AND Gates (×4)

```
Gate 1:               Gate 2:               Gate 3:               Gate 4:
ui_in[0] ──┐         ui_in[2] ──┐         ui_in[4] ──┐         ui_in[6] ──┐
           ├─[AND]►   uo_out[0]              ├─[AND]► uo_out[1]            ├─[AND]► uo_out[2]            ├─[AND]► uo_out[3]
ui_in[1] ──┘         ui_in[3] ──┘         ui_in[5] ──┘         ui_in[7] ──┘
```

### 8-Input AND Gate

```
ui_in[0] ──┐
ui_in[1] ──┤
ui_in[2] ──┤
ui_in[3] ──┼─[8-input AND]─► uo_out[4]
ui_in[4] ──┤
ui_in[5] ──┤
ui_in[6] ──┤
ui_in[7] ──┘
```

## Logic Symbol Representation

```
                  AND Gate Logic Symbols
                  ======================

2-Input AND:                8-Input AND:
                            
A ──┐                      A ──┐
    ├─[&]─► Y                  │
B ──┘                      B ──┤
                           C ──┤
Truth Table:               D ──┼─[&]─► Y  
A B | Y                    E ──┤
0 0 | 0                    F ──┤
0 1 | 0                    G ──┤
1 0 | 0                    H ──┘
1 1 | 1                    
                           Truth: Y = A&B&C&D&E&F&G&H
```

## Pin Mapping Summary

| Function | Input Pins | Output Pin | Logic Operation |
|----------|------------|------------|-----------------|
| AND Gate 1 | ui_in[1:0] | uo_out[0] | ui_in[0] & ui_in[1] |
| AND Gate 2 | ui_in[3:2] | uo_out[1] | ui_in[2] & ui_in[3] |
| AND Gate 3 | ui_in[5:4] | uo_out[2] | ui_in[4] & ui_in[5] |
| AND Gate 4 | ui_in[7:6] | uo_out[3] | ui_in[6] & ui_in[7] |
| 8-Input AND | ui_in[7:0] | uo_out[4] | &ui_in (reduction AND) |
| Unused | - | uo_out[7:5] | 3'b000 (tied to ground) |

## Physical Implementation Notes

- **Combinational Logic**: No clock or sequential elements
- **Propagation Delay**: Typically < 1ns per gate in modern CMOS
- **Power Consumption**: Static (leakage) only, no dynamic switching
- **Area**: Minimal - approximately 5 NAND gate equivalents
- **Testability**: Full controllability via input pins, full observability via output pins