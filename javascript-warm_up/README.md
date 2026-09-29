# JavaScript - Warm up

Small Node.js scripts that introduce the basics of JavaScript: printing, constants, arguments, conditions, loops, functions, recursion, objects and modules.

## Requirements

- Node.js, installed at `/usr/bin/node` (every script starts with `#!/usr/bin/node`)
- Files end with a new line
- No `var`: only `const` and `let`
- Code style checked with [semistandard](https://github.com/standard/semistandard)

## Usage

```
chmod +x *.js
./2-arguments.js Best School
Arguments found
```

Check the style with:

```
semistandard *.js
```

## Files

| File | Description |
|---|---|
| `0-javascript_is_amazing.js` | Prints "JavaScript is amazing" from a constant `myVar` |
| `1-multi_languages.js` | Prints 3 lines: C, Python and JavaScript |
| `2-arguments.js` | Prints "No argument", "Argument found" or "Arguments found" depending on the number of arguments |
| `3-value_argument.js` | Prints the first argument, or "No argument" (without using `length`) |
| `4-concat.js` | Prints `<arg1> is <arg2>` |
| `5-to_integer.js` | Prints `My number: <n>` if the first argument converts to an integer, otherwise "Not a number" |
| `6-multi_languages_loop.js` | Same output as task 1, using an array and a loop with a single `console.log` |
| `7-multi_c.js` | Prints "C is fun" x times, or "Missing number of occurrences" |
| `8-square.js` | Prints a square of `X` of the given size, or "Missing size" |
| `9-add.js` | Prints the sum of two integers with `function add(a, b)` |
| `10-factorial.js` | Computes a factorial recursively (the factorial of NaN is 1) |
| `11-second_biggest.js` | Prints the second biggest integer of the arguments, or 0 if there are fewer than two |
| `12-object.js` | Updates the `value` of an object from 12 to 89 |
| `13-add.js` | Exports an `add` function: `require('./13-add').add(3, 5)` returns 8 |

## Author

Sano ([sanol-1](https://github.com/sanol-1))
