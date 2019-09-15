grammar uclang;

ucprog: ucStmt (NEWLINE ucStmt)*;

ucStmt: (COMMENT|ucSignalStmt);
ucSignalStmt: IDENTIFIER ':' signalList IDENTIFIER?;

signalList: '[' signals ']';
signals: signal (',' signal)*;
signal: IDENTIFIER ('=' NUMBER)?;

COMMENT: '//'~[\r\n]*;
IDENTIFIER: [a-zA-Z_][0-9a-zA-Z_-]*;
NUMBER: DEC | HEX | BIN;
DEC: [1-9][0-9]*;
HEX: '0x'[0-9A-Fa-f]+;
BIN: '0b'[0-1]+;
WHITESPACE: [ \t] -> skip;
NEWLINE: [\r\n];
