fetch0: [gPC, LdMAR] fetch1       // Drive PC to MAR
fetch1: [LdPC, PCMuxSel=0] fetch2 // Increment PC
fetch2: [gMEM, LdIR] fetch3       // Load IR from Memory
fetch3: [optest]                  // go to next state based on Opcode

@HALT: 0 halt0
// =======
// | ALU |
// =======
@ADD: 01 add0
@SUB: 02 sub0
// @MUL: 03 mul0
@XCHG: 04 xchg0
@CMP: 05 cmp0
@OR: 06 or0
@XOR: 07 xor0
@AND: 08 and0
@NOT: 09 not0
// @SHR: 0A shr0
// @SHL 0B shl0

// ================
// | Control Flow |
// ===============
@BR: 0xC br0
@CALL: 0xD call0
@RET: 0xE ret0

// ======
// | IO |
// ======
@IN: 0x10 in0
@OUT: 0x11 out0

// ==========
// | Memory |
// ==========
@PUSH: 0x14 push0
@POP: 0x15 pop0
@LW: 0x16 lw0
@SW: 0x17 sw0

//

00001 100 0001 0000 0000101011001111       ADDI r1 0 acf
10100 000 0000 0000 0000 000000000000

// aluop
// 0: +
// 1: &
// 2: |
// 3: ^
// 4: -
// 5: ~A
// 6: A
// 7: NONE

// =========
// |  ALU  |
// =========

// 0 in ALUMode means reg, 1 means imm
add0: [gImm, p2mux=0, amux=0, immctrlsel=1, LdA, LdB] add1
add1: [aluop=0, gALU, wrreg, ldflags] fetch0

sub0: [gImm, p2mux=0, amux=0, immctrlsel=1, LdA, LdB] sub1
sub1: [aluop=4, gALU, wrreg, ldflags] fetch0

// DR exchanges with SR1, SR2 unused
xchg0: [amux=0, LdA] xchg1
xchg1: [p2mux=1, gP2, WrSr, wrreg] xchg2
xchg2: [aluop=6, gALU, wrreg] fetch0

cmp0: [gImm, p2mux=0, amux=0, immctrlsel=1, LdA, LdB] sub1
cmp1: [aluop=4, ldflags] fetch0

or0: [gImm, p2mux=0, amux=0, immctrlsel=1, LdA, LdB] or1
or1: [aluop=2, gALU, wrreg, ldflags] fetch0

xor0: [gImm, p2mux=0, amux=0, immctrlsel=1, LdA, LdB] xor1
xor1: [aluop=3, gALU, wrreg, ldflags] fetch0

and0: [gImm, p2mux=0, amux=0, immctrlsel=1, LdA, LdB] and1
and1: [aluop=1, gALU, wrreg, ldflags] fetch0

not0: [gImm, p2mux=0, amux=0, immctrlsel=1, LdA, LdB] and1
not1: [aluop=5, gALU, wrreg, ldflags] fetch0

// ==================
// |  Control Flow  |
// ==================

// Branches
br0: [gImm, amux=0, bmux=1, immctrlsel=0, LdA, LdB, cmptest]
dobr0: [gALU, LdPC, PCMuxSel=1] fetch0

// Function Calls
call0: [p1mux=1, amux=0, LdA, LdB1, LdB] call1          // Load SP into A, 1 into B
call1: [aluop=4, gALU, LdMAR, WrREG] call2        // Load SP-1 into MAR
call2: [p1mux=1, gPC, WrMEM] call3                      // Save PC into SP-1
call3: [gImm, p2mux=0, amux=0, bmux=1, LdA, LdB] call4  // Load sr1 into A, imm into B (Jump address)
call4: [aluop=0, gALU, LdPC, pcmuxsel=1] fetch0                     // PC = sr1 + imm

ret0: [p1mux=1, gP1, LdMAR, LdA, LdB1, LdB] ret1        // Load SP into MAR, Load SP into A, 1 into B
ret1: [aluop=0, gALU, WrREG] ret2                       // Load SP + 1 into SP (DR is SP)
ret2: [gMEM, LdPC, pcmuxsel=1] fetch0                               // Load Memory (Return Address) into PC


// ======
// | IO |
// ======

// in0: []

out0: [gImm, LdIOAddr, iowe=1] out1
out1: [p2mux=1, gP2, driodataext, iowe=1] out2
out2: [p2mux=1, gP2, driodataext, io, iowe=1] fetch0

in0: [gImm, LdIOAddr, iowe=0] in1
in1: [io] in2
in2: [io, LdIOData] in3
in3: [gIOData, wrreg] fetch0

// ==========
// | Memory |
// ==========

// DR   |   BaseR / SP (SR1)    |   Imm
push0: [amux=0, LdA, LdB1, LdB] push1
push1: [aluop=4, gALU, LdMAR, WrREG, WrSR] push2
push2: [p2mux=1, gP2, WrMEM] fetch0

pop0: [gP1, LdMAR, LdA, LdB1, LdB] pop1
pop1: [aluop=0, gALU, WrREG, WrSR] pop2
pop2: [gMEM, WrREG] fetch0

// DR   |   SR1     |   Imm
// Save Mem[SR1 + Imm] to DR
lw0: [amux=0, gImm, LdA, LdB, immctrlsel=0, bmux=1, LdB1=0] lw1
lw1: [aluop=0, gALU, LdMAR] lw2
lw2: [] lw3 // Wait one cycle after LdMAR to read from it
lw3: [gMEM, WrREG] fetch0

// Write DR to Mem[SR1 + Imm]
sw0: [amux=0, gImm, LdA, LdB, immctrlsel=0, bmux=1, LdB1=0] sw1
sw1: [aluop=0, gALU, LdMAR] sw2
sw2: [p2mux=1, gP2, WrMEM] fetch0


halt0: [] halt0

// =================
// | Condition ROM |
// =================

!NOP: 0 fetch0
!BR: 1 dobr0
