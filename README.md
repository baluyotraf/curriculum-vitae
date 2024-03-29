# Curriculum-Vitae

This is the template used for my CV, deployed in [CV Software+ML].

## Dependencies

The pages are generated using Python. This is particularly tested with
Python 3.8. Once there is a working Python environment, install the
dependencies from the `requirements.txt` file by running the command below.

```bash
pip install -r requirements.txt
```

## CV Information

The information in the CV are all written in the `cv.yaml` file. To make it
easier to fill up the needed information, it is recommended to generate a
JSON schema and use a yaml linter to ensure correctness. The JSON schema can
be generated by the command below.

```bash
python cv.py schema cv.json
```

## Generating the Pages

The tool generates two kinds of pages, one that is for web publishing and
another that is for printing. The currently deployed version shows both
version, with the web version as the default. The web and the print version
can be generated by the `html` and `print` commands respectively.

```bash
python cv.py html cv.yaml site
```

```
python cv.py print cv.yaml print
```

## Theming

The current YAML configuration supports theming, allowing customization of
colors based on Material Design 2 parameters.

If these options does not work
for you, there's an option to further customize the HTML and CSS in the
`templates` folder. These templates were created using [Mako].


[CV Software+ML]: https://cv.baluyotraf.com/
[Mako]: https://www.makotemplates.org/