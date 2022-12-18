# whisper_demo
OpenAIによって公開されているWhisperをDockerより駆動させるデモリポジトリ

# devices
- Windows11
- WSL2
- docker
- nvidia-docker2
- RTX 3060

# how to
本リポジトリのクローン
> git clone https://github.com/Gyabi/whisper_demo.git

参照するDockerImageをローカルに落とす。
> docker pull nvcr.io/nvidia/pytorch:22.09-py3

docker imageのビルド
> cd whisper
> docker compose build

コンテナの起動
> docker compose run whisper

サンプル実行
> python code/main.py

# reference
参考にしたサイト
- [https://zenn.dev/kento1109/articles/d7d8f512802935](https://zenn.dev/kento1109/articles/d7d8f512802935)


[こちらのサイト](http://pro-video.jp/voice/announce/)よりデモ音声を利用しています。
