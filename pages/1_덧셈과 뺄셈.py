import streamlit as st

st.title("📘 덧셈과 뺄셈 학습지")

st.markdown(
    """
    ### 1. 덧셈과 뺄셈이 뭐예요?

    - **덧셈(+)**은 수를 더하는 계산이에요. 예를 들어 3 + 2는 3과 2를 더해서 5가 됩니다.
    - **뺄셈(−)**은 수를 빼는 계산이에요. 예를 들어 7 − 4는 7에서 4를 빼서 3이 됩니다.

    **중요한 점**
    - 덧셈에서는 "더하기"라고 말해요.
    - 뺄셈에서는 "빼기"라고 말해요.
    """
)

st.header("📌 예시 문제")
with st.expander("덧셈 예시 보기"):
    st.write("3 + 4 = 7")
    st.write("5 + 6 = 11")
    st.write("8 + 2 = 10")

with st.expander("뺄셈 예시 보기"):
    st.write("9 - 3 = 6")
    st.write("10 - 4 = 6")
    st.write("12 - 7 = 5")

st.markdown(
    """
    ### 2. 덧셈 문제를 풀어요
    아래 문제를 읽고 답을 쓰세요.
    """
)

addition_questions = [
    (4, 3),
    (7, 2),
    (5, 5),
    (9, 1),
    (6, 4),
]

answers = []
for i, (a, b) in enumerate(addition_questions, start=1):
    answer = st.number_input(f"{i}. {a} + {b} =", min_value=0, max_value=100, value=0, key=f"add_{i}")
    answers.append(answer)

st.markdown("---")

st.markdown(
    """
    ### 3. 뺄셈 문제를 풀어요
    아래 문제를 읽고 답을 쓰세요.
    """
)

subtraction_questions = [
    (8, 5),
    (10, 3),
    (7, 7),
    (12, 4),
    (9, 2),
]

sub_answers = []
for i, (a, b) in enumerate(subtraction_questions, start=1):
    answer = st.number_input(f"{i}. {a} - {b} =", min_value=0, max_value=100, value=0, key=f"sub_{i}")
    sub_answers.append(answer)

st.markdown("---")

st.markdown("### 4. 정답 확인하기")
if st.button("정답 확인"):
    add_correct = [a + b for a, b in addition_questions]
    sub_correct = [a - b for a, b in subtraction_questions]

    st.write("#### 덧셈 정답")
    for i, correct in enumerate(add_correct, start=1):
        user = answers[i - 1]
        result = "✅ 맞았어요" if user == correct else f"❌ 틀렸어요 (정답: {correct})"
        st.write(f"{i}. {addition_questions[i-1][0]} + {addition_questions[i-1][1]} = {user} → {result}")

    st.write("#### 뺄셈 정답")
    for i, correct in enumerate(sub_correct, start=1):
        user = sub_answers[i - 1]
        result = "✅ 맞았어요" if user == correct else f"❌ 틀렸어요 (정답: {correct})"
        st.write(f"{i}. {subtraction_questions[i-1][0]} - {subtraction_questions[i-1][1]} = {user} → {result}")

st.markdown("---")

st.header("✏️ 추가 연습")
st.write("자유롭게 풀어볼 수 있는 문제를 아래에 적어보세요.")
for i in range(1, 4):
    st.text_input(f"연습 문제 {i}", value="", key=f"free_{i}")

st.markdown(
    """
    ### 5. 팁
    - 덧셈은 수를 모두 합칩니다.
    - 뺄셈은 큰 수에서 작은 수를 빼서 남은 값을 구합니다.
    - 계산을 할 때는 먼저 숫자를 천천히 읽고, 두 수를 정확히 확인하세요.
    """
)
