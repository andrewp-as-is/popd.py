<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/popd.svg?longCache=True)](https://pypi.org/project/popd/)
[![](https://img.shields.io/pypi/v/popd.svg?maxAge=3600)](https://pypi.org/project/popd/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/popd.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/popd.py/)

#### Installation
```bash
$ [sudo] pip install popd
```

#### Functions
function|`__doc__`
-|-
`popd.popd(func)` |`@popd` decorator. restore previous current directory

#### Examples
```python
import popd

@popd.popd
def func():
    os.chdir('/tmp')
    print(os.getcwd())
```

```python
>>> os.getcwd()
'/Users/username'
>>> func()
'/tmp'
>>> os.getcwd()
'/Users/username'
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>