# Deep Learning Transformer LLM

## 1. LLM (Large Language Model)

LLM은 대규모 텍스트 데이터를 학습한 딥러닝 기반 언어 모델입니다.
수십억 개 이상의 파라미터를 사용하여 자연어 이해와 생성 작업을 수행합니다.

주요 활용 분야:

* Text Generation (텍스트 생성)
* Question Answering (질의응답)
* Translation (번역)
* Summarization (요약)
* Code Generation (코드 생성)
* Document Analysis (문서 분석)

대표적인 LLM:

* GPT
* Gemini
* Llama
* Claude

---

# 2. Transformer Architecture

Transformer는 2017년 발표된 딥러닝 아키텍처로,
**Self-Attention Mechanism**을 기반으로 문장 내 단어 간 관계를 학습합니다.

기존 RNN 방식과 달리 입력 데이터를 병렬 처리할 수 있어
대규모 언어 모델 학습에 적합합니다.

## Transformer 핵심 구조

```
Input Text
    ↓
Tokenization
    ↓
Embedding
    ↓
Transformer Blocks
    ↓
Linear Layer
    ↓
Next Token Prediction
    ↓
Generated Text
```

---

# 3. Self-Attention

Transformer의 핵심 기술입니다.

문장 내 각 단어가 다른 단어와 얼마나 관련 있는지 계산합니다.

Attention 공식:

```
Attention(Q,K,V)
=
softmax(QKᵀ / √dₖ)V
```

구성 요소:

* Query (Q): 현재 필요한 정보
* Key (K): 정보의 특징
* Value (V): 실제 전달할 정보

이를 통해 문맥(Context)을 이해합니다.

예:

```
나는 은행에 가서 돈을 찾았다.
```

Transformer는 "은행"이 금융기관이라는 의미를
"돈", "찾았다"와의 관계를 통해 학습합니다.

---

# 4. GPT 기반 LLM 구조

GPT 계열 모델은 주로
**Decoder-only Transformer** 구조를 사용합니다.

```
Input Tokens
      ↓
Embedding
      ↓
Transformer Layer
      ↓
Transformer Layer
      ↓
...
      ↓
Probability Distribution
      ↓
Next Token Generation
```

예:

입력:

```
오늘 날씨는
```

예측:

```
좋다
맑다
춥다
```

가장 높은 확률의 토큰을 선택하여 문장을 생성합니다.

---

# 5. LLM Training Process

## 1) Pre-training

대규모 텍스트 데이터를 이용해
다음 토큰 예측 방식으로 학습합니다.

Example:

Input:

```
나는 학교에
```

Target:

```
간다
```

---

## 2) Fine-tuning

특정 목적에 맞는 데이터로 추가 학습합니다.

Example:

```
Q: Python이란?
A: 프로그래밍 언어이며 다양한 분야에서 사용됩니다.
```

---

## 3) RLHF (Reinforcement Learning from Human Feedback)

사람의 평가 데이터를 활용하여
더 자연스럽고 유용한 답변을 생성하도록 최적화합니다.

---

# 6. Development Stack

## Deep Learning Framework

* PyTorch
* TensorFlow

## NLP / LLM Libraries

* Hugging Face Transformers
* Hugging Face Hub

## Hardware Acceleration

* NVIDIA GPU
* CUDA
* TPU

---

# 7. Learning Roadmap

```
Python
  ↓
NumPy / PyTorch
  ↓
Deep Learning Basics
  ↓
Neural Network
  ↓
NLP Fundamentals
  ↓
Embedding & Tokenization
  ↓
Transformer
  ↓
LLM Architecture
  ↓
Fine-tuning / RAG / LoRA
```

---

# 8. Summary

LLM은 다음 요소들의 결합입니다.

```
LLM
=
Large Scale Data
+
Transformer Architecture
+
Self-Attention
+
Deep Learning Training
```

Transformer 기반 LLM은 현재 자연어 처리, 검색, 챗봇, 코드 생성 등 다양한 AI 서비스의 핵심 기술입니다.

