# JavaScript - Objects, Scopes and Closures

Node.js scripts that practice ES6 classes and inheritance, module exports, scopes and closures.

## Requirements

- Node.js, installed at `/usr/bin/node` (every script starts with `#!/usr/bin/node`)
- Files end with a new line
- No `var`: only `const` and `let`
- Code style checked with [semistandard](https://github.com/standard/semistandard)

## Usage

```
chmod +x *.js
semistandard *.js
```

Each file is a module. Load it from a small script, for example:

```js
const Rectangle = require('./3-rectangle');
new Rectangle(2, 3).print();
```

## Files

| File | Description |
|---|---|
| `0-rectangle.js` | An empty `Rectangle` class |
| `1-rectangle.js` | `Rectangle` with `width` and `height` set from the constructor |
| `2-rectangle.js` | Same, but creates an empty object if `w` or `h` is not a positive integer |
| `3-rectangle.js` | Adds `print()`, which draws the rectangle with `X` |
| `4-rectangle.js` | Adds `rotate()` (swaps width and height) and `double()` (doubles both) |
| `5-square.js` | `Square` extends `Rectangle` and calls `super(size, size)` |
| `6-square.js` | `Square` extends the previous `Square` and adds `charPrint(c)` (defaults to `X`) |
| `7-occurrences.js` | `nbOccurences(list, searchElement)` counts how often an element appears |
| `8-esrever.js` | `esrever(list)` returns the reversed list without using `reverse` |
| `9-logme.js` | `logMe(item)` prints `<number already printed>: <item>` using a module-level counter |
| `10-converter.js` | `converter(base)` returns a function that converts a base-10 number to `base` |

## Author

Sano ([sanol-1](https://github.com/sanol-1))
