# 포토인터럽터(Photo Interrupter)

## 1. 개요

포토인터럽터는 적외선 LED와 수광부를 이용하여 **물체의 통과 여부를 감지하는 센서**이다.

물체가 적외선을 차단하면 출력 신호가 변하고, 이를 Arduino에서 감지하여 물체의 유무를 판단할 수 있다.

## 2. 동작 원리

```text
적외선 LED  ───────→  수광부
       적외선 통과
            ↓
        물체 없음

적외선 LED  ──→  물체  ──→  수광부
                  ↓
               빛 차단
                  ↓
              물체 감지
```

## 3. 결선

| 포토인터럽터 | Arduino UNO |
| ------ | ----------- |
| VCC    | 5V          |
| GND    | GND         |
| OUT    | D2          |

## 4. Arduino 코드

```cpp
const int sensorPin = 2;
const int ledPin = 13;

void setup()
{
  pinMode(sensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  int sensorValue = digitalRead(sensorPin);

  if (sensorValue == LOW)
  {
    // 빛 차단 → 물체 감지
    digitalWrite(ledPin, HIGH);
  }
  else
  {
    // 빛 통과 → 물체 없음
    digitalWrite(ledPin, LOW);
  }
}
```

## 5. 동작 결과

* 적외선이 통과하면 → LED OFF
* 물체가 적외선을 차단하면 → LED ON

## 6. 활용

* 물체 통과 감지
* 회전수 측정
* 모터 속도 측정
* 위치 검출
* 엔코더
* 자동화 장비의 물체 감지

### 핵심 정리

> **포토인터럽터 = 적외선의 차단/통과를 이용하여 물체의 움직임을 감지하는 센서**
