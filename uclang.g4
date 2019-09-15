grammar uclang;

ucprog: ucStmt (NEWLINE ucStmt)*;

ucStmt: (ucSignalStmt|ucSequencerStmt|ucCmpStmt|);
ucSignalStmt: IDENTIFIER ':' signalList IDENTIFIER?;
ucSequencerStmt: '@' IDENTIFIER ':' number IDENTIFIER;
ucCmpStmt: '!' IDENTIFIER ':' number IDENTIFIER;

signalList: '[' signals ']';
signals: signal? (',' signal)*;
signal: IDENTIFIER ('=' number)?;

number: dec_num|hex_num|bin_num;
dec_num: T_DEC;
hex_num: T_HEX;
bin_num: T_BIN;

COMMENT: '//'~[\r\n]* -> skip;
IDENTIFIER: [a-zA-Z_][0-9a-zA-Z_-]*;
T_DEC: [0-9]+;
T_HEX: '0x'[0-9A-Fa-f]+;
T_BIN: '0b'[0-1]+;
WHITESPACE: [ \t] -> skip;
NEWLINE: [\r\n];
