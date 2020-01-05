# Generate a BIP39 mnemonic seed from an image

## Quickstart

Run the below to get started

```
python3 app.py <path_to_image.image_extension>
```

For testing, an image 'test.jpeg' is included in the repo.

## How it works

<ol>
  <li>User-selected image gets converted to base64 string</li>
  <li>Random characters are taken from the base64 string</li>
  <li>The random string generated above gets fed as entropy</li>
  <li>Terminal outputs your binary and seed phrase</li>
</ol>

Since we use random characters from the b64 string, processing the same image multiple times will generate multiple seed phrases. There is, however, a finite number of phrases that any image can generate.

## Disclaimer

This is for fun and is a very beta version of an idea, there are known and unknown flaws in this and I am not responsible for any loss of funds or data resulting from the use of this script.