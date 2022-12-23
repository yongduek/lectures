# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['spaceship_game.py'],
             pathex=['G:\\내 드라이브\\[SuanLab]\\Publish\\Python Game\\sources\\8 Spaceship Game'],
             binaries=[],
             datas=[('assets\\rock\\rock01.png', 'assets\\rock'), ('assets\\rock\\rock02.png', 'assets\\rock'), ('assets\\rock\\rock03.png', 'assets\\rock'), ('assets\\rock\\rock04.png', 'assets\\rock'), ('assets\\rock\\rock05.png', 'assets\\rock'), ('assets\\rock\\rock06.png', 'assets\\rock'), ('assets\\rock\\rock07.png', 'assets\\rock'), ('assets\\rock\\rock08.png', 'assets\\rock'), ('assets\\rock\\rock09.png', 'assets\\rock'), ('assets\\rock\\rock10.png', 'assets\\rock'), ('assets\\rock\\rock11.png', 'assets\\rock'), ('assets\\rock\\rock12.png', 'assets\\rock'), ('assets\\rock\\rock13.png', 'assets\\rock'), ('assets\\rock\\rock14.png', 'assets\\rock'), ('assets\\rock\\rock15.png', 'assets\\rock'), ('assets\\rock\\rock16.png', 'assets\\rock'), ('assets\\rock\\rock17.png', 'assets\\rock'), ('assets\\rock\\rock18.png', 'assets\\rock'), ('assets\\rock\\rock19.png', 'assets\\rock'), ('assets\\rock\\rock20.png', 'assets\\rock'), ('assets\\rock\\rock21.png', 'assets\\rock'), ('assets\\rock\\rock22.png', 'assets\\rock'), ('assets\\rock\\rock23.png', 'assets\\rock'), ('assets\\rock\\rock24.png', 'assets\\rock'), ('assets\\rock\\rock25.png', 'assets\\rock'), ('assets\\rock\\rock26.png', 'assets\\rock'), ('assets\\rock\\rock27.png', 'assets\\rock'), ('assets\\rock\\rock28.png', 'assets\\rock'), ('assets\\rock\\rock29.png', 'assets\\rock'), ('assets\\rock\\rock30.png', 'assets\\rock'), ('assets\\background.jpg', 'assets'), ('assets\\explosion.png', 'assets'), ('assets\\explosion.wav', 'assets'), ('assets\\game_screen.png', 'assets'), ('assets\\Inner_Sanctum.mp3', 'assets'), ('assets\\NanumGothic.ttf', 'assets'), ('assets\\spaceship.png', 'assets'), ('assets\\warp.png', 'assets'), ('assets\\warp.wav', 'assets')],
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
          name='spaceship_game',
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
