/*
 * Copyright (c) 2024 hasekimi
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_hasekimi_and_circuit (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    // AND Gate Circuit Implementation
    // 
    // Pin Assignment:
    //   ui_in[1:0] -> AND Gate 1 (A, B)
    //   ui_in[3:2] -> AND Gate 2 (C, D)
    //   ui_in[5:4] -> AND Gate 3 (E, F)
    //   ui_in[7:6] -> AND Gate 4 (G, H)
    //
    // Output Assignment:
    //   uo_out[0] -> AND Gate 1 output (A & B)
    //   uo_out[1] -> AND Gate 2 output (C & D)
    //   uo_out[2] -> AND Gate 3 output (E & F)
    //   uo_out[3] -> AND Gate 4 output (G & H)
    //   uo_out[4] -> 8-input AND gate (all inputs)
    //   uo_out[7:5] -> Unused (tied to 0)

    // Four 2-input AND gates
    assign uo_out[0] = ui_in[0] & ui_in[1];  // AND Gate 1: A & B
    assign uo_out[1] = ui_in[2] & ui_in[3];  // AND Gate 2: C & D
    assign uo_out[2] = ui_in[4] & ui_in[5];  // AND Gate 3: E & F
    assign uo_out[3] = ui_in[6] & ui_in[7];  // AND Gate 4: G & H
    
    // One 8-input AND gate (all inputs combined)
    assign uo_out[4] = &ui_in;  // 8-input AND: ui_in[7] & ui_in[6] & ... & ui_in[0]
    
    // Unused outputs tied to 0
    assign uo_out[7:5] = 3'b000;
    
    // All bidirectional IOs are unused in this combinational design
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;  // All IOs set as inputs
    
    // List all unused inputs to prevent warnings
    // This is a combinational circuit, so ena, clk, rst_n are not used
    wire _unused = &{ena, clk, rst_n, uio_in, 1'b0};

endmodule

`default_nettype wire
