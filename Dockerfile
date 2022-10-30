# FROM python:3.9-slim
# FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime
FROM nvcr.io/nvidia/pytorch:22.09-py3

# タイムゾーン設定
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install git+https://github.com/openai/whisper.git 