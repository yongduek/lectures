# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['car_game.py'],
             pathex=['G:\\내 드라이브\\[SuanLab]\\Publish\\Python Game\\sources\\7 Racing Car Game'],
             binaries=[],
             datas=[('assets\\car\\car_01.png', 'assets\\car'), ('assets\\car\\car_02.png', 'assets\\car'), ('assets\\car\\car_03.png', 'assets\\car'), ('assets\\car\\car_04.png', 'assets\\car'), ('assets\\car\\car_05.png', 'assets\\car'), ('assets\\car\\car_06.png', 'assets\\car'), ('assets\\car\\car_07.png', 'assets\\car'), ('assets\\car\\car_08.png', 'assets\\car'), ('assets\\car\\car_09.png', 'assets\\car'), ('assets\\car\\car_10.png', 'assets\\car'), ('assets\\car\\car_11.png', 'assets\\car'), ('assets\\car\\car_12.png', 'assets\\car'), ('assets\\car\\car_13.png', 'assets\\car'), ('assets\\car\\car_14.png', 'assets\\car'), ('assets\\car\\car_15.png', 'assets\\car'), ('assets\\car\\car_16.png', 'assets\\car'), ('assets\\car\\car_17.png', 'assets\\car'), ('assets\\car\\car_18.png', 'assets\\car'), ('assets\\car\\car_19.png', 'assets\\car'), ('assets\\car\\car_20.png', 'assets\\car'), ('assets\\collision.wav', 'assets'), ('assets\\crash.png', 'assets'), ('assets\\crash.wav', 'assets'), ('assets\\engine.wav', 'assets'), ('assets\\menu_car.png', 'assets'), ('assets\\NanumGothicCoding-Bold.ttf', 'assets'), ('assets\\race.wav', 'assets')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='car_game',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
