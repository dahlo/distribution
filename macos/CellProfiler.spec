# -*- mode: python -*-

import os.path

import PyInstaller.compat
import PyInstaller.utils.hooks

binaries = []

block_cipher = None

datas = []

datas += PyInstaller.utils.hooks.collect_data_files("bioformats")
datas += PyInstaller.utils.hooks.collect_data_files("cellprofiler")
datas += PyInstaller.utils.hooks.collect_data_files("javabridge")
datas += PyInstaller.utils.hooks.collect_data_files("prokaryote")
datas += PyInstaller.utils.hooks.collect_data_files("skimage.io._plugins")

datas += [
    ("CellProfiler/cellprofiler/data/images/*", "cellprofiler/data/images")
]

hiddenimports = []

hiddenimports += PyInstaller.utils.hooks.collect_submodules('cellprofiler.modules')
hiddenimports += PyInstaller.utils.hooks.collect_submodules('skimage.io._plugins')

hiddenimports += [
    "pywt._extensions._cwt"
]

a = Analysis(
    [
        'CellProfiler/CellProfiler.py'
    ],
    binaries=binaries,
    cipher=block_cipher,
    datas=datas,
    excludes=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    pathex=[
        'CellProfiler'
    ],
    runtime_hooks=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False
)

pathname = PyInstaller.utils.hooks.get_homebrew_path("libpng")

pathname = os.path.join(pathname, "lib", "libpng16.16.dylib")

java_pathname = "/usr/libexec/java_home"

java_pathname = os.path.join(java_pathname, "jre/lib/server/libjvm.dylib")

a.binaries += [
    ("libpng16.16.dylib", pathname, "BINARY"),
    ("libjvm.dylib", "/Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home/jre/lib/server/libjvm.dylib", "BINARY")
]

exclude_binaries = [
    ('libpng16.16.dylib', '/usr/local/lib/python2.7/site-packages/matplotlib/.dylibs/libpng16.16.dylib', 'BINARY'),
    ('libwx_osx_cocoau_webview-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_osx_cocoau_webview-3.0.dylib', 'BINARY'),
    ('libwx_osx_cocoau_html-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_osx_cocoau_html-3.0.dylib', 'BINARY'),
    ('libwx_osx_cocoau_xrc-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_osx_cocoau_xrc-3.0.dylib', 'BINARY'),
    ('libwx_osx_cocoau_core-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_osx_cocoau_core-3.0.dylib', 'BINARY'),
    ('libwx_osx_cocoau_adv-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_osx_cocoau_adv-3.0.dylib', 'BINARY'),
    ('libwx_osx_cocoau_qa-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_osx_cocoau_qa-3.0.dylib', 'BINARY'),
    ('libwx_baseu_xml-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_baseu_xml-3.0.dylib', 'BINARY'),
    ('libwx_baseu_net-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_baseu_net-3.0.dylib', 'BINARY'),
    ('libwx_baseu-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_baseu-3.0.dylib', 'BINARY'),
    ('libwx_osx_cocoau_stc-3.0.dylib', '/usr/local/opt/wxmac/lib/libwx_osx_cocoau_stc-3.0.dylib', 'BINARY')
]

a.binaries = [binary for binary in a.binaries if binary not in exclude_binaries]

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    console=False,
    debug=False,
    icon="CellProfiler.icns",
    name="CellProfiler",
    strip=False,
    upx=True
)

app = BUNDLE(
    exe,
    bundle_identifier=None,
    icon="CellProfiler.icns",
    name="CellProfiler.app"
)
