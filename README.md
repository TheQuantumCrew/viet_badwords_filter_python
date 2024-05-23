# viet_badwords_filter

This library has been published in [PyPI](https://pypi.org/project/viet-badwords-filter)

## Special thanks

Special thanks to everyone in [this repository](https://github.com/Eris-182/vn-badwords) for badwords list.
If you want to add some bad words, please create a Pull Request.

## Features

This package is developed to filter Bad Words in Vietnamese 🇻🇳🇻🇳
```md
Thư viện này dùng để lọc mấy từ bậy bạ chửi tục trong Tiếng Việt
```

## Getting started
### Install the package
```bash
pip install viet_badwords_filter
```

## Usage
### Support clean and check functio
```python

from viet_badwords_filter.filter import VNBadwordsFilter

filter = VNBadwordsFilter()

print(filter.is_profane("hello"))  # False
print(filter.is_profane("vcl"))  # True
print(filter.clean("hello vcl"))  # hello ***

```