var fs = require("fs")
var verify = require("./verify.js")

// Print the op table to easily do replacement
for (var i in verify._0xda23) {
    var s = "0x" + Buffer.from(verify._0xda23[i], 'utf8').toString('hex');
    s = s.padEnd(26);
    console.log(s + " : " + i.padStart(2) + " : " + verify._0xda23[i]);
}

// partially deobfuscate js file
function deobfuscate(filename) {
    var f = fs.readFileSync(filename, 'utf-8');
    f = f.replace(/\[?_0xda23\[([0-9]+)\]\]?/g, (matched, index, original) => {
        if (matched.startsWith("[")) {
            matched = matched.substring(1, matched.length - 1);
            return "." + eval("verify." + matched);
        } else {
            return "\"" + eval("verify." + matched) + "\"";
        }
    });

    fs.writeFileSync("deobfuscated." + filename, f);
}

deobfuscate("verify.js")

// Ok, now to own the algo.

// a2 = a * 31 + b
// -b = 31a
//
function reverse_hash(h, out_len) {
    var out = "";
    for (var i = 0; i < out_len; i++) {
        
    }
}

// Get message length
verify.seed(18458);
var a = 1;
var TRUE = (1 == 2);
var FALSE = !TRUE;

b = Math.pow(++a, a + ++a + TRUE) - FALSE + TRUE;
c = Math.pow(a++ - FALSE, a += FALSE + FALSE) - FALSE;
d = (verify.random() + verify.random()) & b;

var len = verify.random() & c;

var code = "flag{" + "0_0R0_000_aaaaaaaaaaaaaaaaaaaa" + "}"

// nwords == f
var nwords = verify.random() & b - d;
nwords *= nwords; // 4

verify.seed(97632000);
var e = Math.floor(b / (FALSE - TRUE + FALSE));
c = (verify.random() >> (e - TRUE + FALSE)) & b; // 11
d = (verify.random() >> (e - TRUE + FALSE)) & b; // 9

// length of 3rd word is 2
var lw3 = c - d;


var message = fs.readFileSync("code.dat", 'utf-8');
var sig = "g6Gj<bQ\w";
verify.check(message, code, sig);

var test = "test";
var h = verify.hash(test);
console.log(h);

