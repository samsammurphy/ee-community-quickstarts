# Contribute Your Repositories to GEE community for Easy Life

This page shows how to shared you gee repositories and get simple indexing to help other people find useful stuffs easily.

- Oragnized your snippets under meanning folders using [code editor](https://code.earthengine.google.com/)
- Add one/two lines comment in the head of your scripts as following
```
// Composite an image collection and clip it to a boundary.
// See also: FilteredComposite, which filters the collection by bounds instead.
```
- Use git to retrieve your repo to local
```
$ git clone https://earthengine.googlesource.com/[your repo]
```
- Use [ee-index.py](ee-index.py) to parse header comments to index page
```
$ python ee-index.py [your repo folder]
```
- Git push your repo to github and transfer the ownership to gee-community, then people can see your repo and index [here](https://github.com/gee-community):
- Add your repo and introducation in the end of this READEME.md file.


# List of Repos
- []()
- [Google Earth Engine Examples](https://github.com/gee-community/ee-examples)
- [Jun Xiong's snippets](https://github.com/gee-community/ee-snippets)
