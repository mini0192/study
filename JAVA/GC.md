# Garbage Collection
프로그램에서 더 이상 사용하지 않는 객체를 자동으로 메모리에서 제거하는 과정이다.
GC는 JVM의 실행엔진에서 동작하며, Heap 영역에 할당된 객체들을 대상으로 메모리 회수 작업을 수행한다.

## 세대적 GC
자바의 GC에서 객체의 생명주기를 고려하여 Heap 영역을 여러개로 나누어 관리하는 방식이다.
1. 대부분의 객체는 오랜시간동안 살아있지 않는다.
2. 오래된 객체에서 젊은 객체로의 참조는 아주 적게 일어난다.
이러한 두가지 조건하에 GC를 효율적으로 동작시키기 위해 HotSpot VM 에서는 메모리를 크게 Old와 Young으로 2개의 물리적 공간으로 나누었다.
이러한 방식의 운영을 세대적 GC이라고 한다.

> ### HotSpot VM
> Oracle JDK와 OpenJDK에서 제공하는 JVM의 기본 구현체이다.
> JVM을 이야기 할 땐 보통 HotSpot VM을 이야기 한다.

## Hotspot Heap Structure
### Young
생성된지 얼마 안된 객체들이 저장되는 장소이다. 해당 영역에서 일어나는 GC를 Minor GC라고 한다.
Young 영역은 새부적으로 Eden, Survivor 0, Survivor 1 3가지 영역으로 나뉜다.
1. Eden: new를 통히 새로 생성된 객체가 위치한다. GC가 실행되고 살아남은 객체들은 Survivor 영역으로 보낸다.
2. Survivor 0 / Survivor 1: 최소 1번의 GC가 실행되고 살아남은 객체가 존재하는 영역이다. 두개의 Survivor이 번갈아가며 사용된다.
### Old
생성된지 오래된 객체들이 저장되는 장소이다. Young 영역에서 살아남은 객체들이 Old 영역으로 옮겨지고 해당 영역에서 일어나는 GC를 Major GC 혹은 Full GC라고 한다.


## Mark And Sweep
Mark-Sweep 이란 다양한 GC에서 사용되는 객체를 솎아내는 내부 알고리즘이다.
GC의 대상을 식별(Mark)하고 제거(Sweep)하며 객체가 제거되어 파편화된 메모리 영역을 앞에서 부터 채워나가는 작업(Compaction)을 수행하게 된다.
- Mark 과정: Root Space로 부터 그래프 순회를 통해 연결된 객체들을 찾아내어 각각 어떤 객체를 참조하고 있는지 찾아 마킹한다.
- Sweep 과정: 참조하고 있지 않은 객체 즉 Unreachable 객체들을 Heap에서 제거한다.
- Compact 과정: Sweep 후에 분산된 객체들을 Heap 시작 주소로 모아 메모리가 할당된 부분과 그렇지 않은 부분으로 압축한다.(GC의 종류에 따라 다르다)

## Minor GC
Young 영역에서 일어나는 GC이다.
Young 영역은 상대적으로 작기 때문에 빠로고 자주 발생한다.

1. 처음에 생성된 객체는 Young 영역의 일부인 Eden 영역에 위치하게 된다.
2. 객체가 계속 생성되어 Eden 영역이 꽉차게 되면 Minor GC가 실행된다.
3. Mark 동작을 통해 Reachable 객체를 탐색한다.
4. Eden 영역에서 살아남은 객체는 Survivor 0(또는 1) 영역으로 이동한다.
5. Eden 영역에서 사용되지 않는 객체(Unreachable)의 메모리를 해제(Sweep)한다.
6. 살아남은 객체들은 age 값이 1 증가하게 된다.
7. 또 다시 Eden 영역이 꽉차게 되면 Minor GC가 실행된다.
8. Mark 동작을 통해 Reachable 객체는 Servivor 1(또는 0)에 이동하고 해제(Sweep) 한다.
9. 다시 살아남은 객체들은 age 값이 1 증가하게 된다.
10. 해당 과정을 반복한다.

## Full GC or Major GC
Young 영역의 객체의 age의 임계값이 차게되면 Old 영역으로 이동된다.
HotSpot VM에 경우 age의 임계값은 31이다.

1. 객체의 age가 임계값에 도달하게 되면 이 객체들은 Old 영역으로 이동하게 된다 이를 Promotion이라 부른다.
2. 위에 과정이 반복되어 Old 영역의 메모리 공간이 부족하게 되면 Major GC가 발생한다.