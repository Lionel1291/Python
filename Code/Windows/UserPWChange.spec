# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['UserPWChange.py'],
             pathex=['C:\\Users\\Lionel Baur\\OneDrive - ICT Berufsfachschulen Kanton Thurgau\\Dokumente\\GitHub\\PasswordCracker\\Code\\Windows'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='UserPWChange',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
