#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle


CLASSIFIERS = {
    'en': 'classifiers/cl_en.pickle',
    'ru': 'classifiers/cl_ru.pickle'
}


class Classifier(object):

    def __init__(self):
        # deserialize classifiers
        self._classifiers = self._load_classifiers()

    def _load_classifiers(self):
        classifiers = dict()
        for lang, file_path in CLASSIFIERS.items():
            with open(file_path, 'rb') as f:
                classifiers[lang] = pickle.load(f)
        return classifiers

    def is_adult(self, text, language):
        classifier = self._classifiers.get(language)
        if not classifier:
            pass
        else:
            text_is_valid = classifier.classify(text)
            if not text_is_valid:
                return True

        return False


if __name__ == '__main__':
    adult_text = 'porn'
    valid_text = 'example'
    cl = Classifier()
    print(cl.is_adult(adult_text, 'en'))
    print(cl.is_adult(valid_text, 'en'))
