# JavaScript - Web scraping

Node.js scripts that read and write files and make HTTP requests with the `request` module.

## Requirements

- Node.js, installed at `/usr/bin/node` (every script starts with `#!/usr/bin/node`)
- The [`request`](https://www.npmjs.com/package/request) module: `npm install request`
- Files end with a new line
- No `var`: only `const` and `let`
- Code style checked with [semistandard](https://github.com/standard/semistandard)

## Usage

```
chmod +x *.js
./0-readme.js cisfun
./2-statuscode.js https://alu-intranet.hbtn.io/status
code: 200
```

## Files

| File | Description |
|---|---|
| `0-readme.js` | Reads a file (UTF-8) and prints it, or prints the error |
| `1-writeme.js` | Writes a string to a file (UTF-8), or prints the error |
| `2-statuscode.js` | Prints `code: <status code>` for a GET request |
| `3-starwars_title.js` | Prints the title of the Star Wars film with the given ID |
| `4-starwars_count.js` | Prints how many films include the character Wedge Antilles (ID 18) |
| `5-request_store.js` | Saves the body of a web page to a file (UTF-8) |
| `6-completed_tasks.js` | Prints the number of completed tasks per user ID |

## Author

Sano ([sanol-1](https://github.com/sanol-1))
