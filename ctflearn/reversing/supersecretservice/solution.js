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

// Get message length
var b = 31;
var c = 14;
var d = 3;
var e = 15;

var code = "flag{" + "0_0R0_00000000000_aaaaaaaaaaaa" + "}"

// nwords == f
var nwords = 4;


// length of 3rd word is 11
var lw3 = c - d;

// Solve for number that makes up first word of the flag
// that means solve for m_w1

//var result_actual = 1865600952;
//var mask = 0xffffffff;
//var m_z0 = 1991189455;
//var m_z1 = (36969 * (m_z0 & 65535) + (m_z0 >> 16)) & mask;
//// solve for m_w0
//for (var i = 0; i < 1000; i++) {
    //var m_w1 = (18000 * (i & 65535) + (i >> 16)) & mask;

    //var rand = ((m_z1 << 16) + m_w1) & mask;
    //var g = 

    //if (result == result_actual) {
        //console.log("FOUND! m_w0 = " + i);
        //break;
    //}
//}

console.log();
var message = fs.readFileSync("code.dat", 'utf-8');
var sig = "g6Gj<bQ\w";
verify.check(message, code, sig);

