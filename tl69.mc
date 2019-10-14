fetch0: [gPC, LdMAR] fetch1
fetch1: [gMEM, LdIR] fetch2
fetch2: [LdPC, PCMuxSel=0, optest]

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
@HALT: 0x14 halt0

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
// 7: B

// =========
// |  ALU  |
// =========

// 0 in ALUMode means reg, 1 means imm
add0: [gImm, p2mux=0, amux=0, bmux=0, immctrlsel=1, LdA, LdB] add1
add1: [aluop=0, gALU, wrreg] fetch0

sub0: [gImm, p2mux=0, amux=0, bmux=0, immctrlsel=1, LdA, LdB] sub1
sub1: [aluop=4, gALU, wrreg] fetch0

// DR exchanges with SR1, SR2 unused
xchg0: [amux=0, LdA] xchg1
xchg1: [p2mux=1, gP2, WrSr, wrreg] xchg2
xchg2: [aluop=6, gALU, wrreg] fetch0

cmp0: [gImm, p2mux=0, amux=0, bmux=0, immctrlsel=1, LdA, LdB] cmp1
cmp1: [aluop=4, gALU, wrreg] fetch0

or0: [gImm, p2mux=0, amux=0, bmux=0, immctrlsel=1, LdA, LdB] or1
or1: [aluop=2, gALU, wrreg] fetch0

xor0: [gImm, p2mux=0, amux=0, bmux=0, immctrlsel=1, LdA, LdB] xor1
xor1: [aluop=3, gALU, wrreg] fetch0

and0: [gImm, p2mux=0, amux=0, bmux=0, immctrlsel=1, LdA, LdB] and1
and1: [aluop=1, gALU, wrreg] fetch0

not0: [gImm, p2mux=0, amux=0, bmux=0, immctrlsel=1, LdA, LdB] and1
not1: [aluop=5, gALU, wrreg] fetch0

halt0: [] halt0
