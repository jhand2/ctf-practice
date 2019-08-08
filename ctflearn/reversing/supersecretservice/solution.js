var verify = require("./verify.js")

// Print the op table to easily do replacement
for (var i in verify.op_table) {
    var s = "0x" + Buffer.from(verify.op_table[i], 'utf8').toString('hex');
    s = s.padEnd(30);
    console.log(s + " : " + i.padStart(2) + " : " + verify.op_table[i]);
}

console.log("\nDoing Check\n");
verify.check();
