#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Calculate the area of the polygon.
# Copyright (c) 2011, Nycholas de Oliveira e Oliveira <nycholas@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# * Neither the name of the Nycholas de Oliveira e Oliveira nor the names of
#    its contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
import os
import sys
import glob
import locale
import fnmatch
from distutils.core import setup
from setuptools import find_packages

if sys.platform == 'win32':
    import py2exe

    # If run without args, build executables, in quiet mode.
    if len(sys.argv) == 1:
        sys.argv.append('py2exe')
        sys.argv.append('-q')
    Executable = lambda x, *y, **z: x
    setup_requires = ['py2exe']
elif sys.platform == 'linux2':
    import cx_Freeze
    from cx_Freeze import setup, Executable

    setup_requires = ['cx_Freeze']
elif sys.platform == 'darwin':
    import py2app

    Executable = lambda x, *y, **z: x
    setup_requires = ['py2app']
else:
    print('Error in buld!')
    sys.exit()


locale.setlocale(locale.LC_ALL, '')
try:
    sys.setappdefaultencoding('utf-8')
except AttributeError:
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
    except LookupError:
        pass

if sys.version_info[0] == 3:
    extra_args = dict(use_2to3=True)
else:
    extra_args = dict()

long_description = '''\
area-polygon
============

Calculate the area of the polygon.


Method
======

You need to know the coordinates of the vertices (corners) of the
polygon. For a state, you could determine those with a GPS device
or through surveying. Each vertex will have coordinates with respect
to some coordinate system, like (x1,y1), (x2,y2),...,(xn,yn),
where 'n' is the last vertex. With that information, there is a
formula for calculating the area. I can give you a reference to a web
site that explains the formula:

Polygon Area:

If, for example, you have a plot of land with five vertices
(x1,y1), (x2,y2),(x3,y3),(x4,y4) and (x5,y5), the area would be

A = (1/2)(x1*y2 - x2*y1 + x2*y3 - x3*y2 + x3y4 - x4y3 +
    + x4*y5 - x5*y4 + x5*y1 - x1*y5)

    
Referencies
===========

http://mathworld.wolfram.com/PolygonArea.html
http://mathforum.org/library/drmath/view/64552.html
http://matemagicasenumeros.blogspot.com/2011/02/mate-magica-na-area.html
'''

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Environment :: X11 Applications :: Qt',
    'Intended Audience :: Education',
    'License :: OSI Approved :: New BSD License',
    'Natural Language :: English',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Programming Language :: Python :: 2.7',
    'Topic :: Education',
    'Topic :: Scientific/Engineering :: Mathematics',
]

manifest = '''\
<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<assembly xmlns='urn:schemas-microsoft-com:asm.v1' manifestVersion='1.0'>
    <assemblyIdentity version='0.64.1.0' processorArchitecture='x86'
     name='Controls' type='win32' />
    <description>Polygon Area</description>
    <dependency>
        <dependentAssembly>
            <assemblyIdentity type='win32'
             name='Microsoft.Windows.Common-Controls' version='6.0.0.0'
             processorArchitecture='X86' publicKeyToken='6595b64144ccf1df'
             language='*' />
        </dependentAssembly>
    </dependency>
</assembly>
'''

def get_packages():
    return find_packages()

def get_all_packages():
    fls = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(os.curdir,
                                                             'moonstone')):
        for filename in fnmatch.filter(filenames, '*.py'):
            fileui = os.path.join(dirpath, filename)
            if not os.access(fileui, os.R_OK):
                raise IOError('Can not access the file {0}' \
                        .format(fileui))
            fileui = fileui.replace('%s%s' % (os.curdir, os.sep), '')
            fileui = fileui.replace('%s' % os.sep, '.')
            fileui = fileui.replace('.py', '')
            fileui = fileui.replace('.__init__', '')
            fls.append(fileui)
    return fls

def get_include_modules():
    inc = [
        'encodings.utf_8',
    ]
    return inc

def get_package_modules():
    return [
        'encodings',
    ]

def get_scripts():
    if os.name == 'posix':
        return [os.path.join('resources', 'scripts', 'moonstone')]
    return [os.path.join('resources', 'scripts', 'moonstone.bat')]

def get_data_files():
    data_files = []

    data_path_src = os.curdir
    data_path_dst = os.curdir
    data_files.append((data_path_src,
                       ['AUTHORS', 'ChangeLog', 'CONTRIBUTORS', 'COPYING',
                        'FAQ', 'INSTALL', 'README', 'THANKS', 'TODO',]))

    data_path_src = os.path.join('resources')
    data_path_dst = os.path.join('resources')
    data_files.append((data_path_dst,
                      [os.path.join(data_path_src, 'logging.conf'),]))

    data_path_src = os.path.join('resources')
    data_path_dst = os.path.join(os.path.expanduser('~'), '.moonstone',
                                 'resources')
    data_files.append((data_path_dst,
                      [os.path.join(data_path_src, 'logging.conf'),]))

    data_path_src = os.path.join('resources', 'log')
    data_path_dst = os.path.join('resources', 'log')
    data_files.append((data_path_dst, []))

    data_path_src = os.path.join('resources', 'log')
    data_path_dst = os.path.join(os.path.expanduser('~'), '.moonstone', 'log')
    data_files.append((data_path_dst, []))

    data_path_src = os.path.join('moonstone', 'ilsa', 'resources')
    data_path_dst = os.path.join('resources', 'ilsa')
    data_files.append((data_path_dst,
                      [os.path.join(data_path_src, 'plugin.conf'),]))

    data_path_src = os.path.join('moonstone', 'ilsa', 'resources')
    data_path_dst = os.path.join(os.path.expanduser('~'), '.moonstone',
                                 'resources', 'ilsa')
    data_files.append((data_path_dst,
                      [os.path.join(data_path_src, 'plugin.conf'),]))

    locale = os.path.join('resources', 'locale')
    try:
        langs = [i for i in os.listdir(locale) \
                 if os.path.isdir(os.path.join(locale, i))]
    except OSError:
        langs = []
    for lang in langs:
        listFiles = []
        diretory = os.path.join('resources', 'locale', lang, 'LC_MESSAGES')
        mo = os.path.join('resources', 'locale', lang,
                          'LC_MESSAGES', 'moonstone.mo')
        if os.path.isfile(mo):
           listFiles.append(mo)
        qm = os.path.join('resources', 'locale', lang,
                          'LC_MESSAGES', 'moonstone.qm')
        if os.path.isfile(qm):
            listFiles.append(qm)
        data_files.append((diretory, listFiles))
    return data_files

def get_include_files():
    include_files = []

    data_path_src = os.curdir
    data_path_dst = os.curdir
    filelist = ['AUTHORS', 'ChangeLog', 'CONTRIBUTORS', 'COPYING',
                'FAQ', 'INSTALL', 'README', 'THANKS', 'TODO',]
    for fl in filelist:
        include_files.append((os.path.join(data_path_src, fl),
                           os.path.join(data_path_dst, fl)))

    data_path_src = os.path.join('resources')
    data_path_dst = os.path.join('resources')
    filelist = ['logging.conf',]
    for fl in filelist:
        include_files.append((os.path.join(data_path_src, fl),
                           os.path.join(data_path_dst, fl)))

    data_path_src = os.path.join('resources', 'log')
    data_path_dst = os.path.join('resources', 'log')
    filelist = []
    for fl in filelist:
        include_files.append((os.path.join(data_path_src, fl),
                           os.path.join(data_path_dst, fl)))

    data_path_src = os.path.join('moonstone', 'ilsa', 'resources')
    data_path_dst = os.path.join('resources', 'ilsa')
    filelist = ['plugin.conf']
    for fl in filelist:
        include_files.append((os.path.join(data_path_src, fl),
                           os.path.join(data_path_dst, fl)))

    locale = os.path.join('resources', 'locale')
    try:
        langs = [i for i in os.listdir(locale) \
                 if os.path.isdir(os.path.join(locale, i))]
    except OSError:
        langs = []
    for lang in langs:
        listFiles = []
        data_path_src = os.path.join('resources', 'locale', lang, 'LC_MESSAGES')
        data_path_dst = os.path.join('resources', 'locale', lang, 'LC_MESSAGES')
        mo = os.path.join('resources', 'locale', lang,
                          'LC_MESSAGES', 'moonstone.mo')
        if os.path.isfile(mo):
           include_files.append((mo, mo))
        qm = os.path.join('resources', 'locale', lang,
                          'LC_MESSAGES', 'moonstone.qm')
        if os.path.isfile(qm):
            include_files.append((qm, qm))
    return include_files

def run():
    setup(name='Polygon Area',
          version='0.1',
          url='http://https://github.com/nycholas/area-polygon/',
          download_url='http://https://github.com/nycholas/area-polygon/',
          license='New BSD License',
          description='''Calculate the area of the polygon.''',
          long_description=long_description,
          classifiers=classifiers,
          platforms=['Many'],
          packages=get_packages(),
          scripts=get_scripts(),
          options={
            'py2exe': {
                'compressed': 1,
                'optimize': 2,
                'ascii': 1,
                'excludes': [
                    'pywin',
                    'pywin.debugger',
                    'pywin.debugger.dbgcon',
                    'pywin.dialogs',
                    'pywin.dialogs.list',
                ],
                'includes': get_include_modules(),
                'packages': get_package_modules(),
            },
            'build_exe': {
                'compressed': 1,
                'optimize': 2,
                'includes': get_include_modules(),
                'packages': get_package_modules(),
                'include_files': get_include_files(),
                'create_shared_zip': 1,
                'include_in_shared_zip': get_include_files(),
                'icon': os.path.join(os.curdir, 'resources', 'static',
                                     'polygon_area.png'),
            },
            'py2app': {
                'compressed': 1,
                'optimize': 2,
                'argv_emulation': 0,
                'includes': get_include_modules() + get_all_packages(),
                'packages': get_package_modules(),
                'resources': ['AUTHORS', 'ChangeLog', 'CONTRIBUTORS', 'COPYING',
                              'FAQ', 'INSTALL', 'README', 'THANKS', 'TODO',],
                'iconfile': os.path.join(os.curdir, 'resources', 'static',
                                         'polygon_area.icns'),
                'plist': {
                    'CFBundleName': 'Polygon Area',
                    'CFBundleShortVersionString': '0.1.0', # must be in X.X.X format
                    'CFBundleGetInfoString': 'Polygon Area 0.1',
                    'CFBundleExecutable': 'Polygon Area',
                    'CFBundleIdentifier': 'org.cenobites.polygon_area',
                },
            },
          },
          zipfile=None,
          windows=[
            {
                'script': 'polygon_area.pyw',
                'icon_resources': [
                    (1, os.path.join(os.curdir, 'resources', 'static',
                                     'polygon_area.ico'))
                ],
            },
          ],
          data_files=get_data_files(),
          executables=[
              Executable(
                 'polygon_area.py',
                 copyDependentFiles=1,
                 icon=os.path.join(os.curdir, 'resources', 'static',
                                   'polygon_area.png'),
              )
          ],
          app=['polygon_area.py'],
          package_data={
            'py2app.apptemplate': [
                'prebuilt/main-i386',
                'prebuilt/main-ppc',
                'prebuilt/main-x86_64',
                'prebuilt/main-ppc64',
                'prebuilt/main-fat',
                'prebuilt/main-fat3',
                'prebuilt/main-intel',
                'prebuilt/main-universal',
                'lib/__error__.sh',
                'lib/site.py',
                'src/main.c',
            ],
            'py2app.bundletemplate': [
                'prebuilt/main-i386',
                'prebuilt/main-ppc',
                'prebuilt/main-x86_64',
                'prebuilt/main-ppc64',
                'prebuilt/main-fat',
                'prebuilt/main-fat3',
                'prebuilt/main-intel',
                'prebuilt/main-universal',
                'lib/__error__.sh',
                'lib/site.py',
                'src/main.m',
            ],
          },
          entry_points={
            'distutils.commands': [
                'py2app = py2app.build_app:py2app',
            ],
            'distutils.setup_keywords': [
                'app = py2app.build_app:validate_target',
                'plugin = py2app.build_app:validate_target',
            ],
            'console_scripts': [
                'py2applet = py2app.script_py2applet:main',
            ],
            'py2app.converter': [
                'xib          = py2app.converters.nibfile:convert_xib',
                'datamodel    = py2app.converters.coredata:convert_datamodel',
                'mappingmodel = py2app.converters.coredata:convert_mappingmodel',
            ],
            'py2app.recipe': [
            ]
          },
          setup_requires=setup_requires,
          **extra_args
    )


# Commands:
# ./setup.py clean -a
# ./setup.py build
# ./setup.py py2exe
# ./setup.py install -c -O2
# ./setup.py sdist --formats=bztar, gztar, tar, zip, ztar
# ./setup.py bdist --formats=rpm, gztar, bztar, ztar, tar, wininst, zip
if __name__ == '__main__':
    run()