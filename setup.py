from setuptools import setup, find_packages

setup(
    name = 'studyskills',
    version = '1.0.0',
    author = 'Central Piedmont Community College',
    description = ('Assessment used to evaluate student study skills.'),
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Education',
        ('License :: OSI Approved :: GNU Library or Lesser General '
         'Public License (LGPL)'),
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: JavaScript'
    ]
)
