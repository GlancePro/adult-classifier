# Simple adult content detector


Supported languages: ru, en
---------------------------

Usage:
------
```
    adult_text = 'porn'
    valid_text = 'example'
    cl = Classifier()
    print(cl.is_adult(adult_text, 'en'))
    print(cl.is_adult(valid_text, 'en'))

```