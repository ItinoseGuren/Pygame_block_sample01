# -*- coding: utf-8 -*-
import pygame.mixer
import time

# メイン
def main():
    pygame.mixer.init(frequency = 44100)    # 初期設定
    pygame.mixer.music.load("See_you.mp3")     # 音楽ファイルの読み込み
    pygame.mixer.music.play(1)              # 音楽の再生回数(1回)
    time.sleep(100)                         # 音楽の再生時間
    pygame.mixer.music.stop()               # 再生の終了


if __name__ == '__main__':
    main()