const ck = require("chalk");
const dm = require("douyu-danmu");

console.log("hello");

console.log(ck.blue("hello"));
console.log(ck.red("hello"));
console.log(ck.blue.bgRed.bold("hello"));
console.log(ck.blue("hello", ck.underline.bgRed("hello")));

console.log(`
CPU: ${ck.red('90%')}
RAM: ${ck.green('40%')}
DISK: ${ck.yellow('70%')}
`);

console.log(ck.keyword('orange')('Yay for orange colored text!'));
console.log(ck.rgb(123, 45, 67).underline('Underlined reddish color'));
console.log(ck.hex('#DEADED').bold('Bold gray!'));

