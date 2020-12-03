<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/popd.svg?maxAge=3600)](https://pypi.org/project/popd/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/popd.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/popd.py/actions)

### Installation
```bash
$ [sudo] pip install popd
```

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
