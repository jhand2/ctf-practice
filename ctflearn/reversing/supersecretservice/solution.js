var fs = require("fs")
var verify = require("./verify.js")
var sleep = require('thread-sleep');

// Print the op table to easily do replacement
//for (var i in verify._0xda23) {
    //var s = "0x" + Buffer.from(verify._0xda23[i], 'utf8').toString('hex');
    //s = s.padEnd(26);
    //console.log(s + " : " + i.padStart(2) + " : " + verify._0xda23[i]);
//}

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

// nwords == f
var nwords = 4;


// length of 3rd word is 11
var lw3 = c - d;

function get_character_class(start, end) {
    result = [];
    for (var i = start.charCodeAt(0); i <= end.charCodeAt(0); i++) {
        result.push(String.fromCharCode(i));
    }

    return result;
}

var characters = get_character_class('a', 'z').concat(get_character_class('A', 'Z')).concat(get_character_class('0', '9')).concat(["_"]);

// Complexity gets unreasonably high after a few letters
function bruteforce_callback(word, len, callback) {
    var success = false;
    for (let c of characters) {
        var w = word + c;
        try {
            //callback(w);
            success = bruteforce_callback(w, len, callback);
            if (success)
                return true;
        } catch (e) {
            continue;
        }
    }

    return success;
}

function bruteforce_char(word, idx, nsuccesses, callback) {
    for (let c of characters) {
        var w = word.substr(0, idx) + c + word.substr(idx + 1);
        try {
            var success_count = callback(w);
            if (typeof(success_count) != "number") {
                console.log((typeof(success_count)))
                return [success_count];
            } else if (success_count >= nsuccesses) {
                return w;
            }
        } catch (e) {
            continue;
        }
    }
}

var message = fs.readFileSync("code.dat", 'utf-8');
var sig = "g6Gj<bQ\\w";
//verify.check(message, code, sig);

// Code to solve for input[2]
function solve_word_2() {
    var idx = 9;
    var success_expected = 2;
    var w = "12345678912";
    while (true) {
    //for (var i = 0; i < idx_order.length; i++) {
        // The correct character at index 9 is o
        w = bruteforce_char(w, idx, success_expected, (word) => {
            console.log(word)
            return verify.runcode(sig, verify.xor(message, 11), word)
        });

        if (typeof(w) != "number" && typeof(w) != "string") {
            console.log(w[0]);
            break;
        }

        console.log(w)
        success_expected++;
        idx = verify.last_decoding_idx
        console.log("Next Index: " + idx)
    }
}

// Code to solve for input[0]
function solve_word_0() {
    var frag1 = "_0R0_";
    var frag2 = "0BfuSc4t1on_"
    var frag3 = "a3Bn9cQ|";

    for (var i = 1000; i < 10000; i++) {
        try {
            var flag = "flag{" + i.toString() + frag1 + frag2 + frag3 + "}";
            console.log(flag)
            verify.check2(message, flag, sig);
            console.log(flag)
            return;
        } catch (e) {
            continue;
        }
    }
}

var code = "flag{0000_0R0_0BfuSc4t1on_a3Bn9cQWv}"
//solve_word_2()
//solve_word_0()
verify.check(message, code, sig);
