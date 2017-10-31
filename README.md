# Contribute Your Repositories to GEE community

This page shows how to share you gee repositories and get simple indexing to help other people find useful stuff easily.

- Oragnize your snippets in folders using the [code editor](https://code.earthengine.google.com/)
- Add one/two line comments in the head of your scripts as following
```javascript
// Composite an image collection and clip it to a boundary.
// See also: FilteredComposite, which filters the collection by bounds instead.
```
- Use git to retrieve your repo locally
```
$ git clone https://earthengine.googlesource.com/[your repo]
```
- Use [ee-index.py](ee-index.py) to parse header comments to index page
```
$ python ee-index.py [your repo folder]
```
- Git push your repo to github and transfer the ownership to gee-community, then people can see your repo and index [here](https://github.com/gee-community):
- Add your repo and introduction in the end of this README.md file.


# List of Repos
- [Google Earth Engine Examples](https://github.com/gee-community/ee-examples)
- [Jun Xiong's snippets](https://github.com/gee-community/ee-snippets)
