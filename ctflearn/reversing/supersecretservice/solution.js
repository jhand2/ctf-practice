var verify = require("./verify.js")

for (let op of verify.op_table) {
    console.log(op);
}

console.log("\nDoing Check\n");
verify.check();
