# Simple adult content detector for `en` and `ru` languages


Usage:
------
.. code:: python

    adult_text = 'porn'
    valid_text = 'example'
    cl = Classifier()
    print(cl.is_adult(adult_text, 'en'))
    print(cl.is_adult(valid_text, 'en'))

